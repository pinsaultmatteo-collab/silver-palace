/* ============================================================
   SILVER PALACE — interactions
   Vanilla JS, zéro dépendance.
   ============================================================ */
(() => {
  "use strict";

  // [QA temporaire — retirer avant mise en ligne]
  const qaTarget = new URLSearchParams(location.search).get("s");
  if (qaTarget) {
    document.documentElement.classList.add("qa");
    document.documentElement.style.scrollBehavior = "auto";
    const jump = () => {
      const t = document.getElementById(qaTarget);
      if (t) document.body.style.transform = `translateY(${-t.offsetTop}px)`;
    };
    document.addEventListener("DOMContentLoaded", jump);
    window.addEventListener("load", jump);
  }

  const reduceMotion = window.matchMedia("(prefers-reduced-motion: reduce)").matches;
  const finePointer = window.matchMedia("(pointer: fine)").matches;
  const lerp = (a, b, t) => a + (b - a) * t;

  /* ---------- Preloader ---------- */
  const preloader = document.getElementById("preloader");
  const hidePreloader = () => {
    preloader.classList.add("done");
    setTimeout(() => preloader.remove(), 1000);
  };
  if (document.readyState === "complete") hidePreloader();
  else window.addEventListener("load", () => setTimeout(hidePreloader, 400));
  // Filet de sécurité si un asset distant traîne
  setTimeout(hidePreloader, 3500);

  /* ---------- Split du titre héro ---------- */
  const heroDisplay = document.getElementById("heroDisplay");
  if (heroDisplay) {
    const words = heroDisplay.textContent.trim().split(/\s+/);
    heroDisplay.textContent = "";
    let delay = 0.15;
    words.forEach((word, wi) => {
      const wordSpan = document.createElement("span");
      wordSpan.className = "word";
      [...word].forEach((char) => {
        const span = document.createElement("span");
        span.className = "ch";
        span.textContent = char;
        span.style.animationDelay = `${delay}s`;
        delay += 0.055;
        wordSpan.appendChild(span);
      });
      heroDisplay.appendChild(wordSpan);
      if (wi < words.length - 1) heroDisplay.appendChild(document.createTextNode(" "));
    });
  }

  /* ---------- Onglet recrutement : apparition différée ---------- */
  const dancerTab = document.querySelector(".dancer-tab");
  if (dancerTab) {
    setTimeout(() => dancerTab.classList.add("on"), reduceMotion ? 0 : 1500);
  }

  /* ---------- Header au scroll + barre de progression ---------- */
  const header = document.getElementById("header");
  const progressBar = document.getElementById("scrollProgress");
  const onScrollHeader = () => {
    header.classList.toggle("scrolled", window.scrollY > 40);
    if (progressBar) {
      const max = document.documentElement.scrollHeight - window.innerHeight;
      const p = max > 0 ? Math.min(1, window.scrollY / max) : 0;
      progressBar.style.transform = `scaleX(${p.toFixed(4)})`;
    }
  };
  window.addEventListener("scroll", onScrollHeader, { passive: true });
  onScrollHeader();

  /* ---------- Menu mobile ---------- */
  const burger = document.getElementById("burger");
  const mobileMenu = document.getElementById("mobileMenu");
  const toggleMenu = (force) => {
    const open = force !== undefined ? force : !mobileMenu.classList.contains("open");
    mobileMenu.classList.toggle("open", open);
    burger.classList.toggle("open", open);
    burger.setAttribute("aria-expanded", String(open));
    mobileMenu.setAttribute("aria-hidden", String(!open));
    document.body.style.overflow = open ? "hidden" : "";
  };
  burger.addEventListener("click", () => toggleMenu());
  mobileMenu.querySelectorAll("a").forEach((a) =>
    a.addEventListener("click", () => toggleMenu(false))
  );

  /* ---------- Reveal au scroll ---------- */
  const revealEls = document.querySelectorAll(".reveal-up, .reveal-scale");
  const io = new IntersectionObserver(
    (entries) => {
      entries.forEach((entry) => {
        if (entry.isIntersecting) {
          entry.target.classList.add("in");
          io.unobserve(entry.target);
        }
      });
    },
    { threshold: 0.15, rootMargin: "0px 0px -60px 0px" }
  );
  revealEls.forEach((el) => io.observe(el));

  /* ---------- Parallax au scroll (rAF + lerp) ---------- */
  const parallaxEls = [...document.querySelectorAll("[data-depth]")].map((el) => ({
    el,
    depth: parseFloat(el.dataset.depth) || 0.1,
    current: 0,
  }));

  let ticking = false;
  const updateParallax = () => {
    parallaxEls.forEach((item) => {
      const rect = item.el.getBoundingClientRect();
      const center = rect.top + rect.height / 2 - window.innerHeight / 2;
      const target = -center * item.depth;
      item.current = lerp(item.current, target, 0.09);
      item.el.style.transform = `translate3d(0, ${item.current.toFixed(2)}px, 0)`;
    });
    ticking = parallaxEls.some((i) => Math.abs(i.current) > 0.05);
    if (ticking) requestAnimationFrame(updateParallax);
  };
  if (!reduceMotion && parallaxEls.length) {
    const kick = () => {
      if (!ticking) {
        ticking = true;
        requestAnimationFrame(updateParallax);
      }
    };
    window.addEventListener("scroll", kick, { passive: true });
    kick();
  }

  /* ---------- Particules dorées (héro) ---------- */
  const canvas = document.getElementById("particles");
  if (canvas && !reduceMotion) {
    const ctx = canvas.getContext("2d");
    let particles = [];
    let w, h;
    let running = true;

    const resize = () => {
      const dpr = Math.min(window.devicePixelRatio || 1, 2);
      w = canvas.clientWidth;
      h = canvas.clientHeight;
      canvas.width = w * dpr;
      canvas.height = h * dpr;
      ctx.setTransform(dpr, 0, 0, dpr, 0, 0);
    };
    resize();
    window.addEventListener("resize", resize);

    const COUNT = Math.min(70, Math.floor(window.innerWidth / 18));
    const spawn = () => ({
      x: Math.random() * w,
      y: h + Math.random() * h * 0.3,
      r: 0.6 + Math.random() * 1.7,
      vy: 0.15 + Math.random() * 0.45,
      vx: (Math.random() - 0.5) * 0.18,
      life: 0,
      maxLife: 400 + Math.random() * 500,
      tw: Math.random() * Math.PI * 2,
    });
    for (let i = 0; i < COUNT; i++) {
      const p = spawn();
      p.y = Math.random() * h;
      p.life = Math.random() * p.maxLife;
      particles.push(p);
    }

    const draw = () => {
      if (!running) return;
      ctx.clearRect(0, 0, w, h);
      particles.forEach((p, i) => {
        p.y -= p.vy;
        p.x += p.vx + Math.sin(p.life * 0.015 + p.tw) * 0.12;
        p.life++;
        if (p.y < -10 || p.life > p.maxLife) particles[i] = spawn();
        const fade = Math.sin((p.life / p.maxLife) * Math.PI);
        const twinkle = 0.55 + 0.45 * Math.sin(p.life * 0.08 + p.tw);
        ctx.beginPath();
        ctx.arc(p.x, p.y, p.r, 0, Math.PI * 2);
        ctx.fillStyle = `rgba(242, 169, 210, ${(0.5 * fade * twinkle).toFixed(3)})`;
        ctx.fill();
      });
      requestAnimationFrame(draw);
    };
    draw();

    // Pause hors écran
    new IntersectionObserver(
      ([entry]) => {
        const wasRunning = running;
        running = entry.isIntersecting;
        if (running && !wasRunning) draw();
      },
      { threshold: 0 }
    ).observe(canvas);
  }

  /* ---------- Parallax souris sur le héro ---------- */
  const heroContent = document.querySelector(".hero-content");
  const heroMedia = document.querySelector(".hero-media");
  if (finePointer && !reduceMotion && heroContent) {
    let mx = 0, my = 0, cx = 0, cy = 0;
    let heroRaf = null;
    const hero = document.getElementById("hero");
    hero.addEventListener("mousemove", (e) => {
      const r = hero.getBoundingClientRect();
      mx = (e.clientX - r.left) / r.width - 0.5;
      my = (e.clientY - r.top) / r.height - 0.5;
      if (!heroRaf) heroRaf = requestAnimationFrame(animateHero);
    });
    const animateHero = () => {
      cx = lerp(cx, mx, 0.06);
      cy = lerp(cy, my, 0.06);
      heroContent.style.transform =
        `rotateY(${(cx * 4).toFixed(2)}deg) rotateX(${(-cy * 4).toFixed(2)}deg) translateZ(0)`;
      if (heroMedia) {
        heroMedia.style.setProperty("--mx", cx);
        heroMedia.style.translate = `${(-cx * 18).toFixed(1)}px ${(-cy * 12).toFixed(1)}px`;
      }
      if (Math.abs(cx - mx) > 0.001 || Math.abs(cy - my) > 0.001) {
        heroRaf = requestAnimationFrame(animateHero);
      } else {
        heroRaf = null;
      }
    };
  }

  /* ---------- Tilt 3D cartes ---------- */
  if (finePointer && !reduceMotion) {
    document.querySelectorAll("[data-tilt]").forEach((card) => {
      let raf = null;
      let tx = 0, ty = 0, ctx2 = 0, cty = 0;

      const glare = card.querySelector(".card-glare");

      const animate = () => {
        ctx2 = lerp(ctx2, tx, 0.12);
        cty = lerp(cty, ty, 0.12);
        card.style.transform =
          `perspective(1000px) rotateY(${ctx2.toFixed(2)}deg) rotateX(${cty.toFixed(2)}deg)`;
        if (Math.abs(ctx2 - tx) > 0.02 || Math.abs(cty - ty) > 0.02) {
          raf = requestAnimationFrame(animate);
        } else {
          raf = null;
        }
      };

      card.addEventListener("mousemove", (e) => {
        const r = card.getBoundingClientRect();
        const px = (e.clientX - r.left) / r.width;
        const py = (e.clientY - r.top) / r.height;
        tx = (px - 0.5) * 10;
        ty = (0.5 - py) * 10;
        if (glare) {
          card.style.setProperty("--gx", `${(px * 100).toFixed(1)}%`);
          card.style.setProperty("--gy", `${(py * 100).toFixed(1)}%`);
        }
        if (!raf) raf = requestAnimationFrame(animate);
      });

      card.addEventListener("mouseleave", () => {
        tx = 0;
        ty = 0;
        if (!raf) raf = requestAnimationFrame(animate);
      });
    });
  }

  /* ---------- Traînées de paillettes au scroll (générique) ---------- */
  // track = élément qui définit la progression au scroll ; host = zone visible où dessiner
  const initGlitterTrail = (track, host, canvas, colors) => {
    const gctx = canvas.getContext("2d");
    const COLORS = colors || ["242, 169, 210", "216, 108, 170", "246, 240, 247", "206, 182, 255"];
    let gw = 0, gh = 0;
    let particles = [];
    let lastHead = null;
    let headGlow = 0;
    let glitterVisible = false;
    let glitterRaf = null;

    const gResize = () => {
      const dpr = Math.min(window.devicePixelRatio || 1, 2);
      gw = host.clientWidth;
      gh = host.clientHeight;
      canvas.width = gw * dpr;
      canvas.height = gh * dpr;
      gctx.setTransform(dpr, 0, 0, dpr, 0, 0);
    };
    gResize();
    window.addEventListener("resize", gResize);

    const headPos = () => {
      const r = track.getBoundingClientRect();
      const vh = window.innerHeight;
      let p = (vh - r.top) / (vh + r.height);
      p = Math.max(0, Math.min(1, p));
      const e = p * p * (3 - 2 * p); // smoothstep
      return {
        x: -50 + e * (gw + 100),
        y: gh * 0.48 + Math.sin(e * Math.PI * 2.2 + 0.5) * gh * 0.24,
      };
    };

    const spawn = (x, y, n) => {
      for (let i = 0; i < n; i++) {
        particles.push({
          x: x + (Math.random() - 0.5) * 22,
          y: y + (Math.random() - 0.5) * 22,
          vx: (Math.random() - 0.5) * 0.6,
          vy: -0.15 + (Math.random() - 0.4) * 0.5,
          life: 0,
          max: 55 + Math.random() * 75,
          size: 0.8 + Math.random() * 2.1,
          c: COLORS[(Math.random() * COLORS.length) | 0],
          star: Math.random() < 0.16,
          tw: Math.random() * Math.PI * 2,
          rot: Math.random() * Math.PI,
        });
      }
      if (particles.length > 420) particles.splice(0, particles.length - 420);
    };

    const drawStar = (p, alpha) => {
      const s = p.size * 2.6;
      gctx.save();
      gctx.translate(p.x, p.y);
      gctx.rotate(p.rot);
      gctx.fillStyle = `rgba(${p.c}, ${alpha.toFixed(3)})`;
      gctx.beginPath();
      gctx.moveTo(0, -s);
      gctx.quadraticCurveTo(s * 0.18, -s * 0.18, s, 0);
      gctx.quadraticCurveTo(s * 0.18, s * 0.18, 0, s);
      gctx.quadraticCurveTo(-s * 0.18, s * 0.18, -s, 0);
      gctx.quadraticCurveTo(-s * 0.18, -s * 0.18, 0, -s);
      gctx.fill();
      gctx.restore();
    };

    const glitterLoop = () => {
      gctx.clearRect(0, 0, gw, gh);
      // halo de tête de comète
      if (headGlow > 0.02 && lastHead) {
        const grad = gctx.createRadialGradient(lastHead.x, lastHead.y, 0, lastHead.x, lastHead.y, 46);
        grad.addColorStop(0, `rgba(242, 169, 210, ${(0.32 * headGlow).toFixed(3)})`);
        grad.addColorStop(1, "rgba(242, 169, 210, 0)");
        gctx.fillStyle = grad;
        gctx.beginPath();
        gctx.arc(lastHead.x, lastHead.y, 46, 0, Math.PI * 2);
        gctx.fill();
        headGlow *= 0.94;
      }
      particles = particles.filter((p) => p.life < p.max);
      particles.forEach((p) => {
        p.x += p.vx;
        p.y += p.vy;
        p.vy += 0.0045;
        p.life++;
        const fade = Math.sin((p.life / p.max) * Math.PI);
        const twinkle = 0.45 + 0.55 * Math.sin(p.life * 0.22 + p.tw);
        const alpha = Math.max(0, fade * twinkle);
        if (p.star) {
          drawStar(p, alpha * 0.9);
        } else {
          gctx.beginPath();
          gctx.arc(p.x, p.y, p.size, 0, Math.PI * 2);
          gctx.fillStyle = `rgba(${p.c}, ${(alpha * 0.85).toFixed(3)})`;
          gctx.fill();
        }
      });
      if (particles.length || headGlow > 0.02) {
        glitterRaf = requestAnimationFrame(glitterLoop);
      } else {
        glitterRaf = null;
      }
    };

    const onGlitterScroll = () => {
      if (!glitterVisible) return;
      const h = headPos();
      if (lastHead) {
        const dist = Math.hypot(h.x - lastHead.x, h.y - lastHead.y);
        if (dist > 2) {
          const steps = Math.min(26, Math.max(1, Math.floor(dist / 8)));
          for (let s = 1; s <= steps; s++) {
            const t = s / steps;
            spawn(lastHead.x + (h.x - lastHead.x) * t, lastHead.y + (h.y - lastHead.y) * t, 2);
          }
          headGlow = 1;
        }
      }
      lastHead = h;
      if (!glitterRaf) glitterRaf = requestAnimationFrame(glitterLoop);
    };

    new IntersectionObserver(
      ([entry]) => {
        glitterVisible = entry.isIntersecting;
        if (glitterVisible) {
          gResize();
          lastHead = headPos();
        }
      },
      { threshold: 0 }
    ).observe(track);
    window.addEventListener("scroll", onGlitterScroll, { passive: true });
  };

  if (!reduceMotion) {
    const promiseSection = document.getElementById("promesse");
    const g1 = document.getElementById("glitterCanvas");
    // fond clair : paillettes en tons rose profond / violet
    if (promiseSection && g1) initGlitterTrail(promiseSection, promiseSection, g1,
      ["176, 74, 133", "140, 58, 104", "122, 45, 150", "216, 108, 170"]);
    const teaserSection = document.getElementById("apercu");
    const teaserSticky = document.querySelector(".teaser-sticky");
    const g2 = document.getElementById("glitterCanvas2");
    if (teaserSection && teaserSticky && g2) initGlitterTrail(teaserSection, teaserSticky, g2);
  }

  /* ---------- Courbe du Club : tracé lié au scroll ---------- */
  const curvePath = document.getElementById("clubCurvePath");
  if (curvePath && !reduceMotion) {
    const curveLen = curvePath.getTotalLength();
    curvePath.style.strokeDasharray = String(curveLen);
    curvePath.style.strokeDashoffset = String(curveLen);
    const clubSection = document.getElementById("le-club");
    let curveRaf = null;
    const drawCurve = () => {
      curveRaf = null;
      const r = clubSection.getBoundingClientRect();
      const vh = window.innerHeight;
      // 0 quand la section entre, 1 quand on en a parcouru ~80 %
      let p = (vh - r.top) / (r.height * 0.85);
      p = Math.max(0, Math.min(1, p));
      curvePath.style.strokeDashoffset = String(curveLen * (1 - p));
    };
    window.addEventListener("scroll", () => {
      if (!curveRaf) curveRaf = requestAnimationFrame(drawCurve);
    }, { passive: true });
    window.addEventListener("load", () => setTimeout(drawCurve, 120));
    drawCurve();
  }

  /* ---------- La Promesse : remplissage doré au scroll ---------- */
  const promiseWords = [...document.querySelectorAll(".promise-word")];
  if (promiseWords.length) {
    if (reduceMotion) {
      promiseWords.forEach((w) => (w.style.backgroundPosition = "0% 0"));
    } else {
      let scrubRaf = null;
      const scrub = () => {
        scrubRaf = null;
        const vh = window.innerHeight;
        promiseWords.forEach((w) => {
          const r = w.getBoundingClientRect();
          const mid = r.top + r.height / 2;
          // 0 quand le mot entre en bas, 1 quand il atteint ~40% du viewport
          let p = (vh * 0.92 - mid) / (vh * 0.52);
          p = Math.max(0, Math.min(1, p));
          w.style.backgroundPosition = `${(100 - p * 100).toFixed(1)}% 0`;
        });
      };
      const onScrubScroll = () => {
        if (!scrubRaf) scrubRaf = requestAnimationFrame(scrub);
      };
      window.addEventListener("scroll", onScrubScroll, { passive: true });
      window.addEventListener("resize", onScrubScroll);
      scrub();
    }
  }

  /* ---------- Newsletter ---------- */
  const nlForm = document.getElementById("newsletterForm");
  if (nlForm) {
    nlForm.addEventListener("submit", (e) => {
      e.preventDefault();
      const email = nlForm.querySelector("input[type='email']");
      if (!email.checkValidity()) {
        email.reportValidity();
        return;
      }
      // TODO: brancher sur la plateforme e-mailing du client (Brevo / Mailchimp)
      nlForm.querySelector(".nl-row").style.display = "none";
      nlForm.querySelector(".nl-note").hidden = true;
      nlForm.querySelector(".nl-label").hidden = true;
      nlForm.querySelector(".nl-success").hidden = false;
    });
  }

  /* ---------- Le Spectacle : séquence vidéo pilotée au scroll ---------- */
  const spectacleCanvas = document.getElementById("spectacleCanvas");
  if (spectacleCanvas) {
    const FRAME_COUNT = 76;
    const framePath = (i) => `images/spectacle/frame-${String(i + 1).padStart(3, "0")}.jpg`;
    const sCtx = spectacleCanvas.getContext("2d");
    const frames = new Array(FRAME_COUNT).fill(null);
    const cabaretSection = document.getElementById("cabaret");
    let loadedCount = 0;
    let started = false;
    let currentFrame = 0;
    let targetFrame = 0;
    let lastDrawn = -1;
    let scrubRunning = false;

    const drawFrame = (i) => {
      const img = frames[Math.round(i)];
      if (!img) return;
      sCtx.drawImage(img, 0, 0, spectacleCanvas.width, spectacleCanvas.height);
      lastDrawn = Math.round(i);
    };

    const pinnedMode = window.matchMedia("(min-width: 1025px)");
    const computeTarget = () => {
      const r = cabaretSection.getBoundingClientRect();
      const vh = window.innerHeight;
      let p;
      if (pinnedMode.matches) {
        // section épinglée : l'animation se joue pendant que la section est figée à l'écran
        p = -r.top / (r.height - vh);
      } else {
        // mobile : progression classique à la traversée du viewport
        p = ((vh - r.top) / (vh + r.height) - 0.06) / 0.88;
      }
      p = Math.max(0, Math.min(1, p));
      targetFrame = p * (FRAME_COUNT - 1);
    };

    const scrubLoop = () => {
      currentFrame += (targetFrame - currentFrame) * 0.19;
      if (Math.abs(targetFrame - currentFrame) < 0.05) currentFrame = targetFrame;
      if (Math.round(currentFrame) !== lastDrawn) drawFrame(currentFrame);
      if (currentFrame !== targetFrame) {
        requestAnimationFrame(scrubLoop);
      } else {
        scrubRunning = false;
      }
    };
    const kickScrub = () => {
      computeTarget();
      if (!scrubRunning) {
        scrubRunning = true;
        requestAnimationFrame(scrubLoop);
      }
    };

    const loadFrames = () => {
      if (started) return;
      started = true;
      for (let i = 0; i < FRAME_COUNT; i++) {
        const img = new Image();
        img.decoding = "async";
        img.src = framePath(i);
        img.onload = () => {
          frames[i] = img;
          loadedCount++;
          if (loadedCount === 1) {
            // premier visuel dès que possible
            computeTarget();
            currentFrame = targetFrame;
            drawFrame(currentFrame);
            spectacleCanvas.classList.add("ready");
          }
          if (loadedCount === FRAME_COUNT) kickScrub();
        };
      }
    };

    if (reduceMotion) {
      // version statique : une frame du cœur de la séquence
      const still = new Image();
      still.src = framePath(40);
      still.onload = () => {
        frames[40] = still;
        drawFrame(40);
        spectacleCanvas.classList.add("ready");
      };
    } else {
      // préchargement quand on approche de la section
      new IntersectionObserver(
        ([entry], obs) => {
          if (entry.isIntersecting) {
            loadFrames();
            obs.disconnect();
          }
        },
        { rootMargin: "900px 0px" }
      ).observe(cabaretSection);
      window.addEventListener("scroll", () => { if (started) kickScrub(); }, { passive: true });
      window.addEventListener("resize", () => { if (started) kickScrub(); });
    }
  }

  /* ---------- Aperçu interactif : déblocage au clic + scrub ---------- */
  const teaser = document.getElementById("apercu");
  const teaserCanvas = document.getElementById("teaserCanvas");
  if (teaser && teaserCanvas) {
    const T_COUNT = 76;
    const tPath = (i) => `images/apercu/frame-${String(i + 1).padStart(3, "0")}.jpg`;
    const tCtx = teaserCanvas.getContext("2d");
    const tFrames = new Array(T_COUNT).fill(null);
    const tHint = document.getElementById("teaserHint");
    let tUnlocked = false;
    let tLoaded = 0;
    let tCur = 0, tTgt = 0, tLast = -1, tRunning = false;

    const tDraw = (i) => {
      const im = tFrames[Math.round(i)];
      if (!im) return;
      tCtx.drawImage(im, 0, 0, teaserCanvas.width, teaserCanvas.height);
      tLast = Math.round(i);
    };
    const tTarget = () => {
      const r = teaser.getBoundingClientRect();
      const vh = window.innerHeight;
      let p = -r.top / (r.height - vh);
      p = Math.max(0, Math.min(1, p));
      tTgt = p * (T_COUNT - 1);
      if (p > 0.9) tHint.classList.remove("show");
    };
    const tLoop = () => {
      tCur += (tTgt - tCur) * 0.19;
      if (Math.abs(tTgt - tCur) < 0.05) tCur = tTgt;
      if (Math.round(tCur) !== tLast) tDraw(tCur);
      if (tCur !== tTgt) {
        requestAnimationFrame(tLoop);
      } else {
        tRunning = false;
      }
    };
    const tKick = () => {
      if (!tUnlocked || reduceMotion) return;
      tTarget();
      if (!tRunning) {
        tRunning = true;
        requestAnimationFrame(tLoop);
      }
    };

    document.getElementById("teaserUnlock").addEventListener("click", () => {
      if (tUnlocked) return;
      tUnlocked = true;
      teaser.classList.add("unlocked");
      tHint.classList.add("show");
      for (let i = 0; i < T_COUNT; i++) {
        const im = new Image();
        im.decoding = "async";
        im.src = tPath(i);
        im.onload = () => {
          tFrames[i] = im;
          tLoaded++;
          if (tLoaded === 1) {
            tDraw(reduceMotion ? Math.round(T_COUNT / 2) : 0);
            teaserCanvas.classList.add("ready");
          }
          if (tLoaded === T_COUNT) tKick();
        };
      }
      // cale la scène en position épinglée pour que le scroll pilote la danse
      teaser.scrollIntoView({ behavior: reduceMotion ? "auto" : "smooth", block: "start" });
    });
    window.addEventListener("scroll", tKick, { passive: true });
    window.addEventListener("resize", tKick);
  }

  /* ---------- Les Artistes : carrousel danseuses ---------- */
  const dancersStack = document.getElementById("dancersStack");
  if (dancersStack) {
    // Noms de scène provisoires — à remplacer par les vrais noms fournis par le club
    const DANCERS = [
      {
        name: "Eva",
        role: "Table dance & shows privés",
        bio: "Regard de braise et précision féline. Eva règne sur les salons privés, où chaque danse devient un moment suspendu.",
      },
      {
        name: "Ruby",
        role: "Soirées à thème",
        bio: "Icône des nuits à thème du Silver, Ruby transforme chaque apparition en spectacle. Paillettes, audace et démesure.",
      },
      {
        name: "Scarlett",
        role: "Ambiance & sensualité",
        bio: "Dans la lumière rouge des salons, Scarlett distille une sensualité feutrée, entre satin, pétales et champagne.",
      },
      {
        name: "Nova",
        role: "Pole dance",
        bio: "Athlète du chrome, Nova enchaîne les figures avec une grâce hypnotique. Sa spécialité : défier la gravité.",
      },
      {
        name: "Jade",
        role: "Shows chorégraphiés",
        bio: "Formée à la danse classique, Jade signe des chorégraphies millimétrées qui électrisent la scène centrale.",
      },
    ];
    const photos = [...dancersStack.querySelectorAll(".dancer-photo")];
    const nameEl = document.getElementById("dancerName");
    const roleEl = document.getElementById("dancerRole");
    const bioEl = document.getElementById("dancerBio");
    const countEl = document.getElementById("dancersCount");
    const pad = (n) => String(n + 1).padStart(2, "0");
    let active = 0;

    const renderBio = (text) => {
      bioEl.textContent = "";
      if (reduceMotion) {
        bioEl.textContent = text;
        return;
      }
      text.split(" ").forEach((word, i) => {
        const span = document.createElement("span");
        span.className = "w";
        span.textContent = word;
        span.style.animationDelay = `${i * 0.025}s`;
        bioEl.appendChild(span);
        bioEl.appendChild(document.createTextNode(" "));
      });
    };

    const render = () => {
      photos.forEach((photo, i) => {
        photo.classList.toggle("is-active", i === active);
        photo.classList.toggle("is-behind", i !== active);
        if (i === active) {
          photo.style.zIndex = "10";
        } else {
          // légère rotation aléatoire pour l'effet "pile de polaroids"
          const rot = ((i * 47 + active * 31) % 13) - 6;
          photo.style.setProperty("--rot", `${rot}deg`);
          photo.style.zIndex = String(photos.length - Math.abs(i - active));
        }
      });
      const d = DANCERS[active] || {};
      nameEl.textContent = d.name || "";
      roleEl.textContent = d.role || "";
      renderBio(d.bio || "");
      countEl.textContent = `${pad(active)} — ${pad(photos.length - 1)}`;
    };

    const go = (dir) => {
      active = (active + dir + photos.length) % photos.length;
      render();
    };

    document.getElementById("dancerPrev").addEventListener("click", () => {
      go(-1);
      restartAutoplay();
    });
    document.getElementById("dancerNext").addEventListener("click", () => {
      go(1);
      restartAutoplay();
    });

    // Autoplay, en pause au survol et hors écran
    let autoplayTimer = null;
    let hovering = false;
    let visible = false;
    const startAutoplay = () => {
      if (autoplayTimer || reduceMotion) return;
      autoplayTimer = setInterval(() => {
        if (!hovering && visible) go(1);
      }, 5000);
    };
    const restartAutoplay = () => {
      if (autoplayTimer) clearInterval(autoplayTimer);
      autoplayTimer = null;
      startAutoplay();
    };
    const dancersSection = document.getElementById("artistes");
    dancersSection.addEventListener("mouseenter", () => (hovering = true));
    dancersSection.addEventListener("mouseleave", () => (hovering = false));
    new IntersectionObserver(
      ([entry]) => {
        visible = entry.isIntersecting;
      },
      { threshold: 0.2 }
    ).observe(dancersSection);

    render();
    startAutoplay();
  }

  /* ---------- FAQ : fermer les autres ---------- */
  const faqItems = document.querySelectorAll(".faq-item");
  faqItems.forEach((item) => {
    item.addEventListener("toggle", () => {
      if (item.open) {
        faqItems.forEach((other) => {
          if (other !== item) other.open = false;
        });
      }
    });
  });
})();
