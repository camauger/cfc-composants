---
title: Cartes
description: Documentation du composant Cartes de Bootstrap 5 pour Moodle
template: pages/composant.html
---


Les cartes sont des conteneurs de contenu flexibles et extensibles. Elles incluent des options pour les en-têtes et pieds de carte, une grande variété de contenu, des couleurs de fond contextuelles et de puissantes options d'affichage.

## Exemple de base

Une carte basique contient différents éléments de contenu avec une structure claire.

<div class="preview-tabs">
    <div class="preview-tabs-headers">
        <button class="preview-tab-header active">Aperçu</button>
        <button class="preview-tab-header">Code</button>
    </div>
    <div class="preview-tab-content">
        <div class="component-preview">
            <div class="card" style="width: 18rem;">
                <img src="../images/carte-1.jpg" class="card-img-top" alt="Image d'un cours en ligne montrant un étudiant travaillant sur un ordinateur">
                <div class="card-body">
                    <h5 class="card-title">Introduction à la programmation</h5>
                    <p class="card-text">Apprenez les bases de la programmation avec Python. Ce cours couvre les concepts fondamentaux et inclut des exercices pratiques.</p>
                    <a href="#" class="btn btn-primary">Accéder au cours</a>
                </div>
            </div>
        </div>
    </div>
    <div class="preview-tab-content">
        ```html
        <div class="card" style="width: 18rem;">
            <img src="../images/carte-1.jpg" class="card-img-top" alt="Image d'un cours en ligne montrant un étudiant travaillant sur un ordinateur">
            <div class="card-body">
                <h5 class="card-title">Introduction à la programmation</h5>
                <p class="card-text">Apprenez les bases de la programmation avec Python. Ce cours couvre les concepts fondamentaux et inclut des exercices pratiques.</p>
                <a href="#" class="btn btn-primary">Accéder au cours</a>
            </div>
        </div>
        ```
    </div>
</div>

## Composants de carte

### En-tête et pied de carte

Ajoutez un en-tête ou un pied de carte optionnel avec `.card-header` et `.card-footer`.

<div class="preview-tabs">
    <div class="preview-tabs-headers">
        <button class="preview-tab-header active">Aperçu</button>
        <button class="preview-tab-header">Code</button>
    </div>
    <div class="preview-tab-content">
        <div class="component-preview">
            <div class="card">
                <div class="card-header">
                    En-tête de carte
                </div>
                <div class="card-body">
                    <h5 class="card-title">Titre spécial</h5>
                    <p class="card-text">Avec un texte d'accompagnement ci-dessous comme introduction naturelle à un contenu supplémentaire.</p>
                    <a href="#" class="btn btn-primary">Aller quelque part</a>
                </div>
                <div class="card-footer text-muted">
                    Il y a 2 jours
                </div>
            </div>
        </div>
    </div>
    <div class="preview-tab-content">
        ```html
        <div class="card">
            <div class="card-header">
                En-tête de carte
            </div>
            <div class="card-body">
                <h5 class="card-title">Titre spécial</h5>
                <p class="card-text">Avec un texte d'accompagnement ci-dessous comme introduction naturelle à un contenu supplémentaire.</p>
                <a href="#" class="btn btn-primary">Aller quelque part</a>
            </div>
            <div class="card-footer text-muted">
                Il y a 2 jours
            </div>
        </div>
        ```
    </div>
</div>

### Images dans les cartes

Les cartes incluent des variantes pour les images en haut, en bas ou en arrière-plan.

<div class="preview-tabs">
    <div class="preview-tabs-headers">
        <button class="preview-tab-header active">Aperçu</button>
        <button class="preview-tab-header">Code</button>
    </div>
    <div class="preview-tab-content">
        <div class="component-preview">
            <div class="row">
                <div class="col-md-4">
                    <div class="card mb-3">
                        <img src="https://via.placeholder.com/300x200" class="card-img-top" alt="Image en haut">
                        <div class="card-body">
                            <h5 class="card-title">Image en haut</h5>
                            <p class="card-text">Exemple avec une image en haut de la carte.</p>
                        </div>
                    </div>
                </div>
                <div class="col-md-4">
                    <div class="card mb-3">
                        <div class="card-body">
                            <h5 class="card-title">Image en bas</h5>
                            <p class="card-text">Exemple avec une image en bas de la carte.</p>
                        </div>
                        <img src="https://via.placeholder.com/300x200" class="card-img-bottom" alt="Image en bas">
                    </div>
                </div>
                <div class="col-md-4">
                    <div class="card text-white">
                        <img src="https://via.placeholder.com/300x200" class="card-img" alt="Image de fond">
                        <div class="card-img-overlay">
                            <h5 class="card-title">Image de fond</h5>
                            <p class="card-text">Le texte est superposé sur l'image de fond.</p>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </div>
    <div class="preview-tab-content">
        ```html
        <!-- Carte avec image en haut -->
        <div class="card">
            <img src="..." class="card-img-top" alt="Image en haut">
            <div class="card-body">
                <h5 class="card-title">Image en haut</h5>
                <p class="card-text">Exemple avec une image en haut de la carte.</p>
            </div>
        </div>

        <!-- Carte avec image en bas -->
        <div class="card">
            <div class="card-body">
                <h5 class="card-title">Image en bas</h5>
                <p class="card-text">Exemple avec une image en bas de la carte.</p>
            </div>
            <img src="..." class="card-img-bottom" alt="Image en bas">
        </div>

        <!-- Carte avec image de fond -->
        <div class="card text-white">
            <img src="..." class="card-img" alt="Image de fond">
            <div class="card-img-overlay">
                <h5 class="card-title">Image de fond</h5>
                <p class="card-text">Le texte est superposé sur l'image de fond.</p>
            </div>
        </div>
        ```
    </div>
</div>

### Listes dans les cartes

Intégrez des listes dans vos cartes avec `.list-group`.

<div class="preview-tabs">
    <div class="preview-tabs-headers">
        <button class="preview-tab-header active">Aperçu</button>
        <button class="preview-tab-header">Code</button>
    </div>
    <div class="preview-tab-content">
        <div class="component-preview">
            <div class="card" style="width: 18rem;">
                <div class="card-header">
                    Liste des éléments
                </div>
                <ul class="list-group list-group-flush">
                    <li class="list-group-item">Premier élément</li>
                    <li class="list-group-item">Deuxième élément</li>
                    <li class="list-group-item">Troisième élément</li>
                </ul>
                <div class="card-footer">
                    Pied de carte
                </div>
            </div>
        </div>
    </div>
    <div class="preview-tab-content">
        ```html
        <div class="card" style="width: 18rem;">
            <div class="card-header">
                Liste des éléments
            </div>
            <ul class="list-group list-group-flush">
                <li class="list-group-item">Premier élément</li>
                <li class="list-group-item">Deuxième élément</li>
                <li class="list-group-item">Troisième élément</li>
            </ul>
            <div class="card-footer">
                Pied de carte
            </div>
        </div>
        ```
    </div>
</div>

## Styles de cartes

### Couleurs de fond

Utilisez les utilitaires de couleur de fond pour changer l'apparence d'une carte.

<div class="preview-tabs">
    <div class="preview-tabs-headers">
        <button class="preview-tab-header active">Aperçu</button>
        <button class="preview-tab-header">Code</button>
    </div>
    <div class="preview-tab-content">
        <div class="component-preview">
            <div class="card text-white bg-primary mb-3" style="max-width: 18rem;">
                <div class="card-header">En-tête</div>
                <div class="card-body">
                    <h5 class="card-title">Titre carte primaire</h5>
                    <p class="card-text">Un exemple de texte pour une carte avec fond primaire.</p>
                </div>
            </div>
            <div class="card text-white bg-success mb-3" style="max-width: 18rem;">
                <div class="card-header">En-tête</div>
                <div class="card-body">
                    <h5 class="card-title">Titre carte succès</h5>
                    <p class="card-text">Un exemple de texte pour une carte avec fond succès.</p>
                </div>
            </div>
        </div>
    </div>
    <div class="preview-tab-content">
        ```html
        <div class="card text-white bg-primary mb-3" style="max-width: 18rem;">
            <div class="card-header">En-tête</div>
            <div class="card-body">
                <h5 class="card-title">Titre carte primaire</h5>
                <p class="card-text">Un exemple de texte pour une carte avec fond primaire.</p>
            </div>
        </div>

        <div class="card text-white bg-success mb-3" style="max-width: 18rem;">
            <div class="card-header">En-tête</div>
            <div class="card-body">
                <h5 class="card-title">Titre carte succès</h5>
                <p class="card-text">Un exemple de texte pour une carte avec fond succès.</p>
            </div>
        </div>
        ```
    </div>
</div>

### Bordures

Personnalisez les bordures des cartes avec les utilitaires de bordure.

<div class="preview-tabs">
    <div class="preview-tabs-headers">
        <button class="preview-tab-header active">Aperçu</button>
        <button class="preview-tab-header">Code</button>
    </div>
    <div class="preview-tab-content">
        <div class="component-preview">
            <div class="card border-primary mb-3" style="max-width: 18rem;">
                <div class="card-header">En-tête</div>
                <div class="card-body text-primary">
                    <h5 class="card-title">Titre carte bordure primaire</h5>
                    <p class="card-text">Un exemple de texte pour une carte avec bordure primaire.</p>
                </div>
            </div>
            <div class="card border-success mb-3" style="max-width: 18rem;">
                <div class="card-header">En-tête</div>
                <div class="card-body text-success">
                    <h5 class="card-title">Titre carte bordure succès</h5>
                    <p class="card-text">Un exemple de texte pour une carte avec bordure succès.</p>
                </div>
            </div>
        </div>
    </div>
    <div class="preview-tab-content">
        ```html
        <div class="card border-primary mb-3" style="max-width: 18rem;">
            <div class="card-header">En-tête</div>
            <div class="card-body text-primary">
                <h5 class="card-title">Titre carte bordure primaire</h5>
                <p class="card-text">Un exemple de texte pour une carte avec bordure primaire.</p>
            </div>
        </div>

        <div class="card border-success mb-3" style="max-width: 18rem;">
            <div class="card-header">En-tête</div>
            <div class="card-body text-success">
                <h5 class="card-title">Titre carte bordure succès</h5>
                <p class="card-text">Un exemple de texte pour une carte avec bordure succès.</p>
            </div>
        </div>
        ```
    </div>
</div>

## Disposition des cartes

### Groupes de cartes

Utilisez les groupes de cartes pour rendre les cartes comme un seul élément attaché avec des bordures partagées.

<div class="preview-tabs">
    <div class="preview-tabs-headers">
        <button class="preview-tab-header active">Aperçu</button>
        <button class="preview-tab-header">Code</button>
    </div>
    <div class="preview-tab-content">
        <div class="component-preview">
            <div class="card-group">
                <div class="card">
                    <img src="https://via.placeholder.com/300x200" class="card-img-top" alt="...">
                    <div class="card-body">
                        <h5 class="card-title">Titre de carte 1</h5>
                        <p class="card-text">Contenu de la première carte.</p>
                    </div>
                </div>
                <div class="card">
                    <img src="https://via.placeholder.com/300x200" class="card-img-top" alt="...">
                    <div class="card-body">
                        <h5 class="card-title">Titre de carte 2</h5>
                        <p class="card-text">Contenu de la deuxième carte.</p>
                    </div>
                </div>
                <div class="card">
                    <img src="https://via.placeholder.com/300x200" class="card-img-top" alt="...">
                    <div class="card-body">
                        <h5 class="card-title">Titre de carte 3</h5>
                        <p class="card-text">Contenu de la troisième carte.</p>
                    </div>
                </div>
            </div>
        </div>
    </div>
    <div class="preview-tab-content">
        ```html
        <div class="card-group">
            <div class="card">
                <img src="..." class="card-img-top" alt="...">
                <div class="card-body">
                    <h5 class="card-title">Titre de carte 1</h5>
                    <p class="card-text">Contenu de la première carte.</p>
                </div>
            </div>
            <div class="card">
                <img src="..." class="card-img-top" alt="...">
                <div class="card-body">
                    <h5 class="card-title">Titre de carte 2</h5>
                    <p class="card-text">Contenu de la deuxième carte.</p>
                </div>
            </div>
            <div class="card">
                <img src="..." class="card-img-top" alt="...">
                <div class="card-body">
                    <h5 class="card-title">Titre de carte 3</h5>
                    <p class="card-text">Contenu de la troisième carte.</p>
                </div>
            </div>
        </div>
        ```
    </div>
</div>

### Grille de cartes

Utilisez le système de grille de Bootstrap pour créer des mises en page de cartes responsives.

<div class="preview-tabs">
    <div class="preview-tabs-headers">
        <button class="preview-tab-header active">Aperçu</button>
        <button class="preview-tab-header">Code</button>
    </div>
    <div class="preview-tab-content">
        <div class="component-preview">
            <div class="row row-cols-1 row-cols-md-3 g-4">
                <div class="col">
                    <div class="card h-100">
                        <img src="https://via.placeholder.com/300x200" class="card-img-top" alt="...">
                        <div class="card-body">
                            <h5 class="card-title">Carte 1</h5>
                            <p class="card-text">Description de la carte 1.</p>
                        </div>
                    </div>
                </div>
                <div class="col">
                    <div class="card h-100">
                        <img src="https://via.placeholder.com/300x200" class="card-img-top" alt="...">
                        <div class="card-body">
                            <h5 class="card-title">Carte 2</h5>
                            <p class="card-text">Description de la carte 2.</p>
                        </div>
                    </div>
                </div>
                <div class="col">
                    <div class="card h-100">
                        <img src="https://via.placeholder.com/300x200" class="card-img-top" alt="...">
                        <div class="card-body">
                            <h5 class="card-title">Carte 3</h5>
                            <p class="card-text">Description de la carte 3.</p>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </div>
    <div class="preview-tab-content">
        ```html
        <div class="row row-cols-1 row-cols-md-3 g-4">
            <div class="col">
                <div class="card h-100">
                    <img src="..." class="card-img-top" alt="...">
                    <div class="card-body">
                        <h5 class="card-title">Carte 1</h5>
                        <p class="card-text">Description de la carte 1.</p>
                    </div>
                </div>
            </div>
            <div class="col">
                <div class="card h-100">
                    <img src="..." class="card-img-top" alt="...">
                    <div class="card-body">
                        <h5 class="card-title">Carte 2</h5>
                        <p class="card-text">Description de la carte 2.</p>
                    </div>
                </div>
            </div>
            <div class="col">
                <div class="card h-100">
                    <img src="..." class="card-img-top" alt="...">
                    <div class="card-body">
                        <h5 class="card-title">Carte 3</h5>
                        <p class="card-text">Description de la carte 3.</p>
                    </div>
                </div>
            </div>
        </div>
        ```
    </div>
</div>

## Utilisation dans Moodle

Dans Moodle, les cartes sont fréquemment utilisées pour :

- Afficher des cours dans le tableau de bord
- Présenter des activités et des ressources
- Créer des sections de contenu
- Afficher des informations utilisateur
- Organiser des blocs de contenu

### Exemple d'intégration dans un template Moodle

```php
{{#course}}
    <div class="card">
        <div class="card-header">
            <h3 class="card-title">{{fullname}}</h3>
        </div>
        <div class="card-body">
            {{#image}}
                <img src="{{url}}" class="card-img-top" alt="{{name}}">
            {{/image}}
            <p class="card-text">{{summary}}</p>
            {{#teachers}}
                <p class="card-text"><small class="text-muted">{{name}}</small></p>
            {{/teachers}}
            <a href="{{url}}" class="btn btn-primary">{{#str}}entercourse, moodle{{/str}}</a>
        </div>
    </div>
{{/course}}
```

## Variables CSS personnalisables

Les cartes utilisent des variables CSS locales pour une personnalisation améliorée :

```scss
--#{$prefix}card-spacer-y: #{$card-spacer-y};
--#{$prefix}card-spacer-x: #{$card-spacer-x};
--#{$prefix}card-title-spacer-y: #{$card-title-spacer-y};
--#{$prefix}card-border-width: #{$card-border-width};
--#{$prefix}card-border-color: #{$card-border-color};
--#{$prefix}card-border-radius: #{$card-border-radius};
--#{$prefix}card-box-shadow: #{$card-box-shadow};
--#{$prefix}card-inner-border-radius: #{$card-inner-border-radius};
--#{$prefix}card-cap-padding-y: #{$card-cap-padding-y};
--#{$prefix}card-cap-padding-x: #{$card-cap-padding-x};
--#{$prefix}card-cap-bg: #{$card-cap-bg};
--#{$prefix}card-bg: #{$card-bg};
--#{$prefix}card-img-overlay-padding: #{$card-img-overlay-padding};
```

## Variables Sass

Les cartes peuvent être personnalisées via les variables Sass suivantes :

```scss
$card-spacer-y:                     $spacer;
$card-spacer-x:                     $spacer;
$card-title-spacer-y:              $spacer * .5;
$card-border-width:                 $border-width;
$card-border-radius:                $border-radius;
$card-border-color:                 rgba($black, .125);
$card-inner-border-radius:          subtract($card-border-radius, $card-border-width);
$card-cap-padding-y:               $card-spacer-y * .5;
$card-cap-padding-x:               $card-spacer-x;
$card-cap-bg:                      rgba($black, .03);
$card-cap-color:                    null;
$card-height:                       null;
$card-color:                        null;
$card-bg:                          $white;
```

## Accessibilité

- Utilisez des en-têtes appropriés pour la hiérarchie du contenu
- Assurez-vous que les images ont des textes alternatifs descriptifs
- Maintenez un contraste suffisant pour le texte sur les fonds colorés
- Utilisez des liens explicites pour les actions
- Évitez de masquer des informations importantes dans les superpositions d'images
- Ajoutez des attributs ARIA appropriés pour les contenus interactifs

### Exemples spécifiques à Moodle

#### Carte de cours

<div class="preview-tabs">
    <div class="preview-tabs-headers">
        <button class="preview-tab-header active">Aperçu</button>
        <button class="preview-tab-header">Code</button>
    </div>
    <div class="preview-tab-content">
        <div class="component-preview">
            <div class="card">
                <img src="../images/course-banner.jpg" class="card-img-top" alt="Bannière du cours de programmation web">
                <div class="card-body">
                    <span class="badge bg-success mb-2">Ouvert aux inscriptions</span>
                    <h3 class="card-title">Programmation Web Avancée</h3>
                    <p class="card-text">Maîtrisez les technologies web modernes : HTML5, CSS3, JavaScript et les frameworks populaires.</p>
                    <div class="d-flex align-items-center mb-3">
                        <img src="../images/teacher-avatar.jpg" class="rounded-circle me-2" width="32" height="32" alt="Photo de l'enseignant">
                        <span>Prof. Marie Dubois</span>
                    </div>
                    <div class="progress mb-3" style="height: 5px;">
                        <div class="progress-bar bg-success" role="progressbar" style="width: 25%" aria-valuenow="25" aria-valuemin="0" aria-valuemax="100"></div>
                    </div>
                    <div class="d-flex justify-content-between align-items-center">
                        <small class="text-muted">4 modules • 12 heures</small>
                        <a href="#" class="btn btn-primary">Continuer</a>
                    </div>
                </div>
            </div>
        </div>
    </div>
    <div class="preview-tab-content">
        ```html
        <div class="card">
            <img src="../images/course-banner.jpg" class="card-img-top" alt="Bannière du cours de programmation web">
            <div class="card-body">
                <span class="badge bg-success mb-2">Ouvert aux inscriptions</span>
                <h3 class="card-title">Programmation Web Avancée</h3>
                <p class="card-text">Maîtrisez les technologies web modernes : HTML5, CSS3, JavaScript et les frameworks populaires.</p>
                <div class="d-flex align-items-center mb-3">
                    <img src="../images/teacher-avatar.jpg" class="rounded-circle me-2" width="32" height="32" alt="Photo de l'enseignant">
                    <span>Prof. Marie Dubois</span>
                </div>
                <div class="progress mb-3" style="height: 5px;">
                    <div class="progress-bar bg-success" role="progressbar" style="width: 25%" aria-valuenow="25" aria-valuemin="0" aria-valuemax="100"></div>
                </div>
                <div class="d-flex justify-content-between align-items-center">
                    <small class="text-muted">4 modules • 12 heures</small>
                    <a href="#" class="btn btn-primary">Continuer</a>
                </div>
            </div>
        </div>
        ```
    </div>
</div>

#### Carte d'activité

<div class="preview-tabs">
    <div class="preview-tabs-headers">
        <button class="preview-tab-header active">Aperçu</button>
        <button class="preview-tab-header">Code</button>
    </div>
    <div class="preview-tab-content">
        <div class="component-preview">
            <div class="card border-info">
                <div class="card-header bg-info text-white d-flex justify-content-between align-items-center">
                    <span><i class="fas fa-tasks me-2"></i>Devoir</span>
                    <span class="badge bg-light text-dark">Date limite : 31 mars</span>
                </div>
                <div class="card-body">
                    <h5 class="card-title">Projet final : Application Web</h5>
                    <p class="card-text">Créez une application web complète en utilisant les technologies vues dans le cours.</p>
                    <ul class="list-group list-group-flush mb-3">
                        <li class="list-group-item d-flex justify-content-between align-items-center">
                            État
                            <span class="badge bg-warning">En cours</span>
                        </li>
                        <li class="list-group-item d-flex justify-content-between align-items-center">
                            Note maximale
                            <span>100 points</span>
                        </li>
                    </ul>
                    <div class="d-grid">
                        <a href="#" class="btn btn-outline-info">Soumettre le devoir</a>
                    </div>
                </div>
            </div>
        </div>
    </div>
    <div class="preview-tab-content">
        ```html
        <div class="card border-info">
            <div class="card-header bg-info text-white d-flex justify-content-between align-items-center">
                <span><i class="fas fa-tasks me-2"></i>Devoir</span>
                <span class="badge bg-light text-dark">Date limite : 31 mars</span>
            </div>
            <div class="card-body">
                <h5 class="card-title">Projet final : Application Web</h5>
                <p class="card-text">Créez une application web complète en utilisant les technologies vues dans le cours.</p>
                <ul class="list-group list-group-flush mb-3">
                    <li class="list-group-item d-flex justify-content-between align-items-center">
                        État
                        <span class="badge bg-warning">En cours</span>
                    </li>
                    <li class="list-group-item d-flex justify-content-between align-items-center">
                        Note maximale
                        <span>100 points</span>
                    </li>
                </ul>
                <div class="d-grid">
                    <a href="#" class="btn btn-outline-info">Soumettre le devoir</a>
                </div>
            </div>
        </div>
        ```
    </div>
</div>