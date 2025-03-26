---
title: Progression
description: Documentation du composant Progression de Bootstrap 5 pour Moodle
template: pages/composant.html
---

<div class="container py-4">
  <div class="row">
    <div class="col-lg-3">
      <nav id="navbar-example3" class="h-100 flex-column align-items-stretch pe-4 border-end">
        <nav class="nav nav-pills flex-column">
          <a class="nav-link" href="#description">Description</a>
          <a class="nav-link" href="#exemples-base">Exemples de base</a>
          <a class="nav-link" href="#labels">Avec labels</a>
          <a class="nav-link" href="#striped">Rayée</a>
          <a class="nav-link" href="#animated">Animée</a>
          <a class="nav-link" href="#utilisation-moodle">Utilisation dans Moodle</a>
          <a class="nav-link" href="#accessibilite">Accessibilité</a>
        </nav>
      </nav>
    </div>

    <div class="col-lg-9">
      <div data-bs-spy="scroll" data-bs-target="#navbar-example3" data-bs-smooth-scroll="true" class="scrollspy-example-2" tabindex="0">
        <div id="description">
          <h2>Description</h2>
          <p class="lead">La barre de progression est un composant qui permet d'afficher visuellement l'avancement d'une tâche ou d'un processus.</p>
        </div>

        <div id="exemples-base" class="mt-5">
          <h2>Exemples de base</h2>
          <p>La barre de progression de base affiche un pourcentage de complétion.</p>

          <div class="card mb-4">
            <div class="card-body">
              <div class="component-preview">
                <div class="progress">
                  <div class="progress-bar" role="progressbar" style="width: 25%" aria-valuenow="25" aria-valuemin="0" aria-valuemax="100"></div>
                </div>
              </div>
            </div>
          </div>
        </div>

        <div id="labels" class="mt-5">
          <h2>Avec labels</h2>
          <p>La barre de progression peut inclure des labels pour afficher le pourcentage.</p>

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

        <div id="striped" class="mt-5">
          <h2>Rayée</h2>
          <p>La barre de progression peut avoir un effet rayé.</p>

          <div class="card mb-4">
            <div class="card-body">
              <div class="component-preview">
                <div class="progress">
                  <div class="progress-bar progress-bar-striped" role="progressbar" style="width: 50%" aria-valuenow="50" aria-valuemin="0" aria-valuemax="100"></div>
                </div>
              </div>
            </div>
          </div>
        </div>

        <div id="animated" class="mt-5">
          <h2>Animée</h2>
          <p>La barre de progression peut avoir une animation.</p>

          <div class="card mb-4">
            <div class="card-body">
              <div class="component-preview">
                <div class="progress">
                  <div class="progress-bar progress-bar-striped progress-bar-animated" role="progressbar" style="width: 75%" aria-valuenow="75" aria-valuemin="0" aria-valuemax="100"></div>
                </div>
              </div>
            </div>
          </div>
        </div>

        <div id="utilisation-moodle" class="mt-5">
          <h2>Utilisation dans Moodle</h2>
          <p>Dans Moodle, la barre de progression est utilisée pour :</p>
          <ul class="list-group mb-4">
            <li class="list-group-item">Affichage de la progression dans un cours</li>
            <li class="list-group-item">Indication de l'avancement des activités</li>
            <li class="list-group-item">Visualisation des objectifs d'apprentissage</li>
            <li class="list-group-item">Suivi des compétences</li>
            <li class="list-group-item">Indication du chargement des ressources</li>
          </ul>

          <div class="card mb-4">
            <div class="card-body">
              <h3 class="h5">Exemple d'intégration dans un template Moodle</h3>
              <pre class="bg-light p-3 rounded"><code>{{#hasprogress}}
    &lt;div class="progress"&gt;
        &lt;div class="progress-bar" role="progressbar"
             style="width: {{progress}}%"
             aria-valuenow="{{progress}}"
             aria-valuemin="0"
             aria-valuemax="100"&gt;
            {{progress}}%
        &lt;/div&gt;
    &lt;/div&gt;
{{/hasprogress}}</code></pre>
            </div>
          </div>
        </div>

        <div id="accessibilite" class="mt-5">
          <h2>Accessibilité</h2>
          <ul class="list-group mb-4">
            <li class="list-group-item">Utilisez des attributs ARIA appropriés pour la barre de progression</li>
            <li class="list-group-item">Fournissez des labels descriptifs pour la progression</li>
            <li class="list-group-item">Assurez-vous que les valeurs de progression sont annoncées par les lecteurs d'écran</li>
            <li class="list-group-item">Maintenez un contraste suffisant pour la visibilité</li>
            <li class="list-group-item">Incluez des textes alternatifs pour les animations</li>
          </ul>
        </div>
      </div>
    </div>
  </div>
</div>