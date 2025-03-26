---
title: Icônes
description: Documentation du composant Icônes de Bootstrap 5 pour Moodle
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
          <p class="lead">Les icônes sont des composants visuels qui améliorent l'expérience utilisateur en ajoutant des repères visuels. Bootstrap Icons est une bibliothèque d'icônes open source qui s'intègre parfaitement avec Bootstrap 5.</p>
        </div>

        <div id="exemple-base" class="mt-5">
          <h2>Exemple de base</h2>
          <p>Une icône simple utilisée dans un contexte.</p>
          <div class="card mb-4">
            <div class="card-body">
              <div class="component-preview">
                <button class="btn btn-primary">
                  <i class="bi bi-save"></i> Enregistrer
                </button>
              </div>
            </div>
          </div>
        </div>

        <div id="styles" class="mt-5">
          <h2>Styles</h2>

          <div class="card mb-4">
            <div class="card-body">
              <h3 class="h5">Tailles d'icônes</h3>
              <p>Les icônes peuvent avoir différentes tailles.</p>
              <div class="component-preview">
                <i class="bi bi-star fs-1"></i>
                <i class="bi bi-star fs-2"></i>
                <i class="bi bi-star fs-3"></i>
                <i class="bi bi-star fs-4"></i>
                <i class="bi bi-star fs-5"></i>
                <i class="bi bi-star fs-6"></i>
              </div>
            </div>
          </div>

          <div class="card mb-4">
            <div class="card-body">
              <h3 class="h5">Couleurs d'icônes</h3>
              <p>Les icônes peuvent avoir différentes couleurs.</p>
              <div class="component-preview">
                <i class="bi bi-heart text-primary"></i>
                <i class="bi bi-heart text-success"></i>
                <i class="bi bi-heart text-danger"></i>
                <i class="bi bi-heart text-warning"></i>
                <i class="bi bi-heart text-info"></i>
              </div>
            </div>
          </div>

          <div class="card mb-4">
            <div class="card-body">
              <h3 class="h5">Animations d'icônes</h3>
              <p>Les icônes peuvent avoir des animations.</p>
              <div class="component-preview">
                <i class="bi bi-arrow-repeat"></i>
                <i class="bi bi-arrow-repeat-spin"></i>
                <i class="bi bi-arrow-repeat-spin text-primary"></i>
              </div>
            </div>
          </div>

          <div class="card mb-4">
            <div class="card-body">
              <h3 class="h5">Utilisation dans différents contextes</h3>
              <p>Les icônes peuvent être utilisées dans différents contextes de l'interface.</p>
              <div class="component-preview">
                <button class="btn btn-outline-primary">
                  <i class="bi bi-plus"></i> Ajouter
                </button>
                <button class="btn btn-outline-danger">
                  <i class="bi bi-trash"></i> Supprimer
                </button>
                <div class="alert alert-info">
                  <i class="bi bi-info-circle"></i> Message d'information
                </div>
                <div class="alert alert-warning">
                  <i class="bi bi-exclamation-triangle"></i> Message d'avertissement
                </div>
              </div>
            </div>
          </div>
        </div>

        <div id="utilisation-moodle" class="mt-5">
          <h2>Utilisation dans Moodle</h2>
          <p>Dans Moodle, les icônes sont utilisées pour :</p>
          <ul class="list-group mb-4">
            <li class="list-group-item">Indiquer les actions disponibles</li>
            <li class="list-group-item">Signaler des états et statuts</li>
            <li class="list-group-item">Améliorer la navigation</li>
            <li class="list-group-item">Renforcer les messages</li>
            <li class="list-group-item">Identifier les types de contenu</li>
          </ul>

          <div class="card mb-4">
            <div class="card-body">
              <h3 class="h5">Exemple d'intégration dans un template Moodle</h3>
              <pre class="bg-light p-3 rounded"><code>{{#icon}}
    &lt;i class="bi bi-{{name}} {{#size}}fs-{{size}}{{/size}} {{#color}}text-{{color}}{{/color}} {{#animation}}bi-{{animation}}{{/animation}}"&gt;&lt;/i&gt;
{{/icon}}</code></pre>
            </div>
          </div>
        </div>

        <div id="accessibilite" class="mt-5">
          <h2>Accessibilité</h2>
          <ul class="list-group mb-4">
            <li class="list-group-item">Fournissez un texte alternatif pour les icônes décoratives</li>
            <li class="list-group-item">Utilisez les icônes de manière cohérente</li>
            <li class="list-group-item">Maintenez un contraste suffisant</li>
            <li class="list-group-item">Assurez-vous que les icônes sont accessibles au clavier</li>
          </ul>
        </div>
      </div>
    </div>
  </div>
</div>