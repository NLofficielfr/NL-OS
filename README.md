NL OS Alpha

NL OS est un projet expérimental de système d’exploitation basé sur Linux.

Le but du projet est de créer une base d’OS personnalisée, bootable et évolutive, avec une interface plus moderne, plus claire et plus agréable qu’un environnement Linux classique.

Cette version est une première étape. Elle ne représente pas encore le résultat final, mais elle permet déjà de tester une base fonctionnelle, de démarrer le système depuis une clé USB, et d’intégrer progressivement les éléments propres à NL OS.

Objectif du projet

L’objectif de NL OS est de construire un système simple à utiliser, visuellement propre, moderne, personnalisable, basé sur une vraie base Linux, capable de démarrer depuis une clé USB, et évolutif vers une interface beaucoup plus travaillée.

NL OS n’a pas vocation à rester un simple thème Linux. L’idée est de partir d’une base existante fiable, puis de la transformer progressivement pour créer une vraie expérience différente.

État actuel

La version actuelle est une version Alpha.

Elle contient une base Debian Live XFCE modifiée avec une première couche de personnalisation NL OS. Cette version permet surtout de valider que le système peut être généré, téléchargé, flashé sur une clé USB et lancé sur une machine réelle.

Ce qui fonctionne actuellement :

- démarrage depuis une clé USB ;
- base Debian Live fonctionnelle ;
- environnement graphique XFCE ;
- génération automatique de l’ISO avec GitHub Actions ;
- ajout d’un dossier système dédié à NL OS ;
- ajout de premiers scripts NL OS ;
- ajout d’un prototype de centre de contrôle ;
- début de personnalisation visuelle ;
- possibilité de tester le système sans installation.

Ce qui est inclus

Base système

NL OS utilise actuellement une base Debian Live XFCE. Cette base permet d’avoir un système stable, léger et capable de fonctionner en mode Live USB.

NL Control Center

Un premier prototype de centre de contrôle est inclus. Il sert pour l’instant à tester l’idée d’une application centrale permettant de gérer certains réglages et outils liés à NL OS.

Ce centre de contrôle sera amélioré dans les prochaines versions.

Scripts système

Deux premières commandes sont intégrées :

nl-welcome

Cette commande affiche un message d’accueil et quelques informations de base sur NL OS.

nl-performance

Cette commande applique quelques réglages simples liés aux performances. Elle reste expérimentale et sera améliorée plus tard.

Structure NL OS

Les fichiers personnalisés du système sont placés dans :

/opt/nl-os

Ce dossier sert de base pour organiser les scripts, applications, fichiers visuels et composants spécifiques à NL OS.

Génération de l’ISO

L’ISO de NL OS est générée automatiquement avec GitHub Actions.

Le processus permet de reconstruire le système à partir des fichiers du dépôt. À chaque modification importante envoyée sur GitHub, une nouvelle version bootable peut être produite.

Le workflow actuel :

1. télécharge une base Debian Live XFCE ;
2. extrait le système ;
3. ajoute les fichiers NL OS ;
4. ajoute les scripts et éléments visuels ;
5. reconstruit le système ;
6. génère une nouvelle ISO bootable ;
7. publie l’ISO dans les artifacts GitHub Actions.

Télécharger l’ISO

Pour télécharger la dernière version générée :

1. ouvrir le dépôt GitHub ;
2. aller dans l’onglet Actions ;
3. ouvrir le dernier build réussi ;
4. descendre jusqu’à la section Artifacts ;
5. télécharger l’archive ;
6. décompresser le fichier .zip ;
7. récupérer le fichier .iso.

Le fichier ISO peut ensuite être utilisé pour créer une clé USB bootable.

Tester NL OS

Pour tester NL OS sur une vraie machine :

1. télécharger l’ISO depuis GitHub Actions ;
2. décompresser l’archive ;
3. ouvrir BalenaEtcher ou un outil équivalent ;
4. sélectionner l’ISO NL OS ;
5. sélectionner une clé USB ;
6. flasher l’image ;
7. redémarrer l’ordinateur ;
8. ouvrir le menu de démarrage ;
9. sélectionner la clé USB ;
10. choisir le mode Live.

Il est recommandé de tester le système en mode Live avant toute installation.

Installation

Pour l’instant, il est déconseillé d’installer NL OS comme système principal.

La version Alpha est faite pour être testée depuis une clé USB. L’installation sur un disque interne ou externe pourra être envisagée plus tard, lorsque l’interface, les réglages et la stabilité seront meilleurs.

Direction visuelle

La direction visuelle recherchée pour NL OS est une interface claire, douce et moderne.

L’objectif n’est pas d’avoir un Linux sombre classique ou un thème trop chargé. NL OS doit évoluer vers une interface plus premium, avec une vraie cohérence graphique.

La direction visuelle visée :

- interface claire ;
- effets de verre ;
- coins arrondis ;
- dock propre ;
- icônes personnalisées ;
- fond lumineux ;
- menus simples ;
- fenêtres plus élégantes ;
- meilleure organisation visuelle ;
- impression générale plus fluide et plus moderne.

La version actuelle ne représente pas encore totalement cette vision. Elle sert surtout de base technique pour construire la suite.

Limites actuelles

NL OS Alpha reste une version expérimentale.

Limites connues :

- le branding Debian peut encore apparaître à certains endroits ;
- l’interface XFCE reste limitée visuellement ;
- le design n’est pas encore final ;
- certaines icônes ne sont pas personnalisées ;
- le centre de contrôle est encore très simple ;
- certains éléments peuvent ne pas fonctionner selon la machine ;
- l’expérience n’est pas encore assez fluide ni assez cohérente.

Ces limites seront corrigées progressivement.

Roadmap

Alpha 1

Première base bootable.

Objectifs :

- générer une ISO ;
- vérifier que le système démarre ;
- ajouter les premiers fichiers NL OS ;
- créer une base de travail.

Alpha 2

Première personnalisation visuelle.

Objectifs :

- améliorer le fond d’écran ;
- ajouter une identité visuelle plus claire ;
- commencer à modifier les panels ;
- rendre le bureau moins brut ;
- ajouter des raccourcis NL OS.

Alpha 3

Amélioration du branding.

Objectifs :

- remplacer davantage les éléments Debian ;
- améliorer le menu de démarrage ;
- ajouter un thème plus propre ;
- créer des icônes personnalisées ;
- améliorer l’écran d’accueil.

Alpha 4

Amélioration de l’expérience utilisateur.

Objectifs :

- rendre l’interface plus fluide ;
- améliorer le centre de contrôle ;
- organiser les applications ;
- rendre l’utilisation plus simple ;
- préparer une interface plus personnalisée.

Versions futures

À long terme, NL OS pourra évoluer vers une interface plus indépendante, avec des composants développés spécifiquement pour le projet.

Possibilités futures :

- interface maison ;
- centre de contrôle complet ;
- assistant intégré ;
- store d’applications ;
- système de personnalisation ;
- meilleur dock ;
- meilleure gestion des fenêtres ;
- design plus proche d’un vrai OS moderne.

Technologies utilisées

Le projet utilise actuellement Debian Live, XFCE, GitHub Actions, Bash, Python, SquashFS, Xorriso et des scripts de personnalisation système.

Ces choix permettent de construire rapidement une base fonctionnelle et testable.

Pourquoi Debian Live ?

Debian Live a été choisi comme base parce qu’il permet de créer un système stable, léger et bootable.

C’est une base pratique pour expérimenter sans devoir créer un système complet depuis zéro. Elle permet de se concentrer d’abord sur l’interface, la structure et l’expérience utilisateur.

Avertissement

NL OS Alpha est une version expérimentale.

Elle peut contenir des bugs, des erreurs, des problèmes d’affichage ou des éléments incomplets. Elle ne doit pas être utilisée comme système principal pour le moment.

Il est conseillé de tester NL OS uniquement en mode Live USB ou dans une machine virtuelle.

Auteur

Projet créé par NLofficielfr.

NL OS Alpha est une première étape vers un système plus personnel, plus visuel et plus moderne.
