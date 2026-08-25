# -*- coding: utf-8 -*-
"""Contenu des articles du blog Silver Palace — 52 articles, un par semaine.

Les articles sont répartis par saison pour rester lisibles :
    posts_automne.py    sept. - oct. 2026
    posts_hiver.py      oct. - déc. 2026
    posts_fetes.py      déc. 2026 - fév. 2027
    posts_printemps.py  fév. - avril 2027
    posts_ete1.py       avril - juin 2027
    posts_ete2.py       juin - juil. 2027

Chaque article vise un cluster de mots-clés distinct (voir CALENDRIER-BLOG.md).
La date fait office de programmation : seuls les articles dont la date est
atteinte sont publiés sur le site.

Pour ajouter un article : créer une entrée dans le fichier de la bonne saison,
puis lancer `python3 scripts/build_blog.py`.
"""

POSTS = [
{
    "slug": "organiser-evg-toulouse",
    "date": "2026-08-04",
    "category": "Guide",
    "reading": 7,
    "title": "Organiser un EVG à Toulouse : le guide complet",
    "meta_title": "Organiser un EVG à Toulouse — Le Guide Complet | Silver Palace",
    "description": "Où sortir, quoi prévoir, combien ça coûte : le guide pour organiser un enterrement de vie de garçon réussi à Toulouse, du dîner à la nuit en club.",
    "keywords": "EVG Toulouse, enterrement de vie de garçon Toulouse, organiser EVG Toulouse",
    "image": "/images/danseuse-show-bunny-silver-palace-toulouse.jpg",
    "image_alt": "Danseuse en tenue de show lors d'une soirée EVG au Silver Palace Toulouse",
    "excerpt": "Le témoin idéal ne laisse rien au hasard. Programme, budget, erreurs à éviter : tout ce qu'il faut savoir pour réussir un enterrement de vie de garçon dans la Ville rose.",
    "tags": ["EVG", "Toulouse", "Organisation"],
    "chapo": "Vous êtes témoin, et la mission est tombée : organiser l'EVG. À Toulouse, la matière ne manque pas — encore faut-il construire une soirée qui tienne debout jusqu'au bout de la nuit. Voici la méthode.",
    "body": """
<h2>Fixer le cadre avant de fixer le programme</h2>
<p>Avant même de réserver quoi que ce soit, trois questions décident de tout le reste : combien serez-vous, quel budget par personne, et surtout — qu'est-ce que le futur marié acceptera de vivre ? Un EVG raté est presque toujours un EVG conçu pour le groupe plutôt que pour lui.</p>
<p>Comptez une enveloppe de <strong>80 à 150 € par participant</strong> pour une soirée complète à Toulouse : activité en journée, restaurant, puis club. En dessous, il faudra choisir. Au-dessus, vous entrez dans le sur-mesure.</p>
<div class="callout">
  <p><strong>Le conseil du Silver :</strong> demandez discrètement à la future mariée où se situent les limites. Elle connaît les siennes et celles de son futur mari. C'est la conversation la moins glamour de l'organisation, et de loin la plus utile.</p>
</div>

<h2>Le déroulé d'une soirée qui fonctionne</h2>
<h3>16h — 19h : l'activité qui met en jambes</h3>
<p>Karting à Muret, accrobranche, escape game en centre-ville, ou simplement une terrasse au bord de la Garonne : l'objectif n'est pas la performance, c'est de créer le groupe. Les participants ne se connaissent pas tous — cette première séquence règle ce problème.</p>
<h3>20h — 22h : le dîner, pilier de la soirée</h3>
<p>Ne le sautez pas. Un EVG qui commence directement en bar finit rarement bien. Les quartiers Saint-Cyprien et Carmes regorgent de tables capables d'accueillir un groupe de dix à quinze personnes. Réservez en précisant l'occasion : la plupart des restaurants jouent le jeu.</p>
<h3>22h — 6h : la nuit</h3>
<p>C'est le moment que tout le monde attend, et celui où l'improvisation coûte cher. Un club de striptease comme le <a href="/">Silver Palace</a> reste le grand classique de l'EVG toulousain, à condition d'avoir réservé : arriver à quinze sans prévenir un vendredi soir, c'est prendre le risque de rester debout au bar toute la nuit.</p>

<h2>Ce qu'une formule EVG en club comprend vraiment</h2>
<p>Au Silver Palace, une soirée EVG se construit autour de trois éléments :</p>
<ul>
  <li><strong>Une table réservée</strong> pour le groupe, à l'écart mais avec vue sur la scène centrale ;</li>
  <li><strong>Une bouteille</strong> — champagne le plus souvent — servie à l'arrivée ;</li>
  <li><strong>Un show dédié</strong> au futur marié, avec deux danseuses, sur quatre titres.</li>
</ul>
<p>Le détail des formules figure sur notre <a href="/shows">carte des danses</a>. Comptez à partir de 400 € pour le groupe, ce qui, réparti sur douze personnes, reste très en dessous de ce que beaucoup imaginent.</p>

<h2>Les cinq erreurs qui gâchent un EVG</h2>
<ol>
  <li><strong>Ne pas réserver.</strong> Le vendredi et le samedi, les bonnes tables partent plusieurs jours à l'avance.</li>
  <li><strong>Commencer à boire trop tôt.</strong> Un futur marié hors service à 23h, c'est une soirée terminée avant d'avoir commencé — et un refus à l'entrée du club.</li>
  <li><strong>Négliger le code vestimentaire.</strong> La plupart des clubs privés toulousains exigent une tenue correcte. Prévenez le groupe la veille, pas sur le trottoir.</li>
  <li><strong>Surcharger le programme.</strong> Trois activités valent mieux que six survolées.</li>
  <li><strong>Oublier le retour.</strong> Désignez un capitaine de soirée sobre, ou réservez les VTC à l'avance.</li>
</ol>

<h2>Où dormir, comment rentrer</h2>
<p>Le quartier Matabiau concentre les hôtels abordables et se trouve à cinq minutes à pied de la rue de Stalingrad. Pour un groupe venu de l'extérieur, c'est le choix logique : vous rentrez à pied à 6h du matin plutôt que de chercher un taxi.</p>

<div class="callout">
  <p><strong>En résumé :</strong> une activité pour souder le groupe, un vrai dîner, une table réservée en club, et un retour organisé. Le reste — les gages, les déguisements, les surprises — n'est que du décor sur une structure qui doit tenir.</p>
</div>
""",
    "faq": [
        ("Combien coûte un EVG à Toulouse ?",
         "Comptez 80 à 150 € par personne pour une soirée complète incluant une activité, un dîner et une nuit en club. Une formule EVG en club de striptease démarre autour de 400 € pour l'ensemble du groupe, bouteille et show dédié compris."),
        ("Faut-il réserver pour un EVG en club à Toulouse ?",
         "Oui, c'est indispensable pour un groupe. Le vendredi et le samedi, les tables partent plusieurs jours à l'avance. La réservation garantit aussi que la formule EVG (table, bouteille, show dédié) sera préparée à votre arrivée."),
        ("Quel est le code vestimentaire pour un EVG en club privé ?",
         "Une tenue correcte et élégante est exigée dans la plupart des clubs privés toulousains, y compris au Silver Palace. Prévenez le groupe à l'avance : les déguisements complets sont généralement refusés à l'entrée."),
    ],
},
{
    "slug": "club-striptease-toulouse-premiere-visite",
    "date": "2026-08-11",
    "category": "Les codes",
    "reading": 6,
    "title": "Première visite en club de striptease à Toulouse : les codes à connaître",
    "meta_title": "Club de Striptease à Toulouse : les Codes d'une Première Visite | Silver Palace",
    "description": "Tarifs, pourboires, ce qui se fait et ce qui ne se fait pas : le guide honnête pour une première visite en club de striptease à Toulouse, sans fausse note.",
    "keywords": "club de striptease Toulouse, première visite club striptease, codes club striptease",
    "image": "/images/danseuse-lingerie-noire-pole-silver-palace-toulouse.jpg",
    "image_alt": "Danseuse en lingerie noire à la barre, ambiance d'un club de striptease à Toulouse",
    "excerpt": "Beaucoup n'osent pas pousser la porte, faute de savoir comment ça se passe. Voici, sans détour, ce qui vous attend derrière le rideau — et les quelques règles qui font la différence.",
    "tags": ["Codes", "Première visite", "Toulouse"],
    "chapo": "On imagine souvent le club de striptease à partir des films. La réalité est à la fois plus simple et plus codifiée. Petit manuel à l'usage de celles et ceux qui viennent pour la première fois.",
    "body": """
<h2>Ce qui vous attend en entrant</h2>
<p>Un club de striptease haut de gamme fonctionne comme un bar à ambiance, avec une scène en plus. Vous entrez, on vous accueille, on vous installe — au bar ou à une table selon l'affluence. Au Silver Palace, <strong>le premier verre vous est offert</strong> : c'est le moment d'observer, de vous acclimater, de laisser la soirée venir à vous.</p>
<p>Sur la scène centrale, les shows s'enchaînent toute la nuit. Ils sont compris dans l'entrée : personne ne vous demandera quoi que ce soit pour regarder. C'est la base de l'expérience, et elle est gratuite.</p>

<h2>Comprendre les tarifs sans mauvaise surprise</h2>
<p>La confusion la plus fréquente porte sur ce qui est payant et ce qui ne l'est pas. Le principe est simple :</p>
<ul>
  <li><strong>Les shows sur scène</strong> : compris, sans supplément ;</li>
  <li><strong>Les consommations</strong> : à la carte, de 10 € pour un soft à quelques centaines d'euros pour une grande bouteille de champagne ;</li>
  <li><strong>Les danses privées</strong> : à l'unité, à partir de 40 € pour une chanson, jusqu'aux formules en salon privé.</li>
</ul>
<p>Tout est affiché. Notre <a href="/shows">carte des danses</a> et notre <a href="/carte">carte des boissons</a> sont consultables en ligne avant même de venir — vous savez donc exactement où vous mettez les pieds.</p>
<div class="callout">
  <p><strong>Le réflexe utile :</strong> décidez de votre budget avant d'entrer, pas à trois heures du matin. C'est valable dans un club comme au casino.</p>
</div>

<h2>Les règles qui ne se négocient pas</h2>
<h3>On ne touche pas</h3>
<p>C'est la règle absolue, y compris pendant une danse privée. Les danseuses sont des professionnelles au travail, pas des hôtesses. Cette règle protège tout le monde et n'est jamais discutable — la sécurité veille, et une infraction se solde par une sortie immédiate.</p>
<h3>On ne photographie pas</h3>
<p>Les téléphones restent dans la poche. La discrétion est la contrepartie que le club offre à ses clients comme à ses artistes : personne ne veut se retrouver sur le réseau social de quelqu'un d'autre.</p>
<h3>On demande, on n'impose pas</h3>
<p>Une danseuse peut refuser une danse, et vous pouvez refuser une proposition. Un « non merci » poli est une réponse parfaitement normale, dans les deux sens.</p>

<h2>Le pourboire : combien, quand, comment</h2>
<p>Le pourboire n'est pas obligatoire en France, mais il fait partie de la culture du lieu. Après un show qui vous a plu, quelques euros glissés discrètement sont toujours appréciés. Après une danse privée, c'est un usage courant sans être une règle. Ni obligation, ni tarif caché : un geste, à votre appréciation.</p>

<h2>Venir seul, en couple, en groupe</h2>
<p>Les trois se pratiquent. Venir seul n'a rien d'étrange — c'est même fréquent en semaine, et l'ambiance de bar s'y prête. Les couples sont les bienvenus et représentent une part croissante de la clientèle. Quant aux groupes, ils tirent le meilleur de la soirée en réservant à l'avance, notamment pour les <a href="/events">EVG et anniversaires</a>.</p>

<h2>Tenue et âge : les deux conditions d'entrée</h2>
<p>L'entrée est réservée aux <strong>personnes majeures</strong>, pièce d'identité à l'appui si besoin. Une tenue correcte et élégante est exigée : chemise ou pull soigné, chaussures propres. Ce n'est pas de la coquetterie, c'est ce qui distingue un club privé haut de gamme d'une boîte de nuit ordinaire.</p>
""",
    "faq": [
        ("Combien coûte une entrée en club de striptease à Toulouse ?",
         "Au Silver Palace, les shows sur scène sont compris et le premier verre est offert. Vous ne payez que vos consommations, à partir de 10 €, et éventuellement les danses privées, à partir de 40 € la chanson."),
        ("Peut-on venir seul dans un club de striptease ?",
         "Oui, c'est très courant, en particulier en semaine. L'ambiance de bar s'y prête et le personnel est habitué à accueillir des clients seuls."),
        ("Les couples sont-ils acceptés au Silver Palace ?",
         "Oui. Les couples sont les bienvenus et représentent une part croissante de la clientèle du club."),
    ],
},
{
    "slug": "que-faire-toulouse-apres-minuit",
    "date": "2026-08-18",
    "category": "Ville rose",
    "reading": 6,
    "title": "Que faire à Toulouse après minuit ? Le guide des noctambules",
    "meta_title": "Que Faire à Toulouse Après Minuit ? Guide de la Nuit | Silver Palace",
    "description": "Bars à cocktails, clubs, cabaret, restauration nocturne : le guide honnête de la nuit toulousaine quand les terrasses ferment et que la soirée commence vraiment.",
    "keywords": "sortir à Toulouse le soir, que faire à Toulouse la nuit, nuit toulousaine",
    "image": "/images/facade-silver-palace-club-striptease-toulouse.jpg",
    "image_alt": "Façade illuminée d'un club de nuit rue de Stalingrad à Toulouse",
    "excerpt": "À Toulouse, la vraie soirée démarre quand les terrasses se vident. Panorama des quartiers, des adresses et des rythmes de la nuit dans la Ville rose.",
    "tags": ["Toulouse", "Nightlife", "Guide"],
    "chapo": "Toulouse a cette particularité : elle se couche tard et se raconte en quartiers. Selon l'heure et l'envie, la ville change complètement de visage. Voici comment naviguer la nuit toulousaine.",
    "body": """
<h2>22h — minuit : les quartiers qui s'animent</h2>
<h3>Saint-Pierre, l'incontournable</h3>
<p>La place Saint-Pierre reste le point de départ classique. Étudiante, dense, bruyante : on y vient pour le nombre, pas pour la finesse. C'est parfait pour lancer une soirée en groupe, moins pour une conversation.</p>
<h3>Les Carmes et Saint-Étienne, la version posée</h3>
<p>Quelques rues plus loin, l'ambiance change du tout au tout. Bars à vins, cocktails travaillés, salles plus petites : c'est le Toulouse des soirées qui s'écoutent. Idéal avant de basculer vers la nuit.</p>
<h3>Saint-Cyprien, la rive gauche</h3>
<p>De l'autre côté de la Garonne, le quartier a gagné en réputation ces dernières années. Bonnes tables, bars indépendants, moins de foule qu'en centre-ville.</p>

<h2>Minuit — 3h : le cœur de la nuit</h2>
<p>C'est l'heure où la ville se scinde en deux. D'un côté les clubs et discothèques, de l'autre les lieux plus feutrés — bars à cocktails tardifs, clubs privés, cabaret.</p>
<p>Le <a href="/">Silver Palace</a> ouvre justement à 22h et bat son plein à partir de minuit. Rue de Stalingrad, à cinq minutes de la gare Matabiau, il propose une alternative aux boîtes classiques : <a href="/shows">shows de cabaret et de striptease</a> sur scène centrale, bar à champagne, salons privés. Une soirée qui se regarde autant qu'elle se vit.</p>
<div class="callout">
  <p><strong>Bon à savoir :</strong> à Toulouse, la plupart des clubs ne se remplissent pas avant 1h du matin. Arriver à 23h30, c'est souvent avoir la piste pour soi — ce qui, selon l'humeur, est un défaut ou un luxe.</p>
</div>

<h2>3h — 6h : ceux qui tiennent</h2>
<p>Passé trois heures, l'offre se réduit nettement. Quelques clubs tiennent jusqu'à l'aube, dont le Silver Palace qui ferme à 6h du mardi au samedi. C'est le moment des conversations qui s'étirent et des soirées qui basculent en souvenirs.</p>

<h2>Manger la nuit à Toulouse</h2>
<p>Le classique reste le kebab de Saint-Pierre ou d'Esquirol, ouvert tard. Pour mieux, quelques brasseries autour de Jeanne-d'Arc servent au-delà de minuit. Et pour la faim de 5h, les boulangeries de nuit du côté des Minimes ont sauvé plus d'une fin de soirée.</p>

<h2>Se déplacer et rentrer</h2>
<ul>
  <li><strong>Métro :</strong> jusqu'à minuit en semaine, 3h le vendredi et le samedi ;</li>
  <li><strong>Bus de nuit :</strong> le réseau Noctambus couvre les grands axes ;</li>
  <li><strong>VTC et taxis :</strong> comptez large entre 2h et 4h, c'est le pic de demande ;</li>
  <li><strong>À pied :</strong> le centre de Toulouse est compact — l'option la plus sous-estimée.</li>
</ul>

<h2>Le calendrier de la nuit toulousaine</h2>
<p>Le jeudi est le soir des étudiants, le vendredi celui des groupes, le samedi celui de tout le monde. Le mardi et le mercredi, la ville est plus calme : c'est paradoxalement le meilleur moment pour découvrir un lieu, quand le personnel a le temps de vous accueillir vraiment.</p>
""",
    "faq": [
        ("Jusqu'à quelle heure sort-on à Toulouse ?",
         "Les bars ferment généralement vers 2h, les clubs entre 5h et 6h du matin. Le Silver Palace est ouvert de 22h à 6h, du mardi au samedi."),
        ("Quel est le meilleur quartier pour sortir le soir à Toulouse ?",
         "Saint-Pierre pour l'ambiance étudiante et festive, les Carmes et Saint-Étienne pour les bars à cocktails plus posés, Saint-Cyprien pour la rive gauche. Le quartier Matabiau concentre les clubs de nuit."),
        ("Le métro fonctionne-t-il la nuit à Toulouse ?",
         "Le métro circule jusqu'à minuit en semaine et jusqu'à 3h le vendredi et le samedi. Au-delà, comptez sur les bus Noctambus, les VTC ou la marche : le centre-ville est compact."),
    ],
},
{
    "slug": "devenir-danseuse-cabaret-realite",
    "date": "2026-08-25",
    "category": "Coulisses",
    "reading": 7,
    "title": "Devenir danseuse en cabaret : ce qu'il faut vraiment savoir",
    "meta_title": "Devenir Danseuse en Cabaret à Toulouse : le Vrai Métier | Silver Palace",
    "description": "Rémunération, horaires, sécurité, débuts : ce que personne ne dit sur le métier de danseuse en club et cabaret à Toulouse. Un état des lieux sans fantasme.",
    "keywords": "devenir danseuse Toulouse, travail danseuse cabaret, métier danseuse club",
    "image": "/images/danseuse-resille-pole-silver-palace-toulouse.jpg",
    "image_alt": "Danseuse professionnelle à la barre de pole dance dans un cabaret à Toulouse",
    "excerpt": "Entre les clichés et la réalité, il y a un métier — avec ses exigences, ses horaires, ses avantages réels. Parole de club, sans enjolivure.",
    "tags": ["Métier", "Coulisses", "Recrutement"],
    "chapo": "Chaque semaine, des candidatures arrivent au club. Et chaque semaine, les mêmes questions reviennent : est-ce que c'est bien payé, est-ce que c'est sûr, est-ce qu'il faut savoir danser. Réponses honnêtes.",
    "body": """
<h2>Faut-il savoir danser ?</h2>
<p>Non — et c'est la réponse qui surprend le plus. La majorité des danseuses qui débutent au Silver Palace n'ont aucune formation. Ce qui compte réellement, c'est l'aisance : savoir occuper une scène, soutenir un regard, tenir une conversation au bar. Le reste s'apprend, souvent en quelques semaines, auprès des danseuses confirmées.</p>
<p>La pole dance, elle, est une compétence à part. Elle se travaille, elle impressionne, et elle ouvre des possibilités — mais elle n'est absolument pas un prérequis à l'embauche.</p>

<h2>Combien gagne-t-on vraiment ?</h2>
<p>C'est la question centrale, et celle sur laquelle circulent le plus de bêtises. La rémunération repose sur plusieurs sources : les shows sur scène, les <a href="/shows">danses privées</a>, les soirées événement. Elle varie donc selon les nuits, l'affluence et l'implication.</p>
<p>Un club sérieux vous présente cette structure <strong>en détail et par écrit lors de l'entretien</strong>. Si un établissement reste vague sur ce point ou promet des sommes mirobolantes sans les expliquer, c'est le signal d'alarme le plus fiable qui soit.</p>
<div class="callout">
  <p><strong>À vérifier avant de signer où que ce soit :</strong> comment la rémunération est-elle calculée ? Y a-t-il des frais à votre charge ? Sous quel statut travaillez-vous ? Un club qui esquive ces trois questions n'est pas un club où travailler.</p>
</div>

<h2>Les horaires : l'aspect le plus sous-estimé</h2>
<p>Travailler de 22h à 6h transforme votre vie. Le corps s'adapte — en général en deux à trois semaines — mais la vie sociale, elle, se réorganise durablement : vos amis dorment quand vous travaillez, et l'inverse.</p>
<p>La contrepartie est réelle : la flexibilité. Au Silver Palace, chaque danseuse choisit ses soirs. Beaucoup travaillent deux ou trois nuits par semaine en parallèle d'études ou d'une autre activité. C'est précisément ce qui rend le métier compatible avec un projet personnel.</p>

<h2>La sécurité : ce que doit garantir un club</h2>
<p>C'est le critère qui devrait primer sur tous les autres. Un établissement sérieux met en place :</p>
<ul>
  <li><strong>Une équipe de sécurité présente en salle</strong> chaque nuit d'ouverture, pas seulement à l'entrée ;</li>
  <li><strong>Une règle de non-contact</strong> appliquée sans exception, y compris en salon privé ;</li>
  <li><strong>Un droit de refus</strong> absolu : vous pouvez refuser un client, une danse, une table, sans avoir à vous justifier ;</li>
  <li><strong>Des espaces réservés au personnel</strong>, loges fermées comprises.</li>
</ul>
<p>Ces quatre points ne sont pas des arguments commerciaux, ce sont des minimums. Un club qui n'en coche pas quatre sur quatre est à éviter.</p>

<h2>Les premières semaines</h2>
<p>Le premier soir intimide tout le monde, sans exception. Au Silver Palace, une nouvelle danseuse est accompagnée par une danseuse expérimentée : elle observe, elle monte sur scène quand elle se sent prête, elle apprend le rythme de la salle. Personne n'est jeté dans le grand bain.</p>
<p>La progression tient à trois choses : la régularité, la capacité à créer du lien avec les clients, et la confiance — qui vient plus vite qu'on ne l'imagine.</p>

<h2>Comment postuler</h2>
<p>Le club recrute en continu. La démarche est volontairement simple et confidentielle : un <a href="/application">formulaire de candidature</a>, un échange téléphonique discret, une rencontre au club en journée, puis un essai sans engagement. Vos coordonnées ne servent qu'à vous recontacter.</p>
<p>Une seule condition non négociable : être majeure.</p>
""",
    "faq": [
        ("Faut-il de l'expérience pour devenir danseuse en club ?",
         "Non. La majorité des danseuses qui débutent au Silver Palace n'ont aucune formation en danse. L'aisance en public et l'attitude comptent davantage, et les danseuses confirmées accompagnent les débutantes lors de leurs premiers soirs."),
        ("Comment est rémunérée une danseuse en cabaret ?",
         "La rémunération combine plusieurs sources : shows sur scène, danses privées et soirées événement. Un club sérieux détaille cette structure par écrit lors de l'entretien. Méfiez-vous des établissements qui restent vagues sur ce point."),
        ("Le métier de danseuse est-il compatible avec des études ?",
         "Oui, c'est même fréquent. Au Silver Palace, chaque danseuse choisit ses soirs et beaucoup travaillent deux à trois nuits par semaine en parallèle d'études ou d'une autre activité."),
    ],
},
]

# --- Agrégation des articles programmés -------------------------------------
from posts_automne import POSTS_AUTOMNE
from posts_hiver import POSTS_HIVER
from posts_fetes import POSTS_FETES
from posts_printemps import POSTS_PRINTEMPS
from posts_ete1 import POSTS_ETE1
from posts_ete2 import POSTS_ETE2

POSTS = (POSTS + POSTS_AUTOMNE + POSTS_HIVER + POSTS_FETES
         + POSTS_PRINTEMPS + POSTS_ETE1 + POSTS_ETE2)
