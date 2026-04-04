# ClipScript Storefront Setup

This site is now storefront-ready for direct-download sales. The remaining go-live work is:

1. Create the downloadable Mac archive.
2. Upload that file to a hosted checkout provider.
3. Paste the provider checkout URL into `storefront-config.js`.
4. Deploy the updated site.

## Recommended first pass

Use Lemon Squeezy for the initial direct-download paywall.

Why:

- Hosted checkout works well with a static site.
- Digital products can include downloadable app files.
- Existing customers can get the newest file when you update the product.

Official docs:

- Product files and checkout sharing:
  - https://docs.lemonsqueezy.com/help/products/adding-products
- Test mode:
  - https://docs.lemonsqueezy.com/help/getting-started/test-mode
- Store activation:
  - https://docs.lemonsqueezy.com/help/getting-started/activate-your-store

## Important Lemon Squeezy notes

- Test mode is on by default for a new store.
- File downloads are disabled for test-mode purchases.
- Products created in test mode do not automatically appear in live mode. Copy them to live mode after store activation.
- Live selling requires store activation and identity verification.

## Current release status

- macOS: release build exists locally and can be packaged for download.
- Windows: direct-download storefront is staged on the site, but there is no Windows release file in the repo yet.

Current Mac archive already created on this machine:

- File: `/Users/jeffreywaters/Documents/Walter Claw Software LLC/clipscript/release/ClipScript-macOS-0.1.0.zip`
- Size: about `46 MB`
- SHA-256:
  - `fb3d6dccaaed163d3334ba4ded71490469ab51c8b0117e38f653644485f1aea1`

## Create the macOS archive

Use the current packaged app and make a zip that preserves the `.app` bundle:

```bash
cd "/Users/jeffreywaters/Documents/Walter Claw Software LLC/clipscript"
mkdir -p release
ditto -c -k --sequesterRsrc --keepParent dist/ClipScript.app "release/ClipScript-macOS-0.1.0.zip"
shasum -a 256 "release/ClipScript-macOS-0.1.0.zip"
```

Recommended upload target for Lemon Squeezy:

- Product name: `ClipScript`
- Variant name: `macOS direct download`
- File: `release/ClipScript-macOS-0.1.0.zip`

## Connect the website button

Once you have the hosted checkout URL:

1. Open `storefront-config.js`
2. Set the macOS `checkoutUrl`

Example:

```js
window.WCSStorefront = {
    "clipscript-macos": {
        checkoutUrl: "https://your-store.lemonsqueezy.com/buy/your-mac-checkout",
        liveLabel: "Buy for macOS",
        pendingLabel: "macOS checkout coming next",
        helperText: "Secure checkout and direct file delivery are now live for the macOS release."
    },
    "clipscript-windows": {
        checkoutUrl: "",
        liveLabel: "Buy for Windows",
        pendingLabel: "Windows coming soon",
        helperText: "The Windows direct-download checkout will be enabled after the Windows release file is ready."
    }
};
```

## Suggested product setup in Lemon Squeezy

- Product: `ClipScript`
- Variant 1: `macOS direct download`
- Optional later variant: `Windows direct download`
- Add support link to:
  - `https://walterclawsoftware.com/support.html`
- Add privacy link to:
  - `https://walterclawsoftware.com/privacy.html`
- In the confirmation and receipt copy, tell buyers that download access is delivered directly after purchase.

## Site files touched for storefront launch

- `clipscript.html`
- `index.html`
- `support.html`
- `contact.html`
- `privacy.html`
- `styles.css`
- `storefront-config.js`
- `storefront.js`

## Honest launch posture

The site is now structured so macOS can go live first without pretending the Windows download is ready before it actually exists.
