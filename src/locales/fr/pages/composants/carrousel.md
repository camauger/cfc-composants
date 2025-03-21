---
title: Carrousel
description: Un composant de diaporama pour faire défiler des éléments - images ou textes - comme un carrousel.
template: pages/composant.html
---

Le carrousel est un composant de diaporama permettant de faire défiler une série de contenus, construit avec des transformations CSS 3D et du JavaScript. Il fonctionne avec une série d'images, de textes ou de contenu personnalisé. Il inclut également la prise en charge des contrôles précédent/suivant et des indicateurs.

## Fonctionnement

Dans les navigateurs prenant en charge l'API de visibilité des pages, le carrousel évite de faire défiler lorsque la page web n'est pas visible pour l'utilisateur (par exemple lorsque l'onglet du navigateur est inactif ou que la fenêtre du navigateur est minimisée).

!!! warning "Accessibilité"
    L'effet d'animation de ce composant dépend de la requête média `prefers-reduced-motion`. Les carrousels imbriqués ne sont pas pris en charge et les carrousels ne sont généralement pas conformes aux normes d'accessibilité.

## Exemples

=== "Aperçu"
    <div class="bd-example">
      <div id="carouselExample" class="carousel slide" data-bs-ride="carousel">
        <div class="carousel-inner">
          <div class="carousel-item active">
            <img src="../images/slide-1.jpg" class="d-block w-100" alt="Première diapositive">
          </div>
          <div class="carousel-item">
            <img src="../images/slide-2.jpg" class="d-block w-100" alt="Deuxième diapositive">
          </div>
          <div class="carousel-item">
            <img src="../images/slide-3.jpg" class="d-block w-100" alt="Troisième diapositive">
          </div>
          <div class="carousel-item">
            <img src="../images/slide-4.jpg" class="d-block w-100" alt="Quatrième diapositive">
          </div>
        </div>
        <button class="carousel-control-prev" type="button" data-bs-target="#carouselExample" data-bs-slide="prev">
          <span class="carousel-control-prev-icon" aria-hidden="true"></span>
          <span class="visually-hidden">Précédent</span>
        </button>
        <button class="carousel-control-next" type="button" data-bs-target="#carouselExample" data-bs-slide="next">
          <span class="carousel-control-next-icon" aria-hidden="true"></span>
          <span class="visually-hidden">Suivant</span>
        </button>
      </div>
    </div>

=== "HTML"
    ```html
    <div id="carouselExample" class="carousel slide" data-bs-ride="carousel">
      <div class="carousel-inner">
        <div class="carousel-item active">
          <img src="../images/slide-1.jpg" class="d-block w-100" alt="Première diapositive">
        </div>
        <div class="carousel-item">
          <img src="../images/slide-2.jpg" class="d-block w-100" alt="Deuxième diapositive">
        </div>
        <div class="carousel-item">
          <img src="../images/slide-3.jpg" class="d-block w-100" alt="Troisième diapositive">
        </div>
        <div class="carousel-item">
          <img src="../images/slide-4.jpg" class="d-block w-100" alt="Quatrième diapositive">
        </div>
      </div>
      <button class="carousel-control-prev" type="button" data-bs-target="#carouselExample" data-bs-slide="prev">
        <span class="carousel-control-prev-icon" aria-hidden="true"></span>
        <span class="visually-hidden">Précédent</span>
      </button>
      <button class="carousel-control-next" type="button" data-bs-target="#carouselExample" data-bs-slide="next">
        <span class="carousel-control-next-icon" aria-hidden="true"></span>
        <span class="visually-hidden">Suivant</span>
      </button>
    </div>
    ```

### Avec indicateurs

Ajoutez des indicateurs au carrousel, en plus des contrôles précédent/suivant.

=== "Aperçu"
    <div class="bd-example">
      <div id="carouselExampleIndicators" class="carousel slide" data-bs-ride="carousel">
        <div class="carousel-indicators">
          <button type="button" data-bs-target="#carouselExampleIndicators" data-bs-slide-to="0" class="active" aria-current="true" aria-label="Diapositive 1"></button>
          <button type="button" data-bs-target="#carouselExampleIndicators" data-bs-slide-to="1" aria-label="Diapositive 2"></button>
          <button type="button" data-bs-target="#carouselExampleIndicators" data-bs-slide-to="2" aria-label="Diapositive 3"></button>
          <button type="button" data-bs-target="#carouselExampleIndicators" data-bs-slide-to="3" aria-label="Diapositive 4"></button>
        </div>
        <div class="carousel-inner">
          <div class="carousel-item active">
            <img src="../images/slide-1.jpg" class="d-block w-100" alt="Première diapositive">
          </div>
          <div class="carousel-item">
            <img src="../images/slide-2.jpg" class="d-block w-100" alt="Deuxième diapositive">
          </div>
          <div class="carousel-item">
            <img src="../images/slide-3.jpg" class="d-block w-100" alt="Troisième diapositive">
          </div>
          <div class="carousel-item">
            <img src="../images/slide-4.jpg" class="d-block w-100" alt="Quatrième diapositive">
          </div>
        </div>
        <button class="carousel-control-prev" type="button" data-bs-target="#carouselExampleIndicators" data-bs-slide="prev">
          <span class="carousel-control-prev-icon" aria-hidden="true"></span>
          <span class="visually-hidden">Précédent</span>
        </button>
        <button class="carousel-control-next" type="button" data-bs-target="#carouselExampleIndicators" data-bs-slide="next">
          <span class="carousel-control-next-icon" aria-hidden="true"></span>
          <span class="visually-hidden">Suivant</span>
        </button>
      </div>
    </div>

=== "HTML"
    ```html
    <div id="carouselExampleIndicators" class="carousel slide" data-bs-ride="carousel">
      <div class="carousel-indicators">
        <button type="button" data-bs-target="#carouselExampleIndicators" data-bs-slide-to="0" class="active" aria-current="true" aria-label="Diapositive 1"></button>
        <button type="button" data-bs-target="#carouselExampleIndicators" data-bs-slide-to="1" aria-label="Diapositive 2"></button>
        <button type="button" data-bs-target="#carouselExampleIndicators" data-bs-slide-to="2" aria-label="Diapositive 3"></button>
        <button type="button" data-bs-target="#carouselExampleIndicators" data-bs-slide-to="3" aria-label="Diapositive 4"></button>
      </div>
      <div class="carousel-inner">
        <div class="carousel-item active">
          <img src="../images/slide-1.jpg" class="d-block w-100" alt="Première diapositive">
        </div>
        <div class="carousel-item">
          <img src="../images/slide-2.jpg" class="d-block w-100" alt="Deuxième diapositive">
        </div>
        <div class="carousel-item">
          <img src="../images/slide-3.jpg" class="d-block w-100" alt="Troisième diapositive">
        </div>
        <div class="carousel-item">
          <img src="../images/slide-4.jpg" class="d-block w-100" alt="Quatrième diapositive">
        </div>
      </div>
      <button class="carousel-control-prev" type="button" data-bs-target="#carouselExampleIndicators" data-bs-slide="prev">
        <span class="carousel-control-prev-icon" aria-hidden="true"></span>
        <span class="visually-hidden">Précédent</span>
      </button>
      <button class="carousel-control-next" type="button" data-bs-target="#carouselExampleIndicators" data-bs-slide="next">
        <span class="carousel-control-next-icon" aria-hidden="true"></span>
        <span class="visually-hidden">Suivant</span>
      </button>
    </div>
    ```

### Avec légendes

Ajoutez des légendes à vos diapositives avec l'élément `.carousel-caption`.

=== "Aperçu"
    <div class="bd-example">
      <div id="carouselExampleCaptions" class="carousel slide" data-bs-ride="carousel">
        <div class="carousel-indicators">
          <button type="button" data-bs-target="#carouselExampleCaptions" data-bs-slide-to="0" class="active" aria-current="true" aria-label="Diapositive 1"></button>
          <button type="button" data-bs-target="#carouselExampleCaptions" data-bs-slide-to="1" aria-label="Diapositive 2"></button>
          <button type="button" data-bs-target="#carouselExampleCaptions" data-bs-slide-to="2" aria-label="Diapositive 3"></button>
          <button type="button" data-bs-target="#carouselExampleCaptions" data-bs-slide-to="3" aria-label="Diapositive 4"></button>
        </div>
        <div class="carousel-inner">
          <div class="carousel-item active">
            <img src="../images/slide-1.jpg" class="d-block w-100" alt="Première diapositive">
            <div class="carousel-caption d-none d-md-block">
              <h5>Première diapositive</h5>
              <p>Description de la première image du carrousel.</p>
            </div>
          </div>
          <div class="carousel-item">
            <img src="../images/slide-2.jpg" class="d-block w-100" alt="Deuxième diapositive">
            <div class="carousel-caption d-none d-md-block">
              <h5>Deuxième diapositive</h5>
              <p>Description de la deuxième image du carrousel.</p>
            </div>
          </div>
          <div class="carousel-item">
            <img src="../images/slide-3.jpg" class="d-block w-100" alt="Troisième diapositive">
            <div class="carousel-caption d-none d-md-block">
              <h5>Troisième diapositive</h5>
              <p>Description de la troisième image du carrousel.</p>
            </div>
          </div>
          <div class="carousel-item">
            <img src="../images/slide-4.jpg" class="d-block w-100" alt="Quatrième diapositive">
            <div class="carousel-caption d-none d-md-block">
              <h5>Quatrième diapositive</h5>
              <p>Description de la quatrième image du carrousel.</p>
            </div>
          </div>
        </div>
        <button class="carousel-control-prev" type="button" data-bs-target="#carouselExampleCaptions" data-bs-slide="prev">
          <span class="carousel-control-prev-icon" aria-hidden="true"></span>
          <span class="visually-hidden">Précédent</span>
        </button>
        <button class="carousel-control-next" type="button" data-bs-target="#carouselExampleCaptions" data-bs-slide="next">
          <span class="carousel-control-next-icon" aria-hidden="true"></span>
          <span class="visually-hidden">Suivant</span>
        </button>
      </div>
    </div>

=== "HTML"
    ```html
    <div id="carouselExampleCaptions" class="carousel slide" data-bs-ride="carousel">
      <div class="carousel-indicators">
        <button type="button" data-bs-target="#carouselExampleCaptions" data-bs-slide-to="0" class="active" aria-current="true" aria-label="Diapositive 1"></button>
        <button type="button" data-bs-target="#carouselExampleCaptions" data-bs-slide-to="1" aria-label="Diapositive 2"></button>
        <button type="button" data-bs-target="#carouselExampleCaptions" data-bs-slide-to="2" aria-label="Diapositive 3"></button>
        <button type="button" data-bs-target="#carouselExampleCaptions" data-bs-slide-to="3" aria-label="Diapositive 4"></button>
      </div>
      <div class="carousel-inner">
        <div class="carousel-item active">
          <img src="../images/slide-1.jpg" class="d-block w-100" alt="Première diapositive">
          <div class="carousel-caption d-none d-md-block">
            <h5>Première diapositive</h5>
            <p>Description de la première image du carrousel.</p>
          </div>
        </div>
        <div class="carousel-item">
          <img src="../images/slide-2.jpg" class="d-block w-100" alt="Deuxième diapositive">
          <div class="carousel-caption d-none d-md-block">
            <h5>Deuxième diapositive</h5>
            <p>Description de la deuxième image du carrousel.</p>
          </div>
        </div>
        <div class="carousel-item">
          <img src="../images/slide-3.jpg" class="d-block w-100" alt="Troisième diapositive">
          <div class="carousel-caption d-none d-md-block">
            <h5>Troisième diapositive</h5>
            <p>Description de la troisième image du carrousel.</p>
          </div>
        </div>
        <div class="carousel-item">
          <img src="../images/slide-4.jpg" class="d-block w-100" alt="Quatrième diapositive">
          <div class="carousel-caption d-none d-md-block">
            <h5>Quatrième diapositive</h5>
            <p>Description de la quatrième image du carrousel.</p>
          </div>
        </div>
      </div>
      <button class="carousel-control-prev" type="button" data-bs-target="#carouselExampleCaptions" data-bs-slide="prev">
        <span class="carousel-control-prev-icon" aria-hidden="true"></span>
        <span class="visually-hidden">Précédent</span>
      </button>
      <button class="carousel-control-next" type="button" data-bs-target="#carouselExampleCaptions" data-bs-slide="next">
        <span class="carousel-control-next-icon" aria-hidden="true"></span>
        <span class="visually-hidden">Suivant</span>
      </button>
    </div>
    ```

## Utilisation dans Moodle

Le carrousel peut être utilisé dans Moodle pour :

- Présenter une série d'images dans un cours
- Afficher des annonces importantes de manière rotative
- Créer des présentations interactives de contenu
- Mettre en valeur des ressources ou des activités

### Exemple avec Mustache

```html
{{#carousel}}
<div id="carousel-{{uniqid}}" class="carousel slide" data-bs-ride="carousel">
  <div class="carousel-inner">
    {{#slides}}
    <div class="carousel-item {{#active}}active{{/active}}">
      <img src="{{image}}" class="d-block w-100" alt="{{alt}}">
      {{#caption}}
      <div class="carousel-caption d-none d-md-block">
        <h5>{{title}}</h5>
        <p>{{text}}</p>
      </div>
      {{/caption}}
    </div>
    {{/slides}}
  </div>
  <button class="carousel-control-prev" type="button" data-bs-target="#carousel-{{uniqid}}" data-bs-slide="prev">
    <span class="carousel-control-prev-icon" aria-hidden="true"></span>
    <span class="visually-hidden">{{#str}}previous{{/str}}</span>
  </button>
  <button class="carousel-control-next" type="button" data-bs-target="#carousel-{{uniqid}}" data-bs-slide="next">
    <span class="carousel-control-next-icon" aria-hidden="true"></span>
    <span class="visually-hidden">{{#str}}next{{/str}}</span>
  </button>
</div>
{{/carousel}}
```

## Personnalisation

### Variables CSS

```css
--bs-carousel-transition-duration: 0.6s;
--bs-carousel-control-color: #fff;
--bs-carousel-control-width: 15%;
--bs-carousel-control-opacity: 0.5;
--bs-carousel-control-hover-opacity: 0.9;
--bs-carousel-indicator-width: 30px;
--bs-carousel-indicator-height: 3px;
--bs-carousel-indicator-hit-area-height: 10px;
--bs-carousel-indicator-spacer: 3px;
--bs-carousel-indicator-opacity: 0.5;
--bs-carousel-indicator-active-bg: #fff;
--bs-carousel-indicator-active-opacity: 1;
--bs-carousel-caption-width: 70%;
--bs-carousel-caption-color: #fff;
--bs-carousel-caption-padding-y: 1.25rem;
--bs-carousel-caption-spacer: 1.25rem;
```

### Variables Sass

```scss
$carousel-control-color:             $white;
$carousel-control-width:             15%;
$carousel-control-opacity:           .5;
$carousel-control-hover-opacity:     .9;
$carousel-control-transition:        opacity .15s ease;

$carousel-indicator-width:           30px;
$carousel-indicator-height:          3px;
$carousel-indicator-hit-area-height: 10px;
$carousel-indicator-spacer:          3px;
$carousel-indicator-opacity:         .5;
$carousel-indicator-active-bg:       $white;
$carousel-indicator-active-opacity:  1;
$carousel-indicator-transition:      opacity .6s ease;

$carousel-caption-width:             70%;
$carousel-caption-color:             $white;
$carousel-caption-padding-y:         1.25rem;
$carousel-caption-spacer:           1.25rem;

$carousel-control-icon-width:        2rem;

$carousel-control-prev-icon-bg:      url("data:image/svg+xml,<svg xmlns='http://www.w3.org/2000/svg'....");
$carousel-control-next-icon-bg:      url("data:image/svg+xml,<svg xmlns='http://www.w3.org/2000/svg'....");

$carousel-transition-duration:       .6s;
$carousel-transition:                transform $carousel-transition-duration ease-in-out;
```