# Walter Claw Software Website

This repository contains the standalone static company website for `Walter Claw Software LLC`.

Pages included:

- `index.html`
- `clipscript.html`
- `privacy.html`
- `support.html`
- `contact.html`

## Fast local preview

```powershell
cd C:\walterclawsoftware-website
python -m http.server 8080
```

Then open [http://localhost:8080](http://localhost:8080).

## Netlify

This repository is ready for a simple static Netlify deployment.

- Repository root can be used as the publish directory.
- No build command is required.
- `_redirects` is already included at repo root.
