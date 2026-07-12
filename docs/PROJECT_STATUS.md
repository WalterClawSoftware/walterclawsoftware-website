# Project Status

Last updated: 2026-07-12

This document is public-safe because Netlify publishes the repository root. Live Git, Netlify, public storefronts, and `https://walterclawsoftware.com` override this handoff when they differ.

## Current Product State

- Active public static website for Walter Claw Software LLC.
- The repository root is the Netlify publish directory.
- Product pages emphasize honest capabilities, real screenshots, privacy/support links, and current store availability.

## Recently Completed

- Updated the homepage, Simple Voice Reader product page, storefront configuration, metadata, structured data, FAQ, and update history to show live Apple App Store and Microsoft Store availability.
- Added the live Apple listing for iPhone, iPad, and Mac and a Microsoft Store search link for the Windows listing.
- Split the Apple storefront call to action into clearly labeled Mac and iPhone/iPad buttons; the Mac link uses Apple’s `mt=12` platform hint.
- Clarified Simple Voice Reader’s local text-to-speech privacy wording.
- Established the shared Codex/Hermes continuity contract.

## Verification

- Apple’s public lookup API returned Simple Voice Reader as a free app under ID `6787165967`, supporting iPhone, iPad, and Mac.
- Microsoft Store availability was supplied by the product owner; the public site points to Microsoft Store search until a stable product-detail URL is recorded.
- Clean GitHub-origin continuity checkout inspected.
- No customer-facing HTML, assets, redirects, sitemap, or Netlify configuration changed in this continuity update.

## External State

- Live product availability and prices must be verified against Apple/Microsoft storefronts before changing website claims.

## Known Issues and Risks

- Static copy can drift from store state or application capabilities.
- Any future status update committed here must remain suitable for public exposure.

## Next Recommended Action

- Replace the Microsoft Store search URL with the stable product-detail URL when its product ID is recorded, then smoke-check both storefront links.
