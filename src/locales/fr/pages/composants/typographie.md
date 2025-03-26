---
title: Typographie
description: Documentation de la typographie de Bootstrap 5 pour Moodle
template: pages/composant.html
---

<div class="container py-4">
  <div class="row">
    <div class="col-lg-3">
      <nav id="navbar-example3" class="h-100 flex-column align-items-stretch pe-4 border-end">
        <nav class="nav nav-pills flex-column">
          <a class="nav-link" href="#description">Description</a>
          <a class="nav-link" href="#titres">Titres</a>
          <a class="nav-link" href="#texte">Texte</a>
          <a class="nav-link" href="#listes">Listes</a>
          <a class="nav-link" href="#utilisation-moodle">Utilisation dans Moodle</a>
          <a class="nav-link" href="#accessibilite">Accessibilité</a>
        </nav>
      </nav>
    </div>

    <div class="col-lg-9">
      <div data-bs-spy="scroll" data-bs-target="#navbar-example3" data-bs-smooth-scroll="true" class="scrollspy-example-2" tabindex="0">
        <div id="description">
          <h2>Description</h2>
          <p class="lead">La typographie de Bootstrap fournit des styles de base pour les titres, les paragraphes, les listes et autres éléments de texte, avec des options de personnalisation pour l'alignement, la transformation et le style.</p>
        </div>

        <div id="titres" class="mt-5">
          <h2>Titres</h2>

          <div class="card mb-4">
            <div class="card-body">
              <h3 class="h5">Titres HTML</h3>
              <p>Les titres HTML sont stylisés avec des tailles et des espacements cohérents.</p>
              <div class="component-preview">
                <h1>h1. Titre de niveau 1</h1>
                <h2>h2. Titre de niveau 2</h2>
                <h3>h3. Titre de niveau 3</h3>
                <h4>h4. Titre de niveau 4</h4>
                <h5>h5. Titre de niveau 5</h5>
                <h6>h6. Titre de niveau 6</h6>
              </div>
            </div>
          </div>

          <div class="card mb-4">
            <div class="card-body">
              <h3 class="h5">Classes de titres</h3>
              <p>Utilisez les classes `.h1` à `.h6` pour appliquer les styles de titres à d'autres éléments.</p>
              <div class="component-preview">
                <p class="h1">Titre de niveau 1</p>
                <p class="h2">Titre de niveau 2</p>
                <p class="h3">Titre de niveau 3</p>
              </div>
            </div>
          </div>
        </div>

        <div id="texte" class="mt-5">
          <h2>Texte</h2>

          <div class="card mb-4">
            <div class="card-body">
              <h3 class="h5">Styles de texte</h3>
              <p>Bootstrap fournit des classes utilitaires pour le style du texte.</p>
              <div class="component-preview">
                <p class="lead">Texte en évidence avec la classe .lead</p>
                <p class="text-primary">Texte en couleur primaire</p>
                <p class="text-secondary">Texte en couleur secondaire</p>
                <p class="fw-bold">Texte en gras</p>
                <p class="fst-italic">Texte en italique</p>
              </div>
            </div>
          </div>

          <div class="card mb-4">
            <div class="card-body">
              <h3 class="h5">Alignement du texte</h3>
              <p>Contrôlez l'alignement du texte avec les classes utilitaires.</p>
              <div class="component-preview">
                <p class="text-start">Texte aligné à gauche</p>
                <p class="text-center">Texte centré</p>
                <p class="text-end">Texte aligné à droite</p>
              </div>
            </div>
          </div>
        </div>

        <div id="listes" class="mt-5">
          <h2>Listes</h2>

          <div class="card mb-4">
            <div class="card-body">
              <h3 class="h5">Listes non ordonnées</h3>
              <p>Les listes non ordonnées sont stylisées par défaut.</p>
              <div class="component-preview">
                <ul>
                  <li>Premier élément</li>
                  <li>Deuxième élément</li>
                  <li>Troisième élément</li>
                </ul>
              </div>
            </div>
          </div>

          <div class="card mb-4">
            <div class="card-body">
              <h3 class="h5">Listes ordonnées</h3>
              <p>Les listes ordonnées conservent leur numérotation.</p>
              <div class="component-preview">
                <ol>
                  <li>Premier élément</li>
                  <li>Deuxième élément</li>
                  <li>Troisième élément</li>
                </ol>
              </div>
            </div>
          </div>
        </div>

        <div id="utilisation-moodle" class="mt-5">
          <h2>Utilisation dans Moodle</h2>
          <p>Dans Moodle, la typographie est particulièrement importante pour :</p>
          <ul class="list-group mb-4">
            <li class="list-group-item">Structurer le contenu des cours</li>
            <li class="list-group-item">Créer une hiérarchie visuelle claire</li>
            <li class="list-group-item">Améliorer la lisibilité du contenu</li>
            <li class="list-group-item">Maintenir une cohérence visuelle</li>
          </ul>

          <div class="card mb-4">
            <div class="card-body">
              <h3 class="h5">Exemple d'intégration dans un template Moodle</h3>
              <pre class="bg-light p-3 rounded"><code>{{#course}}
    &lt;div class="course-content"&gt;
        &lt;h1 class="course-title"&gt;{{fullname}}&lt;/h1&gt;
        &lt;p class="lead course-description"&gt;{{summary}}&lt;/p&gt;

        {{#sections}}
            &lt;div class="section"&gt;
                &lt;h2 class="section-title"&gt;{{name}}&lt;/h2&gt;
                &lt;div class="section-content"&gt;
                    {{#modules}}
                        &lt;h3 class="module-title"&gt;{{name}}&lt;/h3&gt;
                        &lt;p class="module-description"&gt;{{description}}&lt;/p&gt;
                    {{/modules}}
                &lt;/div&gt;
            &lt;/div&gt;
        {{/sections}}
    &lt;/div&gt;
{{/course}}</code></pre>
            </div>
          </div>
        </div>

        <div id="accessibilite" class="mt-5">
          <h2>Accessibilité</h2>
          <ul class="list-group mb-4">
            <li class="list-group-item">Utilisez une hiérarchie de titres appropriée (h1, h2, h3, etc.)</li>
            <li class="list-group-item">Maintenez un contraste suffisant pour le texte</li>
            <li class="list-group-item">Évitez d'utiliser uniquement la couleur pour transmettre des informations</li>
            <li class="list-group-item">Utilisez des tailles de police lisibles</li>
            <li class="list-group-item">Assurez-vous que le texte reste lisible lors du zoom</li>
          </ul>
        </div>
      </div>
    </div>
  </div>
</div>