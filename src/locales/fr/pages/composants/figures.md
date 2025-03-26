---
title: Figures
description: Documentation du composant Figures de Bootstrap 5 pour Moodle
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
          <p class="lead">Les figures sont des composants qui associent sémantiquement une image à sa légende. Elles permettent de présenter des illustrations avec leur contexte de manière élégante.</p>
        </div>

        <div id="exemple-base" class="mt-5">
          <h2>Exemple de base</h2>
          <p>Une figure simple avec une image et une légende.</p>
          <div class="card mb-4">
            <div class="card-body">
              <div class="component-preview">
                <figure class="figure">
                  <img src="https://placehold.co/400x300" class="figure-img img-fluid rounded" alt="Image d'exemple">
                  <figcaption class="figure-caption">Une légende pour l'image.</figcaption>
                </figure>
              </div>
            </div>
          </div>
        </div>

        <div id="styles" class="mt-5">
          <h2>Styles</h2>

          <div class="card mb-4">
            <div class="card-body">
              <h3 class="h5">Figures avec légendes alignées</h3>
              <p>Les légendes peuvent être alignées de différentes manières.</p>
              <div class="component-preview">
                <figure class="figure">
                  <img src="https://placehold.co/400x300" class="figure-img img-fluid rounded" alt="Image avec légende alignée à gauche">
                  <figcaption class="figure-caption text-start">Légende alignée à gauche.</figcaption>
                </figure>
                <figure class="figure">
                  <img src="https://placehold.co/400x300" class="figure-img img-fluid rounded" alt="Image avec légende centrée">
                  <figcaption class="figure-caption text-center">Légende centrée.</figcaption>
                </figure>
                <figure class="figure">
                  <img src="https://placehold.co/400x300" class="figure-img img-fluid rounded" alt="Image avec légende alignée à droite">
                  <figcaption class="figure-caption text-end">Légende alignée à droite.</figcaption>
                </figure>
              </div>
            </div>
          </div>

          <div class="card mb-4">
            <div class="card-body">
              <h3 class="h5">Figures avec styles personnalisés</h3>
              <p>Les figures peuvent avoir des styles personnalisés.</p>
              <div class="component-preview">
                <figure class="figure">
                  <img src="https://placehold.co/400x300" class="figure-img img-fluid rounded shadow" alt="Image avec ombre">
                  <figcaption class="figure-caption">Figure avec ombre.</figcaption>
                </figure>
                <figure class="figure">
                  <img src="https://placehold.co/400x300" class="figure-img img-fluid rounded-pill" alt="Image avec coins arrondis">
                  <figcaption class="figure-caption">Figure avec coins arrondis.</figcaption>
                </figure>
              </div>
            </div>
          </div>

          <div class="card mb-4">
            <div class="card-body">
              <h3 class="h5">Figures avec contenu riche</h3>
              <p>Les figures peuvent contenir du contenu riche dans leur légende.</p>
              <div class="component-preview">
                <figure class="figure">
                  <img src="https://placehold.co/400x300" class="figure-img img-fluid rounded" alt="Image avec contenu riche">
                  <figcaption class="figure-caption">
                    <h5>Titre de la figure</h5>
                    <p>Description détaillée de la figure avec du texte supplémentaire.</p>
                    <small>Informations complémentaires</small>
                  </figcaption>
                </figure>
              </div>
            </div>
          </div>
        </div>

        <div id="utilisation-moodle" class="mt-5">
          <h2>Utilisation dans Moodle</h2>
          <p>Dans Moodle, les figures sont utilisées pour :</p>
          <ul class="list-group mb-4">
            <li class="list-group-item">Illustrer des concepts pédagogiques</li>
            <li class="list-group-item">Présenter des diagrammes</li>
            <li class="list-group-item">Montrer des exemples visuels</li>
            <li class="list-group-item">Documenter des procédures</li>
            <li class="list-group-item">Afficher des graphiques et statistiques</li>
          </ul>

          <div class="card mb-4">
            <div class="card-body">
              <h3 class="h5">Exemple d'intégration dans un template Moodle</h3>
              <pre class="bg-light p-3 rounded"><code>{{#figure}}
    &lt;figure class="figure {{#style}}figure-{{style}}{{/style}}"&gt;
        &lt;img src="{{src}}"
             class="figure-img img-fluid {{#rounded}}rounded{{/rounded}} {{#shadow}}shadow{{/shadow}}"
             alt="{{alt}}"
             {{#width}}width="{{width}}"{{/width}}
             {{#height}}height="{{height}}"{{/height}}&gt;
        &lt;figcaption class="figure-caption {{#align}}text-{{align}}{{/align}}"&gt;
            {{#title}}
            &lt;h5&gt;{{title}}&lt;/h5&gt;
            {{/title}}
            {{#text}}
            &lt;p&gt;{{text}}&lt;/p&gt;
            {{/text}}
            {{#small}}
            &lt;small&gt;{{small}}&lt;/small&gt;
            {{/small}}
        &lt;/figcaption&gt;
    &lt;/figure&gt;
{{/figure}}</code></pre>
            </div>
          </div>
        </div>

        <div id="accessibilite" class="mt-5">
          <h2>Accessibilité</h2>
          <ul class="list-group mb-4">
            <li class="list-group-item">Fournissez toujours un texte alternatif descriptif pour l'image</li>
            <li class="list-group-item">Utilisez des légendes claires et descriptives</li>
            <li class="list-group-item">Maintenez un contraste suffisant pour le texte</li>
            <li class="list-group-item">Structurez le contenu de la légende de manière logique</li>
            <li class="list-group-item">Assurez-vous que les figures sont accessibles au clavier</li>
          </ul>
        </div>
      </div>
    </div>
  </div>
</div>