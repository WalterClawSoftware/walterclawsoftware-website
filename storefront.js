document.addEventListener("DOMContentLoaded", () => {
    const config = window.WCSStorefront || {};

    document.querySelectorAll("[data-storefront-card]").forEach((card) => {
        const productKey = card.getAttribute("data-storefront-card");
        const product = config[productKey];
        if (!product) {
            return;
        }

        const cta = card.querySelector("[data-storefront-cta]");
        const helper = card.querySelector("[data-storefront-helper]");
        if (!cta) {
            return;
        }

        if (product.checkoutUrl) {
            cta.textContent = product.liveLabel || "Buy now";
            cta.setAttribute("href", product.checkoutUrl);
            cta.removeAttribute("aria-disabled");
            cta.classList.remove("button-disabled");
        } else {
            cta.textContent = product.pendingLabel || "Checkout coming soon";
            cta.setAttribute("href", "#storefront");
            cta.setAttribute("aria-disabled", "true");
            cta.classList.add("button-disabled");
        }

        if (helper && product.helperText) {
            helper.textContent = product.helperText;
        }
    });
});
