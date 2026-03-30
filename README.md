

# J17V - IT Talent Showcase

## 📖 Description
J17V est une plateforme de gestion de portfolios dédiée aux étudiants en informatique. Elle permet aux utilisateurs de s'inscrire, de personnaliser leur profil et de mettre en avant leurs projets, compétences et expériences professionnelles de manière élégante et interactive.

## ✨ Fonctionnalités Clés
- **Gestion de Profil :** Inscription sécurisée en deux étapes avec photo et bio.
- **Dashboard Personnel :** CRUD complet (Création, Lecture, Mise à jour, Suppression) pour :
  - Projets (avec images, tags et liens GitHub).
  - Expériences professionnelles (postes, dates, descriptions).
  - Compétences techniques.
  - Réseaux sociaux.
  - Tags personnalisés.
- **Showcase Public :** Page d'accueil présentant tous les talents avec une galerie 3D interactive (Cover Flow).
- **API REST :** Points de terminaison pour l'intégration de services tiers.

## 🛠️ Stack Technique
- **Backend :** Django 6.0+, Django Rest Framework.
- **Base de données :** MySQL.
- **Frontend :** HTML5/CSS3 (Templates Django), Tailwind CSS, Bootstrap 5.3, JavaScript (Vanilla).
- **Design :** Glassmorphism, Font Awesome, Google Fonts (Pacifico, Inter).

---

## 🚀 Installation et Lancement

Veuillez suivre ces instructions pour configurer le projet localement avec la base de données MySQL et le jeu d'essai fourni.

### 1. Cloner ou extraire le projet
```bash
git clone [https://github.com/Johnny17V/projetPortfolio/tree/main]
```
*(Si vous avez reçu une archive ZIP, décompressez-la simplement et ouvrez le terminal dans ce dossier).*

### 2. Créer et activer un environnement virtuel (Recommandé)
- **Sous Windows :** 
```bash
  python -m venv venv
  venv\Scripts\activate
  ```
- **Sous macOS/Linux :** 
```bash
  python3 -m venv venv
  source venv/bin/activate
  ```

### 3. Installer les dépendances
Installez toutes les librairies requises (incluant le connecteur MySQL) :
```bash
pip install -r requirements.txt
```

### 4. Configuration de la Base de Données (MySQL)
- Connectez-vous à votre serveur MySQL local.
- Créez la base de données requise en exécutant cette commande SQL : 
  ```sql
  CREATE DATABASE portfoliodb CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
  ```
- ⚠️ **IMPORTANT :** Ouvrez le fichier `settings.py` de Django (ou votre fichier `.env`) et mettez à jour la section `DATABASES` avec **votre propre nom d'utilisateur et mot de passe MySQL local**.

### 5. Appliquer les migrations
Construisez les tables dans la base de données `portfoliodb` :
```bash
python manage.py migrate
```

### 6. Importer les données de test (Fixtures)
Pour peupler la base de données avec le jeu d'essai complet (projets, utilisateurs, tags, etc.) :
```bash
python manage.py loaddata mes_donnees.json
```
*(Note : Le dossier contenant les images uploadées est inclus dans le projet pour que les médias s'affichent correctement dès le lancement).*

### 7. Lancer le serveur de développement
```bash
python manage.py runserver
```
Rendez-vous ensuite sur [http://127.0.0.1:8000/](http://127.0.0.1:8000/) pour voir le site en action.

---

## 🔐 Accès Évaluateur (Comptes de test)
Pour tester rapidement les fonctionnalités du Dashboard et du CRUD sans avoir à créer un nouveau compte depuis zéro, vous pouvez utiliser les identifiants suivants (importés via le fichier JSON) :

- **Identifiant (Username) :** `[cheikh]`
- **Mot de passe :** `[portfolio2026]`
