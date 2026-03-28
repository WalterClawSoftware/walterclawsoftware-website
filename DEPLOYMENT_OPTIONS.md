# Deployment Options

This site is static HTML and CSS, so it can be deployed without a build step.

## Fastest public URL today

1. Netlify manual static deployment
2. Cloudflare Pages direct upload
3. GitHub Pages

## Recommended path today

If you need a public site quickly for Microsoft Partner Center, use Netlify first. It is the simplest path for this static website repo when speed matters more than long-term infrastructure.

## Netlify today

Official docs:

- https://docs.netlify.com/site-deploys/create-deploys/

Suggested flow:

1. Create a Netlify account.
2. Either connect this repository to GitHub for continuous deployment or drag the contents of `C:\walterclawsoftware-website` into a manual deploy.
3. Let Netlify assign a temporary public URL.
4. Use that temporary URL for Partner Center until you are ready to connect a custom domain.

## Cloudflare Pages today

Official docs:

- https://developers.cloudflare.com/pages/get-started/direct-upload/

Suggested flow:

1. Create a Cloudflare account.
2. Create a Pages project by direct upload.
3. Upload the site folder contents.
4. Use the generated Pages URL until you are ready to attach a custom domain.

## GitHub Pages later

Official docs:

- https://docs.github.com/en/pages

GitHub Pages is fine, but it is not the fastest path if your goal is to get a business site live this afternoon.
