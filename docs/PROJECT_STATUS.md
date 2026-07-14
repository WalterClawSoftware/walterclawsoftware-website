# Project Status

Last updated: 2026-07-12

This document is public-safe because Netlify publishes the repository root. Live Git, Netlify, public storefronts, and `https://walterclawsoftware.com` override this handoff when they differ.

## Current Product State

- Active public static website for Walter Claw Software LLC.
- The repository root is the Netlify publish directory.
- Product pages emphasize honest capabilities, real screenshots, privacy/support links, and current store availability.

## Recently Completed

- Restored accurate WAV, MP3, and Smart Chapter Export coverage across the
  Simple Voice Reader product, support, privacy, FAQ, and structured-data copy
  while retaining the newer local-processing and Kokoro disclosures.
- Replaced the Mac product screenshots with current light and dark images that
  visibly show Export, WAV/MP3 selection, and Smart Chapter Export.
- Labeled macOS 1.1 as being in final release testing rather than implying that
  its Kokoro build is already available from the App Store.
- Updated the homepage, Simple Voice Reader product page, storefront configuration, metadata, structured data, FAQ, and update history to show live Apple App Store and Microsoft Store availability.
- Added the live Apple listing for iPhone, iPad, and Mac and a Microsoft Store search link for the Windows listing.
- Split the Apple storefront call to action into clearly labeled Mac and iPhone/iPad buttons; the Mac link uses Apple’s `mt=12` platform hint.
- Clarified Simple Voice Reader’s local text-to-speech privacy wording.
- Established the shared Codex/Hermes continuity contract.

## Verification

- Parsed all three changed HTML pages, validated every JSON-LD block, and
  confirmed referenced image assets exist.
- Local HTTP smoke checks returned 200 for the product, privacy, support, and
  screenshot assets. Both screenshot PNGs are 1280x800 without alpha and were
  visually inspected after derivation from the release screenshots.
- Apple’s public lookup API returned Simple Voice Reader as a free app under ID `6787165967`, supporting iPhone, iPad, and Mac.
- Microsoft Store availability was supplied by the product owner; the public site points to Microsoft Store search until a stable product-detail URL is recorded.
- Clean GitHub-origin continuity checkout inspected.
- No customer-facing HTML, assets, redirects, sitemap, or Netlify configuration changed in this continuity update.

## External State

- Live product availability and prices must be verified against Apple/Microsoft storefronts before changing website claims.
- The current Mac App Store release remains 1.0.1; macOS 1.1 is still in final
  local release testing and has not been represented as available.

## Known Issues and Risks

- Static copy can drift from store state or application capabilities.
- Replace the macOS 1.1 testing language only after App Store Connect and the
  public storefront confirm the corresponding state.
- Any future status update committed here must remain suitable for public exposure.

## Next Recommended Action

- After macOS 1.1 is submitted and released, update its release-state language
  from verified App Store Connect and public storefront evidence. Replace the
  Microsoft Store search URL when its stable product-detail URL is recorded.
