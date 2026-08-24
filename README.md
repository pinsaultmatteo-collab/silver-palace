# Silver Palace — Site vitrine

Refonte du site vitrine du **Silver Palace**, club de striptease & cabaret à Toulouse (31 Rue de Stalingrad, 31000).

Réalisé par PMC Marketing.

## Stack

- **HTML / CSS / JS vanilla** — zéro dépendance, zéro framework : performances maximales (Core Web Vitals) et contenu 100 % crawlable
- Fonts Google (Cinzel, Cormorant Garamond, Jost)
- Photos et vidéos : assets officiels du club (Instagram / Cloudinary), frames extraites via ffmpeg pour les séquences scroll-scrub

## Structure

```
site/
├── index.html            # Home page (JSON-LD NightClub + FAQPage, OG, geo)
├── reservation.html      # + application, events, carte, shows, contact,
├── …                     #   about, legal, privacy, 404 (même template)
├── en/                   # version anglaise (booking, apply, drinks, dances…)
├── es/                   # version espagnole (reservas, trabajo, bebidas, bailes…)
├── blog.html + blog/     # blog français (1 article/semaine)
├── sitemap.xml / robots.txt / llms.txt
├── css/style.css         # Design system complet (palette néon rose/violet)
├── js/main.js            # Interactions (scrub épinglé, paillettes, formulaires…)
└── images/               # Photos optimisées + frames des séquences
```

URLs propres via `vercel.json` (`cleanUrls`) : `/reservation` sert `reservation.html`.

## Développement local

```bash
npx serve -l 4173 site
```

## ⚠️ Avant mise en production

- Retirer le hook QA (`?s=` dans `js/main.js` + bloc `.qa` dans `css/style.css`)
- **Brancher les 4 formulaires** (réservation, candidature, contact, newsletter) sur un backend — Formspree ou e-mail du club (TODO dans `main.js`)
- **Valider avec le club les tarifs** des pages `/carte` et `/shows` (placeholders réalistes, commentaires ⚠ dans le HTML)
- Compléter les mentions légales (`legal.html` : raison sociale, SIRET, directeur de publication)
- Valider les noms de scène du carrousel (tableau `DANCERS` dans `main.js`)
- Remplacer les photos indiquées par la cliente

## Multilingue

Le site existe en français (racine), anglais (`/en/`) et espagnol (`/es/`), avec de
vraies pages traduites — indexables par Google — reliées par `hreflang`. Un sélecteur
à drapeaux (SVG inline, pas d'emoji) est présent dans le header et le menu mobile.

Les pages traduites sont générées à partir des pages françaises :

```bash
python3 scripts/build_i18n.py
```

**Après toute modification du contenu français, relancer ce script** pour répercuter
les changements. Il est idempotent et régénère aussi le `sitemap.xml` multilingue.
Les traductions vivent dans `scripts/i18n_dict.py` (EN), `scripts/i18n_fix.py`
(EN, pages légales) et `scripts/i18n_es.py` (ES).

## Blog

Blog français uniquement — le référencement local visé se joue en français, et
trois versions hebdomadaires seraient intenables. Le contenu vit dans
`scripts/blog_posts.py` ; la stratégie éditoriale et les 24 sujets à venir sont
dans [CALENDRIER-BLOG.md](CALENDRIER-BLOG.md).

```bash
python3 scripts/build_blog.py     # régénère l'index, les articles et le sitemap
```

Chaque article embarque son balisage `BlogPosting`, son fil d'ariane et un bloc
`FAQPage`. **Lancer `build_i18n.py` avant `build_blog.py`** si les deux sont
nécessaires : le premier régénère le sitemap, le second y ajoute les URL du blog.
