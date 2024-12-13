# R5C4_Final_ybenyoussef_abenyoussef
Examen Final R5C4 - 13/12/2024

Ce projet consiste en la mise en place d'une application web pour visualiser et analyser des algorithmes de recherche de chemin.

## Description

Le projet utilise des données collectées lors de recherches de chemins dans une grille via l'application [PathVisualizer](https://tlouvet.github.io/PathVisualizer/). L'objectif est d'explorer les performances de différents algorithmes en termes de temps d'exécution, de longueur de chemin, et de nœuds visités. Les données sont fournies au format JSON et doivent être traitées via un backend Flask et affichées dans une application Angular.

## Fonctionnalités

### Backend (Flask)
- **Connexion Angular** : Application connectée avec un front Angular en local (port 4200).
- **Routes RESTful** :
  - Route paginée pour récupérer les données de `searches.json`.
  - Route pour récupérer toutes les données pour la visualisation.
  - Trois routes stub (création, modification, suppression) qui renvoient une erreur `Method not implemented` avec un code HTTP adapté.

### Frontend (Angular v19)
- **Pages principales** :
  1. **Page d'accueil** :
     - Affiche un titre et un paragraphe d'introduction.
  2. **Page "Liste paginée"** :
     - Affiche les données en liste (30 entrées par page).
     - Inclut une navigation entre les pages.
     - Gestion de la pagination en front avec envoi des paramètres de query dans la requête.
  3. **Page "Graphiques"** :
     - **Cartes chiffres clés** : Nombre d'entrées par algorithme.
     - **Temps moyen de résolution** : Graphique comparatif des temps moyens (grilles de plus de 200 cases).
     - **Nœuds visités** : Graphique comparatif des nœuds moyens visités (distance euclidienne > 10).

- **Types et composants Angular** :
  - Types TypeScript pour les recherches.
  - Composants Angular pour chaque page et les graphiques (ngx-charts).

## Installation et Lancement

### Prérequis
- **Backend** : Python 3.10+
- **Frontend** : Node.js 18+, Angular CLI v19

### Installation

#### Backend
1. Cloner le dépôt :
   ```bash
   git clone https://github.com/votre-repo/r5c4-examen-final.git
   cd r5c4-examen-final/backend
   ```
2. Créer un environnement virtuel :
   ```bash
   python -m venv venv
   source venv/bin/activate  # Linux/macOS
   venv\Scripts\activate   # Windows
   ```
3. Installer les dépendances :
   ```bash
   pip install -r requirements.txt
   ```
4. Lancer le serveur :
   ```bash
   flask run
   ```

#### Frontend
1. Naviguer dans le dossier Angular :
   ```bash
   cd ../frontend
   ```
2. Installer les dépendances :
   ```bash
   npm install
   ```
3. Lancer le serveur Angular :
   ```bash
   ng serve
   ```

### Accès
- **Backend** : [http://localhost:5000](http://localhost:5000)
- **Frontend** : [http://localhost:4200](http://localhost:4200)

## Organisation des fichiers

### Backend
- **app/** : Contient les routes Flask et la logique backend.
- **data/** : Fichier `searches.json` pour les données des recherches.
- **requirements.txt** : Dépendances Python.

### Frontend
- **src/** :
  - **app/** : Composants Angular.
  - **assets/** : Ressources statiques.

## Architecture et Normes
- Respect des principes REST pour les routes backend.
- Utilisation des composants Angular pour la modularité.
- Code propre et bien commenté.

## Extras
- **Documentation claire** : Les étapes d'installation et de lancement sont fournies pour faciliter l'utilisation.
- **Stylisation** : Design agréable et navigation intuitive.
- **Graphiques interactifs** : Comparaisons illustrées pour les utilisateurs.

## Auteur
Projet réalisé dans le cadre de l'examen final du module R5C4.# R5C4_Final_ybenyoussef_abenyoussef
Examen Final R5C4 - 13/12/2024
