---
title: Alertes
description: Documentation du composant Alertes de Bootstrap 5 pour Moodle
template: pages/composant.html
---

Les alertes fournissent des messages de rétroaction contextuels pour les actions typiques des utilisateurs. Bootstrap propose plusieurs styles d'alertes flexibles et personnalisables.

## Exemples de base

<div class="preview-tabs">
    <div class="preview-tabs-headers">
        <button class="preview-tab-header active">Aperçu</button>
        <button class="preview-tab-header">Code</button>
    </div>
    <div class="preview-tab-content">
        <div class="component-preview">
            <div class="alert alert-primary" role="alert">
                Une alerte primaire simple avec <a href="#" class="alert-link">un lien d'exemple</a>.
            </div>
            <div class="alert alert-secondary" role="alert">
                Une alerte secondaire simple avec <a href="#" class="alert-link">un lien d'exemple</a>.
            </div>
            <div class="alert alert-success" role="alert">
                Une alerte succès simple avec <a href="#" class="alert-link">un lien d'exemple</a>.
            </div>
            <div class="alert alert-danger" role="alert">
                Une alerte danger simple avec <a href="#" class="alert-link">un lien d'exemple</a>.
            </div>
            <div class="alert alert-warning" role="alert">
                Une alerte avertissement simple avec <a href="#" class="alert-link">un lien d'exemple</a>.
            </div>
            <div class="alert alert-info" role="alert">
                Une alerte info simple avec <a href="#" class="alert-link">un lien d'exemple</a>.
            </div>
            <div class="alert alert-light" role="alert">
                Une alerte claire simple avec <a href="#" class="alert-link">un lien d'exemple</a>.
            </div>
            <div class="alert alert-dark" role="alert">
                Une alerte sombre simple avec <a href="#" class="alert-link">un lien d'exemple</a>.
            </div>
        </div>
    </div>
    <div class="preview-tab-content">
        ```html
        <div class="alert alert-primary" role="alert">
            Une alerte primaire simple avec <a href="#" class="alert-link">un lien d'exemple</a>.
        </div>
        <div class="alert alert-secondary" role="alert">
            Une alerte secondaire simple avec <a href="#" class="alert-link">un lien d'exemple</a>.
        </div>
        <div class="alert alert-success" role="alert">
            Une alerte succès simple avec <a href="#" class="alert-link">un lien d'exemple</a>.
        </div>
        <div class="alert alert-danger" role="alert">
            Une alerte danger simple avec <a href="#" class="alert-link">un lien d'exemple</a>.
        </div>
        <div class="alert alert-warning" role="alert">
            Une alerte avertissement simple avec <a href="#" class="alert-link">un lien d'exemple</a>.
        </div>
        <div class="alert alert-info" role="alert">
            Une alerte info simple avec <a href="#" class="alert-link">un lien d'exemple</a>.
        </div>
        <div class="alert alert-light" role="alert">
            Une alerte claire simple avec <a href="#" class="alert-link">un lien d'exemple</a>.
        </div>
        <div class="alert alert-dark" role="alert">
            Une alerte sombre simple avec <a href="#" class="alert-link">un lien d'exemple</a>.
        </div>
        ```
    </div>
</div>

## Contenu additionnel

Les alertes peuvent contenir des éléments HTML additionnels comme des en-têtes, des paragraphes et des séparateurs.

<div class="preview-tabs">
    <div class="preview-tabs-headers">
        <button class="preview-tab-header active">Aperçu</button>
        <button class="preview-tab-header">Code</button>
    </div>
    <div class="preview-tab-content">
        <div class="component-preview">
            <div class="alert alert-success" role="alert">
                <h4 class="alert-heading">Bien joué !</h4>
                <p>Vous avez réussi à lire ce message d'alerte important. Ce texte d'exemple va s'exécuter un peu plus longtemps pour que vous puissiez voir comment l'espacement fonctionne avec ce type de contenu.</p>
                <hr>
                <p class="mb-0">Lorsque vous en avez besoin, assurez-vous d'utiliser les utilitaires de marge pour garder les choses bien ordonnées.</p>
            </div>
        </div>
    </div>
    <div class="preview-tab-content">
        ```html
        <div class="alert alert-success" role="alert">
            <h4 class="alert-heading">Bien joué !</h4>
            <p>Vous avez réussi à lire ce message d'alerte important. Ce texte d'exemple va s'exécuter un peu plus longtemps pour que vous puissiez voir comment l'espacement fonctionne avec ce type de contenu.</p>
            <hr>
            <p class="mb-0">Lorsque vous en avez besoin, assurez-vous d'utiliser les utilitaires de marge pour garder les choses bien ordonnées.</p>
        </div>
        ```
    </div>
</div>

## Alertes fermables

Ajoutez la classe `.alert-dismissible` et un bouton de fermeture pour créer une alerte que l'utilisateur peut fermer.

<div class="preview-tabs">
    <div class="preview-tabs-headers">
        <button class="preview-tab-header active">Aperçu</button>
        <button class="preview-tab-header">Code</button>
    </div>
    <div class="preview-tab-content">
        <div class="component-preview">
            <div class="alert alert-warning alert-dismissible fade show" role="alert">
                <strong>Attention !</strong> Vous devriez vérifier certains des champs ci-dessous.
                <button type="button" class="btn-close" data-bs-dismiss="alert" aria-label="Fermer"></button>
            </div>
        </div>
    </div>
    <div class="preview-tab-content">
        ```html
        <div class="alert alert-warning alert-dismissible fade show" role="alert">
            <strong>Attention !</strong> Vous devriez vérifier certains des champs ci-dessous.
            <button type="button" class="btn-close" data-bs-dismiss="alert" aria-label="Fermer"></button>
        </div>
        ```
    </div>
</div>

## Utilisation dans Moodle

Dans Moodle, les alertes sont souvent utilisées pour :

- Afficher des messages de confirmation après une action
- Montrer des erreurs de validation de formulaire
- Présenter des informations importantes aux étudiants
- Afficher des notifications système

### Exemple d'intégration dans un template Moodle

```php
{{#hasalert}}
    <div class="alert alert-{{alerttype}}" role="alert">
        {{{alertmessage}}}
        {{#dismissible}}
            <button type="button" class="btn-close" data-bs-dismiss="alert" aria-label="{{#str}}close, core{{/str}}"></button>
        {{/dismissible}}
    </div>
{{/hasalert}}
```

## Variables Sass personnalisables

Les alertes peuvent être personnalisées via les variables Sass suivantes :

```scss
$alert-padding-y:               $spacer;
$alert-padding-x:               $spacer;
$alert-margin-bottom:           1rem;
$alert-border-radius:           $border-radius;
$alert-link-font-weight:        $font-weight-bold;
$alert-border-width:            $border-width;
$alert-bg-scale:               -80%;
$alert-border-scale:           -70%;
$alert-color-scale:            40%;
$alert-dismissible-padding-r:   $alert-padding-x * 3;
```

## Accessibilité

- Utilisez toujours l'attribut `role="alert"` pour les messages importants
- Pour les alertes fermables, assurez-vous d'inclure un `aria-label` sur le bouton de fermeture
- Utilisez des couleurs avec un contraste suffisant pour le texte et le fond
- Évitez de masquer des informations critiques dans des alertes fermables