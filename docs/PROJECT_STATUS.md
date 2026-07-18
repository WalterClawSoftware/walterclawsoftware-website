# Project Status

Last updated: 2026-07-18

This file is public-safe because Netlify publishes the repository root. Live Git, GitHub, App Store Connect, Microsoft Store, Netlify, and `https://walterclawsoftware.com` override this handoff when they differ.

## Current Product State

- The repository root is the Netlify publish directory for the active Walter Claw Software LLC website.
- Option A and the simplified utilities introduction are live in production from customer-facing revision `928f77667573e99b11a7f8d94d30a562552b24d5`, with the utilities cleanup merged through GitHub pull request 47.
- The selected structure uses `/` as a simple two-path choice, `/utilities` as the familiar product-focused home for the six free utility apps, and `/self-help-improvement` as the separate home for the paid apps in development.
- The `/utilities` introduction is a simple single-column hero without the redundant screenshot/proof panel. Its product grid keeps Simple Voice Reader first and ClipScript Desktop second.
- The root path choice now uses the user-approved blue-and-orange doorway artwork as the interactive landing surface, with each half linking to its corresponding path and separate compact choices for small screens.
- The About page records the founder-supplied company history: Walter Claw Software LLC was founded on March 11, 2026; the name came from Jeffrey Waters naming his original OpenClaw agent Walter; and Hermes Agent was later adopted as the more capable working choice.
- The self-help/improvement page names Threshold Lab, Unspoken Room, and Genome Explorer as projects in development. Unspoken Room is identified as the next planned release and links to `https://unspokenroom.app/`; no release date or final feature set is announced.
- Genome Explorer now has private draft records reserved in App Store Connect and Microsoft Partner Center, and `genomeexplorer.app` is registered. It remains unavailable for download and has no announced release date or final feature set.
- Simple Voice Reader is free on iPhone, iPad, Mac, and Windows.
- macOS 1.1 is Ready for Sale. It uses local Kokoro and installed Apple voices, exports WAV or MP3, and includes resumable Smart Chapter Export.
- The Windows release is public in Microsoft Store under product ID `9NJ66Q625LL6`. It uses local Kokoro and installed Windows voices, exports MP3, WAV, FLAC, OGG, or AIFF, and includes Smart Chapter Export.
- iOS/iPadOS 1.1 build 7 is Ready for Sale and public as a free download. Apple voices remain immediate and serve as the fallback engine. Compatible iOS/iPadOS 26+ devices with at least 5 GB of memory can optionally download an approximately 170 MB Apple-hosted pack of 20 American English Kokoro voices.
- Audio export is not part of the mobile app.
- Text, documents, and rendered audio stay on the user's device. Apple or Microsoft may be contacted only to obtain system voice assets, and Apple hosts the optional mobile Kokoro pack download.

## Completed Work

- Removed the redundant Simple Voice Reader screenshot/proof panel from `/utilities`, converted the introduction to a single-column layout, changed “original six apps” to “utility apps,” and shortened the utilities footer fine print while preserving the requested product order.
- Adopted the exact user-approved 1730 x 909 doorway artwork as the root landing experience. The blue and orange halves are real keyboard-, pointer-, and touch-accessible links, while semantic page copy and mobile choices preserve clarity beyond the embedded image text.
- Implemented selected Option A as a simple two-path company landing page.
- Moved the existing product-heavy homepage experience to `/utilities`, limited it to the six free utility apps, and made Simple Voice Reader the lead app in the hero, product grid, utility menus, and product footers.
- Added `/self-help-improvement` as the separate page for Unspoken Room, Threshold Lab, and Genome Explorer, with paid/in-development status and no unverified dates, final features, or availability claims.
- Removed the desktop-only and creators/small-teams company framing, added clean redirects and sitemap entries for both paths, and created a 1200 x 630 two-path social preview card without overwriting the prior source asset.
- Preserved the three standalone prototype files under `design/homepage-prototypes/` for design history and rollback.
- Replaced every visitor-facing Simple Voice Reader waiting-for-review statement with the verified public iOS/iPadOS 1.1 state across the homepage, product metadata and JSON-LD, product copy and FAQ, About, Updates, support, privacy, storefront configuration, and sitemap.
- Added a dated public update for the July 16 iPhone/iPad release and marked the July 14 review-state note as historical and superseded.
- Replaced the vague About-page founding note with a dedicated founding story that preserves the exact founding date, explains the Walter/OpenClaw name origin, and describes the later move to Hermes without making a universal product claim.
- Added a restrained homepage section for Threshold Lab, Unspoken Room, and Genome Explorer, then identified Unspoken Room as the next planned release and linked its dedicated website without making a release-date or final-feature claim.
- Reserved the exact `Genome Explorer` app name for a macOS record in App Store Connect and an MSIX or PWA app in Microsoft Partner Center, and registered `genomeexplorer.app` through Porkbun.
- Rebuilt the Simple Voice Reader product page around the verified Mac, Windows, iPhone, and iPad editions, with platform-specific capabilities and requirements.
- Added real iPhone and Windows product screenshots while retaining the current Mac screenshot.
- Replaced the Microsoft Store search URL with the permanent product-detail URL.
- Updated product metadata, JSON-LD, privacy, support, homepage, About, Store FAQ, Updates, and storefront configuration.
- Clarified that audio and Smart Chapter export are desktop-only and documented each desktop platform's actual export formats.
- Removed stale desktop-only language from the shared site footer.

## Verification

- Rendered the simplified utilities page at 1600 px and confirmed that the removed panel leaves no empty column, broken media, overlap, or clipped copy. Verified six product cards with Simple Voice Reader first and ClipScript Desktop second.
- Parsed all 22 production-site HTML files and 46 JSON-LD blocks, checked 968 `href` and `src` references with no unresolved local target, parsed the sitemap and web manifest, checked all three JavaScript files, performed byte-exact local HTTP readback for `utilities.html` and `styles.css`, and ran `git diff --check`; all passed.
- Netlify deploy preview `6a5bc2aa245637000858087e` passed its deploy, header-rule, and redirect-rule checks. After normalizing Netlify's preview-only marker, `/utilities` and `styles.css` were byte-for-byte identical to the verified branch files, and the requested copy/removal assertions passed.
- GitHub pull request 47 was squash-merged as customer-facing revision `928f77667573e99b11a7f8d94d30a562552b24d5`. Netlify production deploy `6a5bc2f6a6d39a0008bb7063` reported ready, and cache-busted production readback returned HTTP 200 with byte-exact content for `/utilities` and `styles.css`; the removed panel and footer phrase were absent, the new sentence was present, and Simple Voice Reader remained ahead of ClipScript Desktop.
- Confirmed that the landing artwork is byte-for-byte identical to the user-supplied PNG, is 1730 x 909 with no alpha, and renders cleanly in the centered doorway layout at 1600 px.
- Verified that the artwork path exposes `/utilities` and `/self-help-improvement` as separate accessible links and that small-screen fallback choices state both destinations in live text.
- Netlify deploy preview `6a5bba194f12910008ce15dd` passed its deploy, header-rule, and redirect-rule checks. After normalizing Netlify's preview-only marker, the homepage, both path pages, stylesheet, and artwork were byte-for-byte identical to the verified branch files.
- GitHub pull request 45 was squash-merged as revision `4cd28e28b8561b7a8e2d10c80d9a53eca181aa24`. Netlify production deploy `6a5bbb04a36b6f0008ef98e9` reported ready, and cache-busted production readback returned HTTP 200 with byte-exact content for the homepage, `/utilities`, `/self-help-improvement`, `homepage.css`, and the approved doorway artwork.
- Parsed all 22 production-site HTML files and 46 JSON-LD blocks, resolved 955 local `href` and `src` references, parsed the sitemap, and verified the two path routes.
- Verified exactly six utility cards with Simple Voice Reader first, no Unspoken Room, Threshold Lab, or Genome Explorer names on `/utilities`, all three names on `/self-help-improvement`, removal of the rejected positioning phrases, and Simple Voice Reader first in every shared utility dropdown and product footer.
- Rendered the selected landing page, utility homepage, and self-help/improvement page at 1600 px. The path hierarchy, utility lead, and development-page facts were visually readable without broken media or overlap.
- Verified the new social card at 1200 x 630 with no alpha, checked JavaScript syntax, and ran `git diff --check`; all passed.
- Confirmed that the repository contains no ChatGPT Sites hosting configuration or `chatgpt.site` reference.
- Checked all three prototypes for required company/app names, the two-path hierarchy, Simple Voice Reader platform coverage, portable local asset references, absence of the rejected phrases, responsive rules down to 320px, valid relative assets, and clean rendered 1600×1000 previews.
- Parsed all 20 HTML files and 44 JSON-LD blocks, checked 915 local `href` and `src` references, verified the four founding-story factual anchors and removal of the stale note, and ran `git diff --check`; all passed.
- Tested the founding story locally and on Netlify preview `6a584d537526f82642e80ab1` at desktop and phone widths. The card remained readable and free of horizontal overflow or browser warning/error.
- Netlify production deploy `6a584e1412403b000823ecd4` reported ready for customer-facing revision `f6c2e8785121deb2ce449fc7639924fa1c46c038`.
- Cache-busted production readback returned HTTP 200 with the exact March 11 date, OpenClaw/Walter origin, Hermes transition, and no stale founding note. Live `about.html` was byte-for-byte identical to the verified repository file.
- App Store Connect readback confirmed both macOS 1.1 build 10 and iOS/iPadOS 1.1 build 7 as Ready for Sale and downloadable. The combined iOS review submission is complete, both review items are approved, and the hosted Kokoro asset version is complete.
- Apple's public lookup returned one `Simple Voice Reader` result at version 1.1, price `Free`, with a July 16 release date and release notes covering the optional 20-voice Kokoro pack.
- Re-ran the release-copy validator on July 17: all 20 HTML files, 44 JSON-LD blocks, 738 local references, 20 sitemap URLs, metadata, store-link inventory, and stale-review-language assertions passed; JavaScript syntax, XML parsing, and `git diff --check` also passed.
- Rendered the updated product page in isolated headless Chromium at 1440x1000 and 390x844. The desktop and phone layouts had no horizontal overflow, clipped content, overlap, or visible broken media, and the iPhone/iPad Kokoro requirements remained readable.
- Netlify deploy preview `6a5a785035ed10000886b044` for GitHub pull request 43 returned HTTP 200 on the homepage, About, Updates, product, support, privacy, storefront configuration, and sitemap routes. After removing Netlify's preview-only instrumentation, every response was byte-for-byte identical to the verified repository file.
- GitHub pull request 43 was squash-merged as customer-facing revision `cfb4a0c53f94766dc2ab1fcc07ccc11eb085866b`. Cache-busted production readback returned HTTP 200 on the same eight routes, every response was byte-for-byte identical to that revision, and no stale iPhone/iPad review language remained.
- Tested the product page and support/privacy pages at desktop and phone widths. There was no horizontal overflow, broken media, overlap, or browser console warning/error.
- Netlify preview `6a56cf424db301cb324144cb` returned HTTP 200 for the product, support, privacy, site-wide supporting pages, and both new screenshot assets. Preview copy assertions passed.
- Cache-busted production readback returned HTTP 200 for the same routes and assets, and exact copy assertions passed. The live desktop and phone layouts had no overflow, broken media, or browser console warning/error.
- Porkbun Domain Management listed `genomeexplorer.app` as a new domain in the account with expiration date 2027-07-16.
- App Store Connect showed `Genome Explorer` as macOS 1.0 Prepare for Submission. App Information confirmed Apple ID `6791394608`, bundle ID `com.walterclawsoftware.genomeexplorer`, SKU `GENOMEEXPLORER-MACOS-2026`, and primary language English (U.S.).
- Microsoft Partner Center showed `Genome Explorer` as an In draft MSIX or PWA app. Manage app names reported `Reserved for this app`, and Product Identity confirmed Store ID `9N6CJ95SQR49`, identity name `WalterClawSoftwareLLC.GenomeExplorer`, and PFN `WalterClawSoftwareLLC.GenomeExplorer_jvgzfyt5v7qd8`.

## External State

- The approved two-path homepage is live through the existing GitHub/Netlify workflow. No ChatGPT Sites project, ChatGPT Sites host, or store state was created or changed for this work.
- App Store Connect now contains the private draft Genome Explorer macOS record with Apple ID `6791394608`.
- Microsoft Partner Center now contains the private draft Genome Explorer MSIX or PWA product with Store ID `9N6CJ95SQR49`.
- Porkbun now contains `genomeexplorer.app`, registered through 2027-07-16.
- The self-help/improvement page links to the live `https://unspokenroom.app/` preview and identifies Unspoken Room as the next planned release.
- The About page now publishes the company founding and naming history supplied by founder Jeffrey Waters.
- GitHub `main` published customer-facing revision `928f77667573e99b11a7f8d94d30a562552b24d5` through pull request 47.
- Netlify production deploy `6a5bc2f6a6d39a0008bb7063` published and cache-busted readback verified that revision at `https://walterclawsoftware.com`.

## Known Risks

- The doorway artwork contains embedded display copy. Semantic hidden copy, accessible path links, and live-text mobile choices preserve usability, but any future wording change must keep the artwork and those live-text surfaces aligned.
- The founding narrative is founder-supplied history. Preserve March 11, 2026, the Walter/OpenClaw name origin, and the later Hermes transition as exact anchors unless Jeffrey Waters explicitly revises them.
- Unspoken Room is publicly identified as the next planned release, but no date or final feature set is announced. Keep `unspokenroom.app` and the Walter Claw homepage aligned, and do not use available-now language until the customer artifact and public release state are verified.
- Microsoft states that the Genome Explorer name reservation must be followed by a Store submission within three months or the reservation can be lost.
- Genome Explorer's implemented app source is intentionally kept outside Git in its approved local-only privacy workspace; the reserved Apple and Microsoft identities are not yet wired into a customer build.
- Store and domain availability do not establish trademark rights; complete a separate brand review before public launch.
- The public iOS/iPadOS 1.1 listing and hosted-asset state are verified, but a clean public-install pack-download and playback test remains a separate device-level checkpoint.
- Store state and product capabilities can drift from static website copy; verify live records before future availability changes.

## Next Recommended Action

- Monitor the live two-path choice and simplified utilities introduction for real-device usability, and keep the artwork synchronized with future positioning changes. Separately, verify a clean public Simple Voice Reader iOS/iPadOS 1.1 install, preserve Genome Explorer's Microsoft reservation before its three-month deadline, and prepare the Unspoken Room customer artifact before changing its next-release wording.
