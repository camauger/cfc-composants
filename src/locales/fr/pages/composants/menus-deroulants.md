---
title: Menus déroulants
description: Documentation sur l'utilisation des menus déroulants Bootstrap dans Moodle.
template: pages/composant.html
---

Les menus déroulants (dropdowns) sont des composants d'interface qui affichent une liste d'options contextuelles masquées par défaut et révélées par un clic. Dans Moodle, ils sont particulièrement utiles pour proposer des actions sur des éléments, afficher des listes de navigation ou présenter des options dans un espace réduit.

## Exemple basique

Un menu déroulant Bootstrap standard se compose d'un bouton déclencheur et d'une liste d'options.
<div class="component-preview">
  <div class="dropdown">
    <button class="btn btn-primary dropdown-toggle" type="button" data-bs-toggle="dropdown" aria-expanded="false">
      Menu déroulant
    </button>
    <ul class="dropdown-menu">
      <li><a class="dropdown-item" href="#">Action</a></li>
      <li><a class="dropdown-item" href="#">Autre action</a></li>
      <li><a class="dropdown-item" href="#">Quelque chose d'autre</a></li>
    </ul>
  </div>
</div>

## Directions d'ouverture

Vous pouvez contrôler la direction dans laquelle le menu déroulant s'ouvre.

<div class="component-preview">
    <div class="d-flex flex-wrap gap-2">
        <div class="dropdown me-2 mb-2">
            <button class="btn btn-primary dropdown-toggle" type="button" data-bs-toggle="dropdown" aria-expanded="false">
                Vers le bas
            </button>
            <ul class="dropdown-menu">
                <li><a class="dropdown-item" href="#">Action</a></li>
                <li><a class="dropdown-item" href="#">Autre action</a></li>
                <li><a class="dropdown-item" href="#">Quelque chose d'autre</a></li>
            </ul>
        </div>
    <div class="dropup me-2 mb-2">
            <button class="btn btn-primary dropdown-toggle" type="button" data-bs-toggle="dropdown" aria-expanded="false">
                Vers le haut
            </button>
            <ul class="dropdown-menu">
                <li><a class="dropdown-item" href="#">Action</a></li>
                <li><a class="dropdown-item" href="#">Autre action</a></li>
                <li><a class="dropdown-item" href="#">Quelque chose d'autre</a></li>
            </ul>
        </div>
     <div class="dropend me-2 mb-2">
            <button class="btn btn-primary dropdown-toggle" type="button" data-bs-toggle="dropdown" aria-expanded="false">
                Vers la droite
            </button>
            <ul class="dropdown-menu">
                <li><a class="dropdown-item" href="#">Action</a></li>
                <li><a class="dropdown-item" href="#">Autre action</a></li>
                <li><a class="dropdown-item" href="#">Quelque chose d'autre</a></li>
            </ul>
        </div>
      <div class="dropstart mb-2">
            <button class="btn btn-primary dropdown-toggle" type="button" data-bs-toggle="dropdown" aria-expanded="false">
                Vers la gauche
            </button>
            <ul class="dropdown-menu">
                <li><a class="dropdown-item" href="#">Action</a></li>
                <li><a class="dropdown-item" href="#">Autre action</a></li>
                <li><a class="dropdown-item" href="#">Quelque chose d'autre</a></li>
            </ul>
        </div>
    </div>
</div>

```html
<!-- Menu vers le bas (défaut) -->
<div class="dropdown">
    <button class="btn btn-primary dropdown-toggle" type="button" data-bs-toggle="dropdown" aria-expanded="false">
        Vers le bas
    </button>
    <ul class="dropdown-menu">
        <li><a class="dropdown-item" href="#">Action</a></li>
        <li><a class="dropdown-item" href="#">Autre action</a></li>
        <li><a class="dropdown-item" href="#">Quelque chose d'autre</a></li>
    </ul>
</div>

<!-- Menu vers le haut -->
<div class="dropup">
    <button class="btn btn-primary dropdown-toggle" type="button" data-bs-toggle="dropdown" aria-expanded="false">
        Vers le haut
    </button>
    <ul class="dropdown-menu">
        <li><a class="dropdown-item" href="#">Action</a></li>
        <li><a class="dropdown-item" href="#">Autre action</a></li>
        <li><a class="dropdown-item" href="#">Quelque chose d'autre</a></li>
    </ul>
</div>

<!-- Menu vers la droite -->
<div class="dropend">
    <button class="btn btn-primary dropdown-toggle" type="button" data-bs-toggle="dropdown" aria-expanded="false">
        Vers la droite
    </button>
    <ul class="dropdown-menu">
        <li><a class="dropdown-item" href="#">Action</a></li>
        <li><a class="dropdown-item" href="#">Autre action</a></li>
        <li><a class="dropdown-item" href="#">Quelque chose d'autre</a></li>
    </ul>
</div>

<!-- Menu vers la gauche -->
<div class="dropstart">
    <button class="btn btn-primary dropdown-toggle" type="button" data-bs-toggle="dropdown" aria-expanded="false">
        Vers la gauche
    </button>
    <ul class="dropdown-menu">
        <li><a class="dropdown-item" href="#">Action</a></li>
        <li><a class="dropdown-item" href="#">Autre action</a></li>
        <li><a class="dropdown-item" href="#">Quelque chose d'autre</a></li>
    </ul>
</div>
```

## Menu structuré

Vous pouvez structurer vos menus déroulants avec des en-têtes et des séparateurs pour une meilleure organisation.

<div class="component-preview">
    <div class="dropdown">
        <button class="btn btn-secondary dropdown-toggle" type="button" data-bs-toggle="dropdown" aria-expanded="false">
            Menu structuré
        </button>
        <ul class="dropdown-menu">
            <li><h6 class="dropdown-header">Groupe d'actions 1</h6></li>
            <li><a class="dropdown-item" href="#">Action</a></li>
            <li><a class="dropdown-item" href="#">Autre action</a></li>
            <li><hr class="dropdown-divider"></li>
            <li><h6 class="dropdown-header">Groupe d'actions 2</h6></li>
            <li><a class="dropdown-item" href="#">Action séparée</a></li>
        </ul>
    </div>
</div>

```html
<div class="dropdown">
  <button class="btn btn-secondary dropdown-toggle" type="button" data-bs-toggle="dropdown" aria-expanded="false">
    Menu structuré
  </button>
  <ul class="dropdown-menu">
    <li><h6 class="dropdown-header">Groupe d'actions 1</h6></li>
    <li><a class="dropdown-item" href="#">Action</a></li>
    <li><a class="dropdown-item" href="#">Autre action</a></li>
    <li><hr class="dropdown-divider"></li>
    <li><h6 class="dropdown-header">Groupe d'actions 2</h6></li>
    <li><a class="dropdown-item" href="#">Action séparée</a></li>
  </ul>
</div>
```

## États actifs et désactivés

Vous pouvez indiquer les éléments actifs ou désactiver certaines options.

<div class="component-preview">
    <div class="dropdown">
        <button class="btn btn-primary dropdown-toggle" type="button" data-bs-toggle="dropdown" aria-expanded="false">
            Menu avec états
        </button>
        <ul class="dropdown-menu">
            <li><a class="dropdown-item" href="#">Action régulière</a></li>
            <li><a class="dropdown-item active" href="#" aria-current="true">Action active</a></li>
            <li><a class="dropdown-item disabled" href="#" tabindex="-1" aria-disabled="true">Action désactivée</a></li>
        </ul>
    </div>
</div>

```html
<div class="dropdown">
  <button class="btn btn-primary dropdown-toggle" type="button" data-bs-toggle="dropdown" aria-expanded="false">
    Menu avec états
  </button>
  <ul class="dropdown-menu">
    <li><a class="dropdown-item" href="#">Action régulière</a></li>
    <li><a class="dropdown-item active" href="#" aria-current="true">Action active</a></li>
    <li><a class="dropdown-item disabled" href="#" tabindex="-1" aria-disabled="true">Action désactivée</a></li>
  </ul>
</div>
```

## Alignement

Vous pouvez aligner le menu à droite en utilisant la classe `.dropdown-menu-end`.

<div class="component-preview">
    <div class="dropdown">
        <button class="btn btn-secondary dropdown-toggle" type="button" data-bs-toggle="dropdown" aria-expanded="false">
            Menu aligné à droite
        </button>
        <ul class="dropdown-menu dropdown-menu-end">
            <li><a class="dropdown-item" href="#">Action</a></li>
            <li><a class="dropdown-item" href="#">Autre action</a></li>
            <li><a class="dropdown-item" href="#">Quelque chose d'autre</a></li>
        </ul>
    </div>
</div>

```html
<div class="dropdown">
  <button class="btn btn-secondary dropdown-toggle" type="button" data-bs-toggle="dropdown" aria-expanded="false">
    Menu aligné à droite
  </button>
  <ul class="dropdown-menu dropdown-menu-end">
    <li><a class="dropdown-item" href="#">Action</a></li>
    <li><a class="dropdown-item" href="#">Autre action</a></li>
    <li><a class="dropdown-item" href="#">Quelque chose d'autre</a></li>
  </ul>
</div>
```

## Utilisation avec d'autres composants

### Menu déroulant depuis un bouton split

<div class="component-preview">
    <div class="btn-group">
        <button type="button" class="btn btn-primary">Action</button>
        <button type="button" class="btn btn-primary dropdown-toggle dropdown-toggle-split" data-bs-toggle="dropdown" aria-expanded="false">
            <span class="visually-hidden">Toggle Dropdown</span>
        </button>
        <ul class="dropdown-menu">
            <li><a class="dropdown-item" href="#">Action</a></li>
            <li><a class="dropdown-item" href="#">Autre action</a></li>
            <li><a class="dropdown-item" href="#">Quelque chose d'autre</a></li>
            <li><hr class="dropdown-divider"></li>
            <li><a class="dropdown-item" href="#">Lien séparé</a></li>
        </ul>
    </div>
</div>

```html
<div class="btn-group">
  <button type="button" class="btn btn-primary">Action</button>
  <button type="button" class="btn btn-primary dropdown-toggle dropdown-toggle-split" data-bs-toggle="dropdown" aria-expanded="false">
    <span class="visually-hidden">Toggle Dropdown</span>
  </button>
  <ul class="dropdown-menu">
    <li><a class="dropdown-item" href="#">Action</a></li>
    <li><a class="dropdown-item" href="#">Autre action</a></li>
    <li><a class="dropdown-item" href="#">Quelque chose d'autre</a></li>
    <li><hr class="dropdown-divider"></li>
    <li><a class="dropdown-item" href="#">Lien séparé</a></li>
  </ul>
</div>
```

### Menu déroulant dans la navigation

<div class="component-preview">
    <nav class="navbar navbar-expand-lg navbar-light bg-light">
        <div class="container-fluid">
            <a class="navbar-brand" href="#">Navbar</a>
            <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarNavDropdown" aria-controls="navbarNavDropdown" aria-expanded="false" aria-label="Toggle navigation">
                <span class="navbar-toggler-icon"></span>
            </button>
            <div class="collapse navbar-collapse" id="navbarNavDropdown">
                <ul class="navbar-nav">
                    <li class="nav-item">
                        <a class="nav-link active" aria-current="page" href="#">Accueil</a>
                    </li>
                    <li class="nav-item">
                        <a class="nav-link" href="#">Fonctionnalités</a>
                    </li>
                    <li class="nav-item">
                        <a class="nav-link" href="#">Tarifs</a>
                    </li>
                    <li class="nav-item dropdown">
                        <a class="nav-link dropdown-toggle" href="#" id="navbarDropdownMenuLink" role="button" data-bs-toggle="dropdown" aria-expanded="false">
                            Menu déroulant
                        </a>
                        <ul class="dropdown-menu" aria-labelledby="navbarDropdownMenuLink">
                            <li><a class="dropdown-item" href="#">Action</a></li>
                            <li><a class="dropdown-item" href="#">Autre action</a></li>
                            <li><a class="dropdown-item" href="#">Quelque chose d'autre</a></li>
                        </ul>
                    </li>
                </ul>
            </div>
        </div>
    </nav>
</div>

```html
<nav class="navbar navbar-expand-lg navbar-light bg-light">
  <div class="container-fluid">
    <a class="navbar-brand" href="#">Navbar</a>
    <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarNavDropdown" aria-controls="navbarNavDropdown" aria-expanded="false" aria-label="Toggle navigation">
      <span class="navbar-toggler-icon"></span>
    </button>
    <div class="collapse navbar-collapse" id="navbarNavDropdown">
      <ul class="navbar-nav">
        <li class="nav-item">
          <a class="nav-link active" aria-current="page" href="#">Accueil</a>
        </li>
        <li class="nav-item">
          <a class="nav-link" href="#">Fonctionnalités</a>
        </li>
        <li class="nav-item">
          <a class="nav-link" href="#">Tarifs</a>
        </li>
        <li class="nav-item dropdown">
          <a class="nav-link dropdown-toggle" href="#" id="navbarDropdownMenuLink" role="button" data-bs-toggle="dropdown" aria-expanded="false">
            Menu déroulant
          </a>
          <ul class="dropdown-menu" aria-labelledby="navbarDropdownMenuLink">
            <li><a class="dropdown-item" href="#">Action</a></li>
            <li><a class="dropdown-item" href="#">Autre action</a></li>
            <li><a class="dropdown-item" href="#">Quelque chose d'autre</a></li>
          </ul>
        </li>
      </ul>
    </div>
  </div>
</nav>
```

## Intégration dans Moodle

Pour utiliser les menus déroulants dans Moodle, vous pouvez les intégrer dans vos templates Mustache.

```mustache
{{!
    Exemple de template Mustache pour un menu déroulant
}}
<div class="dropdown">
    <button class="btn btn-secondary dropdown-toggle" type="button" id="dropdownMenuButton" data-bs-toggle="dropdown" aria-expanded="false">
        {{buttonText}}
    </button>
    <ul class="dropdown-menu" aria-labelledby="dropdownMenuButton">
        {{#items}}
            <li><a class="dropdown-item" href="{{url}}">{{text}}</a></li>
        {{/items}}
    </ul>
</div>
```

## Accessibilité

Pour garantir l'accessibilité des menus déroulants :

1. Utilisez toujours l'attribut `aria-expanded` sur l'élément déclencheur
2. Incluez un attribut `aria-labelledby` dans le menu qui fait référence à l'ID du déclencheur
3. Utilisez `tabindex="-1"` et `aria-disabled="true"` pour les éléments désactivés
4. Assurez-vous que les menus sont navigables au clavier