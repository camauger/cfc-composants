---
title: Conteneurs
description: Documentation du composant Conteneurs de Bootstrap 5 pour Moodle
template: pages/composant.html
---

<div class="container py-4">
  <div class="row">
    <div class="col-lg-3">
      <nav id="navbar-example3" class="h-100 flex-column align-items-stretch pe-4 border-end">
        <nav class="nav nav-pills flex-column">
          <a class="nav-link" href="#description">Description</a>
          <a class="nav-link" href="#exemple-base">Exemple de base</a>
          <a class="nav-link" href="#variantes">Variantes de conteneurs</a>
          <a class="nav-link" href="#utilisation-moodle">Utilisation dans Moodle</a>
          <a class="nav-link" href="#accessibilite">Accessibilité</a>
        </nav>
      </nav>
    </div>

    <div class="col-lg-9">
      <div data-bs-spy="scroll" data-bs-target="#navbar-example3" data-bs-smooth-scroll="true" class="scrollspy-example-2" tabindex="0">
        <div id="description">
          <h2>Description</h2>
          <p class="lead">Les conteneurs sont les éléments de base de la mise en page Bootstrap. Ils contiennent, remplissent et centrent votre contenu dans un appareil ou une fenêtre de visualisation donné.</p>
        </div>

        <div id="exemple-base" class="mt-5">
          <h2>Exemple de base</h2>
          <p>Les conteneurs sont nécessaires pour utiliser le système de grille de Bootstrap.</p>
          <div class="card mb-4">
            <div class="card-body">
              <div class="component-preview">
                <div class="container">
                  <div class="row">
                    <div class="col">
                      Contenu de la colonne
                    </div>
                  </div>
                </div>
              </div>
            </div>
          </div>
        </div>

        <div id="variantes" class="mt-5">
          <h2>Variantes de conteneurs</h2>

          <div class="card mb-4">
            <div class="card-body">
              <h3 class="h5">Conteneur responsive</h3>
              <p>Le conteneur par défaut est responsive et s'adapte à toutes les tailles d'écran.</p>
              <div class="component-preview">
                <div class="container">
                  <div class="row">
                    <div class="col">
                      Conteneur responsive
                    </div>
                  </div>
                </div>
              </div>
            </div>
          </div>

          <div class="card mb-4">
            <div class="card-body">
              <h3 class="h5">Conteneur fluide</h3>
              <p>Utilisez `.container-fluid` pour un conteneur qui prend toute la largeur disponible.</p>
              <div class="component-preview">
                <div class="container-fluid">
                  <div class="row">
                    <div class="col">
                      Conteneur fluide
                    </div>
                  </div>
                </div>
              </div>
            </div>
          </div>

          <div class="card mb-4">
            <div class="card-body">
              <h3 class="h5">Conteneurs avec breakpoints</h3>
              <p>Les conteneurs peuvent être configurés pour s'adapter à des breakpoints spécifiques.</p>
              <div class="component-preview">
                <div class="container-sm">100% largeur jusqu'à 576px</div>
                <div class="container-md">100% largeur jusqu'à 768px</div>
                <div class="container-lg">100% largeur jusqu'à 992px</div>
                <div class="container-xl">100% largeur jusqu'à 1200px</div>
                <div class="container-xxl">100% largeur jusqu'à 1400px</div>
              </div>
            </div>
          </div>
        </div>

        <div id="utilisation-moodle" class="mt-5">
          <h2>Utilisation dans Moodle</h2>
          <p>Dans Moodle, les conteneurs sont particulièrement utiles pour :</p>
          <ul class="list-group mb-4">
            <li class="list-group-item">Structurer le contenu des pages de cours</li>
            <li class="list-group-item">Organiser les blocs de contenu</li>
            <li class="list-group-item">Créer des mises en page responsives pour les activités</li>
            <li class="list-group-item">Gérer l'espacement du contenu dans les templates</li>
          </ul>

          <div class="card mb-4">
            <div class="card-body">
              <h3 class="h5">Exemple d'intégration dans un template Moodle</h3>
              <pre class="bg-light p-3 rounded"><code>{{#course}}
    &lt;div class="container"&gt;
        &lt;div class="row"&gt;
            &lt;div class="col-md-8"&gt;
                &lt;div class="course-content"&gt;
                    {{#sections}}
                        &lt;div class="section"&gt;
                            {{name}}
                        &lt;/div&gt;
                    {{/sections}}
                &lt;/div&gt;
            &lt;/div&gt;
            &lt;div class="col-md-4"&gt;
                &lt;div class="course-sidebar"&gt;
                    {{#blocks}}
                        {{&gt; block}}
                    {{/blocks}}
                &lt;/div&gt;
            &lt;/div&gt;
        &lt;/div&gt;
    &lt;/div&gt;
{{/course}}</code></pre>
            </div>
          </div>
        </div>

        <div id="accessibilite" class="mt-5">
          <h2>Accessibilité</h2>
          <ul class="list-group mb-4">
            <li class="list-group-item">Assurez-vous que le contenu reste lisible à toutes les tailles d'écran</li>
            <li class="list-group-item">Maintenez une hiérarchie visuelle claire dans la mise en page</li>
            <li class="list-group-item">Utilisez des marges et espacements appropriés pour améliorer la lisibilité</li>
            <li class="list-group-item">Testez la mise en page avec différents lecteurs d'écran</li>
          </ul>
        </div>
      </div>
    </div>
  </div>
</div>