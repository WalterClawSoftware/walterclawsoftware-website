# Project Status

Last updated: 2026-07-15

This file is public-safe because Netlify publishes the repository root. Live Git, GitHub, App Store Connect, Microsoft Store, Netlify, and `https://walterclawsoftware.com` override this handoff when they differ.

## Current Product State

- The repository root is the Netlify publish directory for the active Walter Claw Software LLC website.
- The homepage names Threshold Lab, Unspoken Room, and Genome Explorer as projects in development without announcing downloads, release dates, platforms, or final feature sets.
- Simple Voice Reader is free on iPhone, iPad, Mac, and Windows.
- macOS 1.1 is Ready for Sale. It uses local Kokoro and installed Apple voices, exports WAV or MP3, and includes resumable Smart Chapter Export.
- The Windows release is public in Microsoft Store under product ID `9NJ66Q625LL6`. It uses local Kokoro and installed Windows voices, exports MP3, WAV, FLAC, OGG, or AIFF, and includes Smart Chapter Export.
- iOS/iPadOS 1.0.1 is public with installed Apple voices, background playback, and Lock Screen controls. Audio export is not part of the mobile app.
- iOS/iPadOS 1.1, including an optional approximately 170 MB Kokoro pack for compatible iOS/iPadOS 26+ devices with at least 5 GB of memory, is Waiting for Review. Apple voices remain the immediate and fallback engine.
- Text, documents, and rendered audio stay on the user's device. Apple or Microsoft may be contacted only to obtain system voice assets, and Apple hosts the optional mobile Kokoro pack download.

## Completed Work

- Added a restrained homepage section for Threshold Lab, Unspoken Room, and Genome Explorer, with no product-page links or availability claims.
- Rebuilt the Simple Voice Reader product page around the verified Mac, Windows, iPhone, and iPad editions, with platform-specific capabilities and requirements.
- Added real iPhone and Windows product screenshots while retaining the current Mac screenshot.
- Replaced the Microsoft Store search URL with the permanent product-detail URL.
- Updated product metadata, JSON-LD, privacy, support, homepage, About, Store FAQ, Updates, and storefront configuration.
- Clarified that audio and Smart Chapter export are desktop-only and documented each desktop platform's actual export formats.
- Removed stale desktop-only language from the shared site footer.

## Verification

- Parsed all 20 HTML files and 44 JSON-LD blocks, checked 914 local `href` and `src` references, and ran `git diff --check`; all passed.
- Tested the new section locally and on Netlify preview `6a5832167526f8bcbee80a1f` at desktop and phone widths. The three cards remained readable, responsive, and free of horizontal overflow or browser warning/error.
- Netlify production deploy `6a5832882fcc580009b16901` reported ready for customer-facing revision `56a4ecd3d6e35a9ad2221e59f378ea6283147bbd`.
- Cache-busted production readback returned HTTP 200 with all three project names, three development status chips, and the full cautionary disclaimer. Live `index.html` and `styles.css` were byte-for-byte identical to the verified repository files.
- App Store Connect readback confirmed macOS 1.1 as Ready for Sale and iOS/iPadOS 1.1 as Waiting for Review.
- Apple's public listing and Microsoft product-detail page both returned HTTP 200 with the correct Simple Voice Reader titles.
- Tested the product page and support/privacy pages at desktop and phone widths. There was no horizontal overflow, broken media, overlap, or browser console warning/error.
- Netlify preview `6a56cf424db301cb324144cb` returned HTTP 200 for the product, support, privacy, site-wide supporting pages, and both new screenshot assets. Preview copy assertions passed.
- Cache-busted production readback returned HTTP 200 for the same routes and assets, and exact copy assertions passed. The live desktop and phone layouts had no overflow, broken media, or browser console warning/error.

## External State

- No Apple or Microsoft store record was changed during this website update.
- GitHub `main` published customer-facing revision `56a4ecd3d6e35a9ad2221e59f378ea6283147bbd`.
- Netlify production deployment `6a5832882fcc580009b16901` published and verified that revision at `https://walterclawsoftware.com`.

## Known Risks

- The three development project names are public, but their scope and release plans remain unsettled. Keep future copy equally limited until details can be verified.
- iOS/iPadOS 1.1 remains subject to Apple review. Do not describe the optional mobile Kokoro pack as publicly available until the public App Store release confirms it.
- Store state and product capabilities can drift from static website copy; verify live records before future availability changes.

## Next Recommended Action

- Keep the development-project wording limited until one project is ready for a verified public introduction; separately, update the Simple Voice Reader review language after Apple releases iOS/iPadOS 1.1.
