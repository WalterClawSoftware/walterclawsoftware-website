# Project Status

Last updated: 2026-07-26

This file is public-safe because Netlify publishes the repository root. Live Git, GitHub, App Store Connect, Microsoft Store, Netlify, and the public websites override this handoff when they differ.

## Current Product State

- The repository root is the Netlify publish directory for `https://walterclawsoftware.com`.
- The home page directs visitors to the six free utility apps or the separate self-help and improvement projects.
- Simple Voice Reader is free on iPhone, iPad, Mac, and Windows.
- Simple Voice Reader for Mac version `1.1.1 (11)` is public. It supports local Kokoro and installed Apple voices, WAV or MP3 export, Smart Chapter Export, adaptive playback buffering, synthesized-word timing, and spoken-word auto-scroll.
- Simple Voice Reader for iPhone and iPad version `1.1 (7)` is public. Apple voices remain immediately available; compatible devices can optionally download the Apple-hosted Kokoro pack. Mobile audio export is not offered.
- Simple Voice Reader for Windows is public through Microsoft Store product `9NJ66Q625LL6`.
- Unspoken Room version 1.0 Build 47 remains described as submitted to App Store Connect and not publicly downloadable. Live store state must be rechecked before changing that copy.
- Threshold Lab has its own public product website at `https://thresholdlab.app/`. Its application and submission work are maintained in their own repositories and are not governed by this handoff.

## Completed Work

- Corrected every current Simple Voice Reader Mac version reference from `1.1` to the verified public `1.1.1`.
- Added the July 21 Mac 1.1.1 release to Updates with the public release notes.
- Kept the July 14 Mac 1.1 entry as explicitly historical rather than presenting it as the current version.
- Left Threshold Lab pages, copy, assets, submission materials, and store state unchanged.

## Verification

- Apple's public Mac storefront page reports Simple Voice Reader `1.1.1`, dated 2026-07-21, with release notes covering adaptive buffering, synthesized-word highlighting, spoken-word auto-scroll, and playback-error cleanup.
- App Store Connect had already confirmed macOS build `11` as released and downloadable.
- All 25 HTML files and 46 JSON-LD blocks parse, 937 `href`/`src` references resolve with no missing local target, the sitemap and all JavaScript parse, and `git diff --check` passes.
- `html-validate` reports the same five pre-existing product-page findings as `origin/main` and no new finding from this correction.

## External State

- GitHub `main` is the canonical website source, and Netlify publishes production from that branch.
- Simple Voice Reader's Apple and Microsoft download links are present on the product page.
- No App Store Connect, Microsoft Partner Center, DNS, pricing, availability, or Threshold Lab state is changed by this website correction.

## Known Risks

- Apple's general lookup endpoint represents the iPhone/iPad listing for this universal app. Mac release truth must be read from the Mac storefront view or App Store Connect.
- Store state can drift from static website copy. Reconcile the public store, authenticated store record, GitHub source, deployed page, and project handoff after releases.
- A clean public-install mobile Kokoro pack download and playback test remains a separate device-level checkpoint.

## Next Recommended Action

- Run the lightweight release-truth reconciliation after each store release and on the recurring schedule, then correct any conclusively verified drift promptly.
