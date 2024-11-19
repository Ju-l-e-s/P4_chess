# Gestion de Tournois d'Échecs

Ce projet est une application console en Python permettant de gérer des tournois d'échecs selon le système suisse. Il offre les fonctionnalités suivantes :

- **Gestion des joueurs** : ajout et listing des joueurs avec leurs informations.
- **Gestion des tournois** : création et gestion de tournois avec plusieurs tours.
- **Génération des appariements** : appariement des joueurs en respectant les règles du système suisse.
- **Enregistrement des résultats** : saisie des résultats des matchs et mise à jour des points.
- **Rapports** : génération de rapports sur les joueurs et les tournois.

## Prérequis

- **Python 3.7** ou supérieur installé sur votre machine.
- Les dépendances Python listées dans `requirements.txt`.

## Installation

1. **Cloner le dépôt du projet :**

```bash
git clone <URL_DU_DÉPÔT>
```

2. **Naviguer dans le répertoire du projet :**

```bash
cd nom_du_projet
```

3. **Créer un environnement virtuel :**

```bash
python -m venv env
```

**Sur Windows :**
```bash
env\Scripts\activate
```

**Sur macOS/Linux :**
```bash
source env/bin/activate
```

4. **Installer les dépendances :**
```bash
pip install -r requirements.txt
```



**Utilisation**
```bash
python main.py
```
Le programme affiche un menu principal permettant d'effectuer les actions suivantes :

1. **Ajouter un joueur** : saisir les informations d'un nouveau joueur.
2. **Lister les joueurs** : afficher la liste des joueurs enregistrés.
3. **Créer un tournoi** : initialiser un nouveau tournoi.
4. **Lister les tournois** : afficher la liste des tournois existants.
5. **Démarrer un tournoi** : lancer le déroulement d'un tournoi sélectionné.
6. **Quitter** : fermer le programme.

### Instructions générales

- **Navigation dans le menu** : entrez le numéro correspondant à l'action que vous souhaitez effectuer.
- **Saisie des informations** : suivez les instructions à l'écran pour entrer les données requises.
- **Format des dates** : les dates doivent être au format `jj/mm/aaaa`.
- **Identifiant national** : doit être composé de deux lettres majuscules suivies de cinq chiffres (exemple : `AB12345`).


## Structure du projet :
```
- controllers/
    - __init__.py
    - joueur_controller.py
    - match_controller.py
    - tour_controller.py
    - tournoi_controller.py
- models/
    - __init__.py
    - joueur.py
    - match.py
    - tour.py
    - tournoi.py
- views/
    - __init__.py
    - joueur_view.py
    - match_view.py
    - tour_view.py
    - tournoi_view.py
- data/
    - joueurs.json
    - tournois.json
- flake8_report/
    - index.html
- main.py
- requirements.txt
- README.md
```