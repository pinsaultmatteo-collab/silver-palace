# -*- coding: utf-8 -*-
"""Génère les versions traduites du site Silver Palace (/en/, /es/).

Les pages françaises sont la source de vérité : après toute modification
du contenu FR, relancer ce script pour répercuter les traductions.

    python3 scripts/build_i18n.py
"""
import os, re, glob, sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
SITE = os.path.join(os.path.dirname(HERE), "site")

from i18n_langs import ORDER, SLUGS, switcher, alternates, url_for
from i18n_dict import T as T_EN
from i18n_fix import LEGAL
from i18n_es import T_ES

T_EN.update(LEGAL)
DICTS = {"en": T_EN, "es": T_ES}
LOCALES = {"en": "en_GB", "es": "es_ES"}
INLANG = {"en": "en", "es": "es"}
BASE = "https://silver-palace.com"
TOKEN = "@@LANGSWITCH@@"


def expand(d):
    """Ajoute les variantes avec & brut (titres, og:title) aux clés en &amp;."""
    for k in list(d):
        if "&amp;" in k:
            d.setdefault(k.replace("&amp;", "&"), d[k].replace("&amp;", "&"))
    return d


def skeleton(raw, slug):
    """Pose le jeton du sélecteur et les balises hreflang, communs à toutes les langues.

    Idempotent : un sélecteur ou des hreflang déjà présents sont remplacés,
    pour que le script puisse être relancé sans dupliquer ni figer l'ancien état.
    """
    out = raw
    # repartir d'une page propre
    out = re.sub(r'\s*<div class="lang-switch".*?</div>', TOKEN, out, flags=re.S)
    out = re.sub(r'\s*<link rel="alternate" hreflang="[^"]*" href="[^"]*">', "", out)

    out = out.replace('<link rel="canonical"', alternates(slug) + '\n  <link rel="canonical"', 1)
    if TOKEN not in out:
        out = out.replace('<div class="header-actions">',
                          f'{TOKEN}\n      <div class="header-actions">', 1)
        m = re.search(r'\n\s*<a href="[^"]*"[^>]*class="mobile-cta">', out)
        if m:
            out = out[:m.start()] + f'\n      {TOKEN}' + out[m.start():]
    return out


def translate_page(skel, slug, lang):
    """Traduit une page et réécrit ses liens internes vers la langue cible."""
    d = expand(DICTS[lang])
    out = skel.replace('<html lang="fr">', f'<html lang="{lang}">', 1)
    out = out.replace('"inLanguage": "fr-FR"', f'"inLanguage": "{INLANG[lang]}"')
    out = out.replace('content="fr_FR"', f'content="{LOCALES[lang]}"')
    for k in sorted(d, key=len, reverse=True):
        out = out.replace(k, d[k])
    for fr_slug, tr_slug in SLUGS[lang].items():
        if fr_slug not in ("index", "404"):
            out = out.replace(f'href="/{fr_slug}"', f'href="/{lang}/{tr_slug}"')
    out = re.sub(r'href="/"(?=[\s>])', f'href="/{lang}"', out)
    # le blog n'existe qu'en français : on retire l'entrée des autres langues
    out = re.sub(r'\n\s*<a href="/blog"[^>]*>[^<]*</a>', "", out)
    out = out.replace(f'"{BASE}{url_for("fr", slug)}"', f'"{BASE}{url_for(lang, slug)}"')
    # la home utilise des chemins relatifs, les sous-dossiers ont besoin d'absolus
    out = out.replace('href="css/style.css"', 'href="/css/style.css"')
    out = out.replace('src="js/main.js"', 'src="/js/main.js"')
    out = re.sub(r'(src|href)="images/', r'\1="/images/', out)
    # en dernier : les liens du sélecteur ne doivent pas être réécrits
    return out.replace(TOKEN, switcher(slug, lang))


def build():
    counts = {}
    for path in sorted(glob.glob(os.path.join(SITE, "*.html"))):
        slug = os.path.basename(path)[:-5]
        if slug not in SLUGS["en"]:
            continue
        skel = skeleton(open(path, encoding="utf-8").read(), slug)
        open(path, "w", encoding="utf-8").write(skel.replace(TOKEN, switcher(slug, "fr")))
        for lang in ORDER:
            if lang == "fr":
                continue
            out_dir = os.path.join(SITE, lang)
            os.makedirs(out_dir, exist_ok=True)
            name = SLUGS[lang][slug] + ".html"
            open(os.path.join(out_dir, name), "w", encoding="utf-8").write(
                translate_page(skel, slug, lang))
            counts[lang] = counts.get(lang, 0) + 1
    return counts


def sitemap():
    pages = [("index", "weekly", 1.0), ("reservation", "monthly", 0.9),
             ("shows", "monthly", 0.8), ("carte", "monthly", 0.8),
             ("events", "weekly", 0.8), ("application", "monthly", 0.7),
             ("about", "yearly", 0.6), ("contact", "yearly", 0.6),
             ("legal", "yearly", 0.2), ("privacy", "yearly", 0.2)]
    codes = {"fr": "fr-FR", "en": "en", "es": "es"}
    out = ['<?xml version="1.0" encoding="UTF-8"?>',
           '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9"',
           '        xmlns:xhtml="http://www.w3.org/1999/xhtml">']
    for slug, freq, prio in pages:
        for lang in ORDER:
            p = prio if lang == "fr" else round(prio - 0.1, 1)
            out.append("  <url>")
            out.append(f"    <loc>{BASE}{url_for(lang, slug)}</loc>")
            for l in ORDER:
                out.append(f'    <xhtml:link rel="alternate" hreflang="{codes[l]}" '
                           f'href="{BASE}{url_for(l, slug)}"/>')
            out.append(f'    <xhtml:link rel="alternate" hreflang="x-default" '
                       f'href="{BASE}{url_for("fr", slug)}"/>')
            out.append("    <lastmod>2026-08-24</lastmod>")
            out.append(f"    <changefreq>{freq}</changefreq>")
            out.append(f"    <priority>{p}</priority>")
            out.append("  </url>")
    out.append("</urlset>")
    open(os.path.join(SITE, "sitemap.xml"), "w", encoding="utf-8").write("\n".join(out) + "\n")
    return len(pages) * len(ORDER)


if __name__ == "__main__":
    c = build()
    n = sitemap()
    print(" ".join(f"{lang}: {v} pages" for lang, v in sorted(c.items())))
    print(f"sitemap : {n} URLs")
