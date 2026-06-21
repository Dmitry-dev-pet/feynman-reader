(() => {
  const panel = document.querySelector(".chapter-media-panel");
  const cards = [...document.querySelectorAll(".study-youtube-card")];
  const reportCards = [...document.querySelectorAll(".study-card[href*='notebooklm-briefing.html'], .study-card[href*='notebooklm-study-guide.html']")];
  if (!panel && !cards.length && !reportCards.length) return;

  const MEDIA_INTENT_KEY = "flp-reader-media-intent";
  const isRu = () => (document.documentElement.lang || "").toLowerCase().startsWith("ru");

  const readMediaIntent = () => {
    try {
      return sessionStorage.getItem(MEDIA_INTENT_KEY) || "";
    } catch (_) {
      return "";
    }
  };

  const setMediaIntent = (type) => {
    try {
      sessionStorage.setItem(MEDIA_INTENT_KEY, type);
    } catch (_) {}
  };

  const clearMediaIntent = () => {
    try {
      sessionStorage.removeItem(MEDIA_INTENT_KEY);
    } catch (_) {}
  };

  const parseStart = (value) => {
    if (!value) return 0;
    if (/^\d+$/.test(value)) return Number(value);
    const match = value.match(/(?:(\d+)h)?(?:(\d+)m)?(?:(\d+)s)?/i);
    if (!match) return 0;
    return (Number(match[1] || 0) * 3600) + (Number(match[2] || 0) * 60) + Number(match[3] || 0);
  };

  const toEmbedUrl = (href, { autoplay = false } = {}) => {
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
    if (autoplay) embed.searchParams.set("autoplay", "1");
    if (start) embed.searchParams.set("start", String(start));
    return embed.toString();
  };

  const withAutoplay = (src) => {
    const url = new URL(src, window.location.href);
    url.searchParams.set("autoplay", "1");
    url.searchParams.set("playsinline", "1");
    return url.toString();
  };

  const isPanelAudioLink = (link) => /слушать|listen/i.test(link.textContent || "");
  const isAudioCard = (card) => {
    const title = card.querySelector("strong")?.textContent || "";
    const text = [
      title,
      card.querySelector("iframe")?.title || "",
      card.querySelector("span")?.textContent || "",
    ].join(" ");
    return /аудио|audio/i.test(text) && !/видео|video/i.test(title);
  };

  const setToolbarActive = (type) => {
    document.querySelectorAll(".media-toolbar-btn").forEach((button) => {
      const active = button.dataset.mediaType === type;
      button.classList.toggle("is-active", active);
      button.setAttribute("aria-pressed", active ? "true" : "false");
    });
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
    player.querySelector(".floating-youtube-close").addEventListener("click", closeFloatingAudio);
    return player;
  };

  const openFloatingAudio = ({ embedUrl, label, href }) => {
    const player = ensureFloatingPlayer();
    const iframe = player.querySelector("iframe");
    player.querySelector(".floating-youtube-label").textContent = label;
    player.querySelector(".floating-youtube-link").href = href;
    iframe.title = label;
    iframe.src = embedUrl;
    player.hidden = false;
    setMediaIntent("audio");
    setToolbarActive("audio");
  };

  function closeFloatingAudio() {
    const player = document.querySelector(".floating-youtube-player");
    if (player) {
      player.querySelector("iframe").removeAttribute("src");
      player.hidden = true;
    }
    document.querySelectorAll(".study-youtube-card.is-playing").forEach((card) => card.classList.remove("is-playing"));
    document.querySelectorAll(".chapter-media-link.is-active").forEach((link) => {
      if (isPanelAudioLink(link)) {
        link.classList.remove("is-active");
        link.setAttribute("aria-pressed", "false");
      }
    });
    clearMediaIntent();
    setToolbarActive("");
  }

  const chapterTitleForPanel = () => panel?.dataset.chapterTitle || panel?.querySelector(".chapter-media-copy strong")?.textContent?.trim() || "";

  const panelLabel = (type) => {
    const title = chapterTitleForPanel();
    const mode = isRu()
      ? (type === "audio" ? "аудио" : "видео")
      : (type === "audio" ? "audio" : "video");
    if (title) return `${title} · ${mode}`;
    if (isRu()) return type === "audio" ? "Аудио главы" : "Видео главы";
    return type === "audio" ? "Chapter audio" : "Chapter video";
  };

  const ensureInlinePanelPlayer = () => {
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

  const activatePanelLink = (link, { scroll = false } = {}) => {
    if (!panel || !link) return false;
    const type = isPanelAudioLink(link) ? "audio" : "video";
    const embedUrl = toEmbedUrl(link.href, { autoplay: type === "audio" });
    if (!embedUrl) return false;
    const label = panelLabel(type);

    if (type === "audio") {
      const inline = panel.querySelector(".chapter-media-player");
      if (inline) {
        inline.hidden = true;
        inline.querySelector("iframe")?.removeAttribute("src");
      }
      openFloatingAudio({ embedUrl, label, href: link.href });
    } else {
      closeFloatingAudio();
      const player = ensureInlinePanelPlayer();
      const iframe = player.querySelector("iframe");
      iframe.src = embedUrl;
      iframe.title = label;
      player.querySelector(".chapter-media-player-label").textContent = label;
      player.querySelector(".chapter-media-youtube").href = link.href;
      player.hidden = false;
      setToolbarActive("video");
    }

    panel.querySelectorAll(".chapter-media-link").forEach((item) => {
      const active = item === link;
      item.classList.toggle("is-active", active);
      item.setAttribute("aria-pressed", active ? "true" : "false");
    });
    if (scroll) panel.scrollIntoView({ block: "start", inline: "nearest" });
    return true;
  };

  const prepareStudyCards = () => {
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
      button.addEventListener("click", () => openStudyAudio(card));
      card.querySelector(".study-youtube-embed")?.before(button);
    });
  };

  const openStudyAudio = (card) => {
    const iframe = card.querySelector("iframe");
    const src = iframe?.dataset.src || iframe?.src || "";
    if (!src) return false;
    const link = card.querySelector(".study-youtube-link");
    const title = iframe?.title || card.querySelector("strong")?.textContent?.trim() || (isRu() ? "Аудиообзор" : "Audio");
    openFloatingAudio({ embedUrl: withAutoplay(src), label: title, href: link?.href || src });
    document.querySelectorAll(".study-youtube-card.is-playing").forEach((item) => item.classList.remove("is-playing"));
    card.classList.add("is-playing");
    return true;
  };

  const showMediaSection = () => {
    const mediaButton = document.querySelector('[data-study-mode="media"]');
    if (mediaButton) {
      mediaButton.click();
      return;
    }
    document.querySelector("#study-panel")?.removeAttribute("hidden");
    document.querySelector('[data-study-section="media"]')?.removeAttribute("hidden");
  };

  const scrollToStudyVideo = (card) => {
    closeFloatingAudio();
    showMediaSection();
    setToolbarActive("video");
    window.requestAnimationFrame(() => {
      card.scrollIntoView({ block: "start", inline: "nearest" });
    });
  };

  const studyReportLinks = () => {
    const overview = reportCards.find((link) => /notebooklm-briefing\.html/i.test(link.getAttribute("href") || ""));
    const guide = reportCards.find((link) => /notebooklm-study-guide\.html/i.test(link.getAttribute("href") || ""));
    return [
      overview ? { type: "overview", href: overview.href } : null,
      guide ? { type: "guide", href: guide.href } : null,
    ].filter(Boolean);
  };

  const injectStudyReportLinks = () => {
    const toolbar = document.querySelector(".reader-toolbar");
    const title = toolbar?.querySelector(".toolbar-title");
    if (!toolbar || !title || toolbar.querySelector(".study-toolbar-links")) return;
    const links = studyReportLinks();
    if (!links.length) return;

    const controls = document.createElement("div");
    controls.className = "toolbar-group study-toolbar-links";
    controls.setAttribute("aria-label", isRu() ? "Учебные материалы" : "Study materials");

    const labels = isRu()
      ? { overview: "Обзор", guide: "Конспект" }
      : { overview: "Overview", guide: "Guide" };

    links.forEach(({ type, href }) => {
      const link = document.createElement("a");
      link.className = "toolbar-btn study-toolbar-link";
      link.href = href;
      link.textContent = labels[type];
      controls.append(link);
    });

    const mediaControls = toolbar.querySelector(".media-toolbar-controls");
    (mediaControls || title).insertAdjacentElement("afterend", controls);
    toolbar.querySelector(".study-mode-switch")?.setAttribute("hidden", "");
  };

  const injectToolbarControls = () => {
    const toolbar = document.querySelector(".reader-toolbar");
    const title = toolbar?.querySelector(".toolbar-title");
    if (!toolbar || !title || toolbar.querySelector(".media-toolbar-controls")) return;

    const panelLinks = panel ? [...panel.querySelectorAll(".chapter-media-link")] : [];
    const panelAudio = panelLinks.find(isPanelAudioLink);
    const panelVideo = panelLinks.find((link) => !isPanelAudioLink(link));
    const studyAudio = cards.find(isAudioCard);
    const studyVideo = cards.find((card) => !isAudioCard(card));

    const audioHandler = panelAudio
      ? () => activatePanelLink(panelAudio)
      : studyAudio
        ? () => openStudyAudio(studyAudio)
        : null;
    const videoHandler = panelVideo
      ? () => activatePanelLink(panelVideo, { scroll: true })
      : studyVideo
        ? () => scrollToStudyVideo(studyVideo)
        : null;
    if (!audioHandler && !videoHandler) return;

    const controls = document.createElement("div");
    controls.className = "toolbar-group media-toolbar-controls";
    controls.setAttribute("aria-label", isRu() ? "Медиа главы" : "Chapter media");

    const makeButton = (type, handler) => {
      const button = document.createElement("button");
      button.className = "toolbar-btn media-toolbar-btn";
      button.type = "button";
      button.dataset.mediaType = type;
      button.setAttribute("aria-pressed", "false");
      button.textContent = isRu()
        ? (type === "audio" ? "Слушать" : "Смотреть")
        : (type === "audio" ? "Listen" : "Watch");
      button.addEventListener("click", handler);
      return button;
    };

    if (audioHandler) controls.append(makeButton("audio", audioHandler));
    if (videoHandler) controls.append(makeButton("video", videoHandler));
    title.insertAdjacentElement("afterend", controls);
  };

  const openPanelFromHash = () => {
    if (!panel) return;
    const hash = decodeURIComponent(window.location.hash || "");
    if (!hash.startsWith("#chapter-media")) return;
    const links = [...panel.querySelectorAll(".chapter-media-link")];
    const wanted = hash.includes("audio") ? "audio" : hash.includes("watch") || hash.includes("video") ? "video" : "";
    const link = links.find((item) => wanted && (isPanelAudioLink(item) ? "audio" : "video") === wanted) || links[0];
    if (link) activatePanelLink(link, { scroll: true });
  };

  const openFromMediaIntent = () => {
    const hash = decodeURIComponent(window.location.hash || "");
    if (hash.startsWith("#chapter-media")) return;
    if (readMediaIntent() !== "audio") return;
    if (panel) {
      const link = [...panel.querySelectorAll(".chapter-media-link")].find(isPanelAudioLink);
      if (link) activatePanelLink(link);
      return;
    }
    const audio = cards.find(isAudioCard);
    if (audio) openStudyAudio(audio);
  };

  document.addEventListener("click", (event) => {
    const link = event.target.closest(".chapter-media-link");
    if (!link || !panel || !toEmbedUrl(link.href)) return;
    event.preventDefault();
    activatePanelLink(link);
  });

  prepareStudyCards();
  injectToolbarControls();
  injectStudyReportLinks();
  window.addEventListener("hashchange", openPanelFromHash);
  window.addEventListener("load", openPanelFromHash);
  openPanelFromHash();
  openFromMediaIntent();
})();
