---
title: Popovers
description: Documentation du composant Popovers de Bootstrap 5 pour Moodle
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
          <p class="lead">Les popovers sont des fenêtres contextuelles qui apparaissent au clic sur un élément pour afficher des informations supplémentaires ou des actions. Ils sont plus complexes que les tooltips et peuvent contenir du contenu riche.</p>
        </div>

        <div id="exemple-base" class="mt-5">
          <h2>Exemple de base</h2>
          <p>Un popover simple avec un titre et un contenu.</p>
          <div class="card mb-4">
            <div class="card-body">
              <div class="component-preview">
                <button type="button" class="btn btn-primary" data-bs-toggle="popover" title="Titre du popover" data-bs-content="Ceci est le contenu du popover.">
                  Cliquez-moi
                </button>
              </div>
            </div>
          </div>
        </div>

        <div id="styles" class="mt-5">
          <h2>Styles</h2>

          <div class="card mb-4">
            <div class="card-body">
              <h3 class="h5">Popovers avec placement</h3>
              <p>Les popovers peuvent apparaître à différentes positions par rapport à l'élément.</p>
              <div class="component-preview">
                <div class="d-flex gap-3 justify-content-center">
                  <button type="button" class="btn btn-primary" data-bs-toggle="popover" data-bs-placement="top" title="Popover en haut" data-bs-content="Contenu du popover en haut.">
                    Haut
                  </button>
                  <button type="button" class="btn btn-primary" data-bs-toggle="popover" data-bs-placement="right" title="Popover à droite" data-bs-content="Contenu du popover à droite.">
                    Droite
                  </button>
                  <button type="button" class="btn btn-primary" data-bs-toggle="popover" data-bs-placement="bottom" title="Popover en bas" data-bs-content="Contenu du popover en bas.">
                    Bas
                  </button>
                  <button type="button" class="btn btn-primary" data-bs-toggle="popover" data-bs-placement="left" title="Popover à gauche" data-bs-content="Contenu du popover à gauche.">
                    Gauche
                  </button>
                </div>
              </div>
            </div>
          </div>

          <div class="card mb-4">
            <div class="card-body">
              <h3 class="h5">Popovers avec HTML</h3>
              <p>Les popovers peuvent contenir du contenu HTML riche.</p>
              <div class="component-preview">
                <button type="button" class="btn btn-primary" data-bs-toggle="popover" data-bs-html="true" title="<em>Popover</em> avec <strong>HTML</strong>" data-bs-content="<ul><li>Liste d'éléments</li><li>Plus de contenu</li><li>Et encore plus</li></ul>">
                  HTML
                </button>
              </div>
            </div>
          </div>

          <div class="card mb-4">
            <div class="card-body">
              <h3 class="h5">Popovers avec délai</h3>
              <p>Les popovers peuvent avoir un délai d'apparition et de disparition.</p>
              <div class="component-preview">
                <button type="button" class="btn btn-primary" data-bs-toggle="popover" data-bs-delay='{"show": 500, "hide": 100}' title="Popover avec délai" data-bs-content="Ce popover apparaît après un délai.">
                  Délai
                </button>
              </div>
            </div>
          </div>
        </div>

        <div id="utilisation-moodle" class="mt-5">
          <h2>Utilisation dans Moodle</h2>
          <p>Dans Moodle, les popovers sont utilisés pour :</p>
          <ul class="list-group mb-4">
            <li class="list-group-item">Afficher des détails sur les activités</li>
            <li class="list-group-item">Fournir des options de configuration rapides</li>
            <li class="list-group-item">Montrer des aperçus de contenu</li>
            <li class="list-group-item">Afficher des actions contextuelles</li>
            <li class="list-group-item">Fournir des informations détaillées sur les éléments</li>
          </ul>

          <div class="card mb-4">
            <div class="card-body">
              <h3 class="h5">Exemple d'intégration dans un template Moodle</h3>
              <pre class="bg-light p-3 rounded"><code>{{#has_popover}}
    &lt;button type="button"
            class="btn {{#style}}btn-{{style}}{{/style}}"
            data-bs-toggle="popover"
            data-bs-placement="{{placement}}"
            {{#html}}data-bs-html="true"{{/html}}
            {{#delay}}data-bs-delay='{"show": {{show}}, "hide": {{hide}}}'{{/delay}}
            title="{{title}}"
            data-bs-content="{{content}}"&gt;
        {{button_text}}
    &lt;/button&gt;
{{/has_popover}}

&lt;script&gt;
document.addEventListener('DOMContentLoaded', function() {
    // Initialiser tous les popovers
    var popoverTriggerList = [].slice.call(document.querySelectorAll('[data-bs-toggle="popover"]'))
    var popoverList = popoverTriggerList.map(function (popoverTriggerEl) {
        return new bootstrap.Popover(popoverTriggerEl)
    })
})
&lt;/script&gt;</code></pre>
            </div>
          </div>
        </div>

        <div id="accessibilite" class="mt-5">
          <h2>Accessibilité</h2>
          <ul class="list-group mb-4">
            <li class="list-group-item">Assurez-vous que le contenu est accessible au clavier</li>
            <li class="list-group-item">Fournissez des alternatives pour les utilisateurs qui ne peuvent pas utiliser la souris</li>
            <li class="list-group-item">Maintenez un contraste suffisant pour le texte</li>
            <li class="list-group-item">Évitez d'utiliser des popovers pour des informations essentielles</li>
            <li class="list-group-item">Permettez aux utilisateurs de contrôler le délai d'apparition</li>
          </ul>
        </div>
      </div>
    </div>
  </div>
</div>