---
title: Navigation
description: Documentation du composant Navigation de Bootstrap 5 pour Moodle
template: pages/composant.html
---

<div class="container py-4">
  <div class="row">
    <div class="col-lg-3">
      <nav id="navbar-example3" class="h-100 flex-column align-items-stretch pe-4 border-end">
        <nav class="nav nav-pills flex-column">
          <a class="nav-link" href="#description">Description</a>
          <a class="nav-link" href="#exemples-base">Exemples de base</a>
          <a class="nav-link" href="#brand">Avec marque</a>
          <a class="nav-link" href="#form">Avec formulaire</a>
          <a class="nav-link" href="#dropdown">Avec menu déroulant</a>
          <a class="nav-link" href="#utilisation-moodle">Utilisation dans Moodle</a>
          <a class="nav-link" href="#accessibilite">Accessibilité</a>
        </nav>
      </nav>
    </div>

    <div class="col-lg-9">
      <div data-bs-spy="scroll" data-bs-target="#navbar-example3" data-bs-smooth-scroll="true" class="scrollspy-example-2" tabindex="0">
        <div id="description">
          <h2>Description</h2>
          <p class="lead">La barre de navigation est un composant de navigation responsive qui peut s'adapter à différentes tailles d'écran et inclure des logos, des liens, des formulaires et des menus déroulants.</p>
        </div>

        <div id="exemples-base" class="mt-5">
          <h2>Exemples de base</h2>
          <p>La barre de navigation de base inclut une marque et des liens de navigation.</p>

          <div class="card mb-4">
            <div class="card-body">
              <div class="component-preview">
                <nav class="navbar navbar-expand-lg navbar-light bg-light">
                  <div class="container-fluid">
                    <a class="navbar-brand" href="#">Navbar</a>
                    <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarNav" aria-controls="navbarNav" aria-expanded="false" aria-label="Toggle navigation">
                      <span class="navbar-toggler-icon"></span>
                    </button>
                    <div class="collapse navbar-collapse" id="navbarNav">
                      <ul class="navbar-nav">
                        <li class="nav-item">
                          <a class="nav-link active" aria-current="page" href="#">Accueil</a>
                        </li>
                        <li class="nav-item">
                          <a class="nav-link" href="#">Fonctionnalités</a>
                        </li>
                        <li class="nav-item">
                          <a class="nav-link" href="#">Tarifs</a>
                        </li>
                      </ul>
                    </div>
                  </div>
                </nav>
              </div>
            </div>
          </div>
        </div>

        <div id="brand" class="mt-5">
          <h2>Avec marque</h2>
          <p>La barre de navigation peut inclure une marque ou un logo.</p>

          <div class="card mb-4">
            <div class="card-body">
              <div class="component-preview">
                <nav class="navbar navbar-expand-lg navbar-light bg-light">
                  <div class="container-fluid">
                    <a class="navbar-brand" href="#">
                      <img src="../../assets/images/logo.png" alt="Logo" height="30" class="d-inline-block align-text-top">
                      Moodle
                    </a>
                    <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarBrand" aria-controls="navbarBrand" aria-expanded="false" aria-label="Toggle navigation">
                      <span class="navbar-toggler-icon"></span>
                    </button>
                    <div class="collapse navbar-collapse" id="navbarBrand">
                      <ul class="navbar-nav">
                        <li class="nav-item">
                          <a class="nav-link" href="#">Accueil</a>
                        </li>
                        <li class="nav-item">
                          <a class="nav-link" href="#">À propos</a>
                        </li>
                      </ul>
                    </div>
                  </div>
                </nav>
              </div>
            </div>
          </div>
        </div>

        <div id="form" class="mt-5">
          <h2>Avec formulaire</h2>
          <p>La barre de navigation peut inclure un formulaire de recherche.</p>

          <div class="card mb-4">
            <div class="card-body">
              <div class="component-preview">
                <nav class="navbar navbar-expand-lg navbar-light bg-light">
                  <div class="container-fluid">
                    <a class="navbar-brand" href="#">Navbar</a>
                    <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarForm" aria-controls="navbarForm" aria-expanded="false" aria-label="Toggle navigation">
                      <span class="navbar-toggler-icon"></span>
                    </button>
                    <div class="collapse navbar-collapse" id="navbarForm">
                      <form class="d-flex ms-auto">
                        <input class="form-control me-2" type="search" placeholder="Rechercher" aria-label="Search">
                        <button class="btn btn-outline-success" type="submit">Rechercher</button>
                      </form>
                    </div>
                  </div>
                </nav>
              </div>
            </div>
          </div>
        </div>

        <div id="dropdown" class="mt-5">
          <h2>Avec menu déroulant</h2>
          <p>La barre de navigation peut inclure des menus déroulants.</p>

          <div class="card mb-4">
            <div class="card-body">
              <div class="component-preview">
                <nav class="navbar navbar-expand-lg navbar-light bg-light">
                  <div class="container-fluid">
                    <a class="navbar-brand" href="#">Navbar</a>
                    <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarDropdown" aria-controls="navbarDropdown" aria-expanded="false" aria-label="Toggle navigation">
                      <span class="navbar-toggler-icon"></span>
                    </button>
                    <div class="collapse navbar-collapse" id="navbarDropdown">
                      <ul class="navbar-nav">
                        <li class="nav-item">
                          <a class="nav-link" href="#">Accueil</a>
                        </li>
                        <li class="nav-item dropdown">
                          <a class="nav-link dropdown-toggle" href="#" id="navbarDropdownMenuLink" role="button" data-bs-toggle="dropdown" aria-expanded="false">
                            Menu déroulant
                          </a>
                          <ul class="dropdown-menu" aria-labelledby="navbarDropdownMenuLink">
                            <li><a class="dropdown-item" href="#">Action</a></li>
                            <li><a class="dropdown-item" href="#">Autre action</a></li>
                            <li><hr class="dropdown-divider"></li>
                            <li><a class="dropdown-item" href="#">Quelque chose d'autre</a></li>
                          </ul>
                        </li>
                      </ul>
                    </div>
                  </div>
                </nav>
              </div>
            </div>
          </div>
        </div>

        <div id="utilisation-moodle" class="mt-5">
          <h2>Utilisation dans Moodle</h2>
          <p>Dans Moodle, la barre de navigation est utilisée pour :</p>
          <ul class="list-group mb-4">
            <li class="list-group-item">Navigation principale du site</li>
            <li class="list-group-item">Navigation dans les cours</li>
            <li class="list-group-item">Accès aux fonctionnalités utilisateur</li>
            <li class="list-group-item">Recherche de contenu</li>
            <li class="list-group-item">Navigation dans les activités</li>
          </ul>

          <div class="card mb-4">
            <div class="card-body">
              <h3 class="h5">Exemple d'intégration dans un template Moodle</h3>
              <pre class="bg-light p-3 rounded"><code>{{#hasnavbar}}
    &lt;nav class="navbar navbar-expand-lg navbar-light bg-light"&gt;
        &lt;div class="container-fluid"&gt;
            &lt;a class="navbar-brand" href="{{homeurl}}"&gt;
                {{#pix}}theme/logo, core{{/pix}}
                {{sitename}}
            &lt;/a&gt;
            &lt;button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarContent"&gt;
                &lt;span class="navbar-toggler-icon"&gt;&lt;/span&gt;
            &lt;/button&gt;
            &lt;div class="collapse navbar-collapse" id="navbarContent"&gt;
                &lt;ul class="navbar-nav me-auto"&gt;
                    {{#navitems}}
                        &lt;li class="nav-item"&gt;
                            &lt;a class="nav-link {{#active}}active{{/active}}" href="{{url}}"&gt;{{text}}&lt;/a&gt;
                        &lt;/li&gt;
                    {{/navitems}}
                &lt;/ul&gt;
                &lt;form class="d-flex"&gt;
                    &lt;input class="form-control me-2" type="search" placeholder="Rechercher"&gt;
                    &lt;button class="btn btn-outline-success" type="submit"&gt;Rechercher&lt;/button&gt;
                &lt;/form&gt;
            &lt;/div&gt;
        &lt;/div&gt;
    &lt;/nav&gt;
{{/hasnavbar}}</code></pre>
            </div>
          </div>
        </div>

        <div id="accessibilite" class="mt-5">
          <h2>Accessibilité</h2>
          <ul class="list-group mb-4">
            <li class="list-group-item">Utilisez des attributs ARIA appropriés pour la navigation</li>
            <li class="list-group-item">Assurez-vous que la navigation est accessible au clavier</li>
            <li class="list-group-item">Fournissez des textes descriptifs pour les liens</li>
            <li class="list-group-item">Maintenez une structure de navigation cohérente</li>
            <li class="list-group-item">Incluez des indicateurs visuels pour l'état actif</li>
          </ul>
        </div>
      </div>
    </div>
  </div>
</div>
