---
title: Navigation
description: Documentation sur l'utilisation des composants de navigation Bootstrap dans Moodle, incluant les barres de navigation et les menus.
template: pages/composant.html
---

La navigation est un élément essentiel de l'interface utilisateur de Moodle. Bootstrap 5 fournit plusieurs composants de navigation puissants, flexibles et responsives qui peuvent être intégrés harmonieusement dans Moodle.

## Barre de navigation (Navbar)

La barre de navigation est un composant puissant qui s'adapte à toutes les tailles d'écran et sert de conteneur pour les menus et fonctionnalités principales.

### Structure de base

<div class="component-preview">
    <nav class="navbar navbar-expand-lg navbar-light bg-light">
        <div class="container-fluid">
            <a class="navbar-brand" href="#">Moodle</a>
            <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarExample" aria-controls="navbarExample" aria-expanded="false" aria-label="Toggle navigation">
                <span class="navbar-toggler-icon"></span>
            </button>
            <div class="collapse navbar-collapse" id="navbarExample">
                <ul class="navbar-nav me-auto mb-2 mb-lg-0">
                    <li class="nav-item">
                        <a class="nav-link active" aria-current="page" href="#">Accueil</a>
                    </li>
                    <li class="nav-item">
                        <a class="nav-link" href="#">Mes cours</a>
                    </li>
                    <li class="nav-item dropdown">
                        <a class="nav-link dropdown-toggle" href="#" id="navbarDropdown" role="button" data-bs-toggle="dropdown" aria-expanded="false">
                            Ressources
                        </a>
                        <ul class="dropdown-menu" aria-labelledby="navbarDropdown">
                            <li><a class="dropdown-item" href="#">Documents</a></li>
                            <li><a class="dropdown-item" href="#">Vidéos</a></li>
                            <li><hr class="dropdown-divider"></li>
                            <li><a class="dropdown-item" href="#">Autres</a></li>
                        </ul>
                    </li>
                </ul>
                <form class="d-flex">
                    <input class="form-control me-2" type="search" placeholder="Rechercher" aria-label="Search">
                    <button class="btn btn-outline-primary" type="submit">Rechercher</button>
                </form>
            </div>
        </div>
    </nav>
</div>

```html
<nav class="navbar navbar-expand-lg navbar-light bg-light">
  <div class="container-fluid">
    <a class="navbar-brand" href="#">Moodle</a>
    <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarExample" aria-controls="navbarExample" aria-expanded="false" aria-label="Toggle navigation">
      <span class="navbar-toggler-icon"></span>
    </button>
    <div class="collapse navbar-collapse" id="navbarExample">
      <ul class="navbar-nav me-auto mb-2 mb-lg-0">
        <li class="nav-item">
          <a class="nav-link active" aria-current="page" href="#">Accueil</a>
        </li>
        <li class="nav-item">
          <a class="nav-link" href="#">Mes cours</a>
        </li>
        <li class="nav-item dropdown">
          <a class="nav-link dropdown-toggle" href="#" id="navbarDropdown" role="button" data-bs-toggle="dropdown" aria-expanded="false">
            Ressources
          </a>
          <ul class="dropdown-menu" aria-labelledby="navbarDropdown">
            <li><a class="dropdown-item" href="#">Documents</a></li>
            <li><a class="dropdown-item" href="#">Vidéos</a></li>
            <li><hr class="dropdown-divider"></li>
            <li><a class="dropdown-item" href="#">Autres</a></li>
          </ul>
        </li>
      </ul>
      <form class="d-flex">
        <input class="form-control me-2" type="search" placeholder="Rechercher" aria-label="Search">
        <button class="btn btn-outline-primary" type="submit">Rechercher</button>
      </form>
    </div>
  </div>
</nav>
```

### Variantes de la barre de navigation

<div class="preview-tabs">
    <div class="preview-tabs-headers">
        <button class="preview-tab-header active">Navbar foncée</button>
        <button class="preview-tab-header">Navbar primaire</button>
        <button class="preview-tab-header">Navbar avec image</button>
    </div>
    <div class="preview-tab-content">
        <nav class="navbar navbar-expand-lg navbar-dark bg-dark">
            <div class="container-fluid">
                <a class="navbar-brand" href="#">Moodle</a>
                <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarDark" aria-controls="navbarDark" aria-expanded="false" aria-label="Toggle navigation">
                    <span class="navbar-toggler-icon"></span>
                </button>
                <div class="collapse navbar-collapse" id="navbarDark">
                    <ul class="navbar-nav me-auto mb-2 mb-lg-0">
                        <li class="nav-item">
                            <a class="nav-link active" aria-current="page" href="#">Accueil</a>
                        </li>
                        <li class="nav-item">
                            <a class="nav-link" href="#">Cours</a>
                        </li>
                        <li class="nav-item">
                            <a class="nav-link" href="#">Calendrier</a>
                        </li>
                    </ul>
                </div>
            </div>
        </nav>

        ```html
        <nav class="navbar navbar-expand-lg navbar-dark bg-dark">
          <div class="container-fluid">
            <a class="navbar-brand" href="#">Moodle</a>
            <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarDark" aria-controls="navbarDark" aria-expanded="false" aria-label="Toggle navigation">
              <span class="navbar-toggler-icon"></span>
            </button>
            <div class="collapse navbar-collapse" id="navbarDark">
              <ul class="navbar-nav me-auto mb-2 mb-lg-0">
                <li class="nav-item">
                  <a class="nav-link active" aria-current="page" href="#">Accueil</a>
                </li>
                <li class="nav-item">
                  <a class="nav-link" href="#">Cours</a>
                </li>
                <li class="nav-item">
                  <a class="nav-link" href="#">Calendrier</a>
                </li>
              </ul>
            </div>
          </div>
        </nav>
        ```
    </div>
    <div class="preview-tab-content">
        <nav class="navbar navbar-expand-lg navbar-dark bg-primary">
            <div class="container-fluid">
                <a class="navbar-brand" href="#">Moodle</a>
                <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarPrimary" aria-controls="navbarPrimary" aria-expanded="false" aria-label="Toggle navigation">
                    <span class="navbar-toggler-icon"></span>
                </button>
                <div class="collapse navbar-collapse" id="navbarPrimary">
                    <ul class="navbar-nav me-auto mb-2 mb-lg-0">
                        <li class="nav-item">
                            <a class="nav-link active" aria-current="page" href="#">Accueil</a>
                        </li>
                        <li class="nav-item">
                            <a class="nav-link" href="#">Cours</a>
                        </li>
                        <li class="nav-item">
                            <a class="nav-link" href="#">Calendrier</a>
                        </li>
                    </ul>
                </div>
            </div>
        </nav>

        ```html
        <nav class="navbar navbar-expand-lg navbar-dark bg-primary">
          <div class="container-fluid">
            <a class="navbar-brand" href="#">Moodle</a>
            <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarPrimary" aria-controls="navbarPrimary" aria-expanded="false" aria-label="Toggle navigation">
              <span class="navbar-toggler-icon"></span>
            </button>
            <div class="collapse navbar-collapse" id="navbarPrimary">
              <ul class="navbar-nav me-auto mb-2 mb-lg-0">
                <li class="nav-item">
                  <a class="nav-link active" aria-current="page" href="#">Accueil</a>
                </li>
                <li class="nav-item">
                  <a class="nav-link" href="#">Cours</a>
                </li>
                <li class="nav-item">
                  <a class="nav-link" href="#">Calendrier</a>
                </li>
              </ul>
            </div>
          </div>
        </nav>
        ```
    </div>
    <div class="preview-tab-content">
        <nav class="navbar navbar-expand-lg navbar-light bg-light">
            <div class="container-fluid">
                <a class="navbar-brand" href="#">
                    <img src="https://via.placeholder.com/30/2e8804/ffffff?text=M" width="30" height="30" class="d-inline-block align-top" alt="Logo Moodle">
                    Moodle
                </a>
                <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarImage" aria-controls="navbarImage" aria-expanded="false" aria-label="Toggle navigation">
                    <span class="navbar-toggler-icon"></span>
                </button>
                <div class="collapse navbar-collapse" id="navbarImage">
                    <ul class="navbar-nav me-auto mb-2 mb-lg-0">
                        <li class="nav-item">
                            <a class="nav-link active" aria-current="page" href="#">Accueil</a>
                        </li>
                        <li class="nav-item">
                            <a class="nav-link" href="#">Cours</a>
                        </li>
                    </ul>
                </div>
            </div>
        </nav>

        ```html
        <nav class="navbar navbar-expand-lg navbar-light bg-light">
          <div class="container-fluid">
            <a class="navbar-brand" href="#">
              <img src="/path/to/logo.png" width="30" height="30" class="d-inline-block align-top" alt="Logo Moodle">
              Moodle
            </a>
            <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarImage" aria-controls="navbarImage" aria-expanded="false" aria-label="Toggle navigation">
              <span class="navbar-toggler-icon"></span>
            </button>
            <div class="collapse navbar-collapse" id="navbarImage">
              <ul class="navbar-nav me-auto mb-2 mb-lg-0">
                <li class="nav-item">
                  <a class="nav-link active" aria-current="page" href="#">Accueil</a>
                </li>
                <li class="nav-item">
                  <a class="nav-link" href="#">Cours</a>
                </li>
              </ul>
            </div>
          </div>
        </nav>
        ```
    </div>
</div>

### Points importants

- **Responsive** : Utilisez `.navbar-expand{-sm|-md|-lg|-xl|-xxl}` pour définir le breakpoint où la barre de navigation se développe
- **Branding** : La classe `.navbar-brand` est utilisée pour le logo ou le nom du site
- **Toggle** : `.navbar-toggler` crée le bouton hamburger sur mobile avec `data-bs-toggle="collapse"`
- **Navigation** : `.navbar-nav` contient les liens de navigation principaux
- **Formulaires** : Les formulaires peuvent être intégrés avec `.d-flex` pour un affichage en ligne
- **Couleurs** : Utilisez `.navbar-light` ou `.navbar-dark` selon la couleur d'arrière-plan pour une meilleure lisibilité

## Navigation par onglets

Les onglets sont couramment utilisés dans Moodle pour organiser le contenu en sections.

<div class="component-preview">
    <ul class="nav nav-tabs">
        <li class="nav-item">
            <a class="nav-link active" aria-current="page" href="#">Vue d'ensemble</a>
        </li>
        <li class="nav-item">
            <a class="nav-link" href="#">Participants</a>
        </li>
        <li class="nav-item">
            <a class="nav-link" href="#">Notes</a>
        </li>
        <li class="nav-item">
            <a class="nav-link" href="#">Compétences</a>
        </li>
    </ul>
    <div class="p-3 border border-top-0">
        Contenu de l'onglet actif
    </div>
</div>

```html
<ul class="nav nav-tabs">
  <li class="nav-item">
    <a class="nav-link active" aria-current="page" href="#">Vue d'ensemble</a>
  </li>
  <li class="nav-item">
    <a class="nav-link" href="#">Participants</a>
  </li>
  <li class="nav-item">
    <a class="nav-link" href="#">Notes</a>
  </li>
  <li class="nav-item">
    <a class="nav-link" href="#">Compétences</a>
  </li>
</ul>
<div class="p-3 border border-top-0">
  Contenu de l'onglet actif
</div>
```

### Onglets avec JavaScript

Pour une navigation par onglets pleinement fonctionnelle, utilisez le composant Tab de Bootstrap avec JavaScript.

<div class="component-preview">
    <ul class="nav nav-tabs" id="myTab" role="tablist">
        <li class="nav-item" role="presentation">
            <button class="nav-link active" id="home-tab" data-bs-toggle="tab" data-bs-target="#home-tab-pane" type="button" role="tab" aria-controls="home-tab-pane" aria-selected="true">Accueil</button>
        </li>
        <li class="nav-item" role="presentation">
            <button class="nav-link" id="profile-tab" data-bs-toggle="tab" data-bs-target="#profile-tab-pane" type="button" role="tab" aria-controls="profile-tab-pane" aria-selected="false">Profil</button>
        </li>
        <li class="nav-item" role="presentation">
            <button class="nav-link" id="contact-tab" data-bs-toggle="tab" data-bs-target="#contact-tab-pane" type="button" role="tab" aria-controls="contact-tab-pane" aria-selected="false">Contact</button>
        </li>
    </ul>
    <div class="tab-content" id="myTabContent">
        <div class="tab-pane fade show active p-3 border border-top-0" id="home-tab-pane" role="tabpanel" aria-labelledby="home-tab" tabindex="0">
            <p>Contenu de l'onglet Accueil. Ce contenu apparaît par défaut.</p>
        </div>
        <div class="tab-pane fade p-3 border border-top-0" id="profile-tab-pane" role="tabpanel" aria-labelledby="profile-tab" tabindex="0">
            <p>Contenu de l'onglet Profil. Ce contenu apparaît lorsque l'onglet Profil est activé.</p>
        </div>
        <div class="tab-pane fade p-3 border border-top-0" id="contact-tab-pane" role="tabpanel" aria-labelledby="contact-tab" tabindex="0">
            <p>Contenu de l'onglet Contact. Ce contenu apparaît lorsque l'onglet Contact est activé.</p>
        </div>
    </div>
</div>

```html
<ul class="nav nav-tabs" id="myTab" role="tablist">
  <li class="nav-item" role="presentation">
    <button class="nav-link active" id="home-tab" data-bs-toggle="tab" data-bs-target="#home-tab-pane" type="button" role="tab" aria-controls="home-tab-pane" aria-selected="true">Accueil</button>
  </li>
  <li class="nav-item" role="presentation">
    <button class="nav-link" id="profile-tab" data-bs-toggle="tab" data-bs-target="#profile-tab-pane" type="button" role="tab" aria-controls="profile-tab-pane" aria-selected="false">Profil</button>
  </li>
  <li class="nav-item" role="presentation">
    <button class="nav-link" id="contact-tab" data-bs-toggle="tab" data-bs-target="#contact-tab-pane" type="button" role="tab" aria-controls="contact-tab-pane" aria-selected="false">Contact</button>
  </li>
</ul>
<div class="tab-content" id="myTabContent">
  <div class="tab-pane fade show active p-3 border border-top-0" id="home-tab-pane" role="tabpanel" aria-labelledby="home-tab" tabindex="0">
    <p>Contenu de l'onglet Accueil. Ce contenu apparaît par défaut.</p>
  </div>
  <div class="tab-pane fade p-3 border border-top-0" id="profile-tab-pane" role="tabpanel" aria-labelledby="profile-tab" tabindex="0">
    <p>Contenu de l'onglet Profil. Ce contenu apparaît lorsque l'onglet Profil est activé.</p>
  </div>
  <div class="tab-pane fade p-3 border border-top-0" id="contact-tab-pane" role="tabpanel" aria-labelledby="contact-tab" tabindex="0">
    <p>Contenu de l'onglet Contact. Ce contenu apparaît lorsque l'onglet Contact est activé.</p>
  </div>
</div>
```

## Navigation par pilules

Les pilules (pills) offrent une alternative aux onglets, avec un style différent mais une fonctionnalité similaire.

<div class="component-preview">
    <ul class="nav nav-pills">
        <li class="nav-item">
            <a class="nav-link active" aria-current="page" href="#">Actif</a>
        </li>
        <li class="nav-item">
            <a class="nav-link" href="#">Lien</a>
        </li>
        <li class="nav-item">
            <a class="nav-link" href="#">Lien</a>
        </li>
        <li class="nav-item">
            <a class="nav-link disabled">Désactivé</a>
        </li>
    </ul>
</div>

```html
<ul class="nav nav-pills">
  <li class="nav-item">
    <a class="nav-link active" aria-current="page" href="#">Actif</a>
  </li>
  <li class="nav-item">
    <a class="nav-link" href="#">Lien</a>
  </li>
  <li class="nav-item">
    <a class="nav-link" href="#">Lien</a>
  </li>
  <li class="nav-item">
    <a class="nav-link disabled">Désactivé</a>
  </li>
</ul>
```

### Pilules avec contenu

Tout comme les onglets, les pilules peuvent être utilisées avec le système d'onglets de Bootstrap.

<div class="component-preview">
    <ul class="nav nav-pills mb-3" id="pills-tab" role="tablist">
        <li class="nav-item" role="presentation">
            <button class="nav-link active" id="pills-home-tab" data-bs-toggle="pill" data-bs-target="#pills-home" type="button" role="tab" aria-controls="pills-home" aria-selected="true">Accueil</button>
        </li>
        <li class="nav-item" role="presentation">
            <button class="nav-link" id="pills-profile-tab" data-bs-toggle="pill" data-bs-target="#pills-profile" type="button" role="tab" aria-controls="pills-profile" aria-selected="false">Profil</button>
        </li>
        <li class="nav-item" role="presentation">
            <button class="nav-link" id="pills-contact-tab" data-bs-toggle="pill" data-bs-target="#pills-contact" type="button" role="tab" aria-controls="pills-contact" aria-selected="false">Contact</button>
        </li>
    </ul>
    <div class="tab-content" id="pills-tabContent">
        <div class="tab-pane fade show active p-3 border rounded" id="pills-home" role="tabpanel" aria-labelledby="pills-home-tab" tabindex="0">
            Contenu de l'onglet Accueil en pilule.
        </div>
        <div class="tab-pane fade p-3 border rounded" id="pills-profile" role="tabpanel" aria-labelledby="pills-profile-tab" tabindex="0">
            Contenu de l'onglet Profil en pilule.
        </div>
        <div class="tab-pane fade p-3 border rounded" id="pills-contact" role="tabpanel" aria-labelledby="pills-contact-tab" tabindex="0">
            Contenu de l'onglet Contact en pilule.
        </div>
    </div>
</div>

```html
<ul class="nav nav-pills mb-3" id="pills-tab" role="tablist">
  <li class="nav-item" role="presentation">
    <button class="nav-link active" id="pills-home-tab" data-bs-toggle="pill" data-bs-target="#pills-home" type="button" role="tab" aria-controls="pills-home" aria-selected="true">Accueil</button>
  </li>
  <li class="nav-item" role="presentation">
    <button class="nav-link" id="pills-profile-tab" data-bs-toggle="pill" data-bs-target="#pills-profile" type="button" role="tab" aria-controls="pills-profile" aria-selected="false">Profil</button>
  </li>
  <li class="nav-item" role="presentation">
    <button class="nav-link" id="pills-contact-tab" data-bs-toggle="pill" data-bs-target="#pills-contact" type="button" role="tab" aria-controls="pills-contact" aria-selected="false">Contact</button>
  </li>
</ul>
<div class="tab-content" id="pills-tabContent">
  <div class="tab-pane fade show active p-3 border rounded" id="pills-home" role="tabpanel" aria-labelledby="pills-home-tab" tabindex="0">
    Contenu de l'onglet Accueil en pilule.
  </div>
  <div class="tab-pane fade p-3 border rounded" id="pills-profile" role="tabpanel" aria-labelledby="pills-profile-tab" tabindex="0">
    Contenu de l'onglet Profil en pilule.
  </div>
  <div class="tab-pane fade p-3 border rounded" id="pills-contact" role="tabpanel" aria-labelledby="pills-contact-tab" tabindex="0">
    Contenu de l'onglet Contact en pilule.
  </div>
</div>
```

## Fil d'Ariane (Breadcrumb)

Le fil d'Ariane est essentiel dans Moodle pour naviguer dans la hiérarchie des cours et activités.

<div class="component-preview">
    <nav aria-label="breadcrumb">
        <ol class="breadcrumb">
            <li class="breadcrumb-item"><a href="#">Accueil</a></li>
            <li class="breadcrumb-item"><a href="#">Catégorie</a></li>
            <li class="breadcrumb-item"><a href="#">Cours</a></li>
            <li class="breadcrumb-item active" aria-current="page">Activité</li>
        </ol>
    </nav>
</div>

```html
<nav aria-label="breadcrumb">
  <ol class="breadcrumb">
    <li class="breadcrumb-item"><a href="#">Accueil</a></li>
    <li class="breadcrumb-item"><a href="#">Catégorie</a></li>
    <li class="breadcrumb-item"><a href="#">Cours</a></li>
    <li class="breadcrumb-item active" aria-current="page">Activité</li>
  </ol>
</nav>
```

## Utilisation dans Moodle

### Template Mustache pour la navigation principale

```html
{{#primarynav}}
<nav class="navbar navbar-expand-lg navbar-light bg-light">
  <div class="container-fluid">
    {{#logo}}
    <a class="navbar-brand" href="{{{url}}}">
      <img src="{{{logourl}}}" alt="{{sitename}}">
    </a>
    {{/logo}}
    <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarNavDropdown" aria-controls="navbarNavDropdown" aria-expanded="false" aria-label="{{#str}}togglenavigation{{/str}}">
      <span class="navbar-toggler-icon"></span>
    </button>
    <div class="collapse navbar-collapse" id="navbarNavDropdown">
      <ul class="navbar-nav">
        {{#items}}
        <li class="nav-item {{#haschildren}}dropdown{{/haschildren}}">
          <a class="nav-link {{#haschildren}}dropdown-toggle{{/haschildren}} {{#active}}active{{/active}}"
             href="{{{url}}}"
             {{#haschildren}}data-bs-toggle="dropdown"{{/haschildren}}
             {{#active}}aria-current="page"{{/active}}>
            {{{text}}}
          </a>
          {{#haschildren}}
          <ul class="dropdown-menu">
            {{#children}}
            <li><a class="dropdown-item" href="{{{url}}}">{{{text}}}</a></li>
            {{/children}}
          </ul>
          {{/haschildren}}
        </li>
        {{/items}}
      </ul>
    </div>
  </div>
</nav>
{{/primarynav}}
```

### Gestion des sous-menus imbriqués

Pour les menus multiniveaux, Moodle peut utiliser cette structure :

```html
{{#haschildren}}
<ul class="dropdown-menu">
  {{#children}}
  <li>
    {{^haschildren}}
    <a class="dropdown-item" href="{{{url}}}">{{{text}}}</a>
    {{/haschildren}}
    {{#haschildren}}
    <a class="dropdown-item dropdown-toggle" href="#" data-bs-toggle="dropdown">{{{text}}}</a>
    <ul class="dropdown-menu dropdown-submenu">
      {{#children}}
      <li><a class="dropdown-item" href="{{{url}}}">{{{text}}}</a></li>
      {{/children}}
    </ul>
    {{/haschildren}}
  </li>
  {{/children}}
</ul>
{{/haschildren}}
```

### Support multilingue

Moodle utilise les chaînes de langue pour la traduction :

```html
<button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarNavDropdown"
  aria-controls="navbarNavDropdown" aria-expanded="false" aria-label="{{#str}}togglenavigation{{/str}}">
  <span class="navbar-toggler-icon"></span>
</button>
```

## Accessibilité

Pour une navigation accessible, suivez ces bonnes pratiques :

- Utilisez l'élément `<nav>` avec `aria-label` pour identifier la navigation
- Ajoutez `aria-current="page"` sur le lien actif pour indiquer la page courante
- Incluez `aria-controls`, `aria-expanded` et `aria-label` pour les boutons de menu mobile
- Assurez-vous que tous les menus sont navigables au clavier (avec Tab et Entrée)
- Pour les menus déroulants, utilisez les attributs ARIA appropriés : `aria-haspopup`, `aria-expanded`

### Attributs ARIA requis

```html
<!-- Pour le bouton hamburger -->
<button aria-controls="navbarNavDropdown" aria-expanded="false" aria-label="Afficher/Masquer la navigation">

<!-- Pour les menus déroulants -->
<a aria-expanded="false" aria-haspopup="true">

<!-- Pour les onglets -->
<button role="tab" aria-selected="true" aria-controls="tab-content-id">
```

## Personnalisation

### Variables CSS

```css
/* Variables pour les liens de navigation */
--bs-nav-link-padding-x: 1rem;
--bs-nav-link-padding-y: 0.5rem;
--bs-nav-link-color: var(--bs-link-color);
--bs-nav-link-hover-color: var(--bs-link-hover-color);

/* Variables pour les onglets */
--bs-nav-tabs-border-color: var(--bs-border-color);
--bs-nav-tabs-link-active-color: var(--bs-emphasis-color);
--bs-nav-tabs-link-active-bg: var(--bs-body-bg);

/* Variables pour les pilules */
--bs-nav-pills-link-active-color: #fff;
--bs-nav-pills-link-active-bg: var(--bs-primary);

/* Variables pour le fil d'Ariane */
--bs-breadcrumb-padding-x: 0;
--bs-breadcrumb-padding-y: 0;
--bs-breadcrumb-margin-bottom: 1rem;
--bs-breadcrumb-divider-color: var(--bs-secondary-color);
--bs-breadcrumb-item-padding-x: 0.5rem;
--bs-breadcrumb-item-active-color: var(--bs-secondary-color);
```

### Variables Sass

```scss
/* Navbar */
$navbar-padding-y: $spacer * .5;
$navbar-padding-x: null;
$navbar-brand-padding-y: $nav-link-padding-y;
$navbar-brand-margin-end: 1rem;
$navbar-brand-font-size: $font-size-lg;
$navbar-toggler-padding-y: .25rem;
$navbar-toggler-padding-x: .75rem;
$navbar-toggler-border-radius: $btn-border-radius;

/* Nav */
$nav-link-padding-y: .5rem;
$nav-link-padding-x: 1rem;
$nav-link-font-weight: null;
$nav-link-color: var(--#{$prefix}link-color);
$nav-link-hover-color: var(--#{$prefix}link-hover-color);
$nav-link-disabled-color: var(--#{$prefix}secondary-color);

/* Breadcrumbs */
$breadcrumb-padding-y: 0;
$breadcrumb-padding-x: 0;
$breadcrumb-item-padding-x: .5rem;
$breadcrumb-margin-bottom: 1rem;
$breadcrumb-divider: quote("/");
$breadcrumb-divider-flipped: $breadcrumb-divider;
$breadcrumb-item-active-color: var(--#{$prefix}secondary-color);
```