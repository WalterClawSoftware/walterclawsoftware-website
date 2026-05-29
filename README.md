# Walter Claw Software Website

Public static website for **Walter Claw Software LLC**.

- Live site: <https://walterclawsoftware.com/>
- GitHub source: <https://github.com/WalterClawSoftware/walterclawsoftware-website>
- Support contact shown on the site: <support@walterclawsoftware.com>

## Public pages

- `index.html` — company homepage and product picker
- `about.html` — company/product context
- `clipscript.html` — ClipScript product page
- `transcript-rescue.html` — Transcript Rescue product page
- `repro-pack.html` — Repro Pack product page
- `bannersafe-youtube.html` — BannerSafe for YouTube product page
- `app-icon-creator.html` — App Icon Creator product page
- `privacy.html` — privacy policy
- `support.html` — support entry point
- `contact.html` — business/contact page
- `purchase-faq.html` — checkout and platform FAQ
- `updates.html` — public product/site updates

## Buyer-trust principles

The website is a public trust surface as well as a marketing site. Keep changes aligned with the current style:

- honest, specific product pages instead of broad platform claims;
- real screenshots and plain limitations before purchase CTAs;
- clear platform/store status and one-time pricing;
- direct support and privacy/contact links easy to find;
- no invented testimonials, customer logos, usage counts, or unverifiable proof.

## Fast local preview

From the repository root:

```bash
python3 -m http.server 8080
```

Then open <http://localhost:8080/>.

For local route checks, open the `.html` filenames directly when needed. Netlify's extensionless routes are handled by `_redirects`, which `python3 -m http.server` does not apply.

## Netlify

This repository is configured for a simple static Netlify deployment.

- Netlify project: `walter-claw-software`
- Publish directory: repository root
- Build command: none
- Redirect rules: `_redirects` at repo root
