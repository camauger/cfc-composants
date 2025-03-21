---
title: Boutons
description: Documentation du composant Boutons de Bootstrap 5 pour Moodle
template: pages/composant.html
---

Les boutons de Bootstrap permettent aux utilisateurs d'effectuer des actions et de faire des choix avec un simple clic. Ils supportent plusieurs tailles, états et variations.

## Exemples de base

Les boutons de base de Bootstrap incluent plusieurs styles prédéfinis pour différents contextes.

<div class="preview-tabs">
    <div class="preview-tabs-headers">
        <button class="preview-tab-header active">Aperçu</button>
        <button class="preview-tab-header">Code</button>
    </div>
    <div class="preview-tab-content">
        <div class="component-preview">
            <button type="button" class="btn btn-primary">Primary</button>
            <button type="button" class="btn btn-secondary">Secondary</button>
            <button type="button" class="btn btn-success">Success</button>
            <button type="button" class="btn btn-danger">Danger</button>
            <button type="button" class="btn btn-warning">Warning</button>
            <button type="button" class="btn btn-info">Info</button>
            <button type="button" class="btn btn-light">Light</button>
            <button type="button" class="btn btn-dark">Dark</button>
            <button type="button" class="btn btn-link">Link</button>
        </div>
    </div>
    <div class="preview-tab-content">
        ```html
        <button type="button" class="btn btn-primary">Primary</button>
        <button type="button" class="btn btn-secondary">Secondary</button>
        <button type="button" class="btn btn-success">Success</button>
        <button type="button" class="btn btn-danger">Danger</button>
        <button type="button" class="btn btn-warning">Warning</button>
        <button type="button" class="btn btn-info">Info</button>
        <button type="button" class="btn btn-light">Light</button>
        <button type="button" class="btn btn-dark">Dark</button>
        <button type="button" class="btn btn-link">Link</button>
        ```
    </div>
</div>

## Styles de boutons

### Boutons avec contour

Utilisez les boutons avec contour pour une alternative moins prononcée.

<div class="preview-tabs">
    <div class="preview-tabs-headers">
        <button class="preview-tab-header active">Aperçu</button>
        <button class="preview-tab-header">Code</button>
    </div>
    <div class="preview-tab-content">
        <div class="component-preview">
            <button type="button" class="btn btn-outline-primary">Primary</button>
            <button type="button" class="btn btn-outline-secondary">Secondary</button>
            <button type="button" class="btn btn-outline-success">Success</button>
            <button type="button" class="btn btn-outline-danger">Danger</button>
        </div>
    </div>
    <div class="preview-tab-content">
        ```html
        <button type="button" class="btn btn-outline-primary">Primary</button>
        <button type="button" class="btn btn-outline-secondary">Secondary</button>
        <button type="button" class="btn btn-outline-success">Success</button>
        <button type="button" class="btn btn-outline-danger">Danger</button>
        ```
    </div>
</div>

### Tailles de boutons

Utilisez `.btn-lg` ou `.btn-sm` pour des boutons plus grands ou plus petits.

<div class="preview-tabs">
    <div class="preview-tabs-headers">
        <button class="preview-tab-header active">Aperçu</button>
        <button class="preview-tab-header">Code</button>
    </div>
    <div class="preview-tab-content">
        <div class="component-preview">
            <button type="button" class="btn btn-primary btn-lg">Grand bouton</button>
            <button type="button" class="btn btn-primary">Bouton normal</button>
            <button type="button" class="btn btn-primary btn-sm">Petit bouton</button>
        </div>
    </div>
    <div class="preview-tab-content">
        ```html
        <button type="button" class="btn btn-primary btn-lg">Grand bouton</button>
        <button type="button" class="btn btn-primary">Bouton normal</button>
        <button type="button" class="btn btn-primary btn-sm">Petit bouton</button>
        ```
    </div>
</div>

## États des boutons

### Boutons désactivés

Ajoutez l'attribut `disabled` pour désactiver un bouton.

<div class="preview-tabs">
    <div class="preview-tabs-headers">
        <button class="preview-tab-header active">Aperçu</button>
        <button class="preview-tab-header">Code</button>
    </div>
    <div class="preview-tab-content">
        <div class="component-preview">
            <button type="button" class="btn btn-primary" disabled>Bouton désactivé</button>
            <button type="button" class="btn btn-outline-primary" disabled>Bouton désactivé</button>
        </div>
    </div>
    <div class="preview-tab-content">
        ```html
        <button type="button" class="btn btn-primary" disabled>Bouton désactivé</button>
        <button type="button" class="btn btn-outline-primary" disabled>Bouton désactivé</button>
        ```
    </div>
</div>

### Boutons avec chargement

Utilisez `data-bs-toggle="button"` pour créer un bouton à bascule.

<div class="preview-tabs">
    <div class="preview-tabs-headers">
        <button class="preview-tab-header active">Aperçu</button>
        <button class="preview-tab-header">Code</button>
    </div>
    <div class="preview-tab-content">
        <div class="component-preview">
            <button type="button" class="btn btn-primary" disabled>
                <span class="spinner-border spinner-border-sm" role="status" aria-hidden="true"></span>
                Chargement...
            </button>
        </div>
    </div>
    <div class="preview-tab-content">
        ```html
        <button type="button" class="btn btn-primary" disabled>
            <span class="spinner-border spinner-border-sm" role="status" aria-hidden="true"></span>
            Chargement...
        </button>
        ```
    </div>
</div>

## Utilisation dans Moodle

Dans Moodle, les boutons sont utilisés pour :

- Actions principales dans les formulaires (Enregistrer, Annuler)
- Navigation entre les sections
- Actions sur les activités et ressources
- Contrôles de workflow (Suivant, Précédent)
- Actions de gestion (Modifier, Supprimer)

### Exemple d'intégration dans un template Moodle

```php
{{#primary_action}}
    <button type="submit" class="btn btn-primary">
        {{#pix}}i/checkmark{{/pix}}
        {{#str}}save, core{{/str}}
    </button>
{{/primary_action}}
```

## Variables CSS personnalisables

Les boutons utilisent des variables CSS locales pour une personnalisation améliorée :

```scss
--#{$prefix}btn-padding-x: #{$btn-padding-x};
--#{$prefix}btn-padding-y: #{$btn-padding-y};
--#{$prefix}btn-font-size: #{$btn-font-size};
--#{$prefix}btn-font-weight: #{$btn-font-weight};
--#{$prefix}btn-line-height: #{$btn-line-height};
--#{$prefix}btn-color: #{$btn-color};
--#{$prefix}btn-bg: transparent;
--#{$prefix}btn-border-width: #{$btn-border-width};
--#{$prefix}btn-border-color: transparent;
--#{$prefix}btn-border-radius: #{$btn-border-radius};
--#{$prefix}btn-hover-border-color: transparent;
--#{$prefix}btn-box-shadow: #{$btn-box-shadow};
--#{$prefix}btn-disabled-opacity: #{$btn-disabled-opacity};
--#{$prefix}btn-focus-box-shadow: #{$btn-focus-box-shadow};
```

## Variables Sass

Les boutons peuvent être personnalisés via les variables Sass suivantes :

```scss
$btn-padding-y:               $input-btn-padding-y;
$btn-padding-x:               $input-btn-padding-x;
$btn-font-size:               $input-btn-font-size;
$btn-line-height:             $input-btn-line-height;
$btn-white-space:             null;
$btn-font-weight:             $font-weight-normal;
$btn-padding-y-sm:            $input-btn-padding-y-sm;
$btn-padding-x-sm:            $input-btn-padding-x-sm;
$btn-font-size-sm:            $input-btn-font-size-sm;
$btn-padding-y-lg:            $input-btn-padding-y-lg;
$btn-padding-x-lg:            $input-btn-padding-x-lg;
$btn-font-size-lg:            $input-btn-font-size-lg;
```

## Accessibilité

- Utilisez le type de bouton approprié (`button`, `submit`, `reset`)
- Fournissez des étiquettes descriptives pour les boutons
- Assurez-vous que les boutons sont accessibles au clavier
- Utilisez des contrastes de couleurs suffisants
- Évitez de désactiver les boutons sauf si nécessaire
- Ajoutez des attributs `aria-label` pour les boutons sans texte (icônes)