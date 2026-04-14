# ClipScript Storefront Setup

This site is now live for ClipScript's macOS direct-download storefront.

## Current approved state

- Lemon Squeezy application: approved
- Storefront product: `ClipScript`
- Current price: `USD 24.99` one-time purchase
- Current direct-download platform: `macOS`
- Current fulfillment file: `/Users/jeffreywaters/Documents/Walter Claw Software LLC/clipscript/release/ClipScript-macOS-1.1.0.dmg`
- Support email used in fulfillment copy: `support@walterclawsoftware.com`
- Custom store domain: `https://store.walterclawsoftware.com`

## Verified checkout behavior

- The public ClipScript store homepage loads on `store.walterclawsoftware.com`.
- The hosted checkout button on the main website currently points to Lemon Squeezy's generated checkout URL:
  - `https://walterclawsoftware.lemonsqueezy.com/checkout/buy/ec986bf5-14cc-4b32-ba46-d9f39cd26370`
- The custom-domain buy path also works, but it currently redirects into Lemon Squeezy's canonical cart flow on `walterclawsoftware.lemonsqueezy.com`.
- The branded store domain is working correctly for the storefront, while the actual cart and checkout still finish on Lemon Squeezy's hosted checkout domain.
- The hosted checkout page resolves to the live `ClipScript` product and shows the current one-time price of `$24.99`.

## Checks that still need a real buyer flow or dashboard review

- A full live purchase is still needed to confirm the buyer receives the current `ClipScript-macOS-1.1.0.dmg` file after payment.
- The Lemon Squeezy checkout payload currently shows blank custom confirmation fields, so the thank-you note and post-purchase confirmation copy should be reviewed in the dashboard.
- The support email was changed to `support@walterclawsoftware.com`, but that should still be confirmed in the final fulfillment email content.

## Website copy that should stay aligned

- `clipscript.html` should say buyers receive the current `DMG`, not a ZIP or a generic "app package."
- `storefront-config.js` should keep the live checkout URL plus DMG-specific helper text.
- The product page media should point at the current real demo video when available.

## Current website assets

- Demo video: `/Users/jeffreywaters/Documents/Walter Claw Software LLC/walterclawsoftware-website/assets/videos/ClipScript-Demo.mp4`
- Demo poster: `/Users/jeffreywaters/Documents/Walter Claw Software LLC/walterclawsoftware-website/assets/screenshots/ClipScript-Demo-Poster.png`

## Next storefront tasks

- Verify one full live purchase and DMG download with a non-owner buyer flow.
- Improve ClipScript product media inside Lemon Squeezy to match the public website.
- Review and polish the thank-you note and fulfillment wording if needed.
- Replace demo assets again when a newer walkthrough is ready.
- Add the Windows product variant once a Windows build exists.

## Reference docs

- Product files and checkout sharing:
  - https://docs.lemonsqueezy.com/help/products/adding-products
- Test mode:
  - https://docs.lemonsqueezy.com/help/getting-started/test-mode
- Store activation:
  - https://docs.lemonsqueezy.com/help/getting-started/activate-your-store

Example storefront config:

```js
window.WCSStorefront = {
    "clipscript-macos": {
        checkoutUrl: "https://walterclawsoftware.lemonsqueezy.com/checkout/buy/ec986bf5-14cc-4b32-ba46-d9f39cd26370",
        liveLabel: "Buy for macOS",
        pendingLabel: "Available now",
        helperText: "Secure hosted checkout is now live for the macOS direct-download release. After purchase, download the current ClipScript DMG and follow the included installation instructions."
    },
    "clipscript-windows": {
        checkoutUrl: "",
        liveLabel: "Buy for Windows",
        pendingLabel: "Windows coming soon",
        helperText: "The Windows direct-download checkout will be enabled after the Windows release file is ready."
    }
};
```
