---
title: Badges
description: Documentation du composant Badges de Bootstrap 5 pour Moodle
template: pages/composant.html
---


Les badges sont de petits composants de comptage et d'étiquetage qui peuvent être utilisés pour ajouter des informations supplémentaires à n'importe quel contenu.

## Exemples de base

Les badges s'adaptent automatiquement à la taille de leur parent immédiat en utilisant une taille de police relative et des unités `em`.

<div class="preview-tabs">
    <div class="preview-tabs-headers">
        <button class="preview-tab-header active">Aperçu</button>
        <button class="preview-tab-header">Code</button>
    </div>
    <div class="preview-tab-content">
        <div class="component-preview">
            <h1>Titre exemple <span class="badge bg-secondary">Nouveau</span></h1>
            <h2>Titre exemple <span class="badge bg-secondary">Nouveau</span></h2>
            <h3>Titre exemple <span class="badge bg-secondary">Nouveau</span></h3>
            <h4>Titre exemple <span class="badge bg-secondary">Nouveau</span></h4>
            <h5>Titre exemple <span class="badge bg-secondary">Nouveau</span></h5>
            <h6>Titre exemple <span class="badge bg-secondary">Nouveau</span></h6>
        </div>
    </div>
    <div class="preview-tab-content">
        ```html
        <h1>Titre exemple <span class="badge bg-secondary">Nouveau</span></h1>
        <h2>Titre exemple <span class="badge bg-secondary">Nouveau</span></h2>
        <h3>Titre exemple <span class="badge bg-secondary">Nouveau</span></h3>
        <h4>Titre exemple <span class="badge bg-secondary">Nouveau</span></h4>
        <h5>Titre exemple <span class="badge bg-secondary">Nouveau</span></h5>
        <h6>Titre exemple <span class="badge bg-secondary">Nouveau</span></h6>
        ```
    </div>
</div>

## Couleurs de fond

Utilisez les classes utilitaires de couleur de fond pour modifier l'apparence des badges.

<div class="preview-tabs">
    <div class="preview-tabs-headers">
        <button class="preview-tab-header active">Aperçu</button>
        <button class="preview-tab-header">Code</button>
    </div>
    <div class="preview-tab-content">
        <div class="component-preview">
            <span class="badge bg-primary">Primary</span>
            <span class="badge bg-secondary">Secondary</span>
            <span class="badge bg-success">Success</span>
            <span class="badge bg-danger">Danger</span>
            <span class="badge bg-warning text-dark">Warning</span>
            <span class="badge bg-info text-dark">Info</span>
            <span class="badge bg-light text-dark">Light</span>
            <span class="badge bg-dark">Dark</span>
        </div>
    </div>
    <div class="preview-tab-content">
        ```html
        <span class="badge bg-primary">Primary</span>
        <span class="badge bg-secondary">Secondary</span>
        <span class="badge bg-success">Success</span>
        <span class="badge bg-danger">Danger</span>
        <span class="badge bg-warning text-dark">Warning</span>
        <span class="badge bg-info text-dark">Info</span>
        <span class="badge bg-light text-dark">Light</span>
        <span class="badge bg-dark">Dark</span>
        ```
    </div>
</div>

## Badges arrondis

Ajoutez la classe `.rounded-pill` pour rendre les badges plus arrondis.

<div class="preview-tabs">
    <div class="preview-tabs-headers">
        <button class="preview-tab-header active">Aperçu</button>
        <button class="preview-tab-header">Code</button>
    </div>
    <div class="preview-tab-content">
        <div class="component-preview">
            <span class="badge rounded-pill bg-primary">Primary</span>
            <span class="badge rounded-pill bg-secondary">Secondary</span>
            <span class="badge rounded-pill bg-success">Success</span>
            <span class="badge rounded-pill bg-danger">Danger</span>
        </div>
    </div>
    <div class="preview-tab-content">
        ```html
        <span class="badge rounded-pill bg-primary">Primary</span>
        <span class="badge rounded-pill bg-secondary">Secondary</span>
        <span class="badge rounded-pill bg-success">Success</span>
        <span class="badge rounded-pill bg-danger">Danger</span>
        ```
    </div>
</div>

## Badges avec boutons

Les badges peuvent être utilisés comme compteurs dans les boutons.

<div class="preview-tabs">
    <div class="preview-tabs-headers">
        <button class="preview-tab-header active">Aperçu</button>
        <button class="preview-tab-header">Code</button>
    </div>
    <div class="preview-tab-content">
        <div class="component-preview">
            <button type="button" class="btn btn-primary">
                Notifications <span class="badge bg-secondary">4</span>
            </button>
            <button type="button" class="btn btn-success">
                Messages <span class="badge bg-white text-success">2</span>
            </button>
        </div>
    </div>
    <div class="preview-tab-content">
        ```html
        <button type="button" class="btn btn-primary">
            Notifications <span class="badge bg-secondary">4</span>
        </button>
        <button type="button" class="btn btn-success">
            Messages <span class="badge bg-white text-success">2</span>
        </button>
        ```
    </div>
</div>

## Utilisation dans Moodle

Dans Moodle, les badges sont couramment utilisés pour :

- Indiquer le nombre de messages non lus
- Signaler de nouvelles activités ou ressources
- Afficher le statut d'achèvement des activités
- Montrer le nombre de participants dans un cours
- Indiquer les notes ou évaluations

### Exemple d'intégration dans un template Moodle

```php
{{#hascount}}
    <span class="badge bg-{{type}}">{{count}}</span>
{{/hascount}}
```

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

## Accessibilité

- Utilisez la couleur comme un indicateur visuel supplémentaire, pas comme seule méthode de communication
- Assurez-vous que le contraste entre le texte et l'arrière-plan est suffisant
- Pour les badges qui servent de compteurs, utilisez `aria-label` pour fournir un contexte plus détaillé
- Évitez d'utiliser les badges pour des informations critiques sans autre moyen de communication