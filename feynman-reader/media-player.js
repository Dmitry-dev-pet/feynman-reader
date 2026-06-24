(() => {
  const dom = {
    cards: [...document.querySelectorAll(".study-youtube-card")],
    reportCards: [...document.querySelectorAll(".study-card[href*='notebooklm-briefing.html'], .study-card[href*='notebooklm-study-guide.html']")],
  };
  let manifestChapter = null;

  const MEDIA_INTENT_KEY = "flp-reader-media-intent";
  const PLAYER_WIDTH_KEY = "flp-floating-player-width";
  const isRu = () => (document.documentElement.lang || "").toLowerCase().startsWith("ru");

  const ReaderManifest = {
    url() {
      const scriptUrl = document.currentScript?.src || document.querySelector('script[src*="media-player.js"]')?.src || "";
      return scriptUrl ? new URL("media-manifest.json", scriptUrl).href : "";
    },
    chapterKey() {
      const match = window.location.pathname.match(/feynman-html-(ru|en)\/volume-([IVX]+)-[^/]+\/chapters\/ch(\d+)\.html$/);
      if (!match) return "";
      return `${match[1]}-${match[2]}/ch${match[3].padStart(2, "0")}`;
    },
    async load() {
      const url = this.url();
      const key = this.chapterKey();
      if (!url || !key || window.location.protocol === "file:") return null;
      try {
        const response = await fetch(url, { cache: "force-cache" });
        if (!response.ok) return null;
        const manifest = await response.json();
        return manifest?.chapters?.[key] || null;
      } catch (_) {
        return null;
      }
    },
  };

  const MediaIntent = {
    read() {
      try {
        return sessionStorage.getItem(MEDIA_INTENT_KEY) || "";
      } catch (_) {
        return "";
      }
    },
    set(type) {
      try {
        sessionStorage.setItem(MEDIA_INTENT_KEY, type);
      } catch (_) {}
    },
    clear() {
      try {
        sessionStorage.removeItem(MEDIA_INTENT_KEY);
      } catch (_) {}
    },
  };

  const YouTube = {
    parseStart(value) {
      if (!value) return 0;
      if (/^\d+$/.test(value)) return Number(value);
      const match = value.match(/(?:(\d+)h)?(?:(\d+)m)?(?:(\d+)s)?/i);
      if (!match) return 0;
      return (Number(match[1] || 0) * 3600) + (Number(match[2] || 0) * 60) + Number(match[3] || 0);
    },
    toEmbedUrl(href, { autoplay = false } = {}) {
      const url = new URL(href, window.location.href);
      let id = "";
      if (url.hostname.includes("youtu.be")) {
        id = url.pathname.split("/").filter(Boolean)[0] || "";
      } else if (url.hostname.includes("youtube.com")) {
        id = url.searchParams.get("v") || url.pathname.split("/embed/")[1] || "";
      }
      if (!id) return "";
      const start = this.parseStart(url.searchParams.get("t") || url.searchParams.get("start"));
      const embed = new URL(`https://www.youtube-nocookie.com/embed/${id}`);
      embed.searchParams.set("rel", "0");
      embed.searchParams.set("modestbranding", "1");
      embed.searchParams.set("playsinline", "1");
      if (autoplay) embed.searchParams.set("autoplay", "1");
      if (start) embed.searchParams.set("start", String(start));
      return embed.toString();
    },
    withAutoplay(src) {
      const url = new URL(src, window.location.href);
      url.searchParams.set("autoplay", "1");
      url.searchParams.set("playsinline", "1");
      return url.toString();
    },
  };

  const ToolbarState = {
    setActive(type) {
      document.querySelectorAll(".media-toolbar-btn").forEach((button) => {
        const active = button.dataset.mediaType === type;
        button.classList.toggle("is-active", active);
        button.setAttribute("aria-pressed", active ? "true" : "false");
      });
    },
  };

  const FloatingPlayer = {
    minWidth: 320,
    maxWidth() {
      return Math.max(this.minWidth, Math.min(760, window.innerWidth - 32));
    },
    savedWidth() {
      try {
        return Number(localStorage.getItem(PLAYER_WIDTH_KEY) || 0);
      } catch (_) {
        return 0;
      }
    },
    saveWidth(width) {
      if (window.innerWidth <= 760) return;
      try {
        localStorage.setItem(PLAYER_WIDTH_KEY, String(Math.round(this.clampWidth(width))));
      } catch (_) {}
    },
    clampWidth(width) {
      return Math.min(this.maxWidth(), Math.max(this.minWidth, Number(width) || 0));
    },
    applySavedSize(player) {
      if (window.innerWidth <= 760) {
        player.style.removeProperty("width");
        return;
      }
      const width = this.savedWidth();
      if (width) player.style.width = `${this.clampWidth(width)}px`;
    },
    resizeBy(delta) {
      const player = this.ensure();
      if (window.innerWidth <= 760) return;
      const current = player.getBoundingClientRect().width || this.savedWidth() || 432;
      const width = this.clampWidth(current + delta);
      player.style.width = `${width}px`;
      this.saveWidth(width);
    },
    resetSize() {
      const player = this.ensure();
      player.style.removeProperty("width");
      try {
        localStorage.removeItem(PLAYER_WIDTH_KEY);
      } catch (_) {}
    },
    observeResize(player) {
      if (player.dataset.resizeObserverReady === "true" || typeof ResizeObserver === "undefined") return;
      player.dataset.resizeObserverReady = "true";
      const observer = new ResizeObserver((entries) => {
        if (player.hidden || window.innerWidth <= 760) return;
        const width = entries[0]?.contentRect?.width;
        if (width) this.saveWidth(width);
      });
      observer.observe(player);
      window.addEventListener("resize", () => this.applySavedSize(player));
    },
    ensure() {
      let player = document.querySelector(".floating-youtube-player");
      if (player) return player;
      player = document.createElement("aside");
      player.className = "floating-youtube-player";
      player.hidden = true;
      player.setAttribute("aria-live", "polite");
      player.innerHTML = `
        <div class="floating-youtube-header">
          <span class="floating-youtube-label"></span>
          <div class="floating-youtube-actions" aria-label="${isRu() ? "Размер плеера" : "Player size"}">
            <button class="floating-youtube-size" type="button" data-player-size="smaller" aria-label="${isRu() ? "Уменьшить плеер" : "Make player smaller"}" title="${isRu() ? "Уменьшить" : "Smaller"}">−</button>
            <button class="floating-youtube-size" type="button" data-player-size="larger" aria-label="${isRu() ? "Увеличить плеер" : "Make player larger"}" title="${isRu() ? "Увеличить" : "Larger"}">+</button>
            <button class="floating-youtube-size" type="button" data-player-size="reset" aria-label="${isRu() ? "Сбросить размер плеера" : "Reset player size"}" title="${isRu() ? "Сбросить размер" : "Reset size"}">□</button>
          </div>
          <button class="floating-youtube-close" type="button" aria-label="${isRu() ? "Закрыть плеер" : "Close player"}" title="${isRu() ? "Закрыть" : "Close"}">×</button>
        </div>
        <div class="floating-youtube-frame">
          <iframe loading="lazy" referrerpolicy="strict-origin-when-cross-origin" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>
        </div>
        <a class="floating-youtube-link" href="#" target="_blank" rel="noopener">${isRu() ? "Открыть на YouTube" : "Open on YouTube"}</a>`;
      document.body.append(player);
      player.querySelector(".floating-youtube-close").addEventListener("click", () => this.close());
      player.querySelector('[data-player-size="smaller"]')?.addEventListener("click", () => this.resizeBy(-72));
      player.querySelector('[data-player-size="larger"]')?.addEventListener("click", () => this.resizeBy(72));
      player.querySelector('[data-player-size="reset"]')?.addEventListener("click", () => this.resetSize());
      this.applySavedSize(player);
      this.observeResize(player);
      return player;
    },
    open({ embedUrl, label, href, type }) {
      const player = this.ensure();
      const iframe = player.querySelector("iframe");
      this.applySavedSize(player);
      player.querySelector(".floating-youtube-label").textContent = label;
      player.querySelector(".floating-youtube-link").href = href;
      iframe.title = label;
      iframe.src = embedUrl;
      player.hidden = false;
      MediaIntent.set(type);
      ToolbarState.setActive(type);
    },
    close() {
      const player = document.querySelector(".floating-youtube-player");
      if (player) {
        player.querySelector("iframe").removeAttribute("src");
        player.hidden = true;
      }
      document.querySelectorAll(".study-youtube-card.is-playing").forEach((card) => card.classList.remove("is-playing"));
      MediaIntent.clear();
      ToolbarState.setActive("");
    },
  };

  const StudyCards = {
    manifestItems() {
      return (manifestChapter?.media || []).map((entry) => ({ source: "manifest", entry }));
    },
    isManifestItem(item) {
      return item?.source === "manifest";
    },
    isAudio(card) {
      if (this.isManifestItem(card)) return card.entry.type === "audio";
      const title = card.querySelector("strong")?.textContent || "";
      const text = [
        title,
        card.querySelector("iframe")?.title || "",
        card.querySelector("span")?.textContent || "",
      ].join(" ");
      return /аудио|audio/i.test(text) && !/видео|video/i.test(title);
    },
    type(card) {
      if (this.isManifestItem(card)) return card.entry.type;
      return this.isAudio(card) ? "audio" : "video";
    },
    prepare() {
      dom.cards.forEach((card) => {
        const iframe = card.querySelector("iframe");
        if (!iframe) return;
        const type = this.type(card);
        iframe.dataset.src = iframe.src;
        iframe.removeAttribute("src");
        card.classList.add("is-floating-card", `is-${type}-card`);
        if (card.querySelector(".study-youtube-play")) return;
        const button = document.createElement("button");
        button.className = "study-youtube-play";
        button.type = "button";
        button.textContent = isRu()
          ? (type === "audio" ? "Слушать" : "Смотреть")
          : (type === "audio" ? "Listen" : "Watch");
        button.addEventListener("click", () => this.open(card, type));
        card.querySelector(".study-youtube-embed")?.before(button);
      });
    },
    open(card, type = this.type(card)) {
      if (this.isManifestItem(card)) return this.openManifest(card.entry, type);
      const iframe = card.querySelector("iframe");
      const src = iframe?.dataset.src || iframe?.src || "";
      if (!src) return false;
      const link = card.querySelector(".study-youtube-link");
      const title = iframe?.title || card.querySelector("strong")?.textContent?.trim() || (isRu()
        ? (type === "audio" ? "Аудиообзор" : "Видеообзор")
        : (type === "audio" ? "Audio" : "Video"));
      FloatingPlayer.open({ embedUrl: YouTube.withAutoplay(src), label: title, href: link?.href || src, type });
      document.querySelectorAll(".study-youtube-card.is-playing").forEach((item) => item.classList.remove("is-playing"));
      card.classList.add("is-playing");
      return true;
    },
    openManifest(entry, type = entry.type) {
      const embed = new URL(`https://www.youtube-nocookie.com/embed/${entry.youtube_id}`);
      embed.searchParams.set("rel", "0");
      embed.searchParams.set("modestbranding", "1");
      embed.searchParams.set("playsinline", "1");
      embed.searchParams.set("autoplay", "1");
      if (entry.start) embed.searchParams.set("start", String(entry.start));
      FloatingPlayer.open({
        embedUrl: embed.toString(),
        label: entry.label || entry.title || (isRu() ? (type === "audio" ? "Аудиообзор" : "Видеообзор") : (type === "audio" ? "Audio" : "Video")),
        href: entry.watch_url || `https://youtu.be/${entry.youtube_id}${entry.start ? `?t=${entry.start}` : ""}`,
        type,
      });
      document.querySelectorAll(".study-youtube-card.is-playing").forEach((item) => item.classList.remove("is-playing"));
      return true;
    },
    first(type) {
      const manifestItem = this.manifestItems().find((item) => item.entry.type === type);
      if (manifestItem) return manifestItem;
      return dom.cards.find((card) => this.type(card) === type);
    },
  };

  const StudyReports = {
    links() {
      if (manifestChapter?.reports) {
        const reports = manifestChapter.reports;
        return [
          reports.overview ? { type: "overview", href: new URL(reports.overview, window.location.href).href } : null,
          reports.guide ? { type: "guide", href: new URL(reports.guide, window.location.href).href } : null,
        ].filter(Boolean);
      }
      const overview = dom.reportCards.find((link) => /notebooklm-briefing\.html/i.test(link.getAttribute("href") || ""));
      const guide = dom.reportCards.find((link) => /notebooklm-study-guide\.html/i.test(link.getAttribute("href") || ""));
      return [
        overview ? { type: "overview", href: overview.href } : null,
        guide ? { type: "guide", href: guide.href } : null,
      ].filter(Boolean);
    },
    injectToolbarLinks() {
      const toolbar = document.querySelector(".reader-toolbar");
      const title = toolbar?.querySelector(".toolbar-title");
      if (!toolbar || !title || toolbar.querySelector(".study-toolbar-links")) return;
      const links = this.links();
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
    },
    removeInlineReports() {
      if (!dom.reportCards.length) return;
      document.querySelector('[data-study-section="notes"]')?.remove();
      document.querySelectorAll('[data-study-mode="notes"]').forEach((button) => button.remove());
      document.querySelector(".study-workspace-header")?.remove();
      StudyWorkspace.closeIfEmpty();
    },
  };

  const StudyWorkspace = {
    showMediaSection() {
      const mediaButton = document.querySelector('[data-study-mode="media"]');
      if (mediaButton) {
        mediaButton.click();
        return;
      }
      document.querySelector("#study-panel")?.removeAttribute("hidden");
      document.querySelector('[data-study-section="media"]')?.removeAttribute("hidden");
    },
    closeIfEmpty() {
      const workspace = document.querySelector(".study-workspace");
      if (!workspace) return;
      const visibleSection = [...document.querySelectorAll("[data-study-section]")].find((section) => !section.hidden);
      if (!visibleSection) workspace.hidden = true;
    },
    normalizeRetiredHash() {
      if (window.location.hash !== "#study-panel") return;
      const workspace = document.querySelector(".study-workspace");
      if (workspace) workspace.hidden = true;
      if (window.history?.replaceState) {
        window.history.replaceState(null, "", `${window.location.pathname}${window.location.search}`);
      }
    },
  };

  const Toolbar = {
    injectMediaControls() {
      const toolbar = document.querySelector(".reader-toolbar");
      const title = toolbar?.querySelector(".toolbar-title");
      if (!toolbar || !title || toolbar.querySelector(".media-toolbar-controls")) return;

      const handlers = {
        audio: StudyCards.first("audio") ? () => StudyCards.open(StudyCards.first("audio"), "audio") : null,
        video: StudyCards.first("video") ? () => StudyCards.open(StudyCards.first("video"), "video") : null,
      };
      if (!handlers.audio && !handlers.video) return;

      const controls = document.createElement("div");
      controls.className = "toolbar-group media-toolbar-controls";
      controls.setAttribute("aria-label", isRu() ? "Медиа главы" : "Chapter media");

      Object.entries(handlers).forEach(([type, handler]) => {
        if (!handler) return;
        const button = document.createElement("button");
        button.className = "toolbar-btn media-toolbar-btn";
        button.type = "button";
        button.dataset.mediaType = type;
        button.setAttribute("aria-pressed", "false");
        button.textContent = isRu()
          ? (type === "audio" ? "Слушать" : "Смотреть")
          : (type === "audio" ? "Listen" : "Watch");
        button.addEventListener("click", handler);
        controls.append(button);
      });
      title.insertAdjacentElement("afterend", controls);
    },
  };

  const HashRoutes = {
    current() {
      return decodeURIComponent(window.location.hash || "");
    },
    openStudyMedia() {
      if (window.location.hash !== "#study-media") return;
      const video = StudyCards.first("video");
      const audio = StudyCards.first("audio");
      if (video) StudyCards.open(video, "video");
      else if (audio) StudyCards.open(audio, "audio");
      else {
        StudyWorkspace.showMediaSection();
        StudyWorkspace.closeIfEmpty();
      }
    },
    openMigratedChapterMedia() {
      const hash = this.current();
      if (!hash.startsWith("#chapter-media")) return;
      const audio = StudyCards.first("audio");
      const video = StudyCards.first("video");
      if (hash.includes("audio") && audio) {
        StudyCards.open(audio, "audio");
        return;
      }
      if ((hash.includes("watch") || hash.includes("video")) && video) {
        StudyCards.open(video, "video");
        return;
      }
      if (video) StudyCards.open(video, "video");
      else if (audio) StudyCards.open(audio, "audio");
    },
    openStoredIntent() {
      const hash = this.current();
      if (hash.startsWith("#chapter-media")) return;
      const intent = MediaIntent.read();
      if (intent !== "audio" && intent !== "video") return;
      const card = StudyCards.first(intent);
      if (card) StudyCards.open(card, intent);
    },
    handleHashChange() {
      StudyWorkspace.normalizeRetiredHash();
      this.openStudyMedia();
      this.openMigratedChapterMedia();
      StudyWorkspace.closeIfEmpty();
    },
  };

  const init = async () => {
    manifestChapter = await ReaderManifest.load();
    if (!dom.cards.length && !dom.reportCards.length && !manifestChapter) return;
    StudyCards.prepare();
    Toolbar.injectMediaControls();
    StudyReports.injectToolbarLinks();
    StudyReports.removeInlineReports();
    StudyWorkspace.normalizeRetiredHash();
    HashRoutes.openStudyMedia();
    HashRoutes.openMigratedChapterMedia();
    window.addEventListener("hashchange", () => HashRoutes.handleHashChange());
    HashRoutes.openStoredIntent();
  };

  init();
})();
