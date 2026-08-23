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
