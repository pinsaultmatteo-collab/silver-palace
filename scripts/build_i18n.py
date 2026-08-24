# -*- coding: utf-8 -*-
"""Génère la version anglaise du site Silver Palace sous /en/ (moteur corrigé)."""
import os, re, glob, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from i18n_dict import T, SLUGS, SITE
from i18n_fix import LEGAL

T.update(LEGAL)
# variantes avec & brut (titres, og:title) en plus des &amp;
for k in list(T):
    if "&amp;" in k:
        T.setdefault(k.replace("&amp;", "&"), T[k].replace("&amp;", "&"))

OUT = os.path.join(SITE, "en")
BASE = "https://silver-palace.com"
TOKEN = "@@LANGSWITCH@@"

fr_url = lambda s: "/" if s == "index" else "/" + s
en_url = lambda s: "/en/" if SLUGS[s] == "index" else "/en/" + SLUGS[s]


def switcher(slug, active):
    fr, en = fr_url(slug), en_url(slug)
    on = ' class="lang-active" aria-current="true"'
    label = "Choix de la langue" if active == "fr" else "Language"
    return (f'<div class="lang-switch" role="group" aria-label="{label}">'
            f'<a href="{fr}" hreflang="fr" lang="fr"{on if active == "fr" else ""}>FR</a>'
            f'<a href="{en}" hreflang="en" lang="en"{on if active == "en" else ""}>EN</a>'
            f'</div>')


def build():
    os.makedirs(OUT, exist_ok=True)
    done = []
    for path in sorted(glob.glob(os.path.join(SITE, "*.html"))):
        slug = os.path.basename(path)[:-5]
        if slug not in SLUGS:
            continue
        raw = open(path, encoding="utf-8").read()

        # --- squelette commun : jeton à la place du sélecteur + hreflang
        alt = (f'<link rel="alternate" hreflang="fr-FR" href="{BASE}{fr_url(slug)}">\n'
               f'  <link rel="alternate" hreflang="en" href="{BASE}{en_url(slug)}">\n'
               f'  <link rel="alternate" hreflang="x-default" href="{BASE}{fr_url(slug)}">\n  ')
        skel = raw
        if 'hreflang="x-default"' not in skel:
            skel = skel.replace('<link rel="canonical"', alt + '<link rel="canonical"', 1)
        if TOKEN not in skel and "lang-switch" not in skel:
            skel = skel.replace('<div class="header-actions">',
                                f'{TOKEN}\n      <div class="header-actions">', 1)
            m = re.search(r'\n\s*<a href="[^"]*"[^>]*class="mobile-cta">', skel)
            if m:
                skel = skel[:m.start()] + f'\n      {TOKEN}' + skel[m.start():]

        # --- FR
        open(path, "w", encoding="utf-8").write(skel.replace(TOKEN, switcher(slug, "fr")))

        # --- EN : traduire puis relier, le jeton protège le sélecteur
        en = skel.replace('<html lang="fr">', '<html lang="en">', 1)
        en = en.replace('"inLanguage": "fr-FR"', '"inLanguage": "en"')
        en = en.replace('content="fr_FR"', 'content="en_GB"')
        for k in sorted(T, key=len, reverse=True):
            en = en.replace(k, T[k])
        for fr_s, en_s in SLUGS.items():
            if fr_s not in ("index", "404"):
                en = en.replace(f'href="/{fr_s}"', f'href="/en/{en_s}"')
        en = re.sub(r'href="/"(?=[\s>])', 'href="/en/"', en)
        en = en.replace(f'"{BASE}{fr_url(slug)}"', f'"{BASE}{en_url(slug)}"')
        # chemins relatifs de la home -> absolus (la page vit dans /en/)
        en = en.replace('href="css/style.css"', 'href="/css/style.css"')
        en = en.replace('src="js/main.js"', 'src="/js/main.js"')
        en = re.sub(r'(src|href)="images/', r'\1="/images/', en)
        # le sélecteur, en dernier : ses liens ne doivent pas être réécrits
        en = en.replace(TOKEN, switcher(slug, "en"))
        open(os.path.join(OUT, SLUGS[slug] + ".html"), "w", encoding="utf-8").write(en)
        done.append(SLUGS[slug])
    return done


if __name__ == "__main__":
    d = build()
    print(f"{len(d)} pages : " + ", ".join(d))
