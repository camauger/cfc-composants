---
title: Tooltips
description: Documentation du composant Tooltips de Bootstrap 5 pour Moodle
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
          <p class="lead">Les tooltips sont des infobulles qui apparaissent au survol d'un élément pour fournir des informations supplémentaires ou des explications. Ils sont idéaux pour les icônes, les boutons ou les éléments qui nécessitent plus de contexte.</p>
        </div>

        <div id="exemple-base" class="mt-5">
          <h2>Exemple de base</h2>
          <p>Un tooltip simple qui apparaît au survol d'un bouton.</p>
          <div class="card mb-4">
            <div class="card-body">
              <div class="component-preview">
                <button type="button" class="btn btn-primary" data-bs-toggle="tooltip" data-bs-placement="top" title="Ceci est un tooltip">
                  Survolez-moi
                </button>
              </div>
            </div>
          </div>
        </div>

        <div id="styles" class="mt-5">
          <h2>Styles</h2>

          <div class="card mb-4">
            <div class="card-body">
              <h3 class="h5">Tooltips avec placement</h3>
              <p>Les tooltips peuvent apparaître à différentes positions par rapport à l'élément.</p>
              <div class="component-preview">
                <div class="d-flex gap-3 justify-content-center">
                  <button type="button" class="btn btn-primary" data-bs-toggle="tooltip" data-bs-placement="top" title="Tooltip en haut">
                    Haut
                  </button>
                  <button type="button" class="btn btn-primary" data-bs-toggle="tooltip" data-bs-placement="right" title="Tooltip à droite">
                    Droite
                  </button>
                  <button type="button" class="btn btn-primary" data-bs-toggle="tooltip" data-bs-placement="bottom" title="Tooltip en bas">
                    Bas
                  </button>
                  <button type="button" class="btn btn-primary" data-bs-toggle="tooltip" data-bs-placement="left" title="Tooltip à gauche">
                    Gauche
                  </button>
                </div>
              </div>
            </div>
          </div>

          <div class="card mb-4">
            <div class="card-body">
              <h3 class="h5">Tooltips avec HTML</h3>
              <p>Les tooltips peuvent contenir du contenu HTML pour plus de richesse.</p>
              <div class="component-preview">
                <button type="button" class="btn btn-primary" data-bs-toggle="tooltip" data-bs-html="true" title="<em>Emphase</em> et <strong>gras</strong>">
                  HTML
                </button>
              </div>
            </div>
          </div>

          <div class="card mb-4">
            <div class="card-body">
              <h3 class="h5">Tooltips avec délai</h3>
              <p>Les tooltips peuvent avoir un délai d'apparition et de disparition.</p>
              <div class="component-preview">
                <button type="button" class="btn btn-primary" data-bs-toggle="tooltip" data-bs-delay='{"show": 500, "hide": 100}' title="Tooltip avec délai">
                  Délai
                </button>
              </div>
            </div>
          </div>
        </div>

        <div id="utilisation-moodle" class="mt-5">
          <h2>Utilisation dans Moodle</h2>
          <p>Dans Moodle, les tooltips sont utilisés pour :</p>
          <ul class="list-group mb-4">
            <li class="list-group-item">Expliquer le fonctionnement des boutons</li>
            <li class="list-group-item">Fournir des informations sur les icônes</li>
            <li class="list-group-item">Afficher des raccourcis clavier</li>
            <li class="list-group-item">Expliquer les options de configuration</li>
            <li class="list-group-item">Fournir des conseils d'utilisation</li>
          </ul>

          <div class="card mb-4">
            <div class="card-body">
              <h3 class="h5">Exemple d'intégration dans un template Moodle</h3>
              <pre class="bg-light p-3 rounded"><code>{{#has_tooltip}}
    &lt;button type="button"
            class="btn {{#style}}btn-{{style}}{{/style}}"
            data-bs-toggle="tooltip"
            data-bs-placement="{{placement}}"
            {{#html}}data-bs-html="true"{{/html}}
            {{#delay}}data-bs-delay='{"show": {{show}}, "hide": {{hide}}}'{{/delay}}
            title="{{title}}"&gt;
        {{content}}
    &lt;/button&gt;
{{/has_tooltip}}

&lt;script&gt;
document.addEventListener('DOMContentLoaded', function() {
    // Initialiser tous les tooltips
    var tooltipTriggerList = [].slice.call(document.querySelectorAll('[data-bs-toggle="tooltip"]'))
    var tooltipList = tooltipTriggerList.map(function (tooltipTriggerEl) {
        return new bootstrap.Tooltip(tooltipTriggerEl)
    })
})
&lt;/script&gt;</code></pre>
            </div>
          </div>
        </div>

        <div id="accessibilite" class="mt-5">
          <h2>Accessibilité</h2>
          <ul class="list-group mb-4">
            <li class="list-group-item">Fournissez des alternatives pour les utilisateurs qui ne peuvent pas utiliser la souris</li>
            <li class="list-group-item">Assurez-vous que le contenu est accessible au clavier</li>
            <li class="list-group-item">Maintenez un contraste suffisant pour le texte</li>
            <li class="list-group-item">Évitez d'utiliser des tooltips pour des informations essentielles</li>
            <li class="list-group-item">Permettez aux utilisateurs de contrôler le délai d'apparition</li>
          </ul>
        </div>
      </div>
    </div>
  </div>
</div>