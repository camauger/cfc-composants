---
title: Barres de progression
description: Documentation du composant Barres de progression de Bootstrap 5 pour Moodle
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
          <p class="lead">Les barres de progression sont des composants qui permettent d'afficher visuellement l'avancement d'une tâche ou d'un processus. Elles sont idéales pour montrer le progrès d'un téléchargement, d'une inscription ou d'une activité.</p>
        </div>

        <div id="exemple-base" class="mt-5">
          <h2>Exemple de base</h2>
          <p>Une barre de progression simple avec un pourcentage.</p>
          <div class="card mb-4">
            <div class="card-body">
              <div class="component-preview">
                <div class="progress">
                  <div class="progress-bar" role="progressbar" style="width: 75%" aria-valuenow="75" aria-valuemin="0" aria-valuemax="100">75%</div>
                </div>
              </div>
            </div>
          </div>
        </div>

        <div id="styles" class="mt-5">
          <h2>Styles</h2>

          <div class="card mb-4">
            <div class="card-body">
              <h3 class="h5">Barres de progression avec couleurs</h3>
              <p>Les barres de progression peuvent utiliser différentes couleurs pour indiquer différents états.</p>
              <div class="component-preview">
                <div class="progress mb-3">
                  <div class="progress-bar bg-success" role="progressbar" style="width: 25%" aria-valuenow="25" aria-valuemin="0" aria-valuemax="100">25%</div>
                </div>
                <div class="progress mb-3">
                  <div class="progress-bar bg-info" role="progressbar" style="width: 50%" aria-valuenow="50" aria-valuemin="0" aria-valuemax="100">50%</div>
                </div>
                <div class="progress mb-3">
                  <div class="progress-bar bg-warning" role="progressbar" style="width: 75%" aria-valuenow="75" aria-valuemin="0" aria-valuemax="100">75%</div>
                </div>
                <div class="progress">
                  <div class="progress-bar bg-danger" role="progressbar" style="width: 100%" aria-valuenow="100" aria-valuemin="0" aria-valuemax="100">100%</div>
                </div>
              </div>
            </div>
          </div>

          <div class="card mb-4">
            <div class="card-body">
              <h3 class="h5">Barres de progression avec rayures</h3>
              <p>Les barres de progression peuvent avoir un effet de rayures animées.</p>
              <div class="component-preview">
                <div class="progress">
                  <div class="progress-bar progress-bar-striped progress-bar-animated" role="progressbar" style="width: 75%" aria-valuenow="75" aria-valuemin="0" aria-valuemax="100">75%</div>
                </div>
              </div>
            </div>
          </div>

          <div class="card mb-4">
            <div class="card-body">
              <h3 class="h5">Barres de progression multiples</h3>
              <p>Les barres de progression peuvent être empilées pour montrer plusieurs valeurs.</p>
              <div class="component-preview">
                <div class="progress">
                  <div class="progress-bar" role="progressbar" style="width: 15%" aria-valuenow="15" aria-valuemin="0" aria-valuemax="100">15%</div>
                  <div class="progress-bar bg-success" role="progressbar" style="width: 30%" aria-valuenow="30" aria-valuemin="0" aria-valuemax="100">30%</div>
                  <div class="progress-bar bg-info" role="progressbar" style="width: 20%" aria-valuenow="20" aria-valuemin="0" aria-valuemax="100">20%</div>
                </div>
              </div>
            </div>
          </div>
        </div>

        <div id="utilisation-moodle" class="mt-5">
          <h2>Utilisation dans Moodle</h2>
          <p>Dans Moodle, les barres de progression sont utilisées pour :</p>
          <ul class="list-group mb-4">
            <li class="list-group-item">Afficher le progrès d'un cours</li>
            <li class="list-group-item">Montrer l'avancement d'un téléchargement</li>
            <li class="list-group-item">Indiquer le temps restant d'une activité</li>
            <li class="list-group-item">Visualiser les statistiques de complétion</li>
            <li class="list-group-item">Montrer le progrès d'une synchronisation</li>
          </ul>

          <div class="card mb-4">
            <div class="card-body">
              <h3 class="h5">Exemple d'intégration dans un template Moodle</h3>
              <pre class="bg-light p-3 rounded"><code>{{#has_progress}}
    &lt;div class="progress"&gt;
        &lt;div class="progress-bar {{#color}}bg-{{color}}{{/color}} {{#striped}}progress-bar-striped{{/striped}} {{#animated}}progress-bar-animated{{/animated}}"
             role="progressbar"
             style="width: {{value}}%"
             aria-valuenow="{{value}}"
             aria-valuemin="0"
             aria-valuemax="100"&gt;
            {{#show_value}}{{value}}%{{/show_value}}
        &lt;/div&gt;
    &lt;/div&gt;

    {{#has_multiple}}
    &lt;div class="progress"&gt;
        {{#items}}
        &lt;div class="progress-bar {{#color}}bg-{{color}}{{/color}} {{#striped}}progress-bar-striped{{/striped}} {{#animated}}progress-bar-animated{{/animated}}"
             role="progressbar"
             style="width: {{value}}%"
             aria-valuenow="{{value}}"
             aria-valuemin="0"
             aria-valuemax="100"&gt;
            {{#show_value}}{{value}}%{{/show_value}}
        &lt;/div&gt;
        {{/items}}
    &lt;/div&gt;
    {{/has_multiple}}
{{/has_progress}}</code></pre>
            </div>
          </div>
        </div>

        <div id="accessibilite" class="mt-5">
          <h2>Accessibilité</h2>
          <ul class="list-group mb-4">
            <li class="list-group-item">Utilisez l'attribut `role="progressbar"`</li>
            <li class="list-group-item">Fournissez des attributs ARIA appropriés (aria-valuenow, aria-valuemin, aria-valuemax)</li>
            <li class="list-group-item">Maintenez un contraste suffisant pour le texte</li>
            <li class="list-group-item">Évitez de dépendre uniquement de la couleur pour indiquer l'état</li>
            <li class="list-group-item">Fournissez une alternative textuelle pour les utilisateurs de lecteurs d'écran</li>
          </ul>
        </div>
      </div>
    </div>
  </div>
</div>