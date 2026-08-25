# Calendrier éditorial — Blog Silver Palace

**52 articles écrits, publiés automatiquement un par semaine** du 4 août 2026 au
27 juillet 2027. Objectif : capter la longue traîne autour de « club de striptease
Toulouse » et « cabaret Toulouse », et faire remonter tout le domaine.

## Comment la publication fonctionne

Les 52 articles sont **déjà rédigés** et vivent dans le dépôt. Chacun porte une
date : le générateur ne produit que ceux dont la date est atteinte. Les autres
restent invisibles — ils n'existent ni sur le site, ni dans le sitemap.

Chaque **mardi à 10h**, une action GitHub relance la génération et pousse le
nouvel article. Vercel déploie dans la foulée. Aucune intervention n'est
nécessaire.

```bash
python3 scripts/build_blog.py --agenda   # voir ce qui est en ligne et ce qui attend
python3 scripts/build_blog.py --all      # tout générer en local pour relecture
```

Le fichier de l'action : `.github/workflows/publier-article.yml`. Le bouton
« Run workflow » sur GitHub permet aussi de déclencher une publication à la main.

## Principe éditorial

Trois familles alternent pour éviter la monotonie :

| Famille | Rôle SEO | Part |
|---|---|---|
| **Guide / Les codes** | Intention commerciale forte (EVG, tarifs, réservation) — ce qui convertit | ~45 % |
| **Ville rose** | Trafic large sur la nuit toulousaine — ce qui fait le volume | ~35 % |
| **Coulisses** | Notoriété, recrutement, contenu que personne d'autre ne produit | ~20 % |

Règles appliquées à chaque article :

- structure H2/H3 claire, 1 000 à 1 500 mots ;
- le mot-clé cible dans le titre, l'URL, le chapô et un H2 ;
- **3 à 5 liens internes** vers les pages de conversion et les autres articles ;
- un bloc **FAQ** balisé `FAQPage` — c'est lui qui décroche les positions zéro
  et les citations dans les IA ;
- une image du club avec `alt` descriptif contenant « Toulouse » ;
- les articles saisonniers tombent avant l'événement (Halloween, Nouvel An,
  Saint-Valentin, Fête de la musique, 14 juillet).

## Le programme complet

### Août 2026

| Date | Article | Mot-clé principal | Famille |
|---|---|---|---|
| 04/08 | Organiser un EVG à Toulouse : le guide complet | `EVG Toulouse` | Guide |
| 11/08 | Première visite en club de striptease à Toulouse : les codes à connaître | `club de striptease Toulouse` | Les codes |
| 18/08 | Que faire à Toulouse après minuit ? Le guide des noctambules | `sortir à Toulouse le soir` | Ville rose |
| 25/08 | Devenir danseuse en cabaret : ce qu'il faut vraiment savoir | `devenir danseuse Toulouse` | Coulisses |

### Septembre 2026

| Date | Article | Mot-clé principal | Famille |
|---|---|---|---|
| 01/09 | Toulouse étudiante : le guide des soirées de la rentrée | `soirée étudiante Toulouse` | Ville rose |
| 08/09 | Combien coûte une soirée en club de striptease à Toulouse ? | `prix club striptease Toulouse` | Guide |
| 15/09 | Table dance, lap dance, salon privé : quelle différence ? | `différence table dance lap dance` | Guide |
| 22/09 | Les plus beaux bars à cocktails de Toulouse | `bar cocktail Toulouse` | Ville rose |
| 29/09 | Venir seul en club de striptease : le guide décomplexé | `venir seul club striptease` | Les codes |

### Octobre 2026

| Date | Article | Mot-clé principal | Famille |
|---|---|---|---|
| 06/10 | L'histoire du cabaret français, du Chat Noir à aujourd'hui | `histoire cabaret français` | Coulisses |
| 13/10 | Réserver une table en club : le mode d'emploi | `réserver table club Toulouse` | Guide |
| 20/10 | Toulouse la nuit : le guide par quartier | `quartier festif Toulouse` | Ville rose |
| 27/10 | Halloween à Toulouse : où sortir le 31 octobre | `Halloween Toulouse` | Ville rose |

### Novembre 2026

| Date | Article | Mot-clé principal | Famille |
|---|---|---|---|
| 03/11 | Organiser un EVJF à Toulouse : le guide des témoins | `EVJF Toulouse` | Guide |
| 10/11 | Venir en couple dans un club de striptease : le guide | `couple club striptease` | Les codes |
| 17/11 | Pole dance : sport, art ou séduction ? | `pole dance discipline` | Coulisses |
| 24/11 | Où dormir près de la gare Matabiau à Toulouse ? | `hôtel Matabiau Toulouse` | Ville rose |

### Décembre 2026

| Date | Article | Mot-clé principal | Famille |
|---|---|---|---|
| 01/12 | Soirée d'entreprise à Toulouse : privatiser un lieu | `privatisation soirée entreprise Toulouse` | Guide |
| 08/12 | Champagne : comment choisir sa bouteille en club | `quel champagne choisir` | Guide |
| 15/12 | Cadeau de Noël original pour homme à Toulouse | `cadeau original homme Toulouse` | Guide |
| 22/12 | Réveillon du Nouvel An à Toulouse : où sortir | `réveillon Toulouse` | Ville rose |
| 29/12 | Les nuits qui ont marqué 2026 au Silver Palace | `Silver Palace Toulouse` | Coulisses |

### Janvier 2027

| Date | Article | Mot-clé principal | Famille |
|---|---|---|---|
| 05/01 | Janvier à Toulouse : sortir quand tout le monde hiberne | `sortir Toulouse janvier` | Ville rose |
| 12/01 | Une nuit dans les coulisses du Silver Palace | `coulisses cabaret` | Coulisses |
| 19/01 | Se déplacer la nuit à Toulouse : métro, VTC, Noctambus | `transport nuit Toulouse` | Ville rose |
| 26/01 | Le métier de videur en club privé | `métier sécurité club` | Coulisses |

### Février 2027

| Date | Article | Mot-clé principal | Famille |
|---|---|---|---|
| 02/02 | Saint-Valentin à Toulouse : sortir en couple, autrement | `Saint-Valentin original Toulouse` | Ville rose |
| 09/02 | Dix idées reçues sur les clubs de striptease | `clichés club striptease` | Les codes |
| 16/02 | Anniversaire à Toulouse : sept idées pour marquer le coup | `anniversaire original Toulouse` | Guide |
| 23/02 | Les tenues de scène : plumes, strass et contraintes | `costume cabaret` | Coulisses |

### Mars 2027

| Date | Article | Mot-clé principal | Famille |
|---|---|---|---|
| 02/03 | Le pourboire en club : usages et montants | `pourboire club striptease` | Les codes |
| 09/03 | Comment se prépare un show de cabaret | `préparation show cabaret` | Coulisses |
| 16/03 | Danseuse et étudiante : concilier les deux | `job étudiant nuit Toulouse` | Coulisses |
| 23/03 | Que faire à Toulouse un mardi soir ? | `sortir Toulouse en semaine` | Ville rose |
| 30/03 | Week-end entre amis à Toulouse : l'itinéraire idéal | `week-end entre amis Toulouse` | Ville rose |

### Avril 2027

| Date | Article | Mot-clé principal | Famille |
|---|---|---|---|
| 06/04 | Le Capitole à 3h du matin : Toulouse insolite | `Toulouse insolite nuit` | Ville rose |
| 13/04 | Les cocktails qu'on ne trouve qu'à Toulouse | `cocktail toulousain` | Ville rose |
| 20/04 | La musique d'une nuit de cabaret | `musique cabaret` | Coulisses |
| 27/04 | EVG : les dix erreurs qui ruinent la soirée | `erreurs EVG` | Guide |

### Mai 2027

| Date | Article | Mot-clé principal | Famille |
|---|---|---|---|
| 04/05 | Toulouse ou Bordeaux : deux façons de sortir | `sortir Toulouse Bordeaux` | Ville rose |
| 11/05 | Les métiers de la nuit : qui fait tourner un club | `métiers de la nuit` | Coulisses |
| 18/05 | Pourquoi les téléphones restent dans la poche | `photo interdite club` | Les codes |
| 25/05 | Saison des EVG : réserver au bon moment | `EVG été` | Guide |

### Juin 2027

| Date | Article | Mot-clé principal | Famille |
|---|---|---|---|
| 01/06 | Devenir barman en club de nuit | `devenir barman club` | Coulisses |
| 08/06 | L'été à Toulouse : sortir quand il fait 35° | `sortir Toulouse été` | Ville rose |
| 15/06 | Fête de la musique à Toulouse : survivre à la nuit du 21 juin | `fête de la musique Toulouse` | Ville rose |
| 22/06 | Le vocabulaire du cabaret, de A à Z | `vocabulaire cabaret` | Coulisses |
| 29/06 | Rooftops et terrasses : commencer la soirée en hauteur | `rooftop Toulouse` | Ville rose |

### Juillet 2027

| Date | Article | Mot-clé principal | Famille |
|---|---|---|---|
| 06/07 | Toulouse en juillet : la ville partagée | `Toulouse juillet` | Ville rose |
| 13/07 | 14 juillet à Toulouse : après le feu d'artifice | `14 juillet Toulouse` | Ville rose |
| 20/07 | Août à Toulouse : la ville rendue à ceux qui restent | `Toulouse août` | Ville rose |
| 27/07 | Un an de nuits : ce que ce blog nous a appris | `blog Silver Palace` | Coulisses |

## Modifier un article avant sa publication

Les articles sont répartis par saison dans `scripts/` :
`posts_automne.py`, `posts_hiver.py`, `posts_fetes.py`, `posts_printemps.py`,
`posts_ete1.py`, `posts_ete2.py`.

Éditez le texte, puis relancez `python3 scripts/build_blog.py`. Un article déjà
publié sera mis à jour ; un article à venir restera invisible jusqu'à sa date.

## Ce qu'il faudra surveiller

- **Search Console** : indexation des nouvelles URL sous 48 h, sinon soumettre à la main ;
- les articles qui remontent doivent être **enrichis** plutôt que multipliés — un
  article qui atteint la page 2 mérite 400 mots de plus, pas un concurrent ;
- **actualiser les articles datés** : les tarifs cités, les horaires de métro et
  les dates d'événements devront être revus dans un an ;
- les **photos** : les 52 articles se partagent une douzaine d'images. Chaque
  nouveau shooting du club permettra d'en varier davantage.
