---
title: Tableaux
description: Documentation du composant Tableaux de Bootstrap 5 pour Moodle
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
          <p class="lead">Les tableaux sont des composants essentiels pour présenter des données structurées. Bootstrap 5 offre plusieurs styles de tableaux pour différents contextes d'utilisation.</p>
        </div>

        <div id="exemple-base" class="mt-5">
          <h2>Exemple de base</h2>
          <p>Un tableau simple avec des en-têtes et des données.</p>
          <div class="card mb-4">
            <div class="card-body">
              <div class="component-preview">
                <table class="table">
                  <thead>
                    <tr>
                      <th scope="col">#</th>
                      <th scope="col">Nom</th>
                      <th scope="col">Prénom</th>
                      <th scope="col">Email</th>
                    </tr>
                  </thead>
                  <tbody>
                    <tr>
                      <th scope="row">1</th>
                      <td>Dupont</td>
                      <td>Jean</td>
                      <td>jean.dupont@exemple.com</td>
                    </tr>
                    <tr>
                      <th scope="row">2</th>
                      <td>Martin</td>
                      <td>Marie</td>
                      <td>marie.martin@exemple.com</td>
                    </tr>
                  </tbody>
                </table>
              </div>
            </div>
          </div>
        </div>

        <div id="styles" class="mt-5">
          <h2>Styles</h2>

          <div class="card mb-4">
            <div class="card-body">
              <h3 class="h5">Tableaux avec bordures</h3>
              <p>Les tableaux peuvent avoir des bordures pour une meilleure lisibilité.</p>
              <div class="component-preview">
                <table class="table table-bordered">
                  <thead>
                    <tr>
                      <th scope="col">#</th>
                      <th scope="col">En-tête 1</th>
                      <th scope="col">En-tête 2</th>
                    </tr>
                  </thead>
                  <tbody>
                    <tr>
                      <th scope="row">1</th>
                      <td>Donnée 1</td>
                      <td>Donnée 2</td>
                    </tr>
                    <tr>
                      <th scope="row">2</th>
                      <td>Donnée 3</td>
                      <td>Donnée 4</td>
                    </tr>
                  </tbody>
                </table>
              </div>
            </div>
          </div>

          <div class="card mb-4">
            <div class="card-body">
              <h3 class="h5">Tableaux rayés</h3>
              <p>Les tableaux peuvent avoir des lignes alternées pour une meilleure lisibilité.</p>
              <div class="component-preview">
                <table class="table table-striped">
                  <thead>
                    <tr>
                      <th scope="col">#</th>
                      <th scope="col">En-tête 1</th>
                      <th scope="col">En-tête 2</th>
                    </tr>
                  </thead>
                  <tbody>
                    <tr>
                      <th scope="row">1</th>
                      <td>Donnée 1</td>
                      <td>Donnée 2</td>
                    </tr>
                    <tr>
                      <th scope="row">2</th>
                      <td>Donnée 3</td>
                      <td>Donnée 4</td>
                    </tr>
                    <tr>
                      <th scope="row">3</th>
                      <td>Donnée 5</td>
                      <td>Donnée 6</td>
                    </tr>
                  </tbody>
                </table>
              </div>
            </div>
          </div>

          <div class="card mb-4">
            <div class="card-body">
              <h3 class="h5">Tableaux avec survol</h3>
              <p>Les tableaux peuvent avoir un effet de survol sur les lignes.</p>
              <div class="component-preview">
                <table class="table table-hover">
                  <thead>
                    <tr>
                      <th scope="col">#</th>
                      <th scope="col">En-tête 1</th>
                      <th scope="col">En-tête 2</th>
                    </tr>
                  </thead>
                  <tbody>
                    <tr>
                      <th scope="row">1</th>
                      <td>Donnée 1</td>
                      <td>Donnée 2</td>
                    </tr>
                    <tr>
                      <th scope="row">2</th>
                      <td>Donnée 3</td>
                      <td>Donnée 4</td>
                    </tr>
                  </tbody>
                </table>
              </div>
            </div>
          </div>

          <div class="card mb-4">
            <div class="card-body">
              <h3 class="h5">Tableaux responsifs</h3>
              <p>Les tableaux peuvent être rendus responsifs pour s'adapter aux différentes tailles d'écran.</p>
              <div class="component-preview">
                <div class="table-responsive">
                  <table class="table">
                    <thead>
                      <tr>
                        <th scope="col">#</th>
                        <th scope="col">En-tête 1</th>
                        <th scope="col">En-tête 2</th>
                        <th scope="col">En-tête 3</th>
                        <th scope="col">En-tête 4</th>
                        <th scope="col">En-tête 5</th>
                      </tr>
                    </thead>
                    <tbody>
                      <tr>
                        <th scope="row">1</th>
                        <td>Donnée 1</td>
                        <td>Donnée 2</td>
                        <td>Donnée 3</td>
                        <td>Donnée 4</td>
                        <td>Donnée 5</td>
                      </tr>
                    </tbody>
                  </table>
                </div>
              </div>
            </div>
          </div>
        </div>

        <div id="utilisation-moodle" class="mt-5">
          <h2>Utilisation dans Moodle</h2>
          <p>Dans Moodle, les tableaux sont utilisés pour :</p>
          <ul class="list-group mb-4">
            <li class="list-group-item">Afficher les notes</li>
            <li class="list-group-item">Présenter les participants</li>
            <li class="list-group-item">Montrer les statistiques</li>
            <li class="list-group-item">Afficher les données de progression</li>
            <li class="list-group-item">Présenter les horaires</li>
          </ul>

          <div class="card mb-4">
            <div class="card-body">
              <h3 class="h5">Exemple d'intégration dans un template Moodle</h3>
              <pre class="bg-light p-3 rounded"><code>{{#table}}
    &lt;div class="{{#responsive}}table-responsive{{/responsive}}"&gt;
        &lt;table class="table {{#bordered}}table-bordered{{/bordered}} {{#striped}}table-striped{{/striped}} {{#hover}}table-hover{{/hover}}"&gt;
            {{#thead}}
            &lt;thead&gt;
                &lt;tr&gt;
                    {{#headers}}
                    &lt;th scope="col"&gt;{{text}}&lt;/th&gt;
                    {{/headers}}
                &lt;/tr&gt;
            &lt;/thead&gt;
            {{/thead}}
            {{#tbody}}
            &lt;tbody&gt;
                {{#rows}}
                &lt;tr&gt;
                    {{#cells}}
                    &lt;{{#header}}th scope="row"{{/header}}{{^header}}td{{/header}}&gt;{{text}}&lt;/{{#header}}th{{/header}}{{^header}}td{{/header}}&gt;
                    {{/cells}}
                &lt;/tr&gt;
                {{/rows}}
            &lt;/tbody&gt;
            {{/tbody}}
        &lt;/table&gt;
    &lt;/div&gt;
{{/table}}</code></pre>
            </div>
          </div>
        </div>

        <div id="accessibilite" class="mt-5">
          <h2>Accessibilité</h2>
          <ul class="list-group mb-4">
            <li class="list-group-item">Utilisez des en-têtes appropriés pour les colonnes</li>
            <li class="list-group-item">Associez les cellules aux en-têtes correspondants</li>
            <li class="list-group-item">Maintenez un contraste suffisant pour le texte</li>
            <li class="list-group-item">Rendez les tableaux responsifs pour les petits écrans</li>
            <li class="list-group-item">Fournissez un résumé pour les lecteurs d'écran</li>
          </ul>
        </div>
      </div>
    </div>
  </div>
</div>