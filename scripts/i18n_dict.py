# -*- coding: utf-8 -*-
"""Génère la version anglaise du site Silver Palace sous /en/."""
import os, re, glob

SITE = "/Users/matteo/Desktop/BUSINESS/PMC MARKETING/clients/silver-palace/site"
OUT = os.path.join(SITE, "en")

# slug FR -> slug EN
SLUGS = {
    "index": "index",
    "reservation": "booking",
    "application": "apply",
    "events": "events",
    "carte": "drinks",
    "shows": "dances",
    "contact": "contact",
    "about": "about",
    "legal": "legal",
    "privacy": "privacy",
    "404": "404",
}

# ---------------------------------------------------------------- TRADUCTIONS
T = {
# ---- Meta / titles
"Silver Palace — Club de Striptease &amp; Cabaret à Toulouse | Gentlemen's Club":
    "Silver Palace — Strip Club &amp; Cabaret in Toulouse | Gentlemen's Club",
"Le Silver Palace, club de striptease et cabaret de nuit à Toulouse. Danseuses d'exception, shows sensuels, champagne et ambiance feutrée au cœur de la Ville rose. Ouvert du mardi au samedi, 22h–6h. Réservez votre table.":
    "Silver Palace is Toulouse's premier strip club and late-night cabaret. Exceptional dancers, sensual shows, champagne and a hushed atmosphere in the heart of the Pink City. Open Tuesday to Saturday, 10pm–6am. Book your table.",
"Silver Palace — Club de Striptease &amp; Cabaret à Toulouse":
    "Silver Palace — Strip Club &amp; Cabaret in Toulouse",
"Danseuses d'exception, shows sensuels et champagne dans le club de nuit le plus envoûtant de Toulouse. Ouvert du mardi au samedi, 22h–6h.":
    "Exceptional dancers, sensual shows and champagne in the most bewitching night club in Toulouse. Open Tuesday to Saturday, 10pm–6am.",
"Le club de nuit le plus envoûtant de la Ville rose. Shows, danseuses, champagne. Mardi–samedi, 22h–6h.":
    "The most bewitching night club in the Pink City. Shows, dancers, champagne. Tuesday–Saturday, 10pm–6am.",
"Réserver une Table — Silver Palace, Club de Striptease à Toulouse":
    "Book a Table — Silver Palace, Strip Club in Toulouse",
"Réservez votre table au Silver Palace, club de striptease et cabaret à Toulouse. Soirée classique, EVG, EVJF, anniversaire : réponse rapide, réservation conseillée le week-end.":
    "Book your table at Silver Palace, strip club and cabaret in Toulouse. Regular night out, stag party, hen party or birthday: fast reply, booking recommended at weekends.",
"Devenir Danseuse à Toulouse — Recrutement | Silver Palace":
    "Dancer Jobs in Toulouse — Now Hiring | Silver Palace",
"Le Silver Palace recrute des danseuses à Toulouse. Cadre professionnel et sécurisé, plannings flexibles, débutantes acceptées. Postulez en 2 minutes, échange confidentiel garanti.":
    "Silver Palace is hiring dancers in Toulouse. Professional, secure setting, flexible schedules, beginners welcome. Apply in 2 minutes — every conversation stays confidential.",
"Événements &amp; Soirées à Thème — Silver Palace Toulouse":
    "Events &amp; Theme Nights — Silver Palace Toulouse",
"Soirées à thème, EVG, EVJF, anniversaires et privatisations au Silver Palace, club de striptease et cabaret à Toulouse. Le programme des nuits de la Ville rose.":
    "Theme nights, stag and hen parties, birthdays and private hire at Silver Palace, strip club and cabaret in Toulouse. What's on in the Pink City after dark.",
"Carte des Boissons &amp; Champagnes — Silver Palace Toulouse":
    "Drinks &amp; Champagne Menu — Silver Palace Toulouse",
"Champagnes de grandes maisons, cocktails signature et spiritueux d'exception au Silver Palace Toulouse. Le premier verre vous est offert à l'entrée du club.":
    "Champagnes from the great houses and exceptional spirits at Silver Palace Toulouse. Your first drink is on us when you walk through the door.",
"Table Dance &amp; Danses Privées — Silver Palace Toulouse":
    "Table Dance &amp; Private Dances — Silver Palace Toulouse",
"Table dance, danses privées et salons VIP au Silver Palace, club de striptease à Toulouse. Shows sur scène en continu chaque soir d'ouverture.":
    "Table dance, private dances and VIP rooms at Silver Palace, strip club in Toulouse. Non-stop stage shows every night we open.",
"Contact — Silver Palace, Club de Striptease à Toulouse":
    "Contact — Silver Palace, Strip Club in Toulouse",
"Contactez le Silver Palace : 05 62 84 51 69, 31 Rue de Stalingrad à Toulouse. Réservations, événements privés, presse et partenariats.":
    "Get in touch with Silver Palace: +33 5 62 84 51 69, 31 Rue de Stalingrad, Toulouse. Bookings, private events, press and partnerships.",
"À Propos du Club — Silver Palace, Cabaret à Toulouse":
    "About the Club — Silver Palace, Cabaret in Toulouse",
"L'histoire et l'esprit du Silver Palace : un club de striptease et cabaret haut de gamme au cœur de Toulouse, où sensualité, élégance et discrétion se rencontrent.":
    "The story and spirit of Silver Palace: an upmarket strip club and cabaret in the heart of Toulouse, where sensuality, elegance and discretion meet.",
"Mentions Légales — Silver Palace Toulouse": "Legal Notice — Silver Palace Toulouse",
"Mentions légales du site silver-palace.com, club Silver Palace à Toulouse.":
    "Legal notice for silver-palace.com, Silver Palace club in Toulouse.",
"Politique de Confidentialité — Silver Palace Toulouse": "Privacy Policy — Silver Palace Toulouse",
"Politique de confidentialité du site silver-palace.com : données collectées, finalités, durées de conservation et droits RGPD.":
    "Privacy policy for silver-palace.com: data collected, purposes, retention periods and your GDPR rights.",
"Page Introuvable — Silver Palace Toulouse": "Page Not Found — Silver Palace Toulouse",
"Cette page n'existe pas ou plus. Retrouvez le Silver Palace, club de striptease et cabaret à Toulouse, depuis la page d'accueil.":
    "This page doesn't exist any more. Find Silver Palace, strip club and cabaret in Toulouse, from the home page.",

# ---- JSON-LD
"Club de striptease et cabaret de nuit haut de gamme à Toulouse. Danseuses professionnelles, shows sensuels, table dance, bar à champagne et ambiance feutrée. Réservé aux adultes.":
    "Upmarket strip club and late-night cabaret in Toulouse. Professional dancers, sensual shows, table dance, champagne bar and a hushed atmosphere. Adults only.",
"Vivez la nuit. Touchez le rêve.": "Live the night. Touch the dream.",
"club striptease Toulouse, cabaret Toulouse, gentlemen's club Toulouse, table dance, club de nuit Toulouse, spectacle sensuel":
    "strip club Toulouse, cabaret Toulouse, gentlemen's club Toulouse, table dance, night club Toulouse, sensual show",
"Bar à champagne": "Champagne bar",
"Salons privés": "Private rooms",

# ---- FAQ (JSON-LD + visible)
"Où se trouve le Silver Palace, club de striptease à Toulouse ?":
    "Where is Silver Palace, the strip club in Toulouse?",
"Le Silver Palace est situé au 31 Rue de Stalingrad, 31000 Toulouse, à quelques minutes à pied de la gare Toulouse-Matabiau et du centre-ville. Le club est facilement accessible en métro, en taxi ou en VTC.":
    "Silver Palace is at 31 Rue de Stalingrad, 31000 Toulouse, a few minutes' walk from Toulouse-Matabiau station and the city centre. The club is easy to reach by metro, taxi or ride-hailing.",
"Quels sont les horaires d'ouverture du Silver Palace ?": "What are Silver Palace's opening hours?",
"Le club est ouvert du mardi au samedi, de 22h à 6h du matin. Il est fermé le dimanche et le lundi. Les soirées les plus animées commencent généralement à partir de minuit.":
    "The club is open Tuesday to Saturday, from 10pm to 6am. It is closed on Sunday and Monday. The liveliest nights usually get going from midnight.",
"Faut-il réserver pour venir au Silver Palace ?": "Do I need to book to come to Silver Palace?",
"La réservation n'est pas obligatoire, mais elle est fortement recommandée pour garantir votre table, notamment le week-end et pour les événements privés (anniversaires, enterrements de vie de garçon ou de jeune fille). Vous pouvez réserver en ligne ou par téléphone au 05 62 84 51 69.":
    "Booking is not compulsory, but it is strongly recommended to secure your table, especially at weekends and for private events (birthdays, stag and hen parties). You can book online or by phone on +33 5 62 84 51 69.",
"Que propose le Silver Palace : striptease, cabaret, table dance ?":
    "What does Silver Palace offer: striptease, cabaret, table dance?",
"Le Silver Palace propose des shows de striptease et des spectacles inspirés de l'univers du cabaret, réalisés par des danseuses professionnelles, ainsi que des danses privées (table dance) et un bar avec une carte de champagnes et cocktails. Chaque soirée mêle spectacle, élégance et sensualité.":
    "Silver Palace offers striptease shows and cabaret-inspired performances by professional dancers, along with private dances (table dance) and a bar with a champagne and cocktail menu. Every night blends spectacle, elegance and sensuality.",
"Peut-on privatiser le club pour un événement (EVG, EVJF, anniversaire) ?":
    "Can the club be hired privately for an event (stag do, hen party, birthday)?",
"Oui. Le Silver Palace accueille les enterrements de vie de garçon et de jeune fille, anniversaires et événements d'entreprise. Des formules avec table réservée, champagne et show dédié sont disponibles sur demande.":
    "Yes. Silver Palace hosts stag and hen parties, birthdays and corporate events. Packages with a reserved table, champagne and a dedicated show are available on request.",
"Quel est le code vestimentaire et l'âge minimum pour entrer ?":
    "What is the dress code and the minimum age?",
"L'entrée est réservée aux personnes majeures (18 ans et plus). Une tenue correcte et élégante est exigée : le Silver Palace est un club privé haut de gamme où le raffinement fait partie de l'expérience.":
    "Entry is for adults only (18 and over). Smart, elegant dress is required: Silver Palace is an upmarket private club where refinement is part of the experience.",
"Quels sont les horaires d'ouverture&nbsp;?": "What are the opening hours?",
"Faut-il réserver pour venir&nbsp;?": "Do I need to book?",
"La réservation n'est pas obligatoire, mais fortement recommandée pour garantir votre table, notamment le week-end et pour les événements privés. Vous pouvez réserver en ligne ou par téléphone au":
    "Booking is not compulsory, but strongly recommended to secure your table, especially at weekends and for private events. You can book online or by phone on",
"Que propose le club : striptease, cabaret, table dance&nbsp;?":
    "What does the club offer: striptease, cabaret, table dance?",
"Le Silver Palace propose des shows de striptease et des spectacles inspirés de l'univers du cabaret, réalisés par des danseuses professionnelles, ainsi que des danses privées (table dance) et un bar avec une carte de champagnes et cocktails.":
    "Silver Palace offers striptease shows and cabaret-inspired performances by professional dancers, along with private dances (table dance) and a bar with a champagne and cocktail menu.",
"Peut-on privatiser le club pour un EVG, un EVJF ou un anniversaire&nbsp;?":
    "Can the club be hired privately for a stag do, hen party or birthday?",
"Oui. Le Silver Palace accueille les enterrements de vie de garçon et de jeune fille, anniversaires et événements d'entreprise. Des formules avec table réservée, champagne et show dédié sont disponibles sur demande.":
    "Yes. Silver Palace hosts stag and hen parties, birthdays and corporate events. Packages with a reserved table, champagne and a dedicated show are available on request.",
"Quel est le code vestimentaire et l'âge minimum&nbsp;?": "What is the dress code and minimum age?",
"Où se trouve le Silver Palace, club de striptease à Toulouse&nbsp;?":
    "Where is Silver Palace, the strip club in Toulouse?",
"Tout savoir avant de <span class=\"accent-italic\">pousser la porte</span>":
    "Everything to know before <span class=\"accent-italic\">you walk in</span>",
"Questions fréquentes": "Frequently asked questions",

# ---- Navigation / header / footer
"Danser&nbsp;au&nbsp;Silver": "Dance&nbsp;at&nbsp;the&nbsp;Silver",
"Danser au Silver": "Dance at the Silver",
"Devenir danseuse au Silver Palace — candidature": "Become a dancer at Silver Palace — apply",
"Réserver une table": "Book a table",
"Navigation principale": "Main navigation",
"Navigation mobile": "Mobile navigation",
"Ouvrir le menu": "Open menu",
"Fermer le menu": "Close menu",
"Fermer l'aperçu": "Close preview",
"Fil d'ariane": "Breadcrumb",
"Pied de page — Informations": "Footer — Information",
"Pied de page — Le club": "Footer — The club",
"Silver Palace — Accueil": "Silver Palace — Home",
"Carte des boissons": "Drinks menu",
"Carte des danses": "Dance menu",
"Mentions légales": "Legal notice",
"Confidentialité": "Privacy",
"Candidature": "Apply",
"Réservation": "Booking",
"Événements": "Events",
"Informations": "Information",
"À propos": "About",
"Accueil": "Home",
"La Carte": "Drinks",
"Les Danses": "Dances",
"Le Club": "The Club",
"Réserver": "Book",

# ---- Home : héro
"Gentlemen's&nbsp;Club&nbsp;·&nbsp;Toulouse": "Gentlemen's&nbsp;Club&nbsp;·&nbsp;Toulouse",
"Club de striptease <em>&amp;</em> cabaret à Toulouse": "Strip club <em>&amp;</em> cabaret in Toulouse",
"Réserver votre table": "Book your table",
"Découvrir le club": "Discover the club",
"Entrer": "Enter",
"Faire défiler vers la section Le Club": "Scroll to The Club section",
"Silver Palace, club de striptease et cabaret à Toulouse":
    "Silver Palace, strip club and cabaret in Toulouse",
"Silver Palace — club de striptease et cabaret à Toulouse":
    "Silver Palace — strip club and cabaret in Toulouse",

# ---- Home : promesse
"L'état d'esprit du Silver Palace": "The Silver Palace state of mind",
"L'état d'esprit": "State of mind",
"Sensualité": "Sensuality",
"Élégance": "Elegance",
"Discrétion": "Discretion",

# ---- Home : le club
"Le club privé le plus <span class=\"accent-italic\">envoûtant</span> de la Ville&nbsp;rose":
    "The most <span class=\"accent-italic\">bewitching</span> private club in the Pink&nbsp;City",
"Plongez dans un décor somptueux où chaque détail est pensé pour éveiller vos sens. Une ambiance sensuelle et feutrée, des lumières qui caressent les courbes, un service exclusif qui vous place au centre de la nuit.":
    "Step into sumptuous surroundings where every detail is designed to awaken your senses. A sensual, hushed atmosphere, lights that trace every curve, and exclusive service that puts you at the centre of the night.",
"Le Silver Palace n'est pas seulement un club de striptease à Toulouse : c'est une expérience où luxe, tentation et sophistication se rencontrent. Un verre offert au bar devient le prélude d'une soirée d'exception, dans un cadre aux codes discrets réservé aux connaisseurs.":
    "Silver Palace is more than a strip club in Toulouse: it is an experience where luxury, temptation and sophistication meet. A drink on the house at the bar becomes the prelude to an exceptional evening, in a discreet setting reserved for those in the know.",
"Danseuse dans un fauteuil baroque argenté, l'écrin feutré du Silver Palace, club privé à Toulouse":
    "Dancer in a silver baroque armchair, the hushed setting of Silver Palace, private club in Toulouse",
"Le Silver": "The Silver",
"Mardi — Samedi": "Tuesday — Saturday",
"Privé &amp; discret": "Private &amp; discreet",
"Cœur de Toulouse": "Heart of Toulouse",
"Nuits par semaine": "Nights a week",

# ---- Home : l'expérience
"Trois façons de <span class=\"accent-italic\">toucher le rêve</span>":
    "Three ways to <span class=\"accent-italic\">touch the dream</span>",
"L'Expérience": "The Experience",
"Shows &amp; Table Dance": "Shows &amp; Table Dance",
"Des danseuses d'exception, des shows sensuels et des danses privées dans l'intimité de nos salons. L'art du striptease élevé au rang de spectacle.":
    "Exceptional dancers, sensual shows and private dances in the intimacy of our rooms. The art of striptease raised to true spectacle.",
"Bar &amp; Champagne": "Bar &amp; Champagne",
"Champagnes de grandes maisons et spiritueux d'exception, servis dans une lumière tamisée. Le premier verre vous est offert.":
    "Champagnes from the great houses and exceptional spirits, served in soft, low light. Your first drink is on us.",
"Événements Privés": "Private Events",
"EVG, EVJF, anniversaires : privatisez une table ou un salon pour une nuit inoubliable, avec show dédié et service sur mesure.":
    "Stag dos, hen parties, birthdays: book a table or a private room for an unforgettable night, with a dedicated show and tailor-made service.",
"Organiser ma soirée": "Plan my night",

# ---- Home : le spectacle
"Un cabaret <span class=\"accent-italic\">contemporain</span> au cœur de Toulouse":
    "A <span class=\"accent-italic\">contemporary</span> cabaret in the heart of Toulouse",
"Le Spectacle": "The Show",
"Héritier de l'esprit des grands cabarets parisiens, le Silver Palace réinvente la revue à la toulousaine : plumes, paillettes, jeux de lumière et chorégraphies millimétrées.":
    "Heir to the spirit of the great Parisian cabarets, Silver Palace reinvents the revue Toulouse-style: feathers, sequins, dramatic lighting and razor-sharp choreography.",
"Chaque semaine, nos danseuses montent sur scène pour des spectacles de cabaret où la sensualité rencontre l'élégance. Un show à Toulouse qui ne ressemble à aucun autre — entre tradition du music-hall et énergie de la nuit.":
    "Every week, our dancers take to the stage for cabaret performances where sensuality meets elegance. A show in Toulouse like no other — part music-hall tradition, part pure night-time energy.",
"Shows chorégraphiés chaque soir d'ouverture": "Choreographed shows every night we open",
"Soirées à thème &amp; événements exclusifs": "Theme nights &amp; exclusive events",
"Scène centrale &amp; salons privés": "Central stage &amp; private rooms",
"Voir les événements": "See what's on",
"Depuis&nbsp;·&nbsp;Toulouse": "Since&nbsp;·&nbsp;Toulouse",
"Danseuse à la barre de pole dance sous les néons violets, spectacle du Silver Palace Toulouse":
    "Dancer on the pole under purple neon, Silver Palace Toulouse show",
"Séquence animée : danseuse du Silver Palace dans les néons violets du club":
    "Animated sequence: Silver Palace dancer in the club's purple neon",

# ---- Home : galerie
"Des artistes qui <span class=\"accent-italic\">hypnotisent</span>":
    "Artists who <span class=\"accent-italic\">hypnotise</span>",
"Les Danseuses": "The Dancers",
"Sur scène comme dans les salons, nos danseuses font de chaque nuit un spectacle : pole dance, shows chorégraphiés et danses privées, dans la lumière rouge et or du club.":
    "On stage and in the private rooms alike, our dancers turn every night into a show: pole dance, choreographed sets and private dances, in the club's red and gold light.",
"Danseuse en lingerie noire au pied de la barre de pole dance, Silver Palace, club de striptease à Toulouse":
    "Dancer in black lingerie at the foot of the pole, Silver Palace, strip club in Toulouse",
"Danseuse en lingerie violette allongée sous les néons du Silver Palace Toulouse":
    "Dancer in purple lingerie lying under the neon at Silver Palace Toulouse",
"Danseuse en tenue de show à la barre lors d'une soirée à thème du Silver Palace Toulouse":
    "Dancer in show costume at the pole during a Silver Palace Toulouse theme night",
"Danseuse en satin rouge parmi les pétales de rose dans un salon privé du Silver Palace":
    "Dancer in red satin among rose petals in a Silver Palace private room",
"Danseuse enlacée à la barre de pole dance dans la lumière rouge du Silver Palace Toulouse":
    "Dancer wrapped around the pole in the red light of Silver Palace Toulouse",
"Danseuse posant sur la scène du Silver Palace, cabaret et club de nuit à Toulouse":
    "Dancer posing on the Silver Palace stage, cabaret and night club in Toulouse",
"Sur scène": "On stage",
"Sous les néons": "Under the neon",
"Soirées à thème": "Theme nights",
"Les salons privés": "Private rooms",
"Pole dance": "Pole dance",
"La scène": "The stage",

# ---- Home : carrousel danseuses
"Les visages de la <span class=\"accent-italic\">nuit</span>":
    "The faces of the <span class=\"accent-italic\">night</span>",
"Rencontrez-les": "Meet them",
"Eva, danseuse du Silver Palace, club de striptease à Toulouse":
    "Eva, dancer at Silver Palace, strip club in Toulouse",
"Ruby, danseuse des soirées à thème du Silver Palace Toulouse":
    "Ruby, theme-night dancer at Silver Palace Toulouse",
"Scarlett, danseuse dans les salons privés du Silver Palace":
    "Scarlett, private-room dancer at Silver Palace",
"Nova, danseuse de pole dance au Silver Palace Toulouse":
    "Nova, pole dancer at Silver Palace Toulouse",
"Jade, danseuse et chorégraphe des shows du Silver Palace":
    "Jade, dancer and choreographer at Silver Palace",
"Danseuse précédente": "Previous dancer",
"Danseuse suivante": "Next dancer",
"Table dance &amp; shows privés": "Table dance &amp; private shows",

# ---- Home : CTA / aperçu
"Réservez votre <span class=\"accent-italic\">nuit inoubliable</span>":
    "Book your <span class=\"accent-italic\">unforgettable night</span>",
"La nuit vous attend": "The night is waiting",
"Réserver maintenant": "Book now",
"ou appelez le": "or call",
"Prenez le contrôle de la <span class=\"accent-italic\">danse</span>":
    "Take control of the <span class=\"accent-italic\">dance</span>",
"Aperçu exclusif": "Exclusive preview",
"Cliquez pour un aperçu": "Click for a preview",
"Scrollez — elle danse à votre rythme": "Scroll — she dances to your rhythm",
"Danseuse du Silver Palace à la barre de pole dance — aperçu interactif du club à Toulouse":
    "Silver Palace dancer on the pole — interactive preview of the club in Toulouse",
"Façade illuminée du Silver Palace, rue de Stalingrad à Toulouse":
    "Illuminated Silver Palace frontage, Rue de Stalingrad in Toulouse",

# ---- Home : infos
"Nous <span class=\"accent-italic\">trouver</span>": "Find <span class=\"accent-italic\">us</span>",
"Infos&nbsp;&amp;&nbsp;Accès": "Info&nbsp;&amp;&nbsp;Access",
"Infos &amp; Accès": "Info &amp; Access",
"À 5 min à pied de la gare Matabiau": "5 min walk from Matabiau station",
"Métro, taxi &amp; VTC à proximité": "Metro, taxi &amp; ride-hailing nearby",
"Itinéraire": "Directions",
"Horaires d'ouverture": "Opening hours",
"Adresse": "Address",
"Horaires": "Opening hours",
"Nous écrire": "Email us",
"Instagram du Silver Palace": "Silver Palace on Instagram",
"Facebook du Silver Palace": "Silver Palace on Facebook",
"Plan d'accès au Silver Palace, 31 Rue de Stalingrad, 31000 Toulouse":
    "Map to Silver Palace, 31 Rue de Stalingrad, 31000 Toulouse",
"31 Rue de Stalingrad — Toulouse": "31 Rue de Stalingrad — Toulouse",
"Lundi": "Monday", "Mardi": "Tuesday", "Mercredi": "Wednesday", "Jeudi": "Thursday",
"Vendredi": "Friday", "Samedi": "Saturday", "Dimanche": "Sunday", "Fermé": "Closed",

# ---- Home : newsletter / socials / join
"Ne manquez aucune <span class=\"accent-italic\">soirée spéciale</span>":
    "Never miss a <span class=\"accent-italic\">special night</span>",
"Le Cercle": "The Circle",
"Soirées à thème, événements exclusifs, invitations privées : les membres du Cercle sont prévenus avant tout le monde. Rejoignez les initiés de la nuit toulousaine.":
    "Theme nights, exclusive events, private invitations: members of the Circle hear first. Join the insiders of Toulouse after dark.",
"Votre adresse e-mail": "Your email address",
"Rejoindre": "Join",
"En vous inscrivant, vous acceptez de recevoir nos invitations par e-mail. Désinscription en un clic — vos données restent strictement confidentielles.":
    "By signing up you agree to receive our invitations by email. Unsubscribe in one click — your details stay strictly confidential.",
"✦&nbsp;&nbsp;Bienvenue dans le Cercle. Vous serez les premiers informés de nos prochaines nuits.":
    "✦&nbsp;&nbsp;Welcome to the Circle. You'll be the first to hear about our next nights.",
"La nuit continue <span class=\"accent-italic\">en ligne</span>":
    "The night carries on <span class=\"accent-italic\">online</span>",
"Suivez-nous": "Follow us",
"Coulisses, soirées à thème, nouvelles danseuses : suivez la vie du club au quotidien.":
    "Backstage, theme nights, new dancers: follow the club's daily life.",
"Danseuse, artiste, performeuse&nbsp;?": "Dancer, artist, performer?",
"Rejoignez la scène du Silver Palace": "Join the Silver Palace stage",
"Recrutement danseuses": "Dancer recruitment",
"Club de striptease, cabaret &amp; gentlemen's club à Toulouse. Votre référence de la nuit dans la Ville rose.":
    "Strip club, cabaret &amp; gentlemen's club in Toulouse. Your reference after dark in the Pink City.",
"© 2026 Silver Palace — Club de striptease &amp; cabaret à Toulouse. Tous droits réservés. Interdit aux moins de 18 ans. L'abus d'alcool est dangereux pour la santé, à consommer avec modération.":
    "© 2026 Silver Palace — Strip club &amp; cabaret in Toulouse. All rights reserved. Strictly 18+. Excessive drinking is harmful to health; please drink responsibly.",
}

T.update({
# ---- Réservation
"Réservez votre <span class=\"accent-italic\">nuit</span>": "Book your <span class=\"accent-italic\">night</span>",
"Votre table vous attend": "Your table is waiting",
"Une table pour la soirée, un salon pour un événement : dites-nous quand vous venez, nous nous occupons du reste. Réservation fortement conseillée le vendredi et le samedi.":
    "A table for the evening, a private room for an event: tell us when you're coming and we'll take care of the rest. Booking strongly advised on Friday and Saturday.",
"Prénom *": "First name *", "Téléphone *": "Phone *", "E-mail": "Email",
"Date souhaitée *": "Preferred date *", "Heure d'arrivée": "Arrival time",
"Nombre de personnes": "Number of guests", "Occasion": "Occasion",
"Message (optionnel)": "Message (optional)",
"22h — ouverture": "10pm — opening", "23h": "11pm", "Minuit": "Midnight",
"1h": "1am", "2h et après": "2am and later",
"1 à 2": "1 to 2", "3 à 5": "3 to 5", "6 à 10": "6 to 10", "Plus de 10": "More than 10",
"Soirée classique": "A regular night out",
"Enterrement de vie de garçon": "Stag do",
"Enterrement de vie de jeune fille": "Hen party",
"Anniversaire": "Birthday",
"Soirée d'entreprise": "Corporate night",
"Autre": "Other",
"Bouteille en table, surprise à organiser, demande particulière…":
    "Bottle service, a surprise to arrange, any special request…",
"Nous vous confirmons la réservation par téléphone dans les plus brefs délais. L'entrée est réservée aux personnes majeures ; tenue correcte exigée.":
    "We'll confirm your booking by phone as soon as possible. Entry is for adults only; smart dress required.",
"Demander ma réservation": "Request my booking",
"✦&nbsp;&nbsp;Demande envoyée. Nous vous rappelons très vite pour confirmer votre table — à ce soir, peut-être.":
    "✦&nbsp;&nbsp;Request sent. We'll call you back shortly to confirm your table — see you tonight, perhaps.",
"Par téléphone": "By phone",
"La ligne directe du club, du mardi au samedi dès 22h :":
    "The club's direct line, Tuesday to Saturday from 10pm:",
"Sur place": "In person",
"31 Rue de Stalingrad, 31000 Toulouse<br>À 5 min à pied de la gare Matabiau.":
    "31 Rue de Stalingrad, 31000 Toulouse<br>5 min walk from Matabiau station.",
"Mardi — Samedi : 22h à 6h<br>Fermé dimanche et lundi.":
    "Tuesday — Saturday: 10pm to 6am<br>Closed Sunday and Monday.",
"Votre prénom": "Your first name",

# ---- Candidature
"Danser au <span class=\"accent-italic\">Silver</span>": "Dance at the <span class=\"accent-italic\">Silver</span>",
"Recrutement": "Now hiring",
"Danseuse confirmée ou grande débutante : si la scène vous attire, le Silver Palace vous ouvre ses portes. Un premier échange confidentiel, sans engagement.":
    "Experienced dancer or complete beginner: if the stage calls to you, Silver Palace is open. A first confidential chat, no strings attached.",
"Un cadre sécurisé": "A secure setting",
"Équipe de sécurité présente chaque soir, direction à l'écoute, règles claires : vous dansez, nous veillons. Le respect n'est pas négociable au Silver.":
    "Security on site every night, management who listen, clear rules: you dance, we watch over you. Respect is non-negotiable at the Silver.",
"Plannings flexibles": "Flexible schedules",
"Vous choisissez vos soirs. Études, autre activité, vie de famille : votre planning s'adapte à votre vie, pas l'inverse.":
    "You choose your nights. Studies, another job, family life: your schedule fits your life, not the other way round.",
"Rémunération attractive": "Attractive pay",
"Shows, danses privées, soirées événement : les détails de la rémunération sont présentés en toute transparence lors de l'entretien.":
    "Shows, private dances, event nights: the full pay structure is explained transparently at interview.",
"Débutantes bienvenues": "Beginners welcome",
"Pas d'expérience de scène ? Nos danseuses confirmées vous accompagnent à vos débuts. L'envie et l'attitude comptent plus que le CV.":
    "No stage experience? Our experienced dancers will guide you through your first nights. Drive and attitude count for more than a CV.",
"Prénom ou nom de scène *": "First name or stage name *",
"Comment vous appeler ?": "What should we call you?",
"Âge *": "Age *", "18 ans minimum": "18 minimum",
"Instagram (optionnel)": "Instagram (optional)", "@votrecompte": "@yourhandle",
"Expérience": "Experience", "Débutante": "Beginner",
"Moins d'un an": "Less than a year", "1 à 3 ans": "1 to 3 years", "Plus de 3 ans": "More than 3 years",
"Vos disponibilités, votre parcours…": "Your availability, your background…",
"Parlez-nous de vous en quelques lignes.": "Tell us about yourself in a few lines.",
"Candidature strictement confidentielle, réservée aux personnes majeures. Vos coordonnées ne servent qu'à vous recontacter — elles ne sont jamais partagées.":
    "Applications are strictly confidential and open to adults only. Your details are used solely to get back to you — never shared.",
"Envoyer ma candidature": "Send my application",
"✦&nbsp;&nbsp;Candidature reçue. Nous vous recontactons rapidement, en toute discrétion. À très vite sur scène.":
    "✦&nbsp;&nbsp;Application received. We'll be in touch shortly, discreetly. See you on stage very soon.",
"Comment ça se passe": "How it works",
"Vous envoyez ce formulaire": "You send this form",
"Échange téléphonique discret": "A discreet phone call",
"Rencontre au club, en journée": "We meet at the club, during the day",
"Essai sans engagement": "A trial night, no commitment",
"Plutôt Instagram ?": "Prefer Instagram?",
"Écrivez-nous directement en message privé :": "Send us a direct message:",

# ---- Événements
"Événements &amp; <span class=\"accent-italic\">soirées</span>": "Events &amp; <span class=\"accent-italic\">nights</span>",
"Les nuits du Silver": "Nights at the Silver",
"Chaque semaine, le Silver Palace réinvente sa nuit : soirées à thème, shows exceptionnels et événements privés. Voici tout ce que le club peut faire de votre soirée.":
    "Every week, Silver Palace reinvents its night: theme nights, exceptional shows and private events. Here's everything the club can make of your evening.",
"Bunny nights, soirées lingerie, thèmes de saison : la troupe se met en scène et le club change de visage. Les dates sont annoncées sur nos réseaux — suivez-nous pour ne rien manquer.":
    "Bunny nights, lingerie nights, seasonal themes: the troupe takes the stage and the club changes face. Dates are announced on our socials — follow us so you don't miss a thing.",
"Le programme sur Instagram": "What's on, over on Instagram",
"EVG &amp; EVJF": "Stag &amp; hen parties",
"Le futur marié sur scène, le champagne qui coule, un show dédié au groupe : nos formules enterrement de vie de garçon et de jeune fille font des adieux au célibat un souvenir mémorable.":
    "The groom-to-be on stage, champagne flowing, a show dedicated to your group: our stag and hen packages turn a farewell to single life into a night to remember.",
"Organiser la soirée": "Plan the night",
"Anniversaires &amp; groupes": "Birthdays &amp; groups",
"Table réservée, bouteille au frais, attention particulière de la troupe pour l'invité d'honneur : fêter un anniversaire au Silver, c'est le fêter deux fois.":
    "Reserved table, bottle on ice, special attention from the troupe for the guest of honour: celebrating a birthday at the Silver means celebrating it twice.",
"Réserver une table": "Book a table",
"Privatisation": "Private hire",
"Comité d'entreprise, lancement, événement privé : le club et sa troupe peuvent être à vous seuls le temps d'une nuit. Devis sur mesure, discrétion totale.":
    "Company event, product launch, private party: the club and its troupe can be yours alone for a night. Bespoke quote, complete discretion.",
"Demander un devis": "Request a quote",
"Une date en tête&nbsp;?": "Got a date in mind?",
"Danseuse en tenue de soirée à thème au Silver Palace Toulouse":
    "Dancer in theme-night costume at Silver Palace Toulouse",

# ---- Carte boissons
"La carte des <span class=\"accent-italic\">boissons</span>": "The <span class=\"accent-italic\">drinks</span> menu",
"Servie dans la lumière tamisée du bar, notre carte célèbre les champagnes de grandes maisons et les spiritueux de caractère. Le premier verre vous est offert — le reste de la nuit vous appartient.":
    "Served in the soft light of the bar, our menu celebrates champagnes from the great houses and spirits with character. Your first drink is on us — the rest of the night is yours.",
"Champagnes": "Champagne", "La coupe": "By the glass", "Digestifs": "Digestifs",
"Liqueurs": "Liqueurs", "Bières — 33cl": "Beers — 33cl", "Softs — 33cl": "Soft drinks — 33cl",
"Jus de fruits": "Fruit juice", "Limonade": "Lemonade", "Sirop à l'eau": "Cordial &amp; water",
"Saint James ambré / blanc": "Saint James amber / white",
"L'abus d'alcool est dangereux pour la santé, à consommer avec modération.":
    "Excessive drinking is harmful to health; please drink responsibly.",
"Danseuse au bar du Silver Palace, club de nuit à Toulouse":
    "Dancer at the Silver Palace bar, night club in Toulouse",
"Le bar vous attend": "The bar is waiting",
"Votre table pour ce soir&nbsp;?": "A table for tonight?",

# ---- Carte danses
"La carte des <span class=\"accent-italic\">danses</span>": "The <span class=\"accent-italic\">dance</span> menu",
"De la table dance au salon VIP, nos danseuses vous invitent dans l'intimité de leurs shows privés. Voici la carte officielle du club.":
    "From table dance to VIP room, our dancers invite you into the intimacy of their private shows. Here is the club's official menu.",
"Shows Privés": "Private Shows",
"1 chanson topless (salle principale)": "1 song topless (main room)",
"1 chanson nue": "1 song fully nude", "2 chansons nue": "2 songs fully nude",
"3 chansons nue": "3 songs fully nude",
"20 min + ½ bouteille de champagne": "20 min + ½ bottle of champagne",
"1 danseuse – 30 min": "1 dancer – 30 min",
"EVG / Anniversaire": "Stag do / Birthday",
"4 chansons, 2 danseuses + 1 bouteille Mercier": "4 songs, 2 dancers + 1 bottle of Mercier",
"60 min + 1 bouteille Mercier": "60 min + 1 bottle of Mercier",
"90 min + 1 bouteille Mum Brut, 2 danseuses": "90 min + 1 bottle of Mumm Brut, 2 dancers",
"4 chansons + 2 consommations": "4 songs + 2 drinks",
"30 min + 1 bouteille Mercier": "30 min + 1 bottle of Mercier",
"Show Lesbien": "Lesbian Show", "30 min": "30 min",
"45 min + 1 bouteille Mercier": "45 min + 1 bottle of Mercier",
"60 min + 1 bouteille Mum Brut, 2 danseuses": "60 min + 1 bottle of Mumm Brut, 2 dancers",
"2h + 1 bouteille Dom Pérignon, 2 danseuses": "2h + 1 bottle of Dom Pérignon, 2 dancers",
"Les danses se déroulent dans le respect des règles de la maison, présentées sur place. Nos équipes veillent au confort de tous — celui de nos danseuses comme le vôtre.":
    "Dances take place within the house rules, explained on site. Our teams look after everyone's comfort — our dancers' as much as yours.",
"Le spectacle vous attend": "The show is waiting",
"Vivez-le depuis votre table": "Experience it from your table",
"Danseuse de pole dance dans la lumière rouge du Silver Palace":
    "Pole dancer in the red light of Silver Palace",

# ---- Contact
"Entrons en <span class=\"accent-italic\">contact</span>": "Let's get <span class=\"accent-italic\">in touch</span>",
"Une question, un projet d'événement, une demande presse ? Écrivez-nous — et pour les réservations du soir même, le téléphone reste le plus rapide.":
    "A question, an event in mind, a press enquiry? Write to us — and for same-night bookings, the phone is still fastest.",
"Nom *": "Name *", "E-mail *": "Email *", "Sujet": "Subject", "Message *": "Message *",
"Question générale": "General question",
"Réservation / événement privé": "Booking / private event",
"Privatisation / entreprise": "Private hire / corporate",
"Presse &amp; partenariats": "Press &amp; partnerships",
"Votre message…": "Your message…", "Votre nom": "Your name",
"Nous répondons généralement sous 24 à 48h. Pour une réservation le soir même, appelez directement le club.":
    "We usually reply within 24 to 48 hours. For a same-night booking, call the club directly.",
"Envoyer le message": "Send message",
"✦&nbsp;&nbsp;Message envoyé. Nous revenons vers vous très vite — merci de votre confiance.":
    "✦&nbsp;&nbsp;Message sent. We'll get back to you very soon — thank you for your trust.",
"Coordonnées": "Contact details",

# ---- À propos
"L'esprit de la <span class=\"accent-italic\">maison</span>": "The spirit of the <span class=\"accent-italic\">house</span>",
"Le Silver Palace": "Silver Palace",
"Derrière la façade lumineuse de la rue de Stalingrad, un club pensé comme un écrin : sensualité assumée, élégance jamais négociée, discrétion absolue.":
    "Behind the glowing frontage on Rue de Stalingrad, a club designed as a jewel box: unapologetic sensuality, elegance never compromised, absolute discretion.",
"Notre histoire": "Our story",
"Un cabaret <span class=\"accent-italic\">contemporain</span>": "A <span class=\"accent-italic\">contemporary</span> cabaret",
"Le Silver Palace est né d'une conviction : Toulouse méritait un club où l'art du striptease se vit comme un spectacle, dans un cadre digne des grandes maisons.":
    "Silver Palace was born of one conviction: Toulouse deserved a club where the art of striptease is experienced as spectacle, in surroundings worthy of the great houses.",
"Scène centrale, salons feutrés, bar à champagne : chaque espace du club a été pensé pour la nuit. Notre troupe de danseuses professionnelles fait vivre l'héritage du cabaret avec l'énergie d'aujourd'hui — plumes et paillettes comprises.":
    "Central stage, hushed private rooms, champagne bar: every space in the club was designed for the night. Our troupe of professional dancers keeps the cabaret heritage alive with today's energy — feathers and sequins included.",
"Ici, les codes sont clairs : le raffinement est exigé, la discrétion garantie, et le respect — celui de nos hôtes comme de nos artistes — est la première règle de la maison.":
    "Here the codes are clear: refinement is expected, discretion guaranteed, and respect — for our guests as much as our artists — is the first rule of the house.",
"Façade illuminée du Silver Palace, club de striptease rue de Stalingrad à Toulouse":
    "Illuminated Silver Palace frontage, strip club on Rue de Stalingrad in Toulouse",
"Rue de Stalingrad": "Rue de Stalingrad",
"L'écrin": "The setting",
"Trois espaces, une seule <span class=\"accent-italic\">nuit</span>":
    "Three spaces, one <span class=\"accent-italic\">night</span>",
"Danseuse à la barre sur la scène centrale du Silver Palace Toulouse":
    "Dancer on the pole on the central stage at Silver Palace Toulouse",
"Le cœur battant du club : la scène centrale et sa barre, visibles de toutes les tables, où les shows s'enchaînent jusqu'à l'aube.":
    "The beating heart of the club: the central stage and its pole, visible from every table, where shows run one after another until dawn.",
"Salon privé du Silver Palace, satin rouge et lumière feutrée":
    "Silver Palace private room, red satin and soft light",
"Derrière les rideaux, les salons feutrés accueillent les danses privées et les moments d'exception, à l'abri des regards.":
    "Behind the curtains, the hushed private rooms host private dances and exceptional moments, away from prying eyes.",
"Le bar du Silver Palace, champagnes et spiritueux à Toulouse":
    "The Silver Palace bar, champagne and spirits in Toulouse",
"Le bar": "The bar",
"Champagnes de grandes maisons et spiritueux de caractère : le bar est le point de départ de toutes les nuits — premier verre offert.":
    "Champagnes from the great houses and spirits with character: the bar is where every night begins — first drink on us.",
"La devise du Silver Palace": "The Silver Palace motto",
"« Vivez la nuit. <span class=\"accent-italic\">Touchez le rêve.</span> »":
    "\"Live the night. <span class=\"accent-italic\">Touch the dream.</span>\"",
"Nos valeurs": "Our values",
"Trois mots, une <span class=\"accent-italic\">promesse</span>":
    "Three words, one <span class=\"accent-italic\">promise</span>",
"Le spectacle avant tout : des shows travaillés, des artistes passionnées, une ambiance qui éveille les sens sans jamais forcer le trait.":
    "Spectacle above all: crafted shows, passionate artists, an atmosphere that awakens the senses without ever overplaying it.",
"Du décor à la carte des champagnes, tout est pensé haut de gamme. La tenue correcte est exigée — l'élégance se partage.":
    "From the décor to the champagne list, everything is designed upmarket. Smart dress is required — elegance is shared.",
"Ce qui se passe au Silver reste au Silver. Codes discrets, personnel attentif : votre tranquillité fait partie de l'expérience.":
    "What happens at the Silver stays at the Silver. Discreet codes, attentive staff: your peace of mind is part of the experience.",
"Le découvrir en vrai": "See it for yourself",
"Poussez la porte, ce soir": "Walk through the door tonight",
"Réserver ma table": "Book my table",
"Fauteuil baroque argenté dans les salons du Silver Palace":
    "Silver baroque armchair in the Silver Palace rooms",

# ---- 404
"Cette porte est <span class=\"accent-italic\">fermée</span>": "This door is <span class=\"accent-italic\">closed</span>",
"Erreur 404": "Error 404",
"La page que vous cherchez n'existe pas — mais la nuit, elle, vous attend toujours.":
    "The page you're looking for doesn't exist — but the night is still waiting for you.",
"Retour à l'accueil": "Back to home",
"Page introuvable": "Page not found",
})

