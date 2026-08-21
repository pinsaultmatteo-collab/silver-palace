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
├── index.html          # Home page (SEO complet : JSON-LD NightClub + FAQPage, OG, geo)
├── css/style.css       # Design system complet (palette néon rose/violet)
├── js/main.js          # Interactions (scrub vidéo épinglé, paillettes, carrousel, parallax…)
└── images/             # Photos optimisées + frames des séquences (spectacle/, apercu/)
```

## Développement local

```bash
npx serve -l 4173 site
```

## ⚠️ Avant mise en production

- Retirer le hook QA (`?s=` dans `js/main.js` + bloc `.qa` dans `css/style.css`)
- Brancher le formulaire newsletter sur l'ESP du client (TODO dans `main.js`)
- Valider les noms de scène du carrousel « Les visages de la nuit » avec le club (tableau `DANCERS` dans `main.js`)
- Ajouter les pages intérieures, `sitemap.xml`, `robots.txt`, `llms.txt`
