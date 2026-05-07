NLOS Lite Alpha 4

NLOS est un projet expérimental de système d’exploitation léger basé sur Linux.

L’objectif est de créer un système bootable, propre, rapide et visuellement moderne, capable de fonctionner sur des machines modestes tout en proposant des modes d’optimisation simples.

Cette version est une Alpha. Elle sert à tester la base technique, l’interface NLOS Center et les premiers outils système.

Objectifs

NLOS vise à proposer :

- une base Linux légère ;
- une interface plus propre qu’un Linux classique ;
- un mode Live USB ;
- des outils d’optimisation ;
- un mode performance ;
- un mode gaming ;
- un mode old machine ;
- une structure claire pour développer un vrai shell NLOS plus tard.

Compatibilité

Cette ISO est destinée aux machines amd64 / x86_64.

Elle peut fonctionner sur beaucoup de PC et de Mac Intel.

Elle n’est pas compatible avec les anciens Mac PowerPC comme certains iMac G4 sans créer une version PowerPC séparée.

Fonctionnalités actuelles

- Base Debian Live XFCE.
- ISO bootable générée avec GitHub Actions.
- NLOS Center en HTML/CSS.
- Commande nlos-boost.
- Commande nlos-game-run.
- Commande nlos-info.
- Mode Live USB.
- Premiers éléments visuels NLOS.

Commandes utiles

Afficher les informations système :

nlos-info

Activer le mode performance :

sudo nlos-boost performance

Activer le mode gaming :

sudo nlos-boost gaming

Activer le mode vieux Mac / machine faible :

sudo nlos-boost oldmac

Lancer un jeu avec les variables d’optimisation :

nlos-game-run commande_du_jeu

Ouvrir le centre NLOS :

nlos-center

Limites

NLOS Alpha 4 n’est pas encore un OS final.

Le système reste basé sur Debian Live XFCE. Certains éléments Debian peuvent encore apparaître.

Le mode gaming améliore l’environnement d’exécution, mais ne rend pas tous les jeux compatibles automatiquement. Les jeux Windows peuvent nécessiter Wine, Proton, DXVK ou des pilotes adaptés. Les jeux macOS natifs ne sont pas compatibles directement avec Linux.

Roadmap

Alpha 5 :

- meilleur thème visuel ;
- suppression plus complète du branding Debian ;
- icônes NLOS ;
- bureau plus propre ;
- meilleur démarrage ;
- optimisations matérielles automatiques.

Alpha 6 :

- vrai shell NLOS ;
- centre de contrôle natif ;
- assistant système ;
- meilleure gestion des profils de performance ;
- interface plus proche d’un OS moderne.

NLOS est une base expérimentale qui évolue progressivement vers un OS léger, clair et personnel.
