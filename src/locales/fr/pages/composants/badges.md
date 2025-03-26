---
title: Badges
description: Documentation du composant Badges de Bootstrap 5 pour Moodle
template: pages/composant.html
---

<div class="container py-4">
  <div class="row">
    <div class="col-lg-3">
      <nav id="navbar-example3" class="h-100 flex-column align-items-stretch pe-4 border-end">
        <nav class="nav nav-pills flex-column">
          <a class="nav-link" href="#description">Description</a>
          <a class="nav-link" href="#exemple-base">Exemple de base</a>
          <a class="nav-link" href="#styles">Styles</a>
          <a class="nav-link" href="#utilisation-moodle">Utilisation dans Moodle</a>
          <a class="nav-link" href="#accessibilite">Accessibilité</a>
        </nav>
      </nav>
    </div>

    <div class="col-lg-9">
      <div data-bs-spy="scroll" data-bs-target="#navbar-example3" data-bs-smooth-scroll="true" class="scrollspy-example-2" tabindex="0">
        <div id="description">
          <h2>Description</h2>
          <p class="lead">Les badges sont des composants visuels qui permettent d'afficher de courtes informations, comme des notifications, des statuts ou des compteurs. Ils sont idéaux pour attirer l'attention sur des éléments importants.</p>
        </div>

        <div id="exemple-base" class="mt-5">
          <h2>Exemple de base</h2>
          <p>Un badge simple avec un texte.</p>
          <div class="card mb-4">
            <div class="card-body">
              <div class="component-preview">
                <span class="badge bg-primary">Nouveau</span>
              </div>
            </div>
          </div>
        </div>

        <div id="styles" class="mt-5">
          <h2>Styles</h2>

          <div class="card mb-4">
            <div class="card-body">
              <h3 class="h5">Badges avec couleurs</h3>
              <p>Les badges peuvent avoir différentes couleurs selon leur contexte.</p>
              <div class="component-preview">
                <span class="badge bg-primary">Primaire</span>
                <span class="badge bg-secondary">Secondaire</span>
                <span class="badge bg-success">Succès</span>
                <span class="badge bg-danger">Danger</span>
                <span class="badge bg-warning">Avertissement</span>
                <span class="badge bg-info">Info</span>
                <span class="badge bg-light">Clair</span>
                <span class="badge bg-dark">Sombre</span>
              </div>
            </div>
          </div>

          <div class="card mb-4">
            <div class="card-body">
              <h3 class="h5">Badges avec coins arrondis</h3>
              <p>Les badges peuvent avoir différents styles de coins arrondis.</p>
              <div class="component-preview">
                <span class="badge rounded-pill bg-primary">Pilule</span>
                <span class="badge rounded-3 bg-primary">Arrondi</span>
                <span class="badge rounded-0 bg-primary">Carré</span>
              </div>
            </div>
          </div>

          <div class="card mb-4">
            <div class="card-body">
              <h3 class="h5">Badges avec icônes</h3>
              <p>Les badges peuvent inclure des icônes.</p>
              <div class="component-preview">
                <span class="badge bg-primary">
                  <i class="bi bi-bell"></i> Notification
                </span>
                <span class="badge bg-success">
                  <i class="bi bi-check-circle"></i> Complété
                </span>
                <span class="badge bg-warning">
                  <i class="bi bi-exclamation-triangle"></i> Attention
                </span>
              </div>
            </div>
          </div>

          <div class="card mb-4">
            <div class="card-body">
              <h3 class="h5">Badges dans différents contextes</h3>
              <p>Les badges peuvent être utilisés dans différents contextes.</p>
              <div class="component-preview">
                <button class="btn btn-primary">
                  Messages
                  <span class="badge bg-light text-dark">3</span>
                </button>
                <div class="mt-3">
                  <h5>Titre avec badge <span class="badge bg-secondary">Beta</span></h5>
                  <p>Texte avec badge <span class="badge bg-info">Important</span></p>
                </div>
              </div>
            </div>
          </div>
        </div>

        <div id="utilisation-moodle" class="mt-5">
          <h2>Utilisation dans Moodle</h2>
          <p>Dans Moodle, les badges sont utilisés pour :</p>
          <ul class="list-group mb-4">
            <li class="list-group-item">Afficher des notifications</li>
            <li class="list-group-item">Indiquer le statut des activités</li>
            <li class="list-group-item">Montrer les niveaux de progression</li>
            <li class="list-group-item">Signaler des mises à jour</li>
            <li class="list-group-item">Identifier des fonctionnalités nouvelles</li>
          </ul>

          <div class="card mb-4">
            <div class="card-body">
              <h3 class="h5">Exemple d'intégration dans un template Moodle</h3>
              <pre class="bg-light p-3 rounded"><code>{{#badge}}
    &lt;span class="badge {{#rounded}}rounded-{{rounded}}{{/rounded}} {{#color}}bg-{{color}}{{/color}}"&gt;
        {{#icon}}
        &lt;i class="bi bi-{{icon}}"&gt;&lt;/i&gt;
        {{/icon}}
        {{text}}
    &lt;/span&gt;
{{/badge}}</code></pre>
            </div>
          </div>
        </div>

        <div id="accessibilite" class="mt-5">
          <h2>Accessibilité</h2>
          <ul class="list-group mb-4">
            <li class="list-group-item">Fournissez un texte descriptif pour les badges</li>
            <li class="list-group-item">Maintenez un contraste suffisant</li>
            <li class="list-group-item">Utilisez les badges de manière cohérente</li>
            <li class="list-group-item">Assurez-vous que les badges sont accessibles au clavier</li>
          </ul>
        </div>
      </div>
    </div>
  </div>
</div>

## Variables CSS personnalisables

Les badges utilisent des variables CSS locales sur `.badge` pour une personnalisation améliorée :

```scss
--#{$prefix}badge-padding-x: #{$badge-padding-x};
--#{$prefix}badge-padding-y: #{$badge-padding-y};
--#{$prefix}badge-font-size: #{$badge-font-size};
--#{$prefix}badge-font-weight: #{$badge-font-weight};
--#{$prefix}badge-color: #{$badge-color};
--#{$prefix}badge-border-radius: #{$badge-border-radius};
```

## Variables Sass

Les badges peuvent être personnalisés via les variables Sass suivantes :

```scss
$badge-font-size:                   .75em;
$badge-font-weight:                 $font-weight-bold;
$badge-color:                       $white;
$badge-padding-y:                   .35em;
$badge-padding-x:                   .65em;
$badge-border-radius:               var(--#{$prefix}border-radius);
```