(() => {
  const cards = [...document.querySelectorAll(".study-youtube-card")];
  if (!cards.length) return;

  const isRu = () => (document.documentElement.lang || "").toLowerCase().startsWith("ru");
  const isAudioCard = (card) => {
    const text = [
      card.querySelector("strong")?.textContent || "",
      card.querySelector("iframe")?.title || "",
      card.querySelector("span")?.textContent || "",
    ].join(" ");
    return /аудио|audio/i.test(text) && !/видео|video/i.test(card.querySelector("strong")?.textContent || "");
  };

  const ensureFloatingPlayer = () => {
    let player = document.querySelector(".floating-youtube-player");
    if (player) return player;
    player = document.createElement("aside");
    player.className = "floating-youtube-player";
    player.hidden = true;
    player.setAttribute("aria-live", "polite");
    player.innerHTML = `
      <div class="floating-youtube-header">
        <span class="floating-youtube-label"></span>
        <button class="floating-youtube-close" type="button" aria-label="${isRu() ? "Закрыть плеер" : "Close player"}" title="${isRu() ? "Закрыть" : "Close"}">×</button>
      </div>
      <div class="floating-youtube-frame">
        <iframe loading="lazy" referrerpolicy="strict-origin-when-cross-origin" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>
      </div>
      <a class="floating-youtube-link" href="#" target="_blank" rel="noopener">${isRu() ? "Открыть на YouTube" : "Open on YouTube"}</a>`;
    document.body.append(player);
    player.querySelector(".floating-youtube-close").addEventListener("click", () => {
      player.querySelector("iframe").removeAttribute("src");
      player.hidden = true;
      document.querySelectorAll(".study-youtube-card.is-playing").forEach((card) => card.classList.remove("is-playing"));
    });
    return player;
  };

  const withAutoplay = (src) => {
    const url = new URL(src, window.location.href);
    url.searchParams.set("autoplay", "1");
    url.searchParams.set("playsinline", "1");
    return url.toString();
  };

  const openAudio = (card) => {
    const iframe = card.querySelector("iframe");
    const link = card.querySelector(".study-youtube-link");
    const src = iframe?.dataset.src || iframe?.src || "";
    if (!src) return;
    const title = iframe?.title || card.querySelector("strong")?.textContent?.trim() || (isRu() ? "Аудиообзор" : "Audio");
    const player = ensureFloatingPlayer();
    player.querySelector(".floating-youtube-label").textContent = title;
    player.querySelector(".floating-youtube-link").href = link?.href || src;
    const playerFrame = player.querySelector("iframe");
    playerFrame.title = title;
    playerFrame.src = withAutoplay(src);
    player.hidden = false;
    document.querySelectorAll(".study-youtube-card.is-playing").forEach((item) => item.classList.remove("is-playing"));
    card.classList.add("is-playing");
  };

  cards.forEach((card) => {
    if (!isAudioCard(card)) return;
    const iframe = card.querySelector("iframe");
    if (!iframe) return;
    iframe.dataset.src = iframe.src;
    iframe.removeAttribute("src");
    card.classList.add("is-audio-card");
    if (card.querySelector(".study-youtube-play")) return;
    const button = document.createElement("button");
    button.className = "study-youtube-play";
    button.type = "button";
    button.textContent = isRu() ? "Слушать" : "Listen";
    button.addEventListener("click", () => openAudio(card));
    card.querySelector(".study-youtube-embed")?.before(button);
  });
})();
