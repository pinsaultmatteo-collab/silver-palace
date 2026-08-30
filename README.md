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
- **Créer le compte Brevo et renseigner les variables d'environnement Vercel** (voir « Formulaires » plus bas) — sans ça, les 4 formulaires affichent une erreur au lieu d'envoyer
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

## Formulaires

Les 4 formulaires (réservation, candidature, contact, newsletter) sont envoyés par
`site/js/main.js` sur `/api/form`, une fonction serverless Vercel (`api/form.js`, sans
dépendance) qui relaie vers **Brevo**. Brevo est une société française : les données
restent en UE et ne transitent par aucun tiers hors Europe — un point qui compte pour
le formulaire de candidature, qui collecte des données personnelles sensibles.

Les trois formulaires transactionnels partent en e-mail ; la newsletter alimente une
liste de diffusion, avec `replyTo` positionné sur l'adresse de la personne pour pouvoir
répondre directement depuis la boîte du club.

### Mise en service

1. Créer un compte sur [brevo.com](https://www.brevo.com) (gratuit jusqu'à 300 envois/jour)
2. Valider l'expéditeur : **Expéditeurs & IP** → ajouter l'adresse et confirmer
3. Créer la liste newsletter : **Contacts → Listes**, noter son identifiant
4. Générer la clé : **SMTP & API → Clés API**
5. Dans Vercel, **Settings → Environment Variables**, ajouter :

| Variable | Rôle |
|---|---|
| `BREVO_API_KEY` | clé API v3 |
| `MAIL_FROM` | expéditeur validé chez Brevo |
| `MAIL_TO_RESERVATION` | boîte de l'accueil |
| `MAIL_TO_CANDIDATURE` | boîte de la direction (confidentiel) |
| `MAIL_TO_CONTACT` | boîte générale |
| `BREVO_LIST_ID` | identifiant de la liste newsletter |
| `BREVO_DOI_TEMPLATE_ID` | *optionnel* — active le double opt-in |
| `BREVO_DOI_REDIRECT` | *optionnel* — page de retour après confirmation |

6. Redéployer (les variables ne sont lues qu'au démarrage de la fonction)

### Double opt-in

Sans `BREVO_DOI_TEMPLATE_ID`, l'adresse est ajoutée directement à la liste. Pour être
pleinement conforme, créer un modèle de confirmation dans Brevo et renseigner son id :
Brevo enverra alors le mail de confirmation et n'ajoutera le contact qu'après clic.

### Anti-spam

Chaque formulaire porte un champ piège (`name="website"`, masqué en CSS). S'il est
rempli, la fonction répond `200` sans rien envoyer — le robot croit avoir réussi.

### Tester

Les erreurs détaillées ne sortent jamais dans la réponse HTTP : consulter les logs de
la fonction dans Vercel (**Deployments → Functions → `api/form`**) en cas de souci.

## Blog — 52 articles, publication automatique

Blog français uniquement : le référencement local visé se joue en français, et
trois versions hebdomadaires seraient intenables pour la cliente.

**Un an de contenu est déjà écrit** (52 articles, du 04/08/2026 au 27/07/2027).
Chaque article porte une date de publication : le générateur ne produit que ceux
dont la date est atteinte, les autres restent invisibles dans le dépôt.

Une **action GitHub** (`.github/workflows/publier-article.yml`) relance la
génération chaque mardi à 10h et pousse le nouvel article — Vercel déploie
dans la foulée, sans intervention.

```bash
python3 scripts/build_blog.py            # publie ce dont la date est atteinte
python3 scripts/build_blog.py --agenda   # ce qui est en ligne / ce qui attend
python3 scripts/build_blog.py --all      # tout générer en local pour relecture
```

Les textes sont répartis par saison dans `scripts/posts_*.py`. Chaque article
embarque son balisage `BlogPosting`, son fil d'ariane et un bloc `FAQPage`.
Programme complet et stratégie : [CALENDRIER-BLOG.md](CALENDRIER-BLOG.md).

⚠️ **Lancer `build_i18n.py` avant `build_blog.py`** si les deux sont nécessaires :
le premier régénère le sitemap, le second y ajoute les URL du blog.
