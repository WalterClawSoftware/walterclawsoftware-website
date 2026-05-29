(() => {
    const safeYouTubeId = (id) => Boolean(id) && !/[^a-zA-Z0-9_-]/.test(id);
    const embedSrc = (id) => `https://www.youtube-nocookie.com/embed/${id}?rel=0&autoplay=1`;

    const setupDirectVideoPosters = () => {
        const posters = document.querySelectorAll(".demo-video-poster[data-youtube-id]");

        posters.forEach((poster) => {
            poster.addEventListener("click", () => {
                const videoId = poster.dataset.youtubeId;
                if (!safeYouTubeId(videoId)) {
                    return;
                }

                const title = poster.dataset.youtubeTitle || "Product demo video";
                const iframe = document.createElement("iframe");
                iframe.className = "demo-video-embed";
                iframe.src = embedSrc(videoId);
                iframe.title = title;
                iframe.loading = "lazy";
                iframe.referrerPolicy = "strict-origin-when-cross-origin";
                iframe.allow = "accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share";
                iframe.allowFullscreen = true;

                poster.replaceWith(iframe);
                iframe.focus();
            }, { once: true });
        });
    };

    const lightbox = document.querySelector(".lightbox");
    const mediaItems = Array.from(document.querySelectorAll("[data-gallery-media]"));

    if (!lightbox || mediaItems.length === 0) {
        setupDirectVideoPosters();
        return;
    }

    const panel = lightbox.querySelector(".lightbox-panel");
    const mediaFrame = lightbox.querySelector(".lightbox-media");
    const imageEl = lightbox.querySelector(".lightbox-image");
    const videoEl = lightbox.querySelector(".lightbox-video");
    const captionEl = lightbox.querySelector(".lightbox-caption");
    const closeButtons = lightbox.querySelectorAll("[data-lightbox-close]");
    const prevButton = lightbox.querySelector("[data-lightbox-prev]");
    const nextButton = lightbox.querySelector("[data-lightbox-next]");
    let currentIndex = 0;
    let lastFocus = null;

    if (!panel || !mediaFrame || !imageEl || !videoEl || !captionEl || !prevButton || !nextButton) {
        setupDirectVideoPosters();
        return;
    }

    const getType = (item) => item.dataset.galleryMedia || "image";

    const getMediaAspectRatio = (item) => {
        const explicitWidth = Number(item.dataset.galleryWidth || item.dataset.width);
        const explicitHeight = Number(item.dataset.galleryHeight || item.dataset.height);
        if (explicitWidth > 0 && explicitHeight > 0) {
            return explicitWidth / explicitHeight;
        }
        if (getType(item) === "youtube") {
            return 16 / 9;
        }
        const thumb = item.querySelector("img");
        if (thumb && thumb.naturalWidth > 0 && thumb.naturalHeight > 0) {
            return thumb.naturalWidth / thumb.naturalHeight;
        }
        return 16 / 9;
    };

    const sizeLightboxFrame = (item) => {
        const aspectRatio = getMediaAspectRatio(item);
        const maxWidth = Math.min(window.innerWidth * 0.92, 1500);
        const maxHeight = Math.max(window.innerHeight * 0.94 - 110, 300);
        let frameWidth = maxWidth;
        let frameHeight = frameWidth / aspectRatio;

        if (frameHeight > maxHeight) {
            frameHeight = maxHeight;
            frameWidth = frameHeight * aspectRatio;
        }

        mediaFrame.style.width = `${frameWidth}px`;
        mediaFrame.style.height = `${frameHeight}px`;
    };

    const stopVideo = () => {
        videoEl.removeAttribute("src");
        videoEl.title = "";
    };

    const showMedia = (index) => {
        currentIndex = (index + mediaItems.length) % mediaItems.length;
        const item = mediaItems[currentIndex];
        const type = getType(item);
        const title = item.dataset.galleryTitle || item.dataset.youtubeTitle || "";

        sizeLightboxFrame(item);
        captionEl.textContent = title;

        if (type === "youtube") {
            const videoId = item.dataset.galleryYoutubeId || item.dataset.youtubeId;
            if (!safeYouTubeId(videoId)) {
                return;
            }
            imageEl.style.display = "none";
            imageEl.removeAttribute("src");
            videoEl.style.display = "block";
            videoEl.src = embedSrc(videoId);
            videoEl.title = title || "Product demo video";
            return;
        }

        const src = item.dataset.gallerySrc || item.dataset.src;
        if (!src) {
            return;
        }
        stopVideo();
        videoEl.style.display = "none";
        imageEl.style.display = "block";
        imageEl.src = src;
        imageEl.alt = item.dataset.galleryAlt || title || "Product screenshot";
    };

    const openLightbox = (index) => {
        lastFocus = document.activeElement;
        showMedia(index);
        lightbox.classList.add("is-open");
        lightbox.setAttribute("aria-hidden", "false");
        document.body.classList.add("lightbox-open");
        panel.focus({ preventScroll: true });
    };

    const closeLightbox = () => {
        lightbox.classList.remove("is-open");
        lightbox.setAttribute("aria-hidden", "true");
        document.body.classList.remove("lightbox-open");
        stopVideo();
        imageEl.removeAttribute("src");
        if (lastFocus && typeof lastFocus.focus === "function") {
            lastFocus.focus({ preventScroll: true });
        }
    };

    mediaItems.forEach((item, index) => {
        item.addEventListener("click", (event) => {
            event.preventDefault();
            openLightbox(index);
        });
    });

    closeButtons.forEach((button) => button.addEventListener("click", closeLightbox));
    prevButton.addEventListener("click", () => showMedia(currentIndex - 1));
    nextButton.addEventListener("click", () => showMedia(currentIndex + 1));

    document.addEventListener("keydown", (event) => {
        if (!lightbox.classList.contains("is-open")) {
            return;
        }
        if (event.key === "Escape") {
            closeLightbox();
        } else if (event.key === "ArrowLeft") {
            showMedia(currentIndex - 1);
        } else if (event.key === "ArrowRight") {
            showMedia(currentIndex + 1);
        }
    });

    window.addEventListener("resize", () => {
        if (!lightbox.classList.contains("is-open")) {
            return;
        }
        sizeLightboxFrame(mediaItems[currentIndex]);
    });
})();
