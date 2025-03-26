---
title: Boutons
description: Documentation du composant Boutons de Bootstrap 5 pour Moodle
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
          <p class="lead">Les boutons sont des composants interactifs essentiels pour la navigation et les actions. Ils permettent aux utilisateurs de déclencher des actions et de naviguer dans l'interface.</p>
        </div>

        <div id="exemple-base" class="mt-5">
          <h2>Exemple de base</h2>
          <p>Un bouton simple avec un texte.</p>
          <div class="card mb-4">
            <div class="card-body">
              <div class="component-preview">
                <button type="button" class="btn btn-primary">Cliquez-moi</button>
              </div>
            </div>
          </div>
        </div>

        <div id="styles" class="mt-5">
          <h2>Styles</h2>

          <div class="card mb-4">
            <div class="card-body">
              <h3 class="h5">Boutons avec couleurs</h3>
              <p>Les boutons peuvent avoir différentes couleurs selon leur contexte.</p>
              <div class="component-preview">
                <button type="button" class="btn btn-primary">Primaire</button>
                <button type="button" class="btn btn-secondary">Secondaire</button>
                <button type="button" class="btn btn-success">Succès</button>
                <button type="button" class="btn btn-danger">Danger</button>
                <button type="button" class="btn btn-warning">Avertissement</button>
                <button type="button" class="btn btn-info">Info</button>
                <button type="button" class="btn btn-light">Clair</button>
                <button type="button" class="btn btn-dark">Sombre</button>
              </div>
            </div>
          </div>

          <div class="card mb-4">
            <div class="card-body">
              <h3 class="h5">Boutons avec icônes</h3>
              <p>Les boutons peuvent inclure des icônes.</p>
              <div class="component-preview">
                <button type="button" class="btn btn-primary">
                  <i class="bi bi-save"></i> Enregistrer
                </button>
                <button type="button" class="btn btn-success">
                  <i class="bi bi-check"></i> Valider
                </button>
                <button type="button" class="btn btn-danger">
                  <i class="bi bi-trash"></i> Supprimer
                </button>
              </div>
            </div>
          </div>

          <div class="card mb-4">
            <div class="card-body">
              <h3 class="h5">Tailles de boutons</h3>
              <p>Les boutons peuvent avoir différentes tailles.</p>
              <div class="component-preview">
                <button type="button" class="btn btn-primary btn-lg">Grand</button>
                <button type="button" class="btn btn-primary">Normal</button>
                <button type="button" class="btn btn-primary btn-sm">Petit</button>
              </div>
            </div>
          </div>

          <div class="card mb-4">
            <div class="card-body">
              <h3 class="h5">États des boutons</h3>
              <p>Les boutons peuvent avoir différents états.</p>
              <div class="component-preview">
                <button type="button" class="btn btn-primary">Normal</button>
                <button type="button" class="btn btn-primary" disabled>Désactivé</button>
                <button type="button" class="btn btn-primary" data-bs-toggle="button">Bascule</button>
              </div>
            </div>
          </div>

          <div class="card mb-4">
            <div class="card-body">
              <h3 class="h5">Boutons avec contour</h3>
              <p>Les boutons peuvent avoir un style avec contour.</p>
              <div class="component-preview">
                <button type="button" class="btn btn-outline-primary">Primaire</button>
                <button type="button" class="btn btn-outline-secondary">Secondaire</button>
                <button type="button" class="btn btn-outline-success">Succès</button>
                <button type="button" class="btn btn-outline-danger">Danger</button>
                <button type="button" class="btn btn-outline-warning">Avertissement</button>
                <button type="button" class="btn btn-outline-info">Info</button>
              </div>
            </div>
          </div>
        </div>

        <div id="utilisation-moodle" class="mt-5">
          <h2>Utilisation dans Moodle</h2>
          <p>Dans Moodle, les boutons sont utilisés pour :</p>
          <ul class="list-group mb-4">
            <li class="list-group-item">Soumettre des formulaires</li>
            <li class="list-group-item">Naviguer entre les pages</li>
            <li class="list-group-item">Déclencher des actions</li>
            <li class="list-group-item">Télécharger des ressources</li>
            <li class="list-group-item">Gérer les paramètres</li>
          </ul>

          <div class="card mb-4">
            <div class="card-body">
              <h3 class="h5">Exemple d'intégration dans un template Moodle</h3>
              <pre class="bg-light p-3 rounded"><code>{{#button}}
    &lt;button type="{{type}}"
            class="btn btn-{{style}} {{#size}}btn-{{size}}{{/size}} {{#outline}}btn-outline-{{style}}{{/outline}}"
            {{#disabled}}disabled{{/disabled}}
            {{#data}}data-{{key}}="{{value}}"{{/data}}&gt;
        {{#icon}}
        &lt;i class="bi bi-{{icon}}"&gt;&lt;/i&gt;
        {{/icon}}
        {{text}}
    &lt;/button&gt;
{{/button}}</code></pre>
            </div>
          </div>
        </div>

        <div id="accessibilite" class="mt-5">
          <h2>Accessibilité</h2>
          <ul class="list-group mb-4">
            <li class="list-group-item">Utilisez des textes descriptifs pour les boutons</li>
            <li class="list-group-item">Maintenez un contraste suffisant</li>
            <li class="list-group-item">Assurez-vous que les boutons sont accessibles au clavier</li>
            <li class="list-group-item">Indiquez clairement l'état des boutons (actif, désactivé)</li>
          </ul>
        </div>
      </div>
    </div>
  </div>
</div>
