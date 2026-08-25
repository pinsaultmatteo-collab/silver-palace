# -*- coding: utf-8 -*-
"""Génère le blog du Silver Palace : index + articles.

    python3 scripts/build_blog.py            # publie les articles dont la date est atteinte
    python3 scripts/build_blog.py --all      # génère aussi les articles à venir (relecture)
    python3 scripts/build_blog.py --agenda   # liste ce qui est publié et ce qui attend

PUBLICATION PROGRAMMÉE : chaque article porte une date. Seuls ceux dont la date
est passée ou atteinte sont écrits sur le site — les autres restent dans le dépôt,
invisibles, jusqu'à leur semaine. Une action GitHub relance ce script chaque mardi
et pousse le nouvel article : voir .github/workflows/publier-article.yml

Le contenu vit dans scripts/blog_posts.py.
"""
import os, re, sys, json, datetime

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
SITE = os.path.join(os.path.dirname(HERE), "site")

from blog_posts import POSTS

BASE = "https://silver-palace.com"
MOIS = ["janvier", "février", "mars", "avril", "mai", "juin", "juillet",
        "août", "septembre", "octobre", "novembre", "décembre"]


def fr_date(iso):
    y, m, d = (int(x) for x in iso.split("-"))
    return f"{d} {MOIS[m - 1]} {y}"


def head(title, desc, url, image, extra_ld="", keywords=""):
    kw = f'\n  <meta name="keywords" content="{keywords}">' if keywords else ""
    return f"""<!DOCTYPE html>
<html lang="fr">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>{title}</title>
  <meta name="description" content="{desc}">{kw}
  <link rel="canonical" href="{url}">
  <meta name="robots" content="index, follow, max-image-preview:large">
  <meta property="og:type" content="article">
  <meta property="og:site_name" content="Silver Palace Toulouse">
  <meta property="og:title" content="{title}">
  <meta property="og:description" content="{desc}">
  <meta property="og:url" content="{url}">
  <meta property="og:image" content="{BASE}{image}">
  <meta property="og:locale" content="fr_FR">
  <meta name="twitter:card" content="summary_large_image">
  <meta name="theme-color" content="#0a0716">
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Cinzel:wght@400;500;600&family=Cormorant+Garamond:ital,wght@0,300;0,400;0,500;1,300;1,400&family=Jost:wght@200;300;400;500&display=swap" rel="stylesheet">
  <link rel="stylesheet" href="/css/style.css">{extra_ld}
</head>
<body>
"""


def chrome(active_blog=True):
    """Header + menu mobile, alignés sur le reste du site."""
    nav = [("/about", "Le Club"), ("/events", "Événements"), ("/carte", "La Carte"),
           ("/shows", "Les Danses"), ("/blog", "Blog"), ("/contact", "Contact")]
    CURRENT = ' aria-current="page"'
    desktop, mobile = [], []
    for h, t in nav:
        on = h == "/blog" and active_blog
        cls = "nav-link active" if on else "nav-link"
        cur = CURRENT if on else ""
        desktop.append(f'        <a href="{h}" class="{cls}"{cur}>{t}</a>')
        mobile.append(f'      <a href="{h}"{cur}>{t}</a>')
    desktop, mobile = "\n".join(desktop), "\n".join(mobile)
    return f"""
  <div class="scroll-progress" id="scrollProgress" aria-hidden="true"></div>
  <div class="grain" aria-hidden="true"></div>

  <header class="header" id="header">
    <div class="header-inner">
      <a href="/" class="brand" aria-label="Silver Palace — Accueil">
        <img src="/images/logo-silver-palace.png" class="brand-logo"
             alt="Silver Palace — club de striptease et cabaret à Toulouse"
             width="300" height="147">
      </a>
      <nav class="nav" aria-label="Navigation principale">
{desktop}
      </nav>
      <div class="header-actions">
        <a href="/reservation" class="btn btn-gold btn-nav">Réserver</a>
        <a href="/application" class="btn btn-ghost btn-nav btn-dance" aria-label="Devenir danseuse au Silver Palace — candidature">
          <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.4" stroke-linecap="round" aria-hidden="true"><path d="M12 3c.9 2.6 1.4 3.9 2.5 5 1.1 1.1 2.4 1.6 5 2.5-2.6.9-3.9 1.4-5 2.5-1.1 1.1-1.6 2.4-2.5 5-.9-2.6-1.4-3.9-2.5-5-1.1-1.1-2.4-1.6-5-2.5 2.6-.9 3.9-1.4 5-2.5 1.1-1.1 1.6-2.4 2.5-5Z"/></svg>
          Danser&nbsp;au&nbsp;Silver
        </a>
      </div>
      <button class="burger" id="burger" aria-label="Ouvrir le menu" aria-expanded="false">
        <span></span><span></span>
      </button>
    </div>
  </header>

  <div class="mobile-menu" id="mobileMenu" aria-hidden="true">
    <button class="menu-close" id="menuClose" type="button" aria-label="Fermer le menu">✕</button>
    <nav aria-label="Navigation mobile">
      <a href="/">Accueil</a>
{mobile}
      <a href="/reservation" class="mobile-cta">Réserver une table</a>
      <a href="/application" class="mobile-cta mobile-cta-ghost">Danser au Silver</a>
    </nav>
    <div class="mobile-menu-foot">
      <a href="tel:+33562845169">05 62 84 51 69</a>
      <span>31 Rue de Stalingrad, Toulouse</span>
    </div>
  </div>

  <main id="main">
"""


FOOTER = """  </main>

  <footer class="footer">
    <div class="footer-inner">
      <div class="footer-brand">
        <img src="/images/logo-silver-palace.png" class="footer-logo-img"
             alt="Logo Silver Palace Toulouse" width="300" height="147" loading="lazy">
        <p class="footer-baseline">Club de striptease, cabaret &amp; gentlemen's club à Toulouse. Votre référence de la nuit dans la Ville rose.</p>
      </div>
      <nav class="footer-nav" aria-label="Pied de page — Le club">
        <p class="footer-head">Le Club</p>
        <a href="/events">Événements</a>
        <a href="/carte">Carte des boissons</a>
        <a href="/shows">Carte des danses</a>
        <a href="/reservation">Réservation</a>
        <a href="/application">Candidature</a>
      </nav>
      <nav class="footer-nav" aria-label="Pied de page — Informations">
        <p class="footer-head">Informations</p>
        <a href="/blog">Blog</a>
        <a href="/about">À propos</a>
        <a href="/contact">Contact</a>
        <a href="/legal">Mentions légales</a>
        <a href="/privacy">Confidentialité</a>
      </nav>
      <div class="footer-contact">
        <p class="footer-head">Contact</p>
        <address>
          31 Rue de Stalingrad<br>31000 Toulouse<br>
          <a href="tel:+33562845169">05 62 84 51 69</a>
        </address>
        <div class="footer-socials">
          <a href="https://www.instagram.com/silverpalace_31000/" target="_blank" rel="noopener" aria-label="Instagram">
            <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5"><rect x="2.5" y="2.5" width="19" height="19" rx="5"/><circle cx="12" cy="12" r="4.2"/><circle cx="17.6" cy="6.4" r="1" fill="currentColor" stroke="none"/></svg>
          </a>
          <a href="https://www.facebook.com/profile.php?id=100063470923089" target="_blank" rel="noopener" aria-label="Facebook">
            <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5"><path d="M15.5 3.5h-2a4 4 0 0 0-4 4v2.5H7v3.5h2.5v7h3.5v-7h2.5l.5-3.5h-3V8a1 1 0 0 1 1-1h2v-3.5Z"/></svg>
          </a>
        </div>
      </div>
    </div>
    <div class="footer-bottom">
      <p>© 2026 Silver Palace — Club de striptease &amp; cabaret à Toulouse. Tous droits réservés. Interdit aux moins de 18 ans. L'abus d'alcool est dangereux pour la santé, à consommer avec modération.</p>
    </div>
  </footer>

  <script src="/js/main.js" defer></script>
</body>
</html>
"""


def card(p, lead=False):
    cls = "post-card post-card-lead" if lead else "post-card"
    h = "h2" if lead else "h3"
    return f"""          <article class="{cls} reveal-up">
            <div class="post-thumb">
              <img src="{p['image']}" alt="{p['image_alt']}" loading="lazy" width="1200" height="675">
            </div>
            <div class="post-body">
              <p class="post-meta">{p['category']}<span class="dot">✦</span><span class="post-time">{p['reading']} min de lecture</span></p>
              <{h}><a href="/blog/{p['slug']}" class="post-link">{p['title']}</a></{h}>
              <p>{p['excerpt']}</p>
              <span class="info-link">Lire l'article <span aria-hidden="true">→</span></span>
            </div>
          </article>
"""


def build_index():
    ld = {
        "@context": "https://schema.org", "@type": "Blog",
        "@id": f"{BASE}/blog#blog", "name": "Le Journal du Silver Palace",
        "description": "Guides, coulisses et bons plans de la nuit toulousaine par le Silver Palace, club de striptease et cabaret à Toulouse.",
        "url": f"{BASE}/blog", "inLanguage": "fr-FR",
        "publisher": {"@id": f"{BASE}/#club"},
        "blogPost": [{"@type": "BlogPosting", "headline": p["title"],
                      "url": f"{BASE}/blog/{p['slug']}", "datePublished": p["date"],
                      "image": f"{BASE}{p['image']}"} for p in POSTS],
    }
    crumbs = {"@context": "https://schema.org", "@type": "BreadcrumbList",
              "itemListElement": [
                  {"@type": "ListItem", "position": 1, "name": "Accueil", "item": f"{BASE}/"},
                  {"@type": "ListItem", "position": 2, "name": "Blog", "item": f"{BASE}/blog"}]}
    extra = ('\n  <script type="application/ld+json">\n' + json.dumps(ld, ensure_ascii=False, indent=2)
             + '\n  </script>\n  <script type="application/ld+json">\n'
             + json.dumps(crumbs, ensure_ascii=False, indent=2) + '\n  </script>')
    cards = "".join(card(p, i == 0) for i, p in enumerate(POSTS))
    html = head("Le Journal — Blog du Silver Palace, Club de Striptease à Toulouse",
                "Guides de la nuit toulousaine, coulisses du cabaret et conseils pratiques : le journal du Silver Palace, club de striptease et cabaret à Toulouse.",
                f"{BASE}/blog", POSTS[0]["image"], extra,
                "blog club Toulouse, nuit toulousaine, cabaret Toulouse")
    html += chrome() + f"""    <section class="page-hero">
      <div class="section-inner">
        <nav class="breadcrumb" aria-label="Fil d'ariane">
          <a href="/">Accueil</a><span class="sep">✦</span><span class="current">Blog</span>
        </nav>
        <p class="kicker">Le Journal</p>
        <h1 class="page-title">Les nuits du <span class="accent-italic">Silver</span>, racontées</h1>
        <p class="lead">Guides pratiques, coulisses du cabaret et adresses de la nuit toulousaine. Un nouvel article chaque semaine.</p>
      </div>
    </section>
    <section class="section" style="padding-top: 0;">
      <div class="section-inner">
        <div class="blog-grid">
{cards}        </div>
      </div>
    </section>
    <section class="page-cta">
      <p class="cta-eyebrow">La nuit vous attend</p>
      <p class="cta-title">Et si vous veniez <span class="accent-italic">la vivre</span>&nbsp;?</p>
      <a href="/reservation" class="btn btn-gold btn-lg">Réserver ma table</a>
    </section>
"""
    open(os.path.join(SITE, "blog.html"), "w", encoding="utf-8").write(html + FOOTER)


def build_post(p, others):
    url = f"{BASE}/blog/{p['slug']}"
    ld = {"@context": "https://schema.org", "@type": "BlogPosting",
          "headline": p["title"], "description": p["description"],
          "image": f"{BASE}{p['image']}", "datePublished": p["date"],
          "dateModified": p["date"], "inLanguage": "fr-FR",
          "mainEntityOfPage": {"@type": "WebPage", "@id": url},
          "author": {"@type": "Organization", "name": "Silver Palace", "url": f"{BASE}/"},
          "publisher": {"@id": f"{BASE}/#club"},
          "keywords": p["keywords"], "wordCount": len(re.sub(r"<[^>]+>", " ", p["body"]).split())}
    crumbs = {"@context": "https://schema.org", "@type": "BreadcrumbList",
              "itemListElement": [
                  {"@type": "ListItem", "position": 1, "name": "Accueil", "item": f"{BASE}/"},
                  {"@type": "ListItem", "position": 2, "name": "Blog", "item": f"{BASE}/blog"},
                  {"@type": "ListItem", "position": 3, "name": p["title"], "item": url}]}
    blocks = [ld, crumbs]
    if p.get("faq"):
        blocks.append({"@context": "https://schema.org", "@type": "FAQPage",
                       "mainEntity": [{"@type": "Question", "name": q,
                                       "acceptedAnswer": {"@type": "Answer", "text": a}}
                                      for q, a in p["faq"]]})
    extra = "".join('\n  <script type="application/ld+json">\n'
                    + json.dumps(b, ensure_ascii=False, indent=2) + '\n  </script>' for b in blocks)

    faq_html = ""
    if p.get("faq"):
        items = "".join(f"""          <details class="faq-item">
            <summary>{q}</summary>
            <div class="faq-answer"><p>{a}</p></div>
          </details>
""" for q, a in p["faq"])
        faq_html = f"""    <section class="section faq" style="padding-top: 0;">
      <div class="section-inner section-narrow">
        <p class="kicker center">Questions fréquentes</p>
        <h2 class="h2 center">On vous répond</h2>
        <div class="faq-list">
{items}        </div>
      </div>
    </section>
"""
    rel = "".join(card(o) for o in others[:3])
    related = f"""    <section class="section" style="padding-top: 0;">
      <div class="section-inner">
        <p class="kicker center">À lire aussi</p>
        <h2 class="h2 center">D'autres <span class="accent-italic">nuits</span></h2>
        <div class="related">
{rel}        </div>
      </div>
    </section>
""" if rel else ""

    tags = "".join(f"<span>{t}</span>" for t in p["tags"])
    html = head(p["meta_title"], p["description"], url, p["image"], extra, p["keywords"])
    html += chrome() + f"""    <article>
    <section class="page-hero has-media">
      <div class="page-hero-media" aria-hidden="true">
        <img src="{p['image']}" alt="" loading="eager" fetchpriority="high"
             width="1440" height="1080" style="object-position: 50% 30%;">
      </div>
      <div class="section-inner">
        <nav class="breadcrumb" aria-label="Fil d'ariane">
          <a href="/">Accueil</a><span class="sep">✦</span><a href="/blog">Blog</a><span class="sep">✦</span><span class="current">{p['category']}</span>
        </nav>
        <p class="kicker">{p['category']}</p>
        <h1 class="page-title">{p['title']}</h1>
        <p class="post-meta"><time datetime="{p['date']}">{fr_date(p['date'])}</time><span class="dot">✦</span><span class="post-time">{p['reading']} min de lecture</span></p>
      </div>
    </section>
    <section class="section" style="padding-top: 0;">
      <div class="section-inner">
        <div class="article-body">
          <p class="chapo">{p['chapo']}</p>
{p['body']}
        </div>
        <div class="article-foot">
          <div class="article-tags">{tags}</div>
          <a href="/blog" class="info-link">Tous les articles <span aria-hidden="true">→</span></a>
        </div>
      </div>
    </section>
    </article>
{faq_html}    <section class="page-cta">
      <p class="cta-eyebrow">La nuit vous attend</p>
      <p class="cta-title">Réservez votre <span class="accent-italic">table</span></p>
      <a href="/reservation" class="btn btn-gold btn-lg">Réserver maintenant</a>
    </section>
{related}"""
    d = os.path.join(SITE, "blog")
    os.makedirs(d, exist_ok=True)
    open(os.path.join(d, p["slug"] + ".html"), "w", encoding="utf-8").write(html + FOOTER)


def sitemap_entries():
    """Lignes à injecter dans le sitemap principal."""
    out = [f"""  <url>
    <loc>{BASE}/blog</loc>
    <lastmod>{POSTS[0]['date']}</lastmod>
    <changefreq>weekly</changefreq>
    <priority>0.8</priority>
  </url>"""]
    for p in POSTS:
        out.append(f"""  <url>
    <loc>{BASE}/blog/{p['slug']}</loc>
    <lastmod>{p['date']}</lastmod>
    <changefreq>monthly</changefreq>
    <priority>0.7</priority>
  </url>""")
    return "\n".join(out)


def inject_sitemap():
    path = os.path.join(SITE, "sitemap.xml")
    s = open(path, encoding="utf-8").read()
    s = re.sub(r"\n  <!-- blog -->.*?(?=</urlset>)", "\n", s, flags=re.S)
    s = s.replace("</urlset>", "  <!-- blog -->\n" + sitemap_entries() + "\n</urlset>")
    open(path, "w", encoding="utf-8").write(s)


def published(posts, today=None):
    """Articles dont la date de publication est atteinte."""
    today = today or datetime.date.today().isoformat()
    return [p for p in posts if p["date"] <= today]


def clean_orphans(slugs):
    """Supprime les pages d'articles qui ne sont plus publiés."""
    d = os.path.join(SITE, "blog")
    if not os.path.isdir(d):
        return 0
    n = 0
    for f in os.listdir(d):
        if f.endswith(".html") and f[:-5] not in slugs:
            os.remove(os.path.join(d, f))
            n += 1
    return n


if __name__ == "__main__":
    args = sys.argv[1:]
    today = datetime.date.today().isoformat()
    everything = sorted(POSTS, key=lambda p: p["date"], reverse=True)

    if "--agenda" in args:
        live = [p for p in everything if p["date"] <= today]
        soon = [p for p in reversed(everything) if p["date"] > today]
        print(f"Aujourd'hui : {today}\n")
        print(f"EN LIGNE ({len(live)})")
        for p in live[:5]:
            print(f"  {p['date']}  {p['title'][:62]}")
        if len(live) > 5:
            print(f"  … et {len(live) - 5} autres")
        print(f"\nÀ VENIR ({len(soon)})")
        for p in soon[:8]:
            print(f"  {p['date']}  {p['title'][:62]}")
        if len(soon) > 8:
            print(f"  … et {len(soon) - 8} autres, jusqu'au {soon[-1]['date']}")
        sys.exit(0)

    posts = everything if "--all" in args else published(everything)
    if not posts:
        print("Aucun article publiable pour l'instant.")
        sys.exit(0)

    POSTS[:] = posts
    build_index()
    for p in posts:
        build_post(p, [o for o in posts if o["slug"] != p["slug"]])
    removed = clean_orphans({p["slug"] for p in posts})
    inject_sitemap()

    attente = len(everything) - len(posts)
    print(f"blog : index + {len(posts)} articles publiés")
    if removed:
        print(f"{removed} page(s) obsolète(s) supprimée(s)")
    if attente:
        prochain = min((p for p in everything if p["date"] > today), key=lambda p: p["date"])
        print(f"{attente} article(s) en attente — prochain le {prochain['date']}")
    print("sitemap mis à jour")
