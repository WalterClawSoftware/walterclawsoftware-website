#!/usr/bin/env python3
"""Static and rendered image-geometry checks for Walter Claw websites.

The static gate enforces a CSS safety invariant that prevents HTML width and
height attributes from becoming a fixed rendered height when an image is made
responsive. The rendered gate opens every HTML page in real Chrome at desktop
and phone widths, then checks image loading, crop/distortion geometry, and
horizontal overflow.
"""

from __future__ import annotations

import argparse
import contextlib
from dataclasses import dataclass
from html.parser import HTMLParser
import json
import os
from pathlib import Path
import re
import shutil
import subprocess
import sys
import tempfile
import threading
from http.server import SimpleHTTPRequestHandler, ThreadingHTTPServer
from typing import Any
from urllib.parse import unquote, urlsplit


CONFIG_NAME = "site-quality.json"
GUARD_NAME = "site-quality.css"
RESULT_ID = "site-quality-results"
RATIO_TOLERANCE = 0.025
VIEWPORTS = (
    {"name": "desktop", "width": 1440, "height": 900},
    {"name": "phone", "width": 390, "height": 844},
)


@dataclass(frozen=True)
class SiteConfig:
    root: Path
    publish_dir: Path
    guard_css: Path
    html_files: tuple[Path, ...]
    approved_crops: tuple[dict[str, str], ...]


class PageParser(HTMLParser):
    def __init__(self) -> None:
        super().__init__(convert_charrefs=True)
        self.stylesheets: list[str] = []
        self.images: list[dict[str, str]] = []

    def handle_starttag(
        self, tag: str, attrs: list[tuple[str, str | None]]
    ) -> None:
        values = {name.lower(): value or "" for name, value in attrs}
        if tag.lower() == "link":
            rel = {part.lower() for part in values.get("rel", "").split()}
            if "stylesheet" in rel and values.get("href"):
                self.stylesheets.append(values["href"])
        elif tag.lower() == "img":
            self.images.append(values)


def load_config(root: Path) -> SiteConfig:
    config_path = root / CONFIG_NAME
    if not config_path.is_file():
        raise ValueError(f"missing {CONFIG_NAME}")

    raw = json.loads(config_path.read_text(encoding="utf-8"))
    publish_value = raw.get("publish_dir")
    if not isinstance(publish_value, str) or not publish_value.strip():
        raise ValueError("site-quality.json must define a non-empty publish_dir")

    publish_dir = (root / publish_value).resolve()
    if not publish_dir.is_dir():
        raise ValueError(f"publish directory does not exist: {publish_dir}")

    excluded = {
        Path(item).as_posix()
        for item in raw.get("exclude_html", [])
        if isinstance(item, str)
    }
    html_files = tuple(
        path
        for path in sorted(publish_dir.rglob("*.html"))
        if path.relative_to(publish_dir).as_posix() not in excluded
        and ".netlify" not in path.parts
        and ".git" not in path.parts
    )
    if not html_files:
        raise ValueError(f"no HTML files found under {publish_dir}")

    approved_raw = raw.get("approved_crops", [])
    if not isinstance(approved_raw, list):
        raise ValueError("approved_crops must be an array")

    approved: list[dict[str, str]] = []
    for index, item in enumerate(approved_raw):
        if not isinstance(item, dict):
            raise ValueError(f"approved_crops[{index}] must be an object")
        entry = {
            "html": str(item.get("html", "")).strip(),
            "src": str(item.get("src", "")).strip(),
            "reason": str(item.get("reason", "")).strip(),
        }
        if not all(entry.values()):
            raise ValueError(
                f"approved_crops[{index}] must define html, src, and reason"
            )
        approved.append(entry)

    return SiteConfig(
        root=root,
        publish_dir=publish_dir,
        guard_css=publish_dir / GUARD_NAME,
        html_files=html_files,
        approved_crops=tuple(approved),
    )


def resolve_local_stylesheet(
    publish_dir: Path, html_file: Path, href: str
) -> Path | None:
    parsed = urlsplit(href)
    if parsed.scheme or parsed.netloc:
        return None
    clean_path = unquote(parsed.path)
    if not clean_path:
        return None
    if clean_path.startswith("/"):
        return (publish_dir / clean_path.lstrip("/")).resolve()
    return (html_file.parent / clean_path).resolve()


def crop_key(html: str, src: str, reason: str) -> tuple[str, str, str]:
    return (Path(html).as_posix(), urlsplit(src).path, reason.strip())


def run_static_checks(config: SiteConfig) -> list[str]:
    failures: list[str] = []
    if not config.guard_css.is_file():
        failures.append(f"missing required safety stylesheet: {config.guard_css}")
        return failures

    compact_css = re.sub(
        r"\s+", "", config.guard_css.read_text(encoding="utf-8")
    )
    required_rule = (
        'img[width][height]:not([data-visual-crop="approved"])'
        "{height:auto!important;}"
    )
    if required_rule not in compact_css:
        failures.append(
            f"{config.guard_css}: missing the immutable responsive-height rule"
        )

    declared_crops = {
        crop_key(item["html"], item["src"], item["reason"])
        for item in config.approved_crops
    }
    used_crops: set[tuple[str, str, str]] = set()

    for html_file in config.html_files:
        relative = html_file.relative_to(config.publish_dir).as_posix()
        parser = PageParser()
        try:
            parser.feed(html_file.read_text(encoding="utf-8"))
        except (OSError, UnicodeDecodeError) as error:
            failures.append(f"{relative}: cannot parse HTML: {error}")
            continue

        linked_guard = any(
            resolve_local_stylesheet(
                config.publish_dir, html_file, href
            ) == config.guard_css.resolve()
            for href in parser.stylesheets
        )
        if not linked_guard:
            failures.append(
                f"{relative}: does not load the required /{GUARD_NAME} safety layer"
            )

        for image in parser.images:
            crop_state = image.get("data-visual-crop", "")
            crop_reason = image.get("data-visual-crop-reason", "").strip()
            if not crop_state and not crop_reason:
                continue
            if crop_state != "approved":
                failures.append(
                    f"{relative}: data-visual-crop must equal 'approved'"
                )
                continue
            if len(crop_reason) < 12:
                failures.append(
                    f"{relative}: approved crop needs a specific reason"
                )
                continue
            src = image.get("src", "")
            key = crop_key(relative, src, crop_reason)
            if key not in declared_crops:
                failures.append(
                    f"{relative}: unlisted approved crop for {src or '<missing src>'}"
                )
            else:
                used_crops.add(key)

    for html, src, reason in sorted(declared_crops - used_crops):
        failures.append(
            f"unused approved crop entry: {html} -> {src} ({reason})"
        )

    return failures


def html_route(path: Path, publish_dir: Path) -> dict[str, str]:
    relative = path.relative_to(publish_dir).as_posix()
    if relative == "index.html":
        url = "/"
    elif relative.endswith("/index.html"):
        url = f"/{relative[:-10]}"
    else:
        url = f"/{relative}"
    return {"file": relative, "url": url}


def make_harness(routes: list[dict[str, str]], viewport: dict[str, Any]) -> str:
    payload = json.dumps(routes, separators=(",", ":"))
    tolerance = json.dumps(RATIO_TOLERANCE)
    width = int(viewport["width"])
    height = int(viewport["height"])
    return f"""<!doctype html>
<meta charset="utf-8">
<title>Walter Claw site quality harness</title>
<style>
  html, body {{ margin: 0; background: #fff; }}
  iframe {{ display: block; width: {width}px; height: {height}px; border: 0; }}
</style>
<iframe id="page-frame" title="site quality target"></iframe>
<script>
(() => {{
  const routes = {payload};
  const viewport = {json.dumps(viewport, separators=(",", ":"))};
  const ratioTolerance = {tolerance};
  const frame = document.getElementById("page-frame");
  const results = [];
  const delay = (ms) => new Promise((resolve) => setTimeout(resolve, ms));

  async function loadRoute(route) {{
    const loaded = new Promise((resolve, reject) => {{
      const timeout = setTimeout(
        () => reject(new Error("page load timed out")),
        8000
      );
      frame.onload = () => {{
        clearTimeout(timeout);
        resolve();
      }};
    }});
    const separator = route.url.includes("?") ? "&" : "?";
    frame.src = `${{route.url}}${{separator}}__site_quality=1`;
    await loaded;

    const doc = frame.contentDocument;
    if (!doc) throw new Error("page is not same-origin");
    const images = Array.from(doc.images);
    for (const image of images) image.loading = "eager";
    await Promise.race([
      Promise.allSettled(images.map(async (image) => {{
        if (!image.complete) {{
          await new Promise((resolve) => {{
            image.addEventListener("load", resolve, {{ once: true }});
            image.addEventListener("error", resolve, {{ once: true }});
          }});
        }}
        if (image.decode) await image.decode().catch(() => undefined);
      }})),
      delay(6000)
    ]);
    if (doc.fonts && doc.fonts.ready) await doc.fonts.ready;
    await new Promise((resolve) =>
      frame.contentWindow.requestAnimationFrame(() =>
        frame.contentWindow.requestAnimationFrame(resolve)
      )
    );

    const root = doc.documentElement;
    const body = doc.body;
    const clientWidth = root.clientWidth;
    const scrollWidth = Math.max(
      root.scrollWidth,
      body ? body.scrollWidth : 0
    );
    const pageFailures = [];
    const pageWarnings = [];
    if (scrollWidth > clientWidth + 2) {{
      const culprits = Array.from(doc.querySelectorAll("body *"))
        .map((element) => {{
          const style = frame.contentWindow.getComputedStyle(element);
          const rect = element.getBoundingClientRect();
          const ancestors = [];
          let parent = element.parentElement;
          while (parent && parent !== body && ancestors.length < 6) {{
            const parentStyle =
              frame.contentWindow.getComputedStyle(parent);
            const parentRect = parent.getBoundingClientRect();
            ancestors.push({{
              selector:
                parent.tagName.toLowerCase() +
                (parent.id ? `#${{parent.id}}` : "") +
                (parent.classList.length
                  ? "." +
                    Array.from(parent.classList).slice(0, 3).join(".")
                  : ""),
              left: Number(parentRect.left.toFixed(2)),
              right: Number(parentRect.right.toFixed(2)),
              width: Number(parentRect.width.toFixed(2)),
              minWidth: parentStyle.minWidth,
              overflowX: parentStyle.overflowX,
              gridTemplateColumns: parentStyle.gridTemplateColumns
            }});
            parent = parent.parentElement;
          }}
          return {{
            selector:
              element.tagName.toLowerCase() +
              (element.id ? `#${{element.id}}` : "") +
              (element.classList.length
                ? "." + Array.from(element.classList).slice(0, 3).join(".")
                : ""),
            left: Number(rect.left.toFixed(2)),
            right: Number(rect.right.toFixed(2)),
            width: Number(rect.width.toFixed(2)),
            display: style.display,
            ancestors
          }};
        }})
        .filter((item) =>
          item.width > 0.5 &&
          (item.left < -2 || item.right > clientWidth + 2)
        )
        .sort((a, b) =>
          Math.max(b.right - clientWidth, -b.left) -
          Math.max(a.right - clientWidth, -a.left)
        )
        .slice(0, 20);
      pageFailures.push({{
        type: "horizontal-page-overflow",
        clientWidth,
        scrollWidth,
        culprits
      }});
    }}

    const imageResults = images.map((image, index) => {{
      const style = frame.contentWindow.getComputedStyle(image);
      const rect = image.getBoundingClientRect();
      const visible =
        rect.width > 0.5 &&
        rect.height > 0.5 &&
        style.display !== "none" &&
        style.visibility !== "hidden";
      const naturalRatio =
        image.naturalWidth > 0 && image.naturalHeight > 0
          ? image.naturalWidth / image.naturalHeight
          : null;
      const renderedRatio =
        rect.width > 0 && rect.height > 0 ? rect.width / rect.height : null;
      const ratioDelta =
        naturalRatio && renderedRatio
          ? Math.abs(renderedRatio / naturalRatio - 1)
          : null;
      const attrWidth = Number(image.getAttribute("width")) || null;
      const attrHeight = Number(image.getAttribute("height")) || null;
      const approved = image.dataset.visualCrop === "approved";
      const source =
        image.currentSrc || image.getAttribute("src") || "<missing src>";
      const failures = [];
      const warnings = [];

      if (visible && source !== "<missing src>" && image.naturalWidth === 0) {{
        failures.push("broken-image");
      }}
      const attributeHeightStuck =
        visible &&
        attrWidth &&
        attrHeight &&
        Math.abs(rect.height - attrHeight) <= 1.5 &&
        Math.abs(rect.width - attrWidth) > 2 &&
        ratioDelta !== null &&
        ratioDelta > ratioTolerance;
      if (attributeHeightStuck && !approved) {{
        failures.push("attribute-height-stuck");
      }}
      if (
        visible &&
        ratioDelta !== null &&
        ratioDelta > ratioTolerance &&
        ["cover", "fill", "none"].includes(style.objectFit) &&
        !approved
      ) {{
        failures.push("cropped-or-distorted");
      }}
      if (
        visible &&
        ratioDelta !== null &&
        ratioDelta > ratioTolerance &&
        ["contain", "scale-down"].includes(style.objectFit) &&
        !approved
      ) {{
        warnings.push("letterboxed-image-box");
      }}
      if (
        visible &&
        (rect.left < -2 || rect.right > clientWidth + 2)
      ) {{
        failures.push("image-outside-horizontal-viewport");
      }}

      return {{
        index,
        source,
        alt: image.getAttribute("alt") || "",
        visible,
        approved,
        objectFit: style.objectFit,
        attrWidth,
        attrHeight,
        naturalWidth: image.naturalWidth,
        naturalHeight: image.naturalHeight,
        renderedWidth: Number(rect.width.toFixed(2)),
        renderedHeight: Number(rect.height.toFixed(2)),
        ratioDelta:
          ratioDelta === null ? null : Number(ratioDelta.toFixed(4)),
        failures,
        warnings
      }};
    }});

    for (const image of imageResults) {{
      for (const type of image.failures) {{
        pageFailures.push({{ type, image }});
      }}
      for (const type of image.warnings) {{
        pageWarnings.push({{ type, image }});
      }}
    }}

    return {{
      file: route.file,
      url: route.url,
      viewport,
      clientWidth,
      scrollWidth,
      images: imageResults,
      failures: pageFailures,
      warnings: pageWarnings
    }};
  }}

  (async () => {{
    for (const route of routes) {{
      try {{
        results.push(await loadRoute(route));
      }} catch (error) {{
        results.push({{
          file: route.file,
          url: route.url,
          viewport,
          failures: [{{
            type: "harness-error",
            message: String(error && error.message ? error.message : error)
          }}],
          warnings: [],
          images: []
        }});
      }}
    }}
    const output = document.createElement("script");
    output.id = "{RESULT_ID}";
    output.type = "application/json";
    output.textContent = JSON.stringify(results);
    document.body.appendChild(output);
    document.documentElement.dataset.siteQualityComplete = "true";
  }})();
}})();
</script>
"""


def make_synchronous_harness(
    routes: list[dict[str, str]], viewport: dict[str, Any]
) -> str:
    """Build a harness whose window load event contains the completed audit.

    Chrome's --dump-dom exits immediately after the load event. Creating every
    same-origin iframe during parsing makes that event a deterministic barrier:
    all target pages, stylesheets, and eager images are loaded before the
    synchronous geometry snapshot is appended to the DOM.
    """

    payload = json.dumps(routes, separators=(",", ":"))
    width = int(viewport["width"])
    height = int(viewport["height"])
    return f"""<!doctype html>
<meta charset="utf-8">
<title>Walter Claw site quality harness</title>
<style>
  html, body {{ margin: 0; background: #fff; }}
  iframe {{ display: block; width: {width}px; height: {height}px; border: 0; }}
</style>
<body>
<script>
(() => {{
  const routes = {payload};
  const viewport = {json.dumps(viewport, separators=(",", ":"))};
  const ratioTolerance = {json.dumps(RATIO_TOLERANCE)};
  const frames = [];

  for (const route of routes) {{
    const frame = document.createElement("iframe");
    frame.title = `site quality target: ${{route.file}}`;
    frame.dataset.file = route.file;
    frame.dataset.url = route.url;
    const separator = route.url.includes("?") ? "&" : "?";
    frame.src = `${{route.url}}${{separator}}__site_quality=1`;
    document.body.appendChild(frame);
    frames.push(frame);
  }}

  function inspect(frame, route) {{
    const doc = frame.contentDocument;
    if (!doc) throw new Error("page is not same-origin");
    const images = Array.from(doc.images);
    const root = doc.documentElement;
    const body = doc.body;
    const clientWidth = root.clientWidth;
    const scrollWidth = Math.max(
      root.scrollWidth,
      body ? body.scrollWidth : 0
    );
    const originalScrollX = frame.contentWindow.scrollX;
    const originalScrollY = frame.contentWindow.scrollY;
    frame.contentWindow.scrollTo(1000000, originalScrollY);
    const maxWindowScrollX = frame.contentWindow.scrollX;
    frame.contentWindow.scrollTo(originalScrollX, originalScrollY);
    const pageFailures = [];
    const pageWarnings = [];
    if (maxWindowScrollX > 2) {{
      const culprits = Array.from(doc.querySelectorAll("body *"))
        .map((element) => {{
          const style = frame.contentWindow.getComputedStyle(element);
          const rect = element.getBoundingClientRect();
          const ancestors = [];
          let parent = element.parentElement;
          while (parent && parent !== body && ancestors.length < 6) {{
            const parentStyle =
              frame.contentWindow.getComputedStyle(parent);
            const parentRect = parent.getBoundingClientRect();
            ancestors.push({{
              selector:
                parent.tagName.toLowerCase() +
                (parent.id ? `#${{parent.id}}` : "") +
                (parent.classList.length
                  ? "." +
                    Array.from(parent.classList).slice(0, 3).join(".")
                  : ""),
              left: Number(parentRect.left.toFixed(2)),
              right: Number(parentRect.right.toFixed(2)),
              width: Number(parentRect.width.toFixed(2)),
              minWidth: parentStyle.minWidth,
              overflowX: parentStyle.overflowX,
              gridTemplateColumns: parentStyle.gridTemplateColumns
            }});
            parent = parent.parentElement;
          }}
          return {{
            selector:
              element.tagName.toLowerCase() +
              (element.id ? `#${{element.id}}` : "") +
              (element.classList.length
                ? "." + Array.from(element.classList).slice(0, 3).join(".")
                : ""),
            left: Number(rect.left.toFixed(2)),
            right: Number(rect.right.toFixed(2)),
            width: Number(rect.width.toFixed(2)),
            display: style.display,
            ancestors,
            containedByOverflowAncestor: ancestors.some((ancestor) =>
              ancestor.left >= -2 &&
              ancestor.right <= clientWidth + 2 &&
              ["auto", "scroll", "hidden", "clip"].includes(
                ancestor.overflowX
              )
            )
          }};
        }})
        .filter((item) =>
          item.width > 0.5 &&
          !item.containedByOverflowAncestor &&
          (item.left < -2 || item.right > clientWidth + 2)
        )
        .sort((a, b) =>
          Math.max(b.right - clientWidth, -b.left) -
          Math.max(a.right - clientWidth, -a.left)
        )
        .slice(0, 20);
      pageFailures.push({{
        type: "horizontal-page-overflow",
        clientWidth,
        scrollWidth,
        maxWindowScrollX,
        culprits
      }});
    }}

    const imageResults = images.map((image, index) => {{
      const style = frame.contentWindow.getComputedStyle(image);
      const rect = image.getBoundingClientRect();
      const visible =
        rect.width > 0.5 &&
        rect.height > 0.5 &&
        style.display !== "none" &&
        style.visibility !== "hidden";
      const naturalRatio =
        image.naturalWidth > 0 && image.naturalHeight > 0
          ? image.naturalWidth / image.naturalHeight
          : null;
      const renderedRatio =
        rect.width > 0 && rect.height > 0 ? rect.width / rect.height : null;
      const ratioDelta =
        naturalRatio && renderedRatio
          ? Math.abs(renderedRatio / naturalRatio - 1)
          : null;
      const attrWidth = Number(image.getAttribute("width")) || null;
      const attrHeight = Number(image.getAttribute("height")) || null;
      const approved = image.dataset.visualCrop === "approved";
      const source =
        image.currentSrc || image.getAttribute("src") || "<missing src>";
      const failures = [];
      const warnings = [];

      if (visible && source !== "<missing src>" && image.naturalWidth === 0) {{
        failures.push("broken-image");
      }}
      const attributeHeightStuck =
        visible &&
        attrWidth &&
        attrHeight &&
        Math.abs(rect.height - attrHeight) <= 1.5 &&
        Math.abs(rect.width - attrWidth) > 2 &&
        ratioDelta !== null &&
        ratioDelta > ratioTolerance;
      if (attributeHeightStuck && !approved) {{
        failures.push("attribute-height-stuck");
      }}
      if (
        visible &&
        ratioDelta !== null &&
        ratioDelta > ratioTolerance &&
        ["cover", "fill", "none"].includes(style.objectFit) &&
        !approved
      ) {{
        failures.push("cropped-or-distorted");
      }}
      if (
        visible &&
        ratioDelta !== null &&
        ratioDelta > ratioTolerance &&
        ["contain", "scale-down"].includes(style.objectFit) &&
        !approved
      ) {{
        warnings.push("letterboxed-image-box");
      }}
      if (visible && (rect.left < -2 || rect.right > clientWidth + 2)) {{
        failures.push("image-outside-horizontal-viewport");
      }}

      return {{
        index,
        source,
        alt: image.getAttribute("alt") || "",
        visible,
        approved,
        objectFit: style.objectFit,
        attrWidth,
        attrHeight,
        naturalWidth: image.naturalWidth,
        naturalHeight: image.naturalHeight,
        renderedWidth: Number(rect.width.toFixed(2)),
        renderedHeight: Number(rect.height.toFixed(2)),
        ratioDelta:
          ratioDelta === null ? null : Number(ratioDelta.toFixed(4)),
        failures,
        warnings
      }};
    }});

    for (const image of imageResults) {{
      for (const type of image.failures) {{
        pageFailures.push({{ type, image }});
      }}
      for (const type of image.warnings) {{
        pageWarnings.push({{ type, image }});
      }}
    }}
    return {{
      file: route.file,
      url: route.url,
      viewport,
      clientWidth,
      scrollWidth,
      maxWindowScrollX,
      images: imageResults,
      failures: pageFailures,
      warnings: pageWarnings
    }};
  }}

  window.addEventListener("load", () => {{
    const results = frames.map((frame, index) => {{
      try {{
        return inspect(frame, routes[index]);
      }} catch (error) {{
        return {{
          file: routes[index].file,
          url: routes[index].url,
          viewport,
          failures: [{{
            type: "harness-error",
            message: String(error && error.message ? error.message : error)
          }}],
          warnings: [],
          images: []
        }};
      }}
    }});
    const output = document.createElement("script");
    output.id = "{RESULT_ID}";
    output.type = "application/json";
    output.textContent = JSON.stringify(results);
    document.body.appendChild(output);
    document.documentElement.dataset.siteQualityComplete = "true";
  }});
}})();
</script>
"""


class HarnessHandler(SimpleHTTPRequestHandler):
    harness_html = ""

    def __init__(self, *args: Any, directory: str, **kwargs: Any) -> None:
        super().__init__(*args, directory=directory, **kwargs)

    def do_GET(self) -> None:
        parsed = urlsplit(self.path)
        if parsed.path == "/__site_quality__.html":
            content = self.harness_html.encode("utf-8")
            self.send_response(200)
            self.send_header("Content-Type", "text/html; charset=utf-8")
            self.send_header("Content-Length", str(len(content)))
            self.send_header("Cache-Control", "no-store")
            self.end_headers()
            self.wfile.write(content)
            return
        if "__site_quality=1" in parsed.query:
            target = Path(self.translate_path(parsed.path))
            if target.is_dir():
                target = target / "index.html"
            if target.is_file() and target.suffix.lower() == ".html":
                content = target.read_text(encoding="utf-8")
                content = re.sub(
                    r"""loading\s*=\s*(["'])lazy\1""",
                    'loading="eager"',
                    content,
                    flags=re.IGNORECASE,
                )
                encoded = content.encode("utf-8")
                self.send_response(200)
                self.send_header("Content-Type", "text/html; charset=utf-8")
                self.send_header("Content-Length", str(len(encoded)))
                self.send_header("Cache-Control", "no-store")
                self.end_headers()
                self.wfile.write(encoded)
                return
        super().do_GET()

    def log_message(self, message_format: str, *args: Any) -> None:
        if os.environ.get("SITE_QUALITY_DEBUG"):
            super().log_message(message_format, *args)
        return

    def copyfile(self, source: Any, outputfile: Any) -> None:
        try:
            super().copyfile(source, outputfile)
        except (BrokenPipeError, ConnectionResetError):
            # The harness intentionally stops Chrome after its result has been
            # captured; large image responses may still be unwinding.
            return


@contextlib.contextmanager
def serve(publish_dir: Path, harness_html: str):
    handler = lambda *args, **kwargs: HarnessHandler(  # noqa: E731
        *args, directory=str(publish_dir), **kwargs
    )
    HarnessHandler.harness_html = harness_html
    server = ThreadingHTTPServer(("127.0.0.1", 0), handler)
    thread = threading.Thread(target=server.serve_forever, daemon=True)
    thread.start()
    try:
        yield f"http://127.0.0.1:{server.server_port}/__site_quality__.html"
    finally:
        server.shutdown()
        server.server_close()
        thread.join(timeout=5)


def find_chrome() -> str:
    candidates = [
        os.environ.get("CHROME_BIN", ""),
        "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome",
        "/Applications/Chromium.app/Contents/MacOS/Chromium",
    ]
    for name in (
        "google-chrome",
        "google-chrome-stable",
        "chromium",
        "chromium-browser",
    ):
        resolved = shutil.which(name)
        if resolved:
            candidates.append(resolved)
    for candidate in candidates:
        if candidate and Path(candidate).is_file():
            return candidate
    raise RuntimeError(
        "Chrome/Chromium not found; set CHROME_BIN to the browser executable"
    )


def browser_results(
    chrome: str,
    publish_dir: Path,
    routes: list[dict[str, str]],
    viewport: dict[str, Any],
) -> list[dict[str, Any]]:
    harness = make_synchronous_harness(routes, viewport)
    with tempfile.TemporaryDirectory(prefix="wcs-site-quality-chrome-") as profile:
        with serve(publish_dir, harness) as url:
            command = [
                chrome,
                "--headless=new",
                "--disable-background-networking",
                "--disable-component-update",
                "--disable-default-apps",
                "--disable-extensions",
                "--disable-gpu",
                "--disable-dev-shm-usage",
                "--disable-sync",
                "--hide-scrollbars",
                "--metrics-recording-only",
                "--mute-audio",
                "--no-first-run",
                "--no-default-browser-check",
                "--no-pings",
                "--run-all-compositor-stages-before-draw",
                f"--window-size={viewport['width']},{viewport['height']}",
                f"--user-data-dir={profile}",
                "--dump-dom",
                url,
            ]
            process = subprocess.Popen(
                command,
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                text=True,
            )
            timed_out = False
            try:
                stdout, stderr = process.communicate(timeout=20)
            except subprocess.TimeoutExpired:
                # Chrome can keep an otherwise completed --dump-dom process
                # alive while child frames exist. Once the deterministic
                # harness has emitted its result, stopping that idle process is
                # expected and does not invalidate the captured DOM.
                timed_out = True
                process.kill()
                stdout, stderr = process.communicate()
    if process.returncode != 0 and not (
        timed_out and f'id="{RESULT_ID}"' in stdout
    ):
        detail = stderr.strip().splitlines()
        tail = "\n".join(detail[-8:])
        raise RuntimeError(
            f"Chrome exited {process.returncode}"
            + (f":\n{tail}" if tail else "")
        )
    match = re.search(
        rf'<script id="{RESULT_ID}" type="application/json">(.*?)</script>',
        stdout,
        flags=re.DOTALL,
    )
    if not match:
        raise RuntimeError(
            "Chrome did not produce site-quality results before its timeout"
        )
    return json.loads(match.group(1))


def run_rendered_checks(
    config: SiteConfig, viewports: tuple[dict[str, Any], ...] = VIEWPORTS
) -> tuple[list[str], list[str], list[dict[str, Any]]]:
    chrome = find_chrome()
    routes = [html_route(path, config.publish_dir) for path in config.html_files]
    failures: list[str] = []
    warnings: list[str] = []
    all_results: list[dict[str, Any]] = []
    for viewport in viewports:
        results = browser_results(
            chrome, config.publish_dir, routes, viewport
        )
        all_results.extend(results)
        for page in results:
            label = f"{page['file']} [{viewport['name']}]"
            for failure in page.get("failures", []):
                image = failure.get("image")
                detail = ""
                if image:
                    detail = (
                        f" src={image['source']}"
                        f" rendered={image['renderedWidth']}x"
                        f"{image['renderedHeight']}"
                        f" natural={image['naturalWidth']}x"
                        f"{image['naturalHeight']}"
                    )
                elif failure.get("message"):
                    detail = f" {failure['message']}"
                elif "scrollWidth" in failure:
                    culprits = ", ".join(
                        item.get("selector", "")
                        for item in failure.get("culprits", [])[:3]
                    )
                    detail = (
                        f" scrollWidth={failure['scrollWidth']}"
                        f" clientWidth={failure['clientWidth']}"
                        + (f" culprits={culprits}" if culprits else "")
                    )
                failures.append(f"{label}: {failure['type']}{detail}")
            for warning in page.get("warnings", []):
                image = warning.get("image", {})
                warnings.append(
                    f"{label}: {warning['type']} src={image.get('source', '')}"
                )
    return failures, warnings, all_results


def run_self_test(root: Path) -> list[str]:
    failures: list[str] = []
    chrome = find_chrome()
    with tempfile.TemporaryDirectory(prefix="wcs-site-quality-self-test-") as temp:
        fixture = Path(temp)
        image = (
            "data:image/svg+xml,"
            "%3Csvg xmlns='http://www.w3.org/2000/svg' "
            "width='800' height='600'%3E"
            "%3Crect width='800' height='600' fill='%23b86a2d'/%3E"
            "%3C/svg%3E"
        )
        broken = f"""<!doctype html><meta charset="utf-8">
<style>img {{ display:block; width:50%; object-fit:cover; }}</style>
<img src="{image}" width="800" height="600" alt="broken fixture">
"""
        fixed = f"""<!doctype html><meta charset="utf-8">
<style>img {{ display:block; width:50%; height:auto; object-fit:cover; }}</style>
<img src="{image}" width="800" height="600" alt="fixed fixture">
"""
        fixed_aspect = f"""<!doctype html><meta charset="utf-8">
<style>
body {{ margin:0; }}
.screenshot-platform-stage {{
  display:block;
  position:relative;
  width:640px;
  aspect-ratio:16 / 10;
  overflow:hidden;
}}
.screenshot-platform-stage img {{
  position:absolute;
  inset:0;
  width:100%;
  height:100%;
  object-fit:contain;
}}
</style>
<link rel="stylesheet" href="/site-quality.css">
<a class="screenshot-platform-stage">
  <img src="{image}" width="800" height="600" alt="fixed aspect fixture">
</a>
"""
        (fixture / "broken.html").write_text(broken, encoding="utf-8")
        (fixture / "fixed.html").write_text(fixed, encoding="utf-8")
        (fixture / "fixed-aspect.html").write_text(
            fixed_aspect, encoding="utf-8"
        )
        (fixture / GUARD_NAME).write_text(
            (root / GUARD_NAME).read_text(encoding="utf-8"),
            encoding="utf-8",
        )
        routes = [
            {"file": "broken.html", "url": "/broken.html"},
            {"file": "fixed.html", "url": "/fixed.html"},
            {"file": "fixed-aspect.html", "url": "/fixed-aspect.html"},
        ]
        viewport = {"name": "self-test", "width": 800, "height": 600}
        results = browser_results(chrome, fixture, routes, viewport)
        by_file = {item["file"]: item for item in results}
        broken_types = {
            item["type"] for item in by_file["broken.html"]["failures"]
        }
        fixed_types = {
            item["type"] for item in by_file["fixed.html"]["failures"]
        }
        fixed_aspect_image = by_file["fixed-aspect.html"]["images"][0]
        if "attribute-height-stuck" not in broken_types:
            failures.append(
                "self-test: original width/height regression was not detected"
            )
        if "cropped-or-distorted" not in broken_types:
            failures.append(
                "self-test: original crop/distortion regression was not detected"
            )
        if fixed_types:
            failures.append(
                "self-test: height:auto fixture should pass, got "
                + ", ".join(sorted(fixed_types))
            )
        if (
            abs(fixed_aspect_image["renderedWidth"] - 640) > 1.5
            or abs(fixed_aspect_image["renderedHeight"] - 400) > 1.5
        ):
            failures.append(
                "self-test: fixed-aspect contain image did not fill its "
                "640x400 stage"
            )
    return failures


def print_findings(title: str, findings: list[str]) -> None:
    if not findings:
        return
    print(title)
    for finding in findings:
        print(f"  - {finding}")


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--static", action="store_true", help="run the deployment-safe static gate"
    )
    parser.add_argument(
        "--render", action="store_true", help="run real-Chrome geometry checks"
    )
    parser.add_argument(
        "--self-test",
        action="store_true",
        help="prove the gate detects the original regression",
    )
    parser.add_argument(
        "--json-report",
        type=Path,
        help="write detailed rendered results to this path",
    )
    args = parser.parse_args()
    if not (args.static or args.render or args.self_test):
        args.static = True
        args.render = True

    root = Path(__file__).resolve().parent.parent
    failures: list[str] = []
    warnings: list[str] = []
    rendered_results: list[dict[str, Any]] = []

    try:
        config = load_config(root)
        if args.static:
            failures.extend(run_static_checks(config))
        if args.self_test:
            failures.extend(run_self_test(root))
        if args.render:
            render_failures, render_warnings, rendered_results = (
                run_rendered_checks(config)
            )
            failures.extend(render_failures)
            warnings.extend(render_warnings)
    except (OSError, ValueError, RuntimeError, subprocess.TimeoutExpired) as error:
        failures.append(str(error))

    if args.json_report:
        args.json_report.parent.mkdir(parents=True, exist_ok=True)
        args.json_report.write_text(
            json.dumps(rendered_results, indent=2) + "\n",
            encoding="utf-8",
        )

    print_findings("Site-quality warnings:", warnings)
    print_findings("Site-quality failures:", failures)
    if failures:
        return 1
    modes = ", ".join(
        name
        for enabled, name in (
            (args.static, "static invariant"),
            (args.self_test, "regression self-test"),
            (args.render, "rendered geometry"),
        )
        if enabled
    )
    print(
        f"Site-quality gate passed: {len(config.html_files)} HTML page(s); {modes}."
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())
