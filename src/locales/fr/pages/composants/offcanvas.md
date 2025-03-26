---
title: Offcanvas
description: Documentation du composant Offcanvas de Bootstrap 5 pour Moodle
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
          <p class="lead">Les offcanvas sont des panneaux latéraux qui glissent depuis les bords de l'écran. Ils sont idéaux pour afficher des menus, des formulaires ou des contenus supplémentaires sans quitter la page principale.</p>
        </div>

        <div id="exemple-base" class="mt-5">
          <h2>Exemple de base</h2>
          <p>Un offcanvas simple qui s'ouvre depuis la droite.</p>
          <div class="card mb-4">
            <div class="card-body">
              <div class="component-preview">
                <button class="btn btn-primary" type="button" data-bs-toggle="offcanvas" data-bs-target="#offcanvasExample" aria-controls="offcanvasExample">
                  Ouvrir l'offcanvas
                </button>

                <div class="offcanvas offcanvas-end" tabindex="-1" id="offcanvasExample" aria-labelledby="offcanvasExampleLabel">
                  <div class="offcanvas-header">
                    <h5 class="offcanvas-title" id="offcanvasExampleLabel">Titre de l'offcanvas</h5>
                    <button type="button" class="btn-close" data-bs-dismiss="offcanvas" aria-label="Fermer"></button>
                  </div>
                  <div class="offcanvas-body">
                    <div>
                      Ceci est le contenu de l'offcanvas. Vous pouvez y mettre n'importe quel contenu.
                    </div>
                  </div>
                </div>
              </div>
            </div>
          </div>
        </div>

        <div id="styles" class="mt-5">
          <h2>Styles</h2>

          <div class="card mb-4">
            <div class="card-body">
              <h3 class="h5">Offcanvas avec placement</h3>
              <p>Les offcanvas peuvent s'ouvrir depuis différents côtés de l'écran.</p>
              <div class="component-preview">
                <div class="d-flex gap-3 justify-content-center">
                  <button class="btn btn-primary" type="button" data-bs-toggle="offcanvas" data-bs-target="#offcanvasTop" aria-controls="offcanvasTop">
                    Haut
                  </button>
                  <button class="btn btn-primary" type="button" data-bs-toggle="offcanvas" data-bs-target="#offcanvasEnd" aria-controls="offcanvasEnd">
                    Droite
                  </button>
                  <button class="btn btn-primary" type="button" data-bs-toggle="offcanvas" data-bs-target="#offcanvasBottom" aria-controls="offcanvasBottom">
                    Bas
                  </button>
                  <button class="btn btn-primary" type="button" data-bs-toggle="offcanvas" data-bs-target="#offcanvasStart" aria-controls="offcanvasStart">
                    Gauche
                  </button>
                </div>

                <div class="offcanvas offcanvas-top" tabindex="-1" id="offcanvasTop" aria-labelledby="offcanvasTopLabel">
                  <div class="offcanvas-header">
                    <h5 class="offcanvas-title" id="offcanvasTopLabel">Offcanvas en haut</h5>
                    <button type="button" class="btn-close" data-bs-dismiss="offcanvas" aria-label="Fermer"></button>
                  </div>
                  <div class="offcanvas-body">
                    Contenu de l'offcanvas en haut
                  </div>
                </div>

                <div class="offcanvas offcanvas-end" tabindex="-1" id="offcanvasEnd" aria-labelledby="offcanvasEndLabel">
                  <div class="offcanvas-header">
                    <h5 class="offcanvas-title" id="offcanvasEndLabel">Offcanvas à droite</h5>
                    <button type="button" class="btn-close" data-bs-dismiss="offcanvas" aria-label="Fermer"></button>
                  </div>
                  <div class="offcanvas-body">
                    Contenu de l'offcanvas à droite
                  </div>
                </div>

                <div class="offcanvas offcanvas-bottom" tabindex="-1" id="offcanvasBottom" aria-labelledby="offcanvasBottomLabel">
                  <div class="offcanvas-header">
                    <h5 class="offcanvas-title" id="offcanvasBottomLabel">Offcanvas en bas</h5>
                    <button type="button" class="btn-close" data-bs-dismiss="offcanvas" aria-label="Fermer"></button>
                  </div>
                  <div class="offcanvas-body">
                    Contenu de l'offcanvas en bas
                  </div>
                </div>

                <div class="offcanvas offcanvas-start" tabindex="-1" id="offcanvasStart" aria-labelledby="offcanvasStartLabel">
                  <div class="offcanvas-header">
                    <h5 class="offcanvas-title" id="offcanvasStartLabel">Offcanvas à gauche</h5>
                    <button type="button" class="btn-close" data-bs-dismiss="offcanvas" aria-label="Fermer"></button>
                  </div>
                  <div class="offcanvas-body">
                    Contenu de l'offcanvas à gauche
                  </div>
                </div>
              </div>
            </div>
          </div>

          <div class="card mb-4">
            <div class="card-body">
              <h3 class="h5">Offcanvas avec fond sombre</h3>
              <p>Les offcanvas peuvent avoir un fond sombre pour un meilleur contraste.</p>
              <div class="component-preview">
                <button class="btn btn-primary" type="button" data-bs-toggle="offcanvas" data-bs-target="#offcanvasDark" aria-controls="offcanvasDark">
                  Ouvrir l'offcanvas sombre
                </button>

                <div class="offcanvas offcanvas-end bg-dark text-white" tabindex="-1" id="offcanvasDark" aria-labelledby="offcanvasDarkLabel">
                  <div class="offcanvas-header">
                    <h5 class="offcanvas-title" id="offcanvasDarkLabel">Offcanvas sombre</h5>
                    <button type="button" class="btn-close btn-close-white" data-bs-dismiss="offcanvas" aria-label="Fermer"></button>
                  </div>
                  <div class="offcanvas-body">
                    Contenu de l'offcanvas avec fond sombre
                  </div>
                </div>
              </div>
            </div>
          </div>

          <div class="card mb-4">
            <div class="card-body">
              <h3 class="h5">Offcanvas avec scrolling</h3>
              <p>Les offcanvas peuvent avoir un défilement indépendant.</p>
              <div class="component-preview">
                <button class="btn btn-primary" type="button" data-bs-toggle="offcanvas" data-bs-target="#offcanvasScroll" aria-controls="offcanvasScroll">
                  Ouvrir l'offcanvas avec défilement
                </button>

                <div class="offcanvas offcanvas-end" tabindex="-1" id="offcanvasScroll" aria-labelledby="offcanvasScrollLabel">
                  <div class="offcanvas-header">
                    <h5 class="offcanvas-title" id="offcanvasScrollLabel">Offcanvas avec défilement</h5>
                    <button type="button" class="btn-close" data-bs-dismiss="offcanvas" aria-label="Fermer"></button>
                  </div>
                  <div class="offcanvas-body">
                    <p>Contenu avec défilement...</p>
                    <p>Ligne après ligne...</p>
                    <p>Pour tester le défilement...</p>
                    <p>Ajoutez beaucoup de contenu...</p>
                    <p>Jusqu'à ce que la barre de défilement apparaisse...</p>
                  </div>
                </div>
              </div>
            </div>
          </div>
        </div>

        <div id="utilisation-moodle" class="mt-5">
          <h2>Utilisation dans Moodle</h2>
          <p>Dans Moodle, les offcanvas sont utilisés pour :</p>
          <ul class="list-group mb-4">
            <li class="list-group-item">Afficher des menus de navigation mobiles</li>
            <li class="list-group-item">Montrer des formulaires de configuration</li>
            <li class="list-group-item">Afficher des détails sur les activités</li>
            <li class="list-group-item">Fournir des options de personnalisation</li>
            <li class="list-group-item">Afficher des aides contextuelles</li>
          </ul>

          <div class="card mb-4">
            <div class="card-body">
              <h3 class="h5">Exemple d'intégration dans un template Moodle</h3>
              <pre class="bg-light p-3 rounded"><code>{{#has_offcanvas}}
    &lt;button class="btn {{#style}}btn-{{style}}{{/style}}"
            type="button"
            data-bs-toggle="offcanvas"
            data-bs-target="#{{id}}"
            aria-controls="{{id}}"&gt;
        {{button_text}}
    &lt;/button&gt;

    &lt;div class="offcanvas {{#placement}}offcanvas-{{placement}}{{/placement}} {{#dark}}bg-dark text-white{{/dark}}"
         tabindex="-1"
         id="{{id}}"
         aria-labelledby="{{id}}Label"&gt;
        &lt;div class="offcanvas-header"&gt;
            &lt;h5 class="offcanvas-title" id="{{id}}Label"&gt;{{title}}&lt;/h5&gt;
            &lt;button type="button"
                    class="btn-close {{#dark}}btn-close-white{{/dark}}"
                    data-bs-dismiss="offcanvas"
                    aria-label="Fermer"&gt;
            &lt;/button&gt;
        &lt;/div&gt;
        &lt;div class="offcanvas-body"&gt;
            {{content}}
        &lt;/div&gt;
    &lt;/div&gt;
{{/has_offcanvas}}</code></pre>
            </div>
          </div>
        </div>

        <div id="accessibilite" class="mt-5">
          <h2>Accessibilité</h2>
          <ul class="list-group mb-4">
            <li class="list-group-item">Utilisez des attributs ARIA appropriés</li>
            <li class="list-group-item">Gérez correctement le focus lors de l'ouverture/fermeture</li>
            <li class="list-group-item">Maintenez un contraste suffisant pour le texte</li>
            <li class="list-group-item">Fournissez des alternatives pour les utilisateurs qui ne peuvent pas utiliser la souris</li>
            <li class="list-group-item">Assurez-vous que le contenu est accessible au clavier</li>
          </ul>
        </div>
      </div>
    </div>
  </div>
</div>