---
title: Grille
description: Documentation du système de grille de Bootstrap 5 pour Moodle
template: pages/composant.html
---

<div class="container py-4">
  <div class="row">
    <div class="col-lg-3">
      <nav id="navbar-example3" class="h-100 flex-column align-items-stretch pe-4 border-end">
        <nav class="nav nav-pills flex-column">
          <a class="nav-link" href="#description">Description</a>
          <a class="nav-link" href="#exemple-base">Exemple de base</a>
          <a class="nav-link" href="#colonnes">Colonnes</a>
          <a class="nav-link" href="#breakpoints">Breakpoints</a>
          <a class="nav-link" href="#utilisation-moodle">Utilisation dans Moodle</a>
          <a class="nav-link" href="#accessibilite">Accessibilité</a>
        </nav>
      </nav>
    </div>

    <div class="col-lg-9">
      <div data-bs-spy="scroll" data-bs-target="#navbar-example3" data-bs-smooth-scroll="true" class="scrollspy-example-2" tabindex="0">
        <div id="description">
          <h2>Description</h2>
          <p class="lead">Le système de grille de Bootstrap utilise une série de conteneurs, de lignes et de colonnes pour organiser et aligner le contenu. Il est construit avec flexbox et est entièrement responsive.</p>
        </div>

        <div id="exemple-base" class="mt-5">
          <h2>Exemple de base</h2>
          <p>Voici un exemple simple d'utilisation du système de grille.</p>
          <div class="card mb-4">
            <div class="card-body">
              <div class="component-preview">
                <div class="container">
                  <div class="row">
                    <div class="col">
                      Colonne 1
                    </div>
                    <div class="col">
                      Colonne 2
                    </div>
                    <div class="col">
                      Colonne 3
                    </div>
                  </div>
                </div>
              </div>
            </div>
          </div>
        </div>

        <div id="colonnes" class="mt-5">
          <h2>Colonnes</h2>

          <div class="card mb-4">
            <div class="card-body">
              <h3 class="h5">Colonnes automatiques</h3>
              <p>Les colonnes s'ajustent automatiquement pour occuper l'espace disponible.</p>
              <div class="component-preview">
                <div class="container">
                  <div class="row">
                    <div class="col">Colonne 1</div>
                    <div class="col">Colonne 2</div>
                    <div class="col">Colonne 3</div>
                  </div>
                </div>
              </div>
            </div>
          </div>

          <div class="card mb-4">
            <div class="card-body">
              <h3 class="h5">Colonnes de largeur fixe</h3>
              <p>Définissez des largeurs spécifiques pour vos colonnes.</p>
              <div class="component-preview">
                <div class="container">
                  <div class="row">
                    <div class="col-4">Colonne 4/12</div>
                    <div class="col-8">Colonne 8/12</div>
                  </div>
                </div>
              </div>
            </div>
          </div>

          <div class="card mb-4">
            <div class="card-body">
              <h3 class="h5">Colonnes responsives</h3>
              <p>Les colonnes peuvent s'adapter à différentes tailles d'écran.</p>
              <div class="component-preview">
                <div class="container">
                  <div class="row">
                    <div class="col-12 col-md-6 col-lg-4">Colonne responsive</div>
                    <div class="col-12 col-md-6 col-lg-4">Colonne responsive</div>
                    <div class="col-12 col-md-6 col-lg-4">Colonne responsive</div>
                  </div>
                </div>
              </div>
            </div>
          </div>
        </div>

        <div id="breakpoints" class="mt-5">
          <h2>Breakpoints</h2>
          <p>Bootstrap utilise six breakpoints pour créer des mises en page responsives :</p>
          <ul class="list-group mb-4">
            <li class="list-group-item">xs (extra small) < 576px</li>
            <li class="list-group-item">sm (small) ≥ 576px</li>
            <li class="list-group-item">md (medium) ≥ 768px</li>
            <li class="list-group-item">lg (large) ≥ 992px</li>
            <li class="list-group-item">xl (extra large) ≥ 1200px</li>
            <li class="list-group-item">xxl (extra extra large) ≥ 1400px</li>
          </ul>
        </div>

        <div id="utilisation-moodle" class="mt-5">
          <h2>Utilisation dans Moodle</h2>
          <p>Dans Moodle, le système de grille est particulièrement utile pour :</p>
          <ul class="list-group mb-4">
            <li class="list-group-item">Organiser le contenu des cours</li>
            <li class="list-group-item">Créer des mises en page de tableaux de bord</li>
            <li class="list-group-item">Structurer les pages d'activités</li>
            <li class="list-group-item">Organiser les blocs de contenu</li>
          </ul>

          <div class="card mb-4">
            <div class="card-body">
              <h3 class="h5">Exemple d'intégration dans un template Moodle</h3>
              <pre class="bg-light p-3 rounded"><code>{{#course}}
    &lt;div class="container"&gt;
        &lt;div class="row"&gt;
            &lt;div class="col-12 col-lg-8"&gt;
                &lt;div class="course-content"&gt;
                    {{#sections}}
                        &lt;div class="section"&gt;
                            {{name}}
                        &lt;/div&gt;
                    {{/sections}}
                &lt;/div&gt;
            &lt;/div&gt;
            &lt;div class="col-12 col-lg-4"&gt;
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
            <li class="list-group-item">Assurez-vous que l'ordre des colonnes est logique pour les lecteurs d'écran</li>
            <li class="list-group-item">Maintenez une hiérarchie de contenu claire</li>
            <li class="list-group-item">Testez la mise en page avec différentes tailles d'écran</li>
            <li class="list-group-item">Utilisez des classes utilitaires pour l'espacement et l'alignement</li>
          </ul>
        </div>
      </div>
    </div>
  </div>
</div>