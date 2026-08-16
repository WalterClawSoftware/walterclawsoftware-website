# Project Status

Last updated: 2026-08-16

Live Git, Netlify, and the public site override this handoff when they differ.

## Current Public State

- `https://walterclawsoftware.com` is the canonical public company website.
- The homepage leads with Threshold Lab, followed by six free utility apps.
- Threshold Lab is the only product shown on the self-help, improvement, and
  understanding route.
- Both Threshold Lab cards describe its optional AI as a structured session-plan
  generator rather than a human conversation or companion chat.
- The company About and Updates pages describe only products that remain in the
  current public catalog.
- The retired product's sales copy, store links, support/privacy links,
  structured data, update entries, and obsolete public design prototypes have
  been removed from the current website tree.
- The company-wide support and privacy pages remain available for the current
  catalog.

## Deployment Policy

- Netlify project: `walter-claw-software`.
- Production deployment is Git-only. Merge a passing change to `main`; do not
  deploy production directly through the CLI, API, MCP, or an agent.
- The repository build runs the static geometry gate before publication.

## Verification

- The two bounded Threshold Lab copy changes pass the geometry regression
  self-test, static invariant, real-Chrome desktop/phone rendered geometry,
  focused HTML validation, and `git diff --check`.
- `git diff --check`, the geometry regression self-test, the static invariant,
  and real-Chrome desktop/phone rendered geometry pass all 22 HTML pages. The
  rendered gate retains five known letterbox warnings in untouched Repro Pack
  and Simple Voice Reader screenshots.
- The four modified HTML pages pass the current `html-validate` CLI. An
  all-tree run also reports 37 pre-existing errors in untouched utility and
  product pages; `html-validate` is not part of the current Netlify build gate.
- All 22 HTML pages have one H1, all 47 JSON-LD documents parse, every local
  reference resolves, and the sitemap XML parses.
- A case-insensitive sweep of the current repository tree finds zero retired
  product-name, domain, Apple product-ID, or Microsoft product-ID references.
- A full-page Chrome readback confirms the single-card paid-app layout remains
  visually coherent without clipping, overlap, or a vacant grid column.
- After merge, verify the exact Git-backed Netlify deploy on canonical,
  cache-busted, and immutable-deploy URLs.

## Next Recommended Action

- Keep the public catalog, structured data, update log, sitemap dates, and live
  marketplace status synchronized when remaining products change.
