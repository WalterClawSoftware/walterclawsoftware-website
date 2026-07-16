# Project Status

Last updated: 2026-07-15

This file is public-safe because Netlify publishes the repository root. Live Git, GitHub, App Store Connect, Microsoft Store, Netlify, and `https://walterclawsoftware.com` override this handoff when they differ.

## Current Product State

- The repository root is the Netlify publish directory for the active Walter Claw Software LLC website.
- The homepage names Threshold Lab, Unspoken Room, and Genome Explorer as projects in development. Unspoken Room is identified as the next planned release and links to `https://unspokenroom.app/`; no release date or final feature set is announced.
- Genome Explorer now has private draft records reserved in App Store Connect and Microsoft Partner Center, and `genomeexplorer.app` is registered. It remains unavailable for download and has no announced release date or final feature set.
- Simple Voice Reader is free on iPhone, iPad, Mac, and Windows.
- macOS 1.1 is Ready for Sale. It uses local Kokoro and installed Apple voices, exports WAV or MP3, and includes resumable Smart Chapter Export.
- The Windows release is public in Microsoft Store under product ID `9NJ66Q625LL6`. It uses local Kokoro and installed Windows voices, exports MP3, WAV, FLAC, OGG, or AIFF, and includes Smart Chapter Export.
- iOS/iPadOS 1.0.1 is public with installed Apple voices, background playback, and Lock Screen controls. Audio export is not part of the mobile app.
- iOS/iPadOS 1.1, including an optional approximately 170 MB Kokoro pack for compatible iOS/iPadOS 26+ devices with at least 5 GB of memory, is Waiting for Review. Apple voices remain the immediate and fallback engine.
- Text, documents, and rendered audio stay on the user's device. Apple or Microsoft may be contacted only to obtain system voice assets, and Apple hosts the optional mobile Kokoro pack download.

## Completed Work

- Added a restrained homepage section for Threshold Lab, Unspoken Room, and Genome Explorer, then identified Unspoken Room as the next planned release and linked its dedicated website without making a release-date or final-feature claim.
- Reserved the exact `Genome Explorer` app name for a macOS record in App Store Connect and an MSIX or PWA app in Microsoft Partner Center, and registered `genomeexplorer.app` through Porkbun.
- Rebuilt the Simple Voice Reader product page around the verified Mac, Windows, iPhone, and iPad editions, with platform-specific capabilities and requirements.
- Added real iPhone and Windows product screenshots while retaining the current Mac screenshot.
- Replaced the Microsoft Store search URL with the permanent product-detail URL.
- Updated product metadata, JSON-LD, privacy, support, homepage, About, Store FAQ, Updates, and storefront configuration.
- Clarified that audio and Smart Chapter export are desktop-only and documented each desktop platform's actual export formats.
- Removed stale desktop-only language from the shared site footer.

## Verification

- Parsed all 20 HTML files and 44 JSON-LD blocks, checked 915 local `href` and `src` references, verified the unique external CTA and its safety attributes, and ran `git diff --check`; all passed.
- Tested the revised Unspoken Room card locally and on Netlify preview `6a5838e4510340d877a2bdcf` at desktop and phone widths. The longer status badge, copy, and button remained readable and free of horizontal overflow or browser warning/error.
- Direct HTTPS checks confirmed `https://unspokenroom.app/` returns HTTP 200 and identifies itself as the intended Unspoken Room Mac preview.
- Netlify production deploy `6a583927bd28be00086f0908` reported ready for customer-facing revision `7dff49c90490c55ea2f560ebb6f24d1a50fad895`.
- Cache-busted production readback returned HTTP 200 with the next-release wording and `unspokenroom.app` CTA. Live `index.html` was byte-for-byte identical to the verified repository file, and the live phone-width card had no overflow or browser warning/error.
- App Store Connect readback confirmed macOS 1.1 as Ready for Sale and iOS/iPadOS 1.1 as Waiting for Review.
- Apple's public listing and Microsoft product-detail page both returned HTTP 200 with the correct Simple Voice Reader titles.
- Tested the product page and support/privacy pages at desktop and phone widths. There was no horizontal overflow, broken media, overlap, or browser console warning/error.
- Netlify preview `6a56cf424db301cb324144cb` returned HTTP 200 for the product, support, privacy, site-wide supporting pages, and both new screenshot assets. Preview copy assertions passed.
- Cache-busted production readback returned HTTP 200 for the same routes and assets, and exact copy assertions passed. The live desktop and phone layouts had no overflow, broken media, or browser console warning/error.
- Porkbun Domain Management listed `genomeexplorer.app` as a new domain in the account with expiration date 2027-07-16.
- App Store Connect showed `Genome Explorer` as macOS 1.0 Prepare for Submission. App Information confirmed Apple ID `6791394608`, bundle ID `com.walterclawsoftware.genomeexplorer`, SKU `GENOMEEXPLORER-MACOS-2026`, and primary language English (U.S.).
- Microsoft Partner Center showed `Genome Explorer` as an In draft MSIX or PWA app. Manage app names reported `Reserved for this app`, and Product Identity confirmed Store ID `9N6CJ95SQR49`, identity name `WalterClawSoftwareLLC.GenomeExplorer`, and PFN `WalterClawSoftwareLLC.GenomeExplorer_jvgzfyt5v7qd8`.

## External State

- App Store Connect now contains the private draft Genome Explorer macOS record with Apple ID `6791394608`.
- Microsoft Partner Center now contains the private draft Genome Explorer MSIX or PWA product with Store ID `9N6CJ95SQR49`.
- Porkbun now contains `genomeexplorer.app`, registered through 2027-07-16.
- The homepage now links to the live `https://unspokenroom.app/` preview and identifies Unspoken Room as the next planned release.
- GitHub `main` published customer-facing revision `7dff49c90490c55ea2f560ebb6f24d1a50fad895`.
- Netlify production deployment `6a583927bd28be00086f0908` published and verified that revision at `https://walterclawsoftware.com`.

## Known Risks

- Unspoken Room is publicly identified as the next planned release, but no date or final feature set is announced. Keep `unspokenroom.app` and the Walter Claw homepage aligned, and do not use available-now language until the customer artifact and public release state are verified.
- Microsoft states that the Genome Explorer name reservation must be followed by a Store submission within three months or the reservation can be lost.
- Genome Explorer's implemented app source is intentionally kept outside Git in its approved local-only privacy workspace; the reserved Apple and Microsoft identities are not yet wired into a customer build.
- Store and domain availability do not establish trademark rights; complete a separate brand review before public launch.
- iOS/iPadOS 1.1 remains subject to Apple review. Do not describe the optional mobile Kokoro pack as publicly available until the public App Store release confirms it.
- Store state and product capabilities can drift from static website copy; verify live records before future availability changes.

## Next Recommended Action

- Prepare and verify the Unspoken Room customer artifact and public release state before changing its next-release wording to available-now language. Separately, preserve Genome Explorer's Microsoft reservation before its three-month deadline and update the Simple Voice Reader review language after Apple releases iOS/iPadOS 1.1.
