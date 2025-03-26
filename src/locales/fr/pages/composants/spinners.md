---
title: Spinners
description: Documentation du composant Spinners de Bootstrap 5 pour Moodle
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
          <p class="lead">Les spinners sont des indicateurs de chargement animés qui permettent de montrer visuellement qu'une action est en cours. Ils sont idéaux pour les opérations asynchrones comme le chargement de contenu ou le traitement de formulaires.</p>
        </div>

        <div id="exemple-base" class="mt-5">
          <h2>Exemple de base</h2>
          <p>Un spinner simple avec animation de rotation.</p>
          <div class="card mb-4">
            <div class="card-body">
              <div class="component-preview">
                <div class="spinner-border" role="status">
                  <span class="visually-hidden">Chargement...</span>
                </div>
              </div>
            </div>
          </div>
        </div>

        <div id="styles" class="mt-5">
          <h2>Styles</h2>

          <div class="card mb-4">
            <div class="card-body">
              <h3 class="h5">Spinners avec couleurs</h3>
              <p>Les spinners peuvent utiliser différentes couleurs pour s'adapter au contexte.</p>
              <div class="component-preview">
                <div class="spinner-border text-primary me-3" role="status">
                  <span class="visually-hidden">Chargement...</span>
                </div>
                <div class="spinner-border text-success me-3" role="status">
                  <span class="visually-hidden">Chargement...</span>
                </div>
                <div class="spinner-border text-danger me-3" role="status">
                  <span class="visually-hidden">Chargement...</span>
                </div>
                <div class="spinner-border text-warning me-3" role="status">
                  <span class="visually-hidden">Chargement...</span>
                </div>
                <div class="spinner-border text-info" role="status">
                  <span class="visually-hidden">Chargement...</span>
                </div>
              </div>
            </div>
          </div>

          <div class="card mb-4">
            <div class="card-body">
              <h3 class="h5">Spinners de différentes tailles</h3>
              <p>Les spinners peuvent être affichés dans différentes tailles.</p>
              <div class="component-preview">
                <div class="spinner-border spinner-border-sm me-3" role="status">
                  <span class="visually-hidden">Chargement...</span>
                </div>
                <div class="spinner-border me-3" role="status">
                  <span class="visually-hidden">Chargement...</span>
                </div>
                <div class="spinner-border" style="width: 3rem; height: 3rem;" role="status">
                  <span class="visually-hidden">Chargement...</span>
                </div>
              </div>
            </div>
          </div>

          <div class="card mb-4">
            <div class="card-body">
              <h3 class="h5">Spinners avec texte</h3>
              <p>Les spinners peuvent être accompagnés de texte pour plus de contexte.</p>
              <div class="component-preview">
                <div class="d-flex align-items-center">
                  <div class="spinner-border me-3" role="status">
                    <span class="visually-hidden">Chargement...</span>
                  </div>
                  <span>Chargement des données...</span>
                </div>
              </div>
            </div>
          </div>
        </div>

        <div id="utilisation-moodle" class="mt-5">
          <h2>Utilisation dans Moodle</h2>
          <p>Dans Moodle, les spinners sont utilisés pour :</p>
          <ul class="list-group mb-4">
            <li class="list-group-item">Indiquer le chargement d'une page</li>
            <li class="list-group-item">Montrer le traitement d'un formulaire</li>
            <li class="list-group-item">Signaler une synchronisation en cours</li>
            <li class="list-group-item">Indiquer le chargement de contenu dynamique</li>
            <li class="list-group-item">Montrer le traitement d'une action asynchrone</li>
          </ul>

          <div class="card mb-4">
            <div class="card-body">
              <h3 class="h5">Exemple d'intégration dans un template Moodle</h3>
              <pre class="bg-light p-3 rounded"><code>{{#is_loading}}
    &lt;div class="d-flex align-items-center"&gt;
        &lt;div class="spinner-border {{#color}}text-{{color}}{{/color}} {{#size}}spinner-border-{{size}}{{/size}}"
             role="status"&gt;
            &lt;span class="visually-hidden"&gt;{{loading_text}}&lt;/span&gt;
        &lt;/div&gt;
        {{#show_text}}
        &lt;span class="ms-3"&gt;{{loading_text}}&lt;/span&gt;
        {{/show_text}}
    &lt;/div&gt;
{{/is_loading}}</code></pre>
            </div>
          </div>
        </div>

        <div id="accessibilite" class="mt-5">
          <h2>Accessibilité</h2>
          <ul class="list-group mb-4">
            <li class="list-group-item">Utilisez l'attribut `role="status"`</li>
            <li class="list-group-item">Fournissez un texte alternatif avec `visually-hidden`</li>
            <li class="list-group-item">Assurez-vous que l'animation n'est pas trop rapide</li>
            <li class="list-group-item">Permettez aux utilisateurs de réduire les animations si nécessaire</li>
            <li class="list-group-item">Évitez d'utiliser des spinners pour des actions longues</li>
          </ul>
        </div>
      </div>
    </div>
  </div>
</div>