# -*- coding: utf-8 -*-
"""Langues du site, drapeaux SVG et sélecteur de langue."""

# Drapeaux SVG inline : les emoji drapeaux ne s'affichent pas sous Windows.
# Coins arrondis via CSS (.flag { border-radius }) pour éviter les ids dupliqués.
FLAGS = {
    "fr": '<svg class="flag" viewBox="0 0 21 15" aria-hidden="true" focusable="false">'
          '<rect width="7" height="15" fill="#002654"/>'
          '<rect x="7" width="7" height="15" fill="#F2F2F2"/>'
          '<rect x="14" width="7" height="15" fill="#ED2939"/></svg>',
    "en": '<svg class="flag" viewBox="0 0 21 15" aria-hidden="true" focusable="false">'
          '<rect width="21" height="15" fill="#012169"/>'
          '<path d="M0 0 21 15M21 0 0 15" stroke="#F2F2F2" stroke-width="3"/>'
          '<path d="M0 0 21 15M21 0 0 15" stroke="#C8102E" stroke-width="1.6"/>'
          '<path d="M10.5 0v15M0 7.5h21" stroke="#F2F2F2" stroke-width="5"/>'
          '<path d="M10.5 0v15M0 7.5h21" stroke="#C8102E" stroke-width="3"/></svg>',
    "es": '<svg class="flag" viewBox="0 0 21 15" aria-hidden="true" focusable="false">'
          '<rect width="21" height="15" fill="#AA151B"/>'
          '<rect y="3.75" width="21" height="7.5" fill="#F1BF00"/></svg>',
}

NAMES = {"fr": "Français", "en": "English", "es": "Español"}
SWITCH_LABEL = {"fr": "Choix de la langue", "en": "Language", "es": "Idioma"}

# slug français -> slug traduit, par langue
SLUGS = {
    "en": {
        "index": "index", "reservation": "booking", "application": "apply",
        "events": "events", "carte": "drinks", "shows": "dances",
        "contact": "contact", "about": "about", "legal": "legal",
        "privacy": "privacy", "404": "404",
    },
    "es": {
        "index": "index", "reservation": "reservas", "application": "trabajo",
        "events": "eventos", "carte": "bebidas", "shows": "bailes",
        "contact": "contacto", "about": "club", "legal": "aviso-legal",
        "privacy": "privacidad", "404": "404",
    },
}

ORDER = ["fr", "en", "es"]


def url_for(lang, slug):
    """URL d'une page dans une langue donnée."""
    if lang == "fr":
        return "/" if slug == "index" else "/" + slug
    tr = SLUGS[lang][slug]
    return f"/{lang}" if tr == "index" else f"/{lang}/{tr}"


def switcher(slug, active):
    """Sélecteur de langue : drapeaux liés à la page équivalente."""
    out = [f'<div class="lang-switch" role="group" aria-label="{SWITCH_LABEL[active]}">']
    for lang in ORDER:
        cls = ' class="lang-active" aria-current="true"' if lang == active else ""
        out.append(f'<a href="{url_for(lang, slug)}" hreflang="{lang}" lang="{lang}"'
                   f'{cls} title="{NAMES[lang]}"><span class="sr-only">{NAMES[lang]}</span>'
                   f'{FLAGS[lang]}</a>')
    out.append("</div>")
    return "".join(out)


def alternates(slug):
    """Balises hreflang réciproques."""
    base = "https://silver-palace.com"
    codes = {"fr": "fr-FR", "en": "en", "es": "es"}
    lines = [f'<link rel="alternate" hreflang="{codes[l]}" href="{base}{url_for(l, slug)}">'
             for l in ORDER]
    lines.append(f'<link rel="alternate" hreflang="x-default" href="{base}{url_for("fr", slug)}">')
    return "\n  ".join(lines)
