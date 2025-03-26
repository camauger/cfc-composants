---
title: Images
description: Documentation du composant Images de Bootstrap 5 pour Moodle
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
          <p class="lead">Les images sont des composants essentiels pour enrichir le contenu visuel. Bootstrap 5 offre plusieurs styles et classes utilitaires pour gérer l'affichage et la mise en page des images.</p>
        </div>

        <div id="exemple-base" class="mt-5">
          <h2>Exemple de base</h2>
          <p>Une image simple avec la classe de base.</p>
          <div class="card mb-4">
            <div class="card-body">
              <div class="component-preview">
                <img src="https://placehold.co/300x200" class="img-fluid" alt="Image d'exemple">
              </div>
            </div>
          </div>
        </div>

        <div id="styles" class="mt-5">
          <h2>Styles</h2>

          <div class="card mb-4">
            <div class="card-body">
              <h3 class="h5">Images responsives</h3>
              <p>Les images peuvent être rendues responsives pour s'adapter à leur conteneur.</p>
              <div class="component-preview">
                <img src="https://placehold.co/800x400" class="img-fluid" alt="Image responsive">
              </div>
            </div>
          </div>

          <div class="card mb-4">
            <div class="card-body">
              <h3 class="h5">Images avec coins arrondis</h3>
              <p>Les images peuvent avoir des coins arrondis.</p>
              <div class="component-preview">
                <img src="https://placehold.co/200x200" class="rounded" alt="Image avec coins arrondis">
                <img src="https://placehold.co/200x200" class="rounded-circle ms-3" alt="Image circulaire">
              </div>
            </div>
          </div>

          <div class="card mb-4">
            <div class="card-body">
              <h3 class="h5">Images avec ombres</h3>
              <p>Les images peuvent avoir des ombres pour plus de profondeur.</p>
              <div class="component-preview">
                <img src="https://placehold.co/200x200" class="shadow" alt="Image avec ombre">
                <img src="https://placehold.co/200x200" class="shadow-sm ms-3" alt="Image avec ombre légère">
              </div>
            </div>
          </div>

          <div class="card mb-4">
            <div class="card-body">
              <h3 class="h5">Images avec légendes</h3>
              <p>Les images peuvent inclure des légendes.</p>
              <div class="component-preview">
                <figure class="figure">
                  <img src="https://placehold.co/400x300" class="figure-img img-fluid rounded" alt="Image avec légende">
                  <figcaption class="figure-caption">Une légende pour l'image.</figcaption>
                </figure>
              </div>
            </div>
          </div>
        </div>

        <div id="utilisation-moodle" class="mt-5">
          <h2>Utilisation dans Moodle</h2>
          <p>Dans Moodle, les images sont utilisées pour :</p>
          <ul class="list-group mb-4">
            <li class="list-group-item">Illustrer le contenu des cours</li>
            <li class="list-group-item">Afficher les avatars des utilisateurs</li>
            <li class="list-group-item">Présenter des ressources pédagogiques</li>
            <li class="list-group-item">Montrer des captures d'écran</li>
            <li class="list-group-item">Enrichir les activités interactives</li>
          </ul>

          <div class="card mb-4">
            <div class="card-body">
              <h3 class="h5">Exemple d'intégration dans un template Moodle</h3>
              <pre class="bg-light p-3 rounded"><code>{{#image}}
    &lt;figure class="figure {{#fluid}}img-fluid{{/fluid}} {{#rounded}}rounded{{/rounded}} {{#circle}}rounded-circle{{/circle}} {{#shadow}}shadow{{/shadow}}"&gt;
        &lt;img src="{{src}}"
             class="figure-img {{#fluid}}img-fluid{{/fluid}}"
             alt="{{alt}}"
             {{#width}}width="{{width}}"{{/width}}
             {{#height}}height="{{height}}"{{/height}}&gt;
        {{#caption}}
        &lt;figcaption class="figure-caption"&gt;{{caption}}&lt;/figcaption&gt;
        {{/caption}}
    &lt;/figure&gt;
{{/image}}</code></pre>
            </div>
          </div>
        </div>

        <div id="accessibilite" class="mt-5">
          <h2>Accessibilité</h2>
          <ul class="list-group mb-4">
            <li class="list-group-item">Fournissez toujours un texte alternatif descriptif</li>
            <li class="list-group-item">Utilisez des images de haute qualité et optimisées</li>
            <li class="list-group-item">Maintenez un contraste suffisant pour les images contenant du texte</li>
            <li class="list-group-item">Évitez d'utiliser des images pour du texte</li>
            <li class="list-group-item">Fournissez des descriptions détaillées pour les images complexes</li>
          </ul>
        </div>
      </div>
    </div>
  </div>
</div>