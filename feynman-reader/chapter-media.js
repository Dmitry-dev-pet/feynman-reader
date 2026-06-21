(() => {
  const panels = [...document.querySelectorAll(".chapter-media-panel")];
  if (!panels.length) return;

  const parseStart = (value) => {
    if (!value) return 0;
    if (/^\d+$/.test(value)) return Number(value);
    const match = value.match(/(?:(\d+)h)?(?:(\d+)m)?(?:(\d+)s)?/i);
    if (!match) return 0;
    return (Number(match[1] || 0) * 3600) + (Number(match[2] || 0) * 60) + Number(match[3] || 0);
  };

  const toEmbedUrl = (href) => {
    const url = new URL(href, window.location.href);
    let id = "";
    if (url.hostname.includes("youtu.be")) {
      id = url.pathname.split("/").filter(Boolean)[0] || "";
    } else if (url.hostname.includes("youtube.com")) {
      id = url.searchParams.get("v") || url.pathname.split("/embed/")[1] || "";
    }
    if (!id) return "";
    const start = parseStart(url.searchParams.get("t") || url.searchParams.get("start"));
    const embed = new URL(`https://www.youtube-nocookie.com/embed/${id}`);
    embed.searchParams.set("rel", "0");
    embed.searchParams.set("modestbranding", "1");
    embed.searchParams.set("playsinline", "1");
    if (start) embed.searchParams.set("start", String(start));
    return embed.toString();
  };

  const isRu = () => (document.documentElement.lang || "").toLowerCase().startsWith("ru");
  const typeOf = (link) => /слушать|listen/i.test(link.textContent || "") ? "audio" : "video";
  const chapterTitleFor = (panel) => panel.dataset.chapterTitle || panel.querySelector(".chapter-media-copy strong")?.textContent?.trim() || "";
  const labelFor = (panel, type) => {
    const title = chapterTitleFor(panel);
    const mode = isRu()
      ? (type === "audio" ? "аудио" : "видео")
      : (type === "audio" ? "audio" : "video");
    if (title) return `${title} · ${mode}`;
    if (isRu()) return type === "audio" ? "Аудио главы" : "Видео главы";
    return type === "audio" ? "Chapter audio" : "Chapter video";
  };

  const ensurePlayer = (panel) => {
    let player = panel.querySelector(".chapter-media-player");
    if (player) return player;
    player = document.createElement("div");
    player.className = "chapter-media-player";
    player.hidden = true;
    player.innerHTML = `
      <div class="chapter-media-frame-wrap">
        <iframe loading="lazy" referrerpolicy="strict-origin-when-cross-origin" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>
      </div>
      <div class="chapter-media-player-footer">
        <span class="chapter-media-player-label"></span>
        <a class="chapter-media-youtube" href="#" target="_blank" rel="noopener">${isRu() ? "Открыть на YouTube" : "Open on YouTube"}</a>
      </div>`;
    panel.append(player);
    return player;
  };

  const activate = (link, { scroll = false } = {}) => {
    const panel = link.closest(".chapter-media-panel");
    const embedUrl = toEmbedUrl(link.href);
    if (!panel || !embedUrl) return false;
    const type = typeOf(link);
    const player = ensurePlayer(panel);
    const iframe = player.querySelector("iframe");
    const label = player.querySelector(".chapter-media-player-label");
    const youtube = player.querySelector(".chapter-media-youtube");
    player.classList.toggle("is-audio", type === "audio");
    player.classList.toggle("is-video", type === "video");
    iframe.src = embedUrl;
    const mediaLabel = labelFor(panel, type);
    iframe.title = mediaLabel;
    label.textContent = mediaLabel;
    youtube.href = link.href;
    player.hidden = false;
    panel.querySelectorAll(".chapter-media-link").forEach((item) => {
      const active = item === link;
      item.classList.toggle("is-active", active);
      item.setAttribute("aria-pressed", active ? "true" : "false");
    });
    if (scroll) panel.scrollIntoView({ block: "start", inline: "nearest" });
    return true;
  };

  document.addEventListener("click", (event) => {
    const link = event.target.closest(".chapter-media-link");
    if (!link) return;
    if (!toEmbedUrl(link.href)) return;
    event.preventDefault();
    activate(link);
  });

  const openFromHash = () => {
    const hash = decodeURIComponent(window.location.hash || "");
    if (!hash.startsWith("#chapter-media")) return;
    const panel = panels[0];
    const links = [...panel.querySelectorAll(".chapter-media-link")];
    const wanted = hash.includes("audio") ? "audio" : hash.includes("watch") || hash.includes("video") ? "video" : "";
    const link = links.find((item) => wanted && typeOf(item) === wanted) || links[0];
    if (link) activate(link, { scroll: true });
  };

  window.addEventListener("hashchange", openFromHash);
  window.addEventListener("load", openFromHash);
  openFromHash();
})();
