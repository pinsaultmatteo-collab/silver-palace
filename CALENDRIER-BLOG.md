# Calendrier éditorial — Blog Silver Palace

Un article par semaine, en français. Objectif : capter la longue traîne autour de
« club de striptease Toulouse » et « cabaret Toulouse », et faire remonter tout le
domaine.

## Principe

Chaque article vise **un cluster de mots-clés** et **une intention de recherche**.
Trois familles se relaient pour éviter la monotonie :

| Famille | Rôle SEO | Fréquence |
|---|---|---|
| **Guides pratiques** | Intention commerciale forte (EVG, réservation, tarifs) — c'est ce qui convertit | 1 sur 2 |
| **Ville rose** | Trafic large sur la nuit toulousaine — c'est ce qui fait le volume | 1 sur 4 |
| **Coulisses / métier** | Notoriété, recrutement de danseuses, contenu que personne d'autre ne produit | 1 sur 4 |

Règles appliquées à chaque article :

- **1 500 à 2 000 mots** minimum, structure H2/H3 claire ;
- le mot-clé cible dans le titre, l'URL, le chapô et un H2 ;
- **3 à 5 liens internes** vers les pages de conversion (`/reservation`, `/shows`, `/carte`, `/application`) ;
- un bloc **FAQ** en fin d'article (balisé `FAQPage`) — c'est lui qui décroche les positions zéro et les citations dans les IA ;
- une image issue du club, avec `alt` descriptif contenant « Toulouse ».

---

## Publiés

| Date | Article | Mot-clé principal |
|---|---|---|
| 25/08 | Organiser un EVG à Toulouse : le guide complet | EVG Toulouse |
| 01/09 | Première visite en club de striptease : les codes | club de striptease Toulouse |
| 08/09 | Que faire à Toulouse après minuit ? | sortir à Toulouse le soir |
| 15/09 | Devenir danseuse en cabaret : ce qu'il faut savoir | devenir danseuse Toulouse |

---

## À venir — 6 mois de contenu

### Guides pratiques (intention commerciale)

1. **Organiser un EVJF à Toulouse : le guide des témoins** — `EVJF Toulouse`
2. **Combien coûte une soirée en club de striptease à Toulouse ?** — `prix club striptease Toulouse`
3. **Anniversaire à Toulouse : 7 idées pour marquer le coup** — `anniversaire original Toulouse`
4. **Privatiser un lieu pour une soirée d'entreprise à Toulouse** — `privatisation soirée entreprise Toulouse`
5. **Champagne : comment choisir sa bouteille en club** — `quel champagne choisir`
6. **Table dance, lap dance, salon privé : quelle différence ?** — `différence table dance lap dance`
7. **Venir en couple dans un club de striptease : le guide** — `couple club striptease`
8. **Réserver une table en club : le mode d'emploi** — `réserver club Toulouse`
9. **Cadeau d'anniversaire original pour homme à Toulouse** — `cadeau original homme Toulouse`
10. **Que faire à Toulouse un mardi soir ?** — `sortir Toulouse en semaine`

### Ville rose (trafic large)

11. **Les plus beaux bars à cocktails de Toulouse** — `bar cocktail Toulouse`
12. **Toulouse la nuit : guide par quartier** — `quartier festif Toulouse`
13. **Où dormir près de la gare Matabiau ?** — `hôtel Matabiau Toulouse`
14. **Le Capitole à 3h du matin : Toulouse insolite** — `Toulouse insolite nuit`
15. **Se déplacer la nuit à Toulouse : métro, VTC, Noctambus** — `transport nuit Toulouse`
16. **Week-end entre amis à Toulouse : l'itinéraire idéal** — `week-end entre amis Toulouse`

### Coulisses & culture (notoriété + recrutement)

17. **L'histoire du cabaret français, du Chat Noir à aujourd'hui** — `histoire cabaret français`
18. **Une nuit dans les coulisses du Silver Palace** — `coulisses cabaret`
19. **Pole dance : sport, art ou séduction ?** — `pole dance discipline`
20. **Le métier de videur en club privé** — `métier sécurité club`
21. **Comment se prépare un show de cabaret** — `préparation show cabaret`
22. **Danseuse et étudiante : concilier les deux** — `job étudiant nuit Toulouse`
23. **Les tenues de scène : plumes, strass et contraintes** — `costume cabaret`
24. **Idées reçues sur les clubs de striptease** — `clichés club striptease`

### Saisonnier (à caler sur le calendrier)

- **Décembre** : Soirée du Nouvel An à Toulouse — `réveillon Toulouse`
- **Février** : Saint-Valentin en couple, autrement — `Saint-Valentin original Toulouse`
- **Juin** : Enterrements de vie de garçon, la haute saison — `EVG été`
- **Rentrée** : Toulouse étudiante, le guide des soirées — `soirée étudiante Toulouse`

---

## Publier un article

1. Ajouter une entrée **en tête** de `POSTS` dans `scripts/blog_posts.py`
   (copier une entrée existante comme modèle) ;
2. Lancer la génération :

```bash
python3 scripts/build_blog.py
```

Le script crée la page, met à jour l'index du blog et ajoute l'URL au `sitemap.xml`.
Les articles sont triés automatiquement par date, le plus récent passe en vedette.

## Ce qu'il faudra surveiller

- **Search Console** : indexation des nouvelles URL sous 48 h, sinon soumettre à la main ;
- les articles qui remontent doivent être **enrichis** plutôt que multipliés — un
  article qui atteint la page 2 mérite 400 mots de plus, pas un article concurrent ;
- garder un œil sur les **liens internes** : chaque nouvel article doit être lié
  depuis au moins un ancien.
