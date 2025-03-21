# CFC Composants

Documentation des composants Bootstrap 5 pour Moodle, basée sur le générateur de site IDOINE.

[![Bootstrap Version](https://img.shields.io/badge/bootstrap-5.3-purple.svg)]()
[![Node Version](https://img.shields.io/badge/node-18%2B-brightgreen.svg)]()
[![Python Version](https://img.shields.io/badge/python-3.9%2B-blue.svg)]()
[![License](https://img.shields.io/badge/license-MIT-green.svg)]()

## 📋 Table des matières

1. [À propos](#-à-propos)
2. [Prérequis](#-prérequis)
3. [Installation](#-installation)
4. [Utilisation](#-utilisation)
5. [Structure du projet](#-structure-du-projet)
6. [Composants documentés](#-composants-documentés)
7. [Contribution](#-contribution)

## 📖 À propos

CFC Composants est un site de documentation qui présente l'utilisation des composants Bootstrap 5 dans le contexte de Moodle. Il fournit des exemples pratiques, des bonnes pratiques et des considérations d'accessibilité pour chaque composant.

## 🔧 Prérequis

- Node.js 18 ou supérieur
- Python 3.9 ou supérieur
- npm
- pip

## 💻 Installation

1. Cloner le dépôt :

```bash
git clone [URL_DU_REPO]
cd cfc-composants
```

2. Installer les dépendances Node.js :

```bash
npm install
```

3. Installer les dépendances Python :

```bash
pip install -r requirements.txt
```

## 🚀 Utilisation

### Développement

Lance le serveur de développement avec rechargement à chaud :

```bash
npm run dev
```

Le site sera accessible sur `http://localhost:9000`

### Production

Génère une version optimisée du site :

```bash
npm run build
```

## 📁 Structure du projet

```
/
├── dist/                # Fichiers générés
├── src/
│   ├── assets/         # Images, polices...
│   ├── locales/        # Contenu en français
│   │   └── fr/
│   │       └── pages/
│   │           └── composants/  # Documentation des composants
│   └── styles/         # Fichiers SCSS
├── scripts/            # Scripts Python
├── templates/          # Templates du site
│   └── pages/
│       └── composant.html  # Template pour les pages de composants
└── package.json        # Dépendances Node.js
```

## 🧩 Composants documentés

### Composants de base
- Accordéon
- Alertes
- Boutons
- Cartes

### Navigation
- Barre de navigation
- Onglets

### Formulaires
- Champs de saisie
- Listes déroulantes

### Mise en page
- Grille
- Conteneurs

Chaque composant inclut :
- Description et utilisation de base
- Exemples pratiques
- Considérations d'accessibilité
- Notes spécifiques à Moodle
- Bonnes pratiques

## 👥 Contribution

1. Fork le projet
2. Créer une branche (`git checkout -b feature/NouveauComposant`)
3. Commit les changements (`git commit -m 'Ajout documentation NouveauComposant'`)
4. Push vers la branche (`git push origin feature/NouveauComposant`)
5. Créer une Pull Request

### Guide de style pour la documentation

- Utiliser le template de composant existant
- Inclure des exemples concrets
- Documenter les considérations d'accessibilité
- Ajouter des notes spécifiques à Moodle
- Fournir des exemples de code complets
