(() => {
    const posters = document.querySelectorAll(".demo-video-poster[data-youtube-id]");

    posters.forEach((poster) => {
        poster.addEventListener("click", () => {
            const videoId = poster.dataset.youtubeId;
            if (!videoId || /[^a-zA-Z0-9_-]/.test(videoId)) {
                return;
            }

            const title = poster.dataset.youtubeTitle || "Product demo video";
            const iframe = document.createElement("iframe");
            iframe.className = "demo-video-embed";
            iframe.src = `https://www.youtube-nocookie.com/embed/${videoId}?rel=0&autoplay=1`;
            iframe.title = title;
            iframe.loading = "lazy";
            iframe.referrerPolicy = "strict-origin-when-cross-origin";
            iframe.allow = "accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share";
            iframe.allowFullscreen = true;

            poster.replaceWith(iframe);
            iframe.focus();
        }, { once: true });
    });
})();
