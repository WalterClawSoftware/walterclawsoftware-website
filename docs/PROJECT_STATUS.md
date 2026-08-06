# Project Status

Last updated: 2026-08-06

This file is public-safe because Netlify publishes the repository root. Live Git, GitHub, App Store Connect, Microsoft Store, Netlify, and the public websites override this handoff when they differ.

## Unified Homepage

- The root two-path chooser is replaced by one unified homepage: Unspoken Room
  and Threshold Lab appear first beneath the combined
  self-help and useful-software message, followed by the existing utility apps
  beneath the exact heading `Free utility apps.` Individual names, purposes,
  assets, platforms, and destinations are preserved without utility-count copy.
- The release changes `index.html`, `homepage.css`, `README.md`, and
  `sitemap.xml`; this status entry records the same homepage scope.
- Verification passed `check_site_geometry.py --self-test`, `--static`, and
  `--render` across all 25 HTML routes, plus focused JSON-LD/content assertions,
  sitemap and JavaScript parsing, `git diff --check`, and desktop/phone Chrome
  render review with no missing imagery, clipping, distortion, or overflow.
- Next action: keep the paid-app and utility details synchronized with their
  individual product pages and verified storefront state.

## Current Product State

- The repository root is the Netlify publish directory for `https://walterclawsoftware.com`.
- The home page directs visitors to six free utility apps or paid apps. Its right panel now uses a `Paid apps` heading matched to the `Free utility apps` scale, followed by `Available now and others in development.`
- The paid-app page now uses a single-column introductory hero followed by the
  two product cards. The redundant hero actions, availability pills, side
  summary card, and lower free-utilities callout are omitted; global navigation
  and the footer retain the free-utilities path.
- Simple Voice Reader is free on iPhone, iPad, Mac, and Windows.
- Simple Voice Reader for Mac version `1.1.1 (11)` is public. It supports local Kokoro and installed Apple voices, WAV or MP3 export, Smart Chapter Export, adaptive playback buffering, synthesized-word timing, and spoken-word auto-scroll.
- Simple Voice Reader for iPhone and iPad version `1.1 (7)` is public. Apple voices remain immediately available; compatible devices can optionally download the Apple-hosted Kokoro pack. Mobile audio export is not offered.
- Simple Voice Reader for Windows is public through Microsoft Store product `9NJ66Q625LL6`.
- Unspoken Room version `1.0 (47)` is available on the Mac App Store for a
  $29.99 one-time U.S. purchase. Its Windows edition is public through Microsoft
  Store product `9NCKL7C5X2X6` at the same U.S. price for Windows 11 PCs with
  x64 or ARM64 processors. The company page links both official storefronts and
  leaves detailed feature information to `unspokenroom.app`.
- Threshold Lab version `1.0` is available for Mac and Windows. The Mac App
  Store listing at Apple ID `6790457966` is a $49.99 one-time U.S. purchase for
  Apple-silicon Macs running macOS 12 or later. Microsoft Store product
  `9P1ZG8P38LWQ` is public for Windows 11 on x64 and ARM64. The product website
  remains available at `https://thresholdlab.app/`.

## Completed Work

- Removed the screenshot-specified hero action row, availability pills,
  `This path` side card, and lower free-utilities callout from the paid-app
  page. The two product cards and all store/product-site links are unchanged.
- Updated the homepage metadata and structured data, paid-app page, About page,
  Updates timeline, README, and sitemap for Unspoken Room's verified Microsoft
  Store release. The paid-app page now links both official storefronts and no
  longer presents the Windows edition as upcoming.
- Updated the homepage metadata and structured data, paid-app page, About page,
  Updates timeline, and sitemap for Threshold Lab's verified Microsoft Store
  release. The paid-app page now links directly to both official storefronts
  and states the supported Mac and Windows platforms without changing the
  established visual design.
- Removed the retired public-distribution project from current pages, metadata,
  structured data, design prototypes, and public continuity notes. The private
  source repository and separately registered domain were not changed.
- Updated the company homepage structured data, paid-app page, Updates timeline,
  and sitemap for Threshold Lab's verified public release. The paid-app page now
  shows two available Mac apps, links directly to Apple's listing, and preserves
  the Threshold Lab product-site link.
- Restored component-owned sizing for the Simple Voice Reader fixed 16:10
  screenshot stages. The safety layer now keeps those three complete captures
  at the stage height with `object-fit: contain` while preserving the general
  responsive-height invariant everywhere else.
- Added the shared responsive-image invariant, explicit crop approval contract,
  static gate, real-Chrome desktop/phone geometry audit, and GitHub
  `site-quality` workflow across all 25 HTML routes.
- Added a Netlify build gate at the repository root and enabled Git-only
  production so direct production deploys cannot bypass source validation.
- Completed a 22-page technical SEO and performance pass: current home-page search/social copy now reflects Unspoken Room availability and Threshold Lab review status, all `.html` duplicates permanently redirect to extensionless canonicals, the Simple Voice Reader privacy/support schemas are complete, and long search titles/descriptions are concise and distinct.
- Preserved the approved `1730x909` landing artwork as the source/rollback PNG and added visually verified `1730x909` and `800x421` responsive WebP derivatives. The homepage now selects the derived artwork without changing its dimensions, bounds, wording, or visual identity.
- Aligned the Simple Voice Reader support and privacy URL families with Netlify's directory routing: trailing-slash canonicals, Open Graph URLs, structured data, sitemap entries, and internal links now agree, while the no-slash and `/index.html` variants permanently redirect to the canonical pages.
- Replaced the technical Unspoken Room feature inventory on the company site with a short description covering its purpose, current Mac availability, upcoming Windows version, and on-device privacy.
- Added `two-path-doorways-landing-paid-apps.png` as a derived landing asset with the new paid-app hierarchy and wired it into the home page.
- Retained the original `two-path-doorways-landing.png` unchanged as the source artwork and immediate rollback asset.
- Updated the landing image alternative text, paid-path accessibility label, mobile paid-app card, and home-page sitemap date to match the new wording.
- Updated only the paid-app page and its sitemap timestamp for the July 27 store-state change.
- Marked Unspoken Room available for Mac, added the direct Mac App Store purchase link, and retained the public product-site link.
- Marked Threshold Lab `Waiting for Review` and explicitly stated that it is not yet approved or downloadable.
- Preserved the landing-page HTML, artwork, and CSS byte-for-byte.
- Corrected every current Simple Voice Reader Mac version reference from `1.1` to the verified public `1.1.1`.
- Added the July 21 Mac 1.1.1 release to Updates with the public release notes.
- Kept the July 14 Mac 1.1 entry as explicitly historical rather than presenting it as the current version.

## Verification

- The screenshot-specified hero controls, side card, and lower callout are
  absent from `self-help-improvement.html`; its HTML and JSON-LD parse, the
  sitemap XML and storefront JavaScript validate, and `git diff --check`
  passes. The geometry self-test, static invariant, and real-Chrome rendered
  audit pass all 25 routes. Focused `1440x900` and `390x844` renders show the
  single-column hero and both app cards without clipping or horizontal
  overflow, while preserving every store and product-site destination.
- Microsoft Store's public U.S. catalog returned HTTP 200 for product
  `9NCKL7C5X2X6` and identified Unspoken Room, Walter Claw Software LLC, a
  $29.99 price, a purchasable Windows Store installer, Windows 11, and x64 or
  ARM64 processor support. The Mac App Store and `unspokenroom.app` links also
  return HTTP 200. The geometry self-test, static invariant, and rendered audit
  pass all 25 routes; focused JSON-LD parsing, sitemap XML validation,
  JavaScript syntax validation, and `git diff --check` also pass.
- Microsoft Store's public catalog resolved Store ID `9P1ZG8P38LWQ` as
  `Threshold Lab`, published by Walter Claw Software LLC, with the expected
  description, privacy URL, Windows Store installer type, and product ID.
  `python3 scripts/check_site_geometry.py --self-test`, `--static`, and
  `--render` pass all 25 public routes. Focused desktop and phone Chrome reviews
  show the Mac, Windows, and product-site actions without clipping or horizontal
  overflow; the changed JSON-LD, canonicals, H1s, sitemap, JavaScript syntax,
  and `git diff --check` also pass.
- A repository-wide case-insensitive scan has zero current-file matches for the
  retired project name, its compact identifier form, former Apple/Microsoft
  product IDs, or its domain. The embedded text in current and rollback landing
  artwork and the paid-app social card was also checked with local OCR.
- `python3 scripts/check_site_geometry.py --self-test`, `--static`, and
  `--render` pass all 25 public routes. The two changed JSON-LD blocks parse,
  `node --check storefront.js` and `git diff --check` pass, and focused local
  Chrome checks at `1440x900` and `390x844` show the two-app page with no
  missing content, clipping, or horizontal overflow.
- Apple's public U.S. Mac storefront returned HTTP 200 for Threshold Lab Apple
  ID `6790457966` and identified Walter Claw Software LLC, version 1.0, the
  $49.99 price, Apple-silicon Mac availability, and macOS 12-or-later support.
- `python3 scripts/check_site_geometry.py --self-test`, `--static`, and
  `--render` pass all 25 public routes. Focused local Chrome reviews at
  `1440x900` and `390x844` show the updated paid-app page and release entry with
  no missing imagery, clipped copy, or horizontal overflow; `git diff --check`
  also passes.
- Release merge `86272f02f4a9b23731298daf6b612177c63249d3` passed the
  required GitHub `Site Quality` check and produced Git-connected Netlify
  production deploy `6a6ccfc1862ce60008b75b19`, which is `ready`. All 25
  cache-busted canonical HTML routes and 86 deployed styles, scripts, images,
  manifests, sitemap, and robots files match the merged source byte-for-byte.
  Focused live Chrome checks of Home, Paid Apps, and Updates pass at `1440x900`
  and `390x844` with loaded imagery and no crop, distortion, clipping, or
  horizontal overflow.
- The fixed-aspect regression fixture uses the real `site-quality.css` and
  requires its test image to fill a `640x400` contain stage. Self-test, static,
  and rendered checks pass all 25 routes; the Simple Voice Reader stages render
  at about `411.33x256.08` on desktop and `352x219` on phone, with expected
  letterbox-only warnings for the portrait and Windows captures.
- The site-quality self-test proves the original stuck width/height regression
  is rejected. Static and rendered checks pass all 25 routes at desktop and
  phone widths; the existing Repro Pack `object-fit: contain` image is reported
  as a non-failing letterbox warning rather than a crop.
- All 22 pages have one self-canonical, one H1, unique titles and descriptions within search-length bounds, complete Open Graph/Twitter metadata, and valid JSON-LD; 47 JSON-LD blocks parse and all 758 local references resolve.
- Netlify preview `6a68c6c71a40d710530c4f3b` passed 23/23 forced redirect checks, 22/22 full-page byte/self-canonical checks, and exact deployed-byte comparisons for the changed pages, sitemap, and responsive artwork.
- Mobile Lighthouse on the homepage improved from performance `74` to `99`, LCP from about `9.4 s` to `1.8 s`, and transferred bytes from about `1.74 MB` to `118 KB`; accessibility and best practices remain `100`. Preview SEO is intentionally limited only by Netlify's preview-wide `noindex`; production baseline SEO is `100`.
- Production deploy `6a68c9dbf15ee20008809fed` at merge `ebed0fd4c31cf937ea0e85dd74ae7716a707fbd9` is `ready`. Canonical, cache-busted canonical, Netlify main-alias, and immutable-deploy readbacks matched source; all 23 forced redirects passed and all 22 sitemap pages returned `200` with matching self-canonicals. Production Lighthouse scored `99/100/100/100`, with LCP about `1.6 s` and about `115 KB` transferred.
- Desktop `1440x900` and phone `390x844` preview checks preserve the approved landing composition with no missing imagery or unintended visual change.
- All 46 JSON-LD blocks parse, all 773 local `href`/`src` references resolve, the sitemap parses with 22 unique canonical URLs, and `git diff --check` passes. Targeted HTML validation has the same five pre-existing `simple-voice-reader.html` findings as `origin/main`, with no new finding.
- Netlify draft deploy `6a68bb0873dde3e2a465bd60` verified one-hop `301` responses from both no-slash and `/index.html` variants to the trailing-slash URLs, `200` responses with matching self-canonicals at both destinations, and byte parity for the support page, privacy page, and sitemap.
- Production deploy `6a68bbcf13f5090008b419e5` at merge `d93112a` passed 18/18 route checks across the canonical domain, Netlify main alias, and immutable deploy URL; 12/12 normal, cache-busted, alias, and deploy-permalink byte comparisons matched source; and all 22 sitemap URLs returned `200` with matching self-canonicals.
- `self-help-improvement.html` passes targeted HTML and JSON-LD validation; the full-site HTML audit retains the same 37 pre-existing findings and no new finding.
- Preview and production checks at `1440x900` and `390x844` show the simplified copy, both destination buttons, and no horizontal overflow. The production page SHA-256 matches the committed file exactly.
- The derived and original landing assets are both opaque `1730x909` PNG files. Pixel differences are confined to a `439x249` right-panel heading region; the original file retains SHA-256 `380a30f41a8e6c1bb50dd2bd1702d330d28fa7d54794016d367b09133cdb5e3e`.
- `index.html` passes `html-validate`; the sitemap and JSON-LD parse; local references resolve; and `git diff --check` passes.
- The full-site HTML audit retains the same 37 pre-existing findings as the pre-change baseline, with no new finding.
- Preview and production browser checks at `1440x900` and `390x844` show the intended hierarchy and mobile companion card with no horizontal overflow.
- Cache-busted production SHA-256 readbacks match the committed home page, derived artwork, original rollback artwork, and sitemap exactly.
- A prior store readback showed Unspoken Room macOS `1.0.0` as `Ready for Distribution` and Threshold Lab macOS `1.0` as `Waiting for Review`; the Threshold Lab state is superseded by the July 31 public storefront verification above.
- `self-help-improvement.html` passes `html-validate`; its JSON-LD parses, the sitemap parses, and `git diff --check` passes.
- The full-site HTML audit has the same 37 pre-existing findings before and after this update, with no new finding introduced.
- Desktop `1440x900` and mobile `390x844` browser checks show the three correct project states, the Mac App Store button, and no horizontal overflow.
- Production paid-page and sitemap SHA-256 values match the committed files exactly. The live landing-page SHA-256 matches the pre-change source exactly.
- Apple's public Mac storefront page reports Simple Voice Reader `1.1.1`, dated 2026-07-21, with release notes covering adaptive buffering, synthesized-word highlighting, spoken-word auto-scroll, and playback-error cleanup.
- App Store Connect had already confirmed macOS build `11` as released and downloadable.
- All 45 JSON-LD blocks across the 20 top-level HTML files parse, 738 top-level local `href`/`src` references resolve, and the JavaScript parses.

## External State

- Unspoken Room's public Microsoft Store listing is
  `https://apps.microsoft.com/detail/9NCKL7C5X2X6`; no Partner Center setting was
  changed by this website update.
- Netlify remains Git-connected to
  `WalterClawSoftware/walterclawsoftware-website` `main`, and
  `prevent_non_git_prod_deploys` is enabled.
- GitHub branch protection requires the up-to-date `site-quality` check on
  `main`, applies to administrators, requires resolved review conversations,
  and blocks force-pushes and deletion.
- GitHub `main` contains Threshold Lab release merge
  `86272f02f4a9b23731298daf6b612177c63249d3`; Netlify production deploy
  `6a6ccfc1862ce60008b75b19` is `ready` from that exact revision, and its public
  HTML and web assets match Git.
- GitHub `main` contains site-quality merge
  `4204c8c02c214972b0b544ef7763403ccf4504d5`; Netlify production deploy
  `6a68e6f8e096dd00082d8c87` is `ready`. Live homepage and safety-stylesheet
  bytes match Git exactly.
- GitHub `main` contains SEO merge `ebed0fd4c31cf937ea0e85dd74ae7716a707fbd9`; Netlify production deploy `6a68c9dbf15ee20008809fed` is `ready` at that revision with verified route, crawlability, asset-cache, and byte parity.
- The live paid-app page is `https://walterclawsoftware.com/self-help-improvement`.
- Threshold Lab's public Mac App Store listing is
  `https://apps.apple.com/us/app/threshold-lab/id6790457966?mt=12`; no App Store
  Connect setting was changed by this website update.
- Threshold Lab's public Microsoft Store listing is
  `https://apps.microsoft.com/detail/9P1ZG8P38LWQ`; no Partner Center setting was
  changed by this website update.
- Simple Voice Reader's Apple and Microsoft download links are present on the product page.
- On 2026-08-03, the corresponding unsubmitted Apple draft was moved to
  Apple's Removed Apps state and disappeared from the active Apps list. The
  corresponding in-draft Microsoft product was deleted and disappeared from a
  freshly reloaded Partner Center product list.
- No other App Store Connect, Microsoft Partner Center, DNS, pricing, or
  availability setting was changed.

## Known Risks

- Search Console can retain historical redirect and alternate-page samples until Google recrawls them; use the property-owning Google account to confirm the new sample URLs and counts after deployment.
- Apple's general lookup endpoint represents the iPhone/iPad listing for this universal app. Mac release truth must be read from the Mac storefront view or App Store Connect.
- Store state can drift from static website copy. Reconcile the public store, authenticated store record, GitHub source, deployed page, and project handoff after releases.
- A clean public-install mobile Kokoro pack download and playback test remains a separate device-level checkpoint.

## Next Recommended Action

- Allow Google to recrawl the canonical URLs, then inspect Search Console with the property-owning account; do not infer ranking changes from lab scores alone.
- Recheck the Search Console examples after Google recrawls the corrected Simple Voice Reader support and privacy URL families.
- Keep the paid-app page synchronized if Threshold Lab's public listing, price,
  system requirements, or Windows availability changes.
- Keep the brief Unspoken Room company copy synchronized with Windows submission and release state while leaving detailed feature explanations to `unspokenroom.app`.
- Run the lightweight release-truth reconciliation after each store release and on the recurring schedule, then correct any conclusively verified drift promptly.
