---
title: Cartes
description: Documentation du composant Cartes de Bootstrap 5 pour Moodle
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
          <p class="lead">Les cartes sont des conteneurs flexibles idéaux pour organiser et présenter des informations. Elles peuvent contenir différents types de contenu et s'adapter à différents contextes.</p>
        </div>

        <div id="exemple-base" class="mt-5">
          <h2>Exemple de base</h2>
          <p>Une carte simple avec un en-tête, un corps et un pied de page.</p>
          <div class="card mb-4">
            <div class="card-body">
              <div class="component-preview">
                <div class="card">
                  <div class="card-header">
                    En-tête de la carte
                  </div>
                  <div class="card-body">
                    <h5 class="card-title">Titre de la carte</h5>
                    <p class="card-text">Contenu de la carte avec du texte.</p>
                  </div>
                  <div class="card-footer">
                    Pied de page de la carte
                  </div>
                </div>
              </div>
            </div>
          </div>
        </div>

        <div id="styles" class="mt-5">
          <h2>Styles</h2>

          <div class="card mb-4">
            <div class="card-body">
              <h3 class="h5">Cartes avec images</h3>
              <p>Les cartes peuvent inclure des images.</p>
              <div class="component-preview">
                <div class="card">
                  <img src="https://placehold.co/400x200" class="card-img-top" alt="Image d'exemple">
                  <div class="card-body">
                    <h5 class="card-title">Titre de la carte</h5>
                    <p class="card-text">Description de l'image.</p>
                  </div>
                </div>
              </div>
            </div>
          </div>

          <div class="card mb-4">
            <div class="card-body">
              <h3 class="h5">Cartes avec couleurs</h3>
              <p>Les cartes peuvent avoir différentes couleurs.</p>
              <div class="component-preview">
                <div class="card bg-primary text-white mb-3">
                  <div class="card-body">
                    <h5 class="card-title">Carte primaire</h5>
                    <p class="card-text">Contenu de la carte.</p>
                  </div>
                </div>
                <div class="card bg-success text-white mb-3">
                  <div class="card-body">
                    <h5 class="card-title">Carte succès</h5>
                    <p class="card-text">Contenu de la carte.</p>
                  </div>
                </div>
                <div class="card bg-danger text-white">
                  <div class="card-body">
                    <h5 class="card-title">Carte danger</h5>
                    <p class="card-text">Contenu de la carte.</p>
                  </div>
                </div>
              </div>
            </div>
          </div>

          <div class="card mb-4">
            <div class="card-body">
              <h3 class="h5">Cartes avec bordures</h3>
              <p>Les cartes peuvent avoir différents styles de bordures.</p>
              <div class="component-preview">
                <div class="card border-primary mb-3">
                  <div class="card-body">
                    <h5 class="card-title">Carte avec bordure primaire</h5>
                    <p class="card-text">Contenu de la carte.</p>
                  </div>
                </div>
                <div class="card border-success">
                  <div class="card-body">
                    <h5 class="card-title">Carte avec bordure succès</h5>
                    <p class="card-text">Contenu de la carte.</p>
                  </div>
                </div>
              </div>
            </div>
          </div>

          <div class="card mb-4">
            <div class="card-body">
              <h3 class="h5">Grille de cartes</h3>
              <p>Les cartes peuvent être organisées en grille.</p>
              <div class="component-preview">
                <div class="row row-cols-1 row-cols-md-3 g-4">
                  <div class="col">
                    <div class="card h-100">
                      <div class="card-body">
                        <h5 class="card-title">Carte 1</h5>
                        <p class="card-text">Contenu de la première carte.</p>
                      </div>
                    </div>
                  </div>
                  <div class="col">
                    <div class="card h-100">
                      <div class="card-body">
                        <h5 class="card-title">Carte 2</h5>
                        <p class="card-text">Contenu de la deuxième carte.</p>
                      </div>
                    </div>
                  </div>
                  <div class="col">
                    <div class="card h-100">
                      <div class="card-body">
                        <h5 class="card-title">Carte 3</h5>
                        <p class="card-text">Contenu de la troisième carte.</p>
                      </div>
                    </div>
                  </div>
                </div>
              </div>
            </div>
          </div>
        </div>

        <div id="utilisation-moodle" class="mt-5">
          <h2>Utilisation dans Moodle</h2>
          <p>Dans Moodle, les cartes sont utilisées pour :</p>
          <ul class="list-group mb-4">
            <li class="list-group-item">Présenter les activités du cours</li>
            <li class="list-group-item">Afficher les informations utilisateur</li>
            <li class="list-group-item">Organiser les sections de contenu</li>
            <li class="list-group-item">Afficher des statistiques</li>
            <li class="list-group-item">Présenter des ressources pédagogiques</li>
          </ul>

          <div class="card mb-4">
            <div class="card-body">
              <h3 class="h5">Exemple d'intégration dans un template Moodle</h3>
              <pre class="bg-light p-3 rounded"><code>{{#card}}
    &lt;div class="card {{#color}}bg-{{color}} text-{{text_color}}{{/color}} {{#border}}border-{{border}}{{/border}}"&gt;
        {{#header}}
        &lt;div class="card-header"&gt;
            {{header}}
        &lt;/div&gt;
        {{/header}}
        {{#image}}
        &lt;img src="{{src}}" class="card-img-top" alt="{{alt}}"&gt;
        {{/image}}
        &lt;div class="card-body"&gt;
            {{#title}}
            &lt;h5 class="card-title"&gt;{{title}}&lt;/h5&gt;
            {{/title}}
            {{#text}}
            &lt;p class="card-text"&gt;{{text}}&lt;/p&gt;
            {{/text}}
            {{#button}}
            &lt;a href="{{href}}" class="btn btn-{{style}}"&gt;{{text}}&lt;/a&gt;
            {{/button}}
        &lt;/div&gt;
        {{#footer}}
        &lt;div class="card-footer"&gt;
            {{footer}}
        &lt;/div&gt;
        {{/footer}}
    &lt;/div&gt;
{{/card}}</code></pre>
            </div>
          </div>
        </div>

        <div id="accessibilite" class="mt-5">
          <h2>Accessibilité</h2>
          <ul class="list-group mb-4">
            <li class="list-group-item">Utilisez des titres descriptifs pour les cartes</li>
            <li class="list-group-item">Maintenez un contraste suffisant</li>
            <li class="list-group-item">Structurez le contenu de manière logique</li>
            <li class="list-group-item">Assurez-vous que les cartes sont accessibles au clavier</li>
          </ul>
        </div>
      </div>
    </div>
  </div>
</div>
