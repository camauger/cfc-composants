---
title: Carrousel
description: Un composant de diaporama pour faire défiler des éléments - images ou textes - comme un carrousel.
template: pages/composant.html
---

<div class="container py-4">
  <div class="row">
    <div class="col-lg-3">
      <nav id="navbar-example3" class="h-100 flex-column align-items-stretch pe-4 border-end">
        <nav class="nav nav-pills flex-column">
          <a class="nav-link" href="#description">Description</a>
          <a class="nav-link" href="#fonctionnement">Fonctionnement</a>
          <a class="nav-link" href="#exemples">Exemples</a>
          <a class="nav-link" href="#utilisation-moodle">Utilisation dans Moodle</a>
        </nav>
      </nav>
    </div>

  <div class="col-lg-9">
      <div data-bs-spy="scroll" data-bs-target="#navbar-example3" data-bs-smooth-scroll="true" class="scrollspy-example-2" tabindex="0">
        <div id="description">
          <h2>Description</h2>
          <p class="lead">Le carrousel est un composant de diaporama permettant de faire défiler une série de contenus, construit avec des transformations CSS 3D et du JavaScript. Il fonctionne avec une série d'images, de textes ou de contenu personnalisé. Il inclut également la prise en charge des contrôles précédent/suivant et des indicateurs.</p>
        </div>

  <div id="fonctionnement" class="mt-5">
          <h2>Fonctionnement</h2>
          <p>Dans les navigateurs prenant en charge l'API de visibilité des pages, le carrousel évite de faire défiler lorsque la page web n'est pas visible pour l'utilisateur (par exemple lorsque l'onglet du navigateur est inactif ou que la fenêtre du navigateur est minimisée).</p>

<div class="alert alert-warning" role="alert">
            <h4 class="alert-heading">Accessibilité</h4>
            <p class="mb-0">L'effet d'animation de ce composant dépend de la requête média `prefers-reduced-motion`. Les carrousels imbriqués ne sont pas pris en charge et les carrousels ne sont généralement pas conformes aux normes d'accessibilité.</p>
          </div>
        </div>

  <div id="exemples" class="mt-5">
          <h2>Exemples</h2>

  <div class="card mb-4">
            <div class="card-body">
              <h3 class="h5">Carrousel de base</h3>
              <div class="bd-example">
                <div id="carouselExample" class="carousel slide" data-bs-ride="carousel">
                  <div class="carousel-inner">
                    <div class="carousel-item active">
                      <img src="../../assets/images/slide-1.jpg" class="d-block w-100" alt="Première diapositive">
                    </div>
                    <div class="carousel-item">
                      <img src="../../assets/images/slide-2.jpg" class="d-block w-100" alt="Deuxième diapositive">
                    </div>
                    <div class="carousel-item">
                      <img src="../../assets/images/slide-3.jpg" class="d-block w-100" alt="Troisième diapositive">
                    </div>
                    <div class="carousel-item">
                      <img src="../../assets/images/slide-4.jpg" class="d-block w-100" alt="Quatrième diapositive">
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
            </div>
          </div>

 <div class="card mb-4">
            <div class="card-body">
              <h3 class="h5">Avec indicateurs</h3>
              <p>Ajoutez des indicateurs au carrousel, en plus des contrôles précédent/suivant.</p>
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
                      <img src="../../assets/images/slide-1.jpg" class="d-block w-100" alt="Première diapositive">
                    </div>
                    <div class="carousel-item">
                      <img src="../../assets/images/slide-2.jpg" class="d-block w-100" alt="Deuxième diapositive">
                    </div>
                    <div class="carousel-item">
                      <img src="../../assets/images/slide-3.jpg" class="d-block w-100" alt="Troisième diapositive">
                    </div>
                    <div class="carousel-item">
                      <img src="../../assets/images/slide-4.jpg" class="d-block w-100" alt="Quatrième diapositive">
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
            </div>
          </div>

   <div class="card mb-4">
            <div class="card-body">
              <h3 class="h5">Avec légendes</h3>
              <p>Ajoutez des légendes à vos diapositives avec l'élément `.carousel-caption`.</p>
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
                      <img src="../../assets/images/slide-1.jpg" class="d-block w-100" alt="Première diapositive">
                      <div class="carousel-caption d-none d-md-block">
                        <h5>Première diapositive</h5>
                        <p>Description de la première image du carrousel.</p>
                      </div>
                    </div>
                    <div class="carousel-item">
                      <img src="../../assets/images/slide-2.jpg" class="d-block w-100" alt="Deuxième diapositive">
                      <div class="carousel-caption d-none d-md-block">
                        <h5>Deuxième diapositive</h5>
                        <p>Description de la deuxième image du carrousel.</p>
                      </div>
                    </div>
                    <div class="carousel-item">
                      <img src="../../assets/images/slide-3.jpg" class="d-block w-100" alt="Troisième diapositive">
                      <div class="carousel-caption d-none d-md-block">
                        <h5>Troisième diapositive</h5>
                        <p>Description de la troisième image du carrousel.</p>
                      </div>
                    </div>
                    <div class="carousel-item">
                      <img src="../../assets/images/slide-4.jpg" class="d-block w-100" alt="Quatrième diapositive">
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
            </div>
          </div>
        </div>

  <div id="utilisation-moodle" class="mt-5">
          <h2>Utilisation dans Moodle</h2>
          <p>Le carrousel peut être utilisé dans Moodle pour :</p>
          <ul class="list-group mb-4">
            <li class="list-group-item">Présenter une série d'images dans un cours</li>
            <li class="list-group-item">Afficher des annonces importantes de manière rotative</li>
            <li class="list-group-item">Créer des présentations interactives de contenu</li>
            <li class="list-group-item">Mettre en valeur des ressources ou des activités</li>
          </ul>

          <div class="card">
            <div class="card-body">
              <h3 class="h5">Exemple avec Mustache</h3>
              <pre class="bg-light p-3 rounded"><code>{{#carousel}}
&lt;div id="carousel-{{uniqid}}" class="carousel slide" data-bs-ride="carousel"&gt;
  &lt;div class="carousel-inner"&gt;
    {{#slides}}
    &lt;div class="carousel-item {{#active}}active{{/active}}"&gt;
      &lt;img src="{{image}}" class="d-block w-100" alt="{{alt}}" /&gt;
      {{#caption}}
      &lt;div class="carousel-caption d-none d-md-block"&gt;
        &lt;h5&gt;{{title}}&lt;/h5&gt;
        &lt;p&gt;{{text}}&lt;/p&gt;
      &lt;/div&gt;
      {{/caption}}
    &lt;/div&gt;
    {{/slides}}
  &lt;/div&gt;
  &lt;button
    class="carousel-control-prev"
    type="button"
    data-bs-target="#carousel-{{uniqid}}"
    data-bs-slide="prev"
  &gt;
    &lt;span class="carousel-control-prev-icon" aria-hidden="true"&gt;&lt;/span&gt;
    &lt;span class="visually-hidden"&gt;{{#str}}previous{{/str}}&lt;/span&gt;
  &lt;/button&gt;
  &lt;button
    class="carousel-control-next"
    type="button"
    data-bs-target="#carousel-{{uniqid}}"
    data-bs-slide="next"
  &gt;
    &lt;span class="carousel-control-next-icon" aria-hidden="true"&gt;&lt;/span&gt;
    &lt;span class="visually-hidden"&gt;{{#str}}next{{/str}}&lt;/span&gt;
  &lt;/button&gt;
&lt;/div&gt;
{{/carousel}}</code></pre>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</div>
