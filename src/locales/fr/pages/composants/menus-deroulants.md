---
title: Menus déroulants
description: Documentation du composant Menus déroulants de Bootstrap 5 pour Moodle
template: pages/composant.html
---

<div class="container py-4">
  <div class="row">
    <div class="col-lg-3">
      <nav id="navbar-example3" class="h-100 flex-column align-items-stretch pe-4 border-end">
        <nav class="nav nav-pills flex-column">
          <a class="nav-link" href="#description">Description</a>
          <a class="nav-link" href="#exemples-base">Exemples de base</a>
          <a class="nav-link" href="#variantes">Variantes</a>
          <a class="nav-link" href="#sous-menus">Sous-menus</a>
          <a class="nav-link" href="#alignement">Alignement</a>
          <a class="nav-link" href="#utilisation-moodle">Utilisation dans Moodle</a>
          <a class="nav-link" href="#accessibilite">Accessibilité</a>
        </nav>
      </nav>
    </div>

    <div class="col-lg-9">
      <div data-bs-spy="scroll" data-bs-target="#navbar-example3" data-bs-smooth-scroll="true" class="scrollspy-example-2" tabindex="0">
        <div id="description">
          <h2>Description</h2>
          <p class="lead">Les menus déroulants Bootstrap sont des composants interactifs qui permettent d'afficher une liste de liens ou d'actions dans un menu contextuel.</p>
        </div>

        <div id="exemples-base" class="mt-5">
          <h2>Exemples de base</h2>
          <p>Les menus déroulants sont construits à l'aide des classes Bootstrap et nécessitent le JavaScript de Bootstrap pour fonctionner.</p>

          <div class="card mb-4">
            <div class="card-body">
              <div class="component-preview">
                <div class="dropdown">
                  <button class="btn btn-secondary dropdown-toggle" type="button" id="dropdownMenuButton" data-bs-toggle="dropdown" aria-expanded="false">
                    Menu déroulant
                  </button>
                  <ul class="dropdown-menu" aria-labelledby="dropdownMenuButton">
                    <li><a class="dropdown-item" href="#">Action</a></li>
                    <li><a class="dropdown-item" href="#">Autre action</a></li>
                    <li><hr class="dropdown-divider"></li>
                    <li><a class="dropdown-item" href="#">Quelque chose d'autre</a></li>
                  </ul>
                </div>
              </div>
            </div>
          </div>
        </div>

        <div id="variantes" class="mt-5">
          <h2>Variantes</h2>
          <p>Les menus déroulants peuvent être déclenchés à partir de différents types de boutons.</p>

          <div class="card mb-4">
            <div class="card-body">
              <div class="component-preview">
                <div class="btn-group">
                  <button type="button" class="btn btn-primary dropdown-toggle" data-bs-toggle="dropdown" aria-expanded="false">
                    Primary
                  </button>
                  <ul class="dropdown-menu">
                    <li><a class="dropdown-item" href="#">Action</a></li>
                    <li><a class="dropdown-item" href="#">Autre action</a></li>
                  </ul>
                </div>
                <div class="btn-group">
                  <button type="button" class="btn btn-success dropdown-toggle" data-bs-toggle="dropdown" aria-expanded="false">
                    Success
                  </button>
                  <ul class="dropdown-menu">
                    <li><a class="dropdown-item" href="#">Action</a></li>
                    <li><a class="dropdown-item" href="#">Autre action</a></li>
                  </ul>
                </div>
                <div class="btn-group">
                  <button type="button" class="btn btn-danger dropdown-toggle" data-bs-toggle="dropdown" aria-expanded="false">
                    Danger
                  </button>
                  <ul class="dropdown-menu">
                    <li><a class="dropdown-item" href="#">Action</a></li>
                    <li><a class="dropdown-item" href="#">Autre action</a></li>
                  </ul>
                </div>
              </div>
            </div>
          </div>
        </div>

        <div id="sous-menus" class="mt-5">
          <h2>Sous-menus</h2>
          <p>Les menus déroulants peuvent contenir des sous-menus imbriqués.</p>

          <div class="card mb-4">
            <div class="card-body">
              <div class="component-preview">
                <div class="dropdown">
                  <button class="btn btn-secondary dropdown-toggle" type="button" data-bs-toggle="dropdown" aria-expanded="false">
                    Menu avec sous-menus
                  </button>
                  <ul class="dropdown-menu">
                    <li><a class="dropdown-item" href="#">Action</a></li>
                    <li><a class="dropdown-item" href="#">Autre action</a></li>
                    <li><hr class="dropdown-divider"></li>
                    <li><a class="dropdown-item" href="#">Sous-menu</a>
                      <ul class="dropdown-menu dropdown-submenu">
                        <li><a class="dropdown-item" href="#">Sous-action 1</a></li>
                        <li><a class="dropdown-item" href="#">Sous-action 2</a></li>
                      </ul>
                    </li>
                  </ul>
                </div>
              </div>
            </div>
          </div>
        </div>

        <div id="alignement" class="mt-5">
          <h2>Alignement</h2>
          <p>Les menus déroulants peuvent être alignés de différentes manières.</p>

          <div class="card mb-4">
            <div class="card-body">
              <div class="component-preview">
                <div class="dropdown">
                  <button class="btn btn-secondary dropdown-toggle" type="button" data-bs-toggle="dropdown" aria-expanded="false">
                    Aligné à droite
                  </button>
                  <ul class="dropdown-menu dropdown-menu-end">
                    <li><a class="dropdown-item" href="#">Action</a></li>
                    <li><a class="dropdown-item" href="#">Autre action</a></li>
                  </ul>
                </div>
                <div class="dropdown">
                  <button class="btn btn-secondary dropdown-toggle" type="button" data-bs-toggle="dropdown" aria-expanded="false">
                    Aligné au centre
                  </button>
                  <ul class="dropdown-menu dropdown-menu-center">
                    <li><a class="dropdown-item" href="#">Action</a></li>
                    <li><a class="dropdown-item" href="#">Autre action</a></li>
                  </ul>
                </div>
              </div>
            </div>
          </div>
        </div>

        <div id="utilisation-moodle" class="mt-5">
          <h2>Utilisation dans Moodle</h2>
          <p>Dans Moodle, les menus déroulants sont utilisés pour :</p>
          <ul class="list-group mb-4">
            <li class="list-group-item">Actions sur les activités et ressources</li>
            <li class="list-group-item">Navigation dans les cours</li>
            <li class="list-group-item">Options de configuration</li>
            <li class="list-group-item">Actions sur les utilisateurs</li>
            <li class="list-group-item">Filtres et tri des données</li>
          </ul>

          <div class="card mb-4">
            <div class="card-body">
              <h3 class="h5">Exemple d'intégration dans un template Moodle</h3>
              <pre class="bg-light p-3 rounded"><code>{{#hasactions}}
    &lt;div class="dropdown"&gt;
        &lt;button class="btn btn-secondary dropdown-toggle" type="button" data-bs-toggle="dropdown"&gt;
            {{action_text}}
        &lt;/button&gt;
        &lt;ul class="dropdown-menu"&gt;
            {{#actions}}
                &lt;li&gt;&lt;a class="dropdown-item" href="{{url}}"&gt;{{text}}&lt;/a&gt;&lt;/li&gt;
            {{/actions}}
        &lt;/ul&gt;
    &lt;/div&gt;
{{/hasactions}}</code></pre>
            </div>
          </div>
        </div>

        <div id="accessibilite" class="mt-5">
          <h2>Accessibilité</h2>
          <ul class="list-group mb-4">
            <li class="list-group-item">Utilisez des attributs ARIA appropriés pour les menus déroulants</li>
            <li class="list-group-item">Assurez-vous que les menus sont accessibles au clavier</li>
            <li class="list-group-item">Fournissez des textes descriptifs pour les actions</li>
            <li class="list-group-item">Maintenez un contraste suffisant pour la lisibilité</li>
            <li class="list-group-item">Évitez les sous-menus trop profonds</li>
          </ul>
        </div>
      </div>
    </div>
  </div>
</div>
