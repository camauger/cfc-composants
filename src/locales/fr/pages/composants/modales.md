---
title: Modales
description: Documentation sur l'utilisation des fenêtres modales Bootstrap dans Moodle, avec des exemples et des bonnes pratiques.
template: pages/composant.html
---

Les modales sont des boîtes de dialogue qui s'affichent par-dessus le contenu principal pour fournir des informations critiques ou demander une décision à l'utilisateur. Dans Moodle, elles sont particulièrement utiles pour afficher des confirmations, des formulaires courts ou des informations détaillées sans quitter la page courante.

## Fonctionnement

Les modales Bootstrap sont construites avec HTML, CSS et JavaScript. Quelques points importants à noter :

- Les modales sont positionnées au-dessus de tout autre élément de la page
- Le défilement de la page est désactivé lorsqu'une modale est ouverte
- Un seul modal peut être affiché à la fois
- Un clic sur l'arrière-plan ferme automatiquement la modale
- Les modales utilisent `position: fixed`

!!! warning "Accessibilité"
    L'effet d'animation de ce composant dépend de la requête média `prefers-reduced-motion`. Pour une meilleure accessibilité, assurez-vous d'inclure des alternatives pour les utilisateurs naviguant au clavier.

## Exemple de base

=== "Aperçu"
    <div class="bd-example">
      <div class="modal" tabindex="-1">
        <div class="modal-dialog">
          <div class="modal-content">
            <div class="modal-header">
              <h5 class="modal-title">Titre de la modale</h5>
              <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Fermer"></button>
            </div>
            <div class="modal-body">
              <p>Contenu de la modale...</p>
            </div>
            <div class="modal-footer">
              <button type="button" class="btn btn-secondary" data-bs-dismiss="modal">Fermer</button>
              <button type="button" class="btn btn-primary">Enregistrer</button>
            </div>
          </div>
        </div>
      </div>
    </div>

=== "HTML"
    ```html
    <!-- Bouton pour ouvrir la modale -->
    <button type="button" class="btn btn-primary" data-bs-toggle="modal" data-bs-target="#exampleModal">
      Ouvrir la modale
    </button>

    <!-- La modale -->
    <div class="modal fade" id="exampleModal" tabindex="-1" aria-labelledby="exampleModalLabel" aria-hidden="true">
      <div class="modal-dialog">
        <div class="modal-content">
          <div class="modal-header">
            <h5 class="modal-title" id="exampleModalLabel">Titre de la modale</h5>
            <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Fermer"></button>
          </div>
          <div class="modal-body">
            <p>Contenu de la modale...</p>
          </div>
          <div class="modal-footer">
            <button type="button" class="btn btn-secondary" data-bs-dismiss="modal">Fermer</button>
            <button type="button" class="btn btn-primary">Enregistrer</button>
          </div>
        </div>
      </div>
    </div>
    ```

## Utilisation dans Moodle

Dans Moodle, les modales sont souvent utilisées pour :

- Afficher des confirmations avant une action importante
- Présenter des informations détaillées sur un élément
- Afficher des formulaires courts
- Montrer des messages d'aide ou des instructions

### Exemple avec Mustache

```html
{{#modal}}
<div class="modal fade" id="modal-{{uniqid}}" tabindex="-1" role="dialog" aria-labelledby="modal-title-{{uniqid}}">
  <div class="modal-dialog {{#isLarge}}modal-lg{{/isLarge}}" role="document">
    <div class="modal-content">
      <div class="modal-header">
        <h5 class="modal-title" id="modal-title-{{uniqid}}">{{title}}</h5>
        <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="{{#str}}close{{/str}}"></button>
      </div>
      <div class="modal-body">
        {{{body}}}
      </div>
      {{#hasFooter}}
      <div class="modal-footer">
        <button type="button" class="btn btn-secondary" data-bs-dismiss="modal">{{#str}}cancel{{/str}}</button>
        <button type="button" class="btn btn-primary" data-action="save">{{#str}}save{{/str}}</button>
      </div>
      {{/hasFooter}}
    </div>
  </div>
</div>
{{/modal}}
```

### Exemple avec JavaScript

```javascript
// Initialisation de la modale
var myModal = new bootstrap.Modal(document.getElementById('myModal'), {
  keyboard: false
});

// Événements
document.getElementById('myModal').addEventListener('shown.bs.modal', function () {
  document.getElementById('myInput').focus();
});

// Ouvrir la modale
myModal.show();

// Fermer la modale
myModal.hide();
```

## Tailles de modale

Bootstrap propose différentes tailles de modales :

=== "HTML"
    ```html
    <!-- Petite modale -->
    <div class="modal-dialog modal-sm">...</div>

    <!-- Modale par défaut -->
    <div class="modal-dialog">...</div>

    <!-- Grande modale -->
    <div class="modal-dialog modal-lg">...</div>

    <!-- Très grande modale -->
    <div class="modal-dialog modal-xl">...</div>

    <!-- Modale plein écran -->
    <div class="modal-dialog modal-fullscreen">...</div>
    ```

## Personnalisation

### Variables CSS

```css
--bs-modal-padding: 1rem;
--bs-modal-margin: 0.5rem;
--bs-modal-color: ;
--bs-modal-bg: #fff;
--bs-modal-border-color: rgba(0, 0, 0, 0.2);
--bs-modal-border-width: 1px;
--bs-modal-border-radius: 0.5rem;
--bs-modal-box-shadow: 0 0.125rem 0.25rem rgba(0, 0, 0, 0.075);
--bs-modal-inner-border-radius: calc(0.5rem - 1px);
--bs-modal-header-padding-x: 1rem;
--bs-modal-header-padding-y: 1rem;
--bs-modal-header-padding: 1rem;
--bs-modal-header-border-color: var(--bs-border-color);
--bs-modal-header-border-width: 1px;
--bs-modal-title-line-height: 1.5;
--bs-modal-footer-gap: 0.5rem;
--bs-modal-footer-border-color: var(--bs-border-color);
--bs-modal-footer-border-width: 1px;
```

### Variables Sass

```scss
$modal-inner-padding:               $spacer;
$modal-footer-margin-between:       .5rem;
$modal-dialog-margin:               .5rem;
$modal-dialog-margin-y-sm-up:       1.75rem;
$modal-title-line-height:           $line-height-base;
$modal-content-color:               null;
$modal-content-bg:                  $white;
$modal-content-border-color:        rgba($black, .2);
$modal-content-border-width:        $border-width;
$modal-content-border-radius:       $border-radius-lg;
$modal-content-inner-border-radius: subtract($modal-content-border-radius, $modal-content-border-width);
$modal-content-box-shadow-xs:       $box-shadow-sm;
$modal-content-box-shadow-sm-up:    $box-shadow;
$modal-backdrop-bg:                 $black;
$modal-backdrop-opacity:            .5;
$modal-sm:                          300px;
$modal-md:                          500px;
$modal-lg:                          800px;
$modal-xl:                          1140px;
```