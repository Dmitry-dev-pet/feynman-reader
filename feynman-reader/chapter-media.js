(() => {
  if (window.__feynmanMediaPlayerLoading) return;
  window.__feynmanMediaPlayerLoading = true;
  const script = document.createElement("script");
  script.defer = true;
  script.src = new URL(
    "media-player.js?v=20260621-manifest-runtime",
    document.currentScript?.src || window.location.href,
  ).toString();
  document.head.append(script);
})();
