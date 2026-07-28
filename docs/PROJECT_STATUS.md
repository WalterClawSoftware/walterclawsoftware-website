# Project Status

Last updated: 2026-07-28

This file is public-safe because Netlify publishes the repository root. Live Git, GitHub, App Store Connect, Microsoft Store, Netlify, and the public websites override this handoff when they differ.

## Current Product State

- The repository root is the Netlify publish directory for `https://walterclawsoftware.com`.
- The home page directs visitors to six free utility apps or paid apps. Its right panel now uses a `Paid apps` heading matched to the `Free utility apps` scale, followed by `Available now and others in development.`
- Simple Voice Reader is free on iPhone, iPad, Mac, and Windows.
- Simple Voice Reader for Mac version `1.1.1 (11)` is public. It supports local Kokoro and installed Apple voices, WAV or MP3 export, Smart Chapter Export, adaptive playback buffering, synthesized-word timing, and spoken-word auto-scroll.
- Simple Voice Reader for iPhone and iPad version `1.1 (7)` is public. Apple voices remain immediately available; compatible devices can optionally download the Apple-hosted Kokoro pack. Mobile audio export is not offered.
- Simple Voice Reader for Windows is public through Microsoft Store product `9NJ66Q625LL6`.
- Unspoken Room version `1.0 (47)` is available on the Mac App Store for a $29.99 one-time U.S. purchase. The paid-app page uses plain-language company copy, notes that Windows is on the way, and leaves feature detail to `unspokenroom.app`.
- Threshold Lab version `1.0 (6)` is `Waiting for Review` in App Store Connect. It is not yet approved or publicly downloadable; its product website remains available at `https://thresholdlab.app/`.
- Genome Explorer remains in development and is not publicly downloadable. The most recent authenticated store readbacks recorded private draft Apple and Microsoft product identities, while `genomeexplorer.app` remains registered.

## Completed Work

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
- Restored the active Genome Explorer reservation, domain, submission-window, and customer-build risks that must survive concise handoff updates.

## Verification

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
- App Store Connect showed Unspoken Room macOS `1.0.0` as `Ready for Distribution` and Threshold Lab macOS `1.0` as `Waiting for Review`; the public Unspoken Room Mac App Store listing is reachable at Apple ID `6788225275`.
- `self-help-improvement.html` passes `html-validate`; its JSON-LD parses, the sitemap parses, and `git diff --check` passes.
- The full-site HTML audit has the same 37 pre-existing findings before and after this update, with no new finding introduced.
- Desktop `1440x900` and mobile `390x844` browser checks show the three correct project states, the Mac App Store button, and no horizontal overflow.
- Production paid-page and sitemap SHA-256 values match the committed files exactly. The live landing-page SHA-256 matches the pre-change source exactly.
- Apple's public Mac storefront page reports Simple Voice Reader `1.1.1`, dated 2026-07-21, with release notes covering adaptive buffering, synthesized-word highlighting, spoken-word auto-scroll, and playback-error cleanup.
- App Store Connect had already confirmed macOS build `11` as released and downloadable.
- All 45 JSON-LD blocks across the 20 top-level HTML files parse, 738 top-level local `href`/`src` references resolve, and the JavaScript parses.
- The separately maintained Genome Explorer handoff still records the reserved Apple and Microsoft identities and confirms that the customer build is not yet a public-distribution candidate.
- Google Registry RDAP confirms `genomeexplorer.app` was registered on 2026-07-16 through Porkbun and expires on 2027-07-16.

## External State

- GitHub `main` contains paid-app page revision `c2fe41a`, landing hierarchy revision `db919bc`, plain-language Unspoken Room revision `9132e44`, and canonical-route revision `d93112a`; Netlify production deploy `6a68bbcf13f5090008b419e5` is `ready` with verified route and byte parity.
- The live paid-app page is `https://walterclawsoftware.com/self-help-improvement`.
- Simple Voice Reader's Apple and Microsoft download links are present on the product page.
- The most recent authenticated store records identify Apple ID `6791394608` and Microsoft Store ID `9N6CJ95SQR49` for Genome Explorer. These identifiers are continuity evidence, not approval or public-availability evidence.
- `genomeexplorer.app` is registered through 2027-07-16; no public product site is currently served from the domain.
- No App Store Connect, Microsoft Partner Center, DNS, pricing, or availability setting was changed by this website correction.

## Known Risks

- Search Console can retain historical redirect and alternate-page samples until Google recrawls them; use the property-owning Google account to confirm the new sample URLs and counts after deployment.
- Apple's general lookup endpoint represents the iPhone/iPad listing for this universal app. Mac release truth must be read from the Mac storefront view or App Store Connect.
- Store state can drift from static website copy. Reconcile the public store, authenticated store record, GitHub source, deployed page, and project handoff after releases.
- The phrase `Windows on the way` should be updated when the Windows submission or release state materially changes.
- Microsoft states that the Genome Explorer name reservation must be followed by a Store submission within three months or the reservation can be lost; reverify the live deadline before acting.
- The reserved Apple and Microsoft identities are not yet wired into a production-signed, installed, customer-tested Genome Explorer build.
- A clean public-install mobile Kokoro pack download and playback test remains a separate device-level checkpoint.

## Next Recommended Action

- Recheck the Search Console examples after Google recrawls the corrected Simple Voice Reader support and privacy URL families.
- Keep the paid-app page synchronized with App Store Connect when Threshold Lab's review state changes; do not alter the landing page without explicit direction.
- Keep the brief Unspoken Room company copy synchronized with Windows submission and release state while leaving detailed feature explanations to `unspokenroom.app`.
- Run the lightweight release-truth reconciliation after each store release and on the recurring schedule, then correct any conclusively verified drift promptly.
- Keep the Genome Explorer reservations and domain in the recurring reconciliation until a verified customer build is ready for the relevant submission gates.
