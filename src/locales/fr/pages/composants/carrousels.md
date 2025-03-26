---
title: Carrousels
description: Documentation du composant Carrousels de Bootstrap 5 pour Moodle
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
          <p class="lead">Les carrousels sont des composants de diaporama qui permettent de faire défiler du contenu de manière cyclique. Ils sont idéaux pour présenter des images, des témoignages ou des fonctionnalités de manière interactive.</p>
        </div>

        <div id="exemple-base" class="mt-5">
          <h2>Exemple de base</h2>
          <p>Un carrousel simple avec des images et des contrôles de navigation.</p>
          <div class="card mb-4">
            <div class="card-body">
              <div class="component-preview">
                <div id="basicCarousel" class="carousel slide" data-bs-ride="carousel">
                  <div class="carousel-indicators">
                    <button type="button" data-bs-target="#basicCarousel" data-bs-slide-to="0" class="active" aria-current="true" aria-label="Slide 1"></button>
                    <button type="button" data-bs-target="#basicCarousel" data-bs-slide-to="1" aria-label="Slide 2"></button>
                    <button type="button" data-bs-target="#basicCarousel" data-bs-slide-to="2" aria-label="Slide 3"></button>
                  </div>

                  <div class="carousel-inner">
                    <div class="carousel-item active">
                      <img src="https://placehold.co/800x400" class="d-block w-100" alt="Première diapositive">
                    </div>
                    <div class="carousel-item">
                      <img src="https://placehold.co/800x400" class="d-block w-100" alt="Deuxième diapositive">
                    </div>
                    <div class="carousel-item">
                      <img src="https://placehold.co/800x400" class="d-block w-100" alt="Troisième diapositive">
                    </div>
                  </div>

                  <button class="carousel-control-prev" type="button" data-bs-target="#basicCarousel" data-bs-slide="prev">
                    <span class="carousel-control-prev-icon" aria-hidden="true"></span>
                    <span class="visually-hidden">Précédent</span>
                  </button>
                  <button class="carousel-control-next" type="button" data-bs-target="#basicCarousel" data-bs-slide="next">
                    <span class="carousel-control-next-icon" aria-hidden="true"></span>
                    <span class="visually-hidden">Suivant</span>
                  </button>
                </div>
              </div>
            </div>
          </div>
        </div>

        <div id="styles" class="mt-5">
          <h2>Styles</h2>

          <div class="card mb-4">
            <div class="card-body">
              <h3 class="h5">Carrousel avec légendes</h3>
              <p>Les carrousels peuvent inclure des légendes pour chaque diapositive.</p>
              <div class="component-preview">
                <div id="captionCarousel" class="carousel slide" data-bs-ride="carousel">
                  <div class="carousel-inner">
                    <div class="carousel-item active">
                      <img src="https://placehold.co/800x400" class="d-block w-100" alt="Première diapositive">
                      <div class="carousel-caption d-none d-md-block">
                        <h5>Première diapositive</h5>
                        <p>Description de la première diapositive</p>
                      </div>
                    </div>
                    <div class="carousel-item">
                      <img src="https://placehold.co/800x400" class="d-block w-100" alt="Deuxième diapositive">
                      <div class="carousel-caption d-none d-md-block">
                        <h5>Deuxième diapositive</h5>
                        <p>Description de la deuxième diapositive</p>
                      </div>
                    </div>
                  </div>
                </div>
              </div>
            </div>
          </div>

          <div class="card mb-4">
            <div class="card-body">
              <h3 class="h5">Carrousel avec fond sombre</h3>
              <p>Les carrousels peuvent avoir un fond sombre pour un meilleur contraste.</p>
              <div class="component-preview">
                <div id="darkCarousel" class="carousel slide carousel-dark" data-bs-ride="carousel">
                  <div class="carousel-inner">
                    <div class="carousel-item active">
                      <div class="bg-dark text-white p-5 text-center">
                        <h3>Première diapositive</h3>
                        <p>Contenu de la première diapositive</p>
                      </div>
                    </div>
                    <div class="carousel-item">
                      <div class="bg-dark text-white p-5 text-center">
                        <h3>Deuxième diapositive</h3>
                        <p>Contenu de la deuxième diapositive</p>
                      </div>
                    </div>
                  </div>
                </div>
              </div>
            </div>
          </div>

          <div class="card mb-4">
            <div class="card-body">
              <h3 class="h5">Carrousel avec défilement automatique</h3>
              <p>Les carrousels peuvent défiler automatiquement après un délai.</p>
              <div class="component-preview">
                <div id="autoCarousel" class="carousel slide" data-bs-ride="carousel" data-bs-interval="3000">
                  <div class="carousel-inner">
                    <div class="carousel-item active">
                      <img src="https://placehold.co/800x400" class="d-block w-100" alt="Première diapositive">
                    </div>
                    <div class="carousel-item">
                      <img src="https://placehold.co/800x400" class="d-block w-100" alt="Deuxième diapositive">
                    </div>
                    <div class="carousel-item">
                      <img src="https://placehold.co/800x400" class="d-block w-100" alt="Troisième diapositive">
                    </div>
                  </div>
                </div>
              </div>
            </div>
          </div>
        </div>

        <div id="utilisation-moodle" class="mt-5">
          <h2>Utilisation dans Moodle</h2>
          <p>Dans Moodle, les carrousels sont utilisés pour :</p>
          <ul class="list-group mb-4">
            <li class="list-group-item">Présenter les fonctionnalités principales</li>
            <li class="list-group-item">Afficher des témoignages d'étudiants</li>
            <li class="list-group-item">Montrer des exemples de travaux</li>
            <li class="list-group-item">Présenter des tutoriels</li>
            <li class="list-group-item">Afficher des annonces importantes</li>
          </ul>

          <div class="card mb-4">
            <div class="card-body">
              <h3 class="h5">Exemple d'intégration dans un template Moodle</h3>
              <pre class="bg-light p-3 rounded"><code>{{#has_carousel}}
    &lt;div id="{{carousel_id}}" class="carousel slide" data-bs-ride="carousel" {{#interval}}data-bs-interval="{{interval}}"{{/interval}}&gt;
        {{#indicators}}
        &lt;div class="carousel-indicators"&gt;
            {{#items}}
            &lt;button type="button" data-bs-target="#{{../carousel_id}}" data-bs-slide-to="{{index}}" {{#active}}class="active" aria-current="true"{{/active}} aria-label="Diapositive {{number}}"&gt;&lt;/button&gt;
            {{/items}}
        &lt;/div&gt;
        {{/indicators}}

        &lt;div class="carousel-inner"&gt;
            {{#items}}
            &lt;div class="carousel-item {{#active}}active{{/active}}"&gt;
                {{#image}}
                &lt;img src="{{url}}" class="d-block w-100" alt="{{alt}}"&gt;
                {{/image}}

                {{#caption}}
                &lt;div class="carousel-caption d-none d-md-block"&gt;
                    {{#title}}&lt;h5&gt;{{title}}&lt;/h5&gt;{{/title}}
                    {{#text}}&lt;p&gt;{{text}}&lt;/p&gt;{{/text}}
                &lt;/div&gt;
                {{/caption}}
            &lt;/div&gt;
            {{/items}}
        &lt;/div&gt;

        {{#controls}}
        &lt;button class="carousel-control-prev" type="button" data-bs-target="#{{../carousel_id}}" data-bs-slide="prev"&gt;
            &lt;span class="carousel-control-prev-icon" aria-hidden="true"&gt;&lt;/span&gt;
            &lt;span class="visually-hidden"&gt;{{#str}}previous, core{{/str}}&lt;/span&gt;
        &lt;/button&gt;
        &lt;button class="carousel-control-next" type="button" data-bs-target="#{{../carousel_id}}" data-bs-slide="next"&gt;
            &lt;span class="carousel-control-next-icon" aria-hidden="true"&gt;&lt;/span&gt;
            &lt;span class="visually-hidden"&gt;{{#str}}next, core{{/str}}&lt;/span&gt;
        &lt;/button&gt;
        {{/controls}}
    &lt;/div&gt;
{{/has_carousel}}</code></pre>
            </div>
          </div>
        </div>

        <div id="accessibilite" class="mt-5">
          <h2>Accessibilité</h2>
          <ul class="list-group mb-4">
            <li class="list-group-item">Fournissez des alternatives textuelles pour les images</li>
            <li class="list-group-item">Utilisez des contrôles clairs et accessibles au clavier</li>
            <li class="list-group-item">Maintenez un contraste suffisant pour le texte</li>
            <li class="list-group-item">Permettez de mettre en pause le défilement automatique</li>
            <li class="list-group-item">Évitez les informations essentielles uniquement dans le carrousel</li>
          </ul>
        </div>
      </div>
    </div>
  </div>
</div>