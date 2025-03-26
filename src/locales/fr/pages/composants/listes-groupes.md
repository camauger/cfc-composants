---
title: Listes groupées
description: Documentation du composant Listes groupées de Bootstrap 5 pour Moodle
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
          <p class="lead">Les listes groupées sont des composants qui permettent d'afficher une série d'éléments liés dans un conteneur. Elles sont idéales pour organiser et présenter des informations de manière structurée.</p>
        </div>

        <div id="exemple-base" class="mt-5">
          <h2>Exemple de base</h2>
          <p>Une liste groupée simple avec des éléments.</p>
          <div class="card mb-4">
            <div class="card-body">
              <div class="component-preview">
                <ul class="list-group">
                  <li class="list-group-item">Premier élément</li>
                  <li class="list-group-item">Deuxième élément</li>
                  <li class="list-group-item">Troisième élément</li>
                </ul>
              </div>
            </div>
          </div>
        </div>

        <div id="styles" class="mt-5">
          <h2>Styles</h2>

          <div class="card mb-4">
            <div class="card-body">
              <h3 class="h5">Listes groupées avec actions</h3>
              <p>Les listes groupées peuvent inclure des boutons et des liens.</p>
              <div class="component-preview">
                <div class="list-group">
                  <a href="#" class="list-group-item list-group-item-action active">
                    Élément actif
                  </a>
                  <a href="#" class="list-group-item list-group-item-action">Élément cliquable</a>
                  <button type="button" class="list-group-item list-group-item-action">Bouton</button>
                </div>
              </div>
            </div>
          </div>

          <div class="card mb-4">
            <div class="card-body">
              <h3 class="h5">Listes groupées avec badges</h3>
              <p>Les listes groupées peuvent inclure des badges pour afficher des informations supplémentaires.</p>
              <div class="component-preview">
                <ul class="list-group">
                  <li class="list-group-item d-flex justify-content-between align-items-center">
                    Élément avec badge
                    <span class="badge bg-primary rounded-pill">12</span>
                  </li>
                  <li class="list-group-item d-flex justify-content-between align-items-center">
                    Élément avec statut
                    <span class="badge bg-success">Complété</span>
                  </li>
                </ul>
              </div>
            </div>
          </div>

          <div class="card mb-4">
            <div class="card-body">
              <h3 class="h5">Listes groupées avec contenu personnalisé</h3>
              <p>Les listes groupées peuvent contenir du contenu HTML personnalisé.</p>
              <div class="component-preview">
                <div class="list-group">
                  <a href="#" class="list-group-item list-group-item-action">
                    <div class="d-flex w-100 justify-content-between">
                      <h5 class="mb-1">Titre de l'élément</h5>
                      <small>Il y a 3 jours</small>
                    </div>
                    <p class="mb-1">Description détaillée de l'élément qui peut s'étendre sur plusieurs lignes.</p>
                  </a>
                  <a href="#" class="list-group-item list-group-item-action">
                    <div class="d-flex w-100 justify-content-between">
                      <h5 class="mb-1">Autre élément</h5>
                      <small>Il y a 5 jours</small>
                    </div>
                    <p class="mb-1">Une autre description détaillée avec des informations supplémentaires.</p>
                  </a>
                </div>
              </div>
            </div>
          </div>
        </div>

        <div id="utilisation-moodle" class="mt-5">
          <h2>Utilisation dans Moodle</h2>
          <p>Dans Moodle, les listes groupées sont particulièrement utiles pour :</p>
          <ul class="list-group mb-4">
            <li class="list-group-item">Afficher la liste des activités d'un cours</li>
            <li class="list-group-item">Présenter les participants d'un forum</li>
            <li class="list-group-item">Montrer les ressources disponibles</li>
            <li class="list-group-item">Organiser les paramètres de configuration</li>
          </ul>

          <div class="card mb-4">
            <div class="card-body">
              <h3 class="h5">Exemple d'intégration dans un template Moodle</h3>
              <pre class="bg-light p-3 rounded"><code>&lt;div class="course-activities"&gt;
    &lt;h4&gt;Activités du cours&lt;/h4&gt;
    &lt;div class="list-group"&gt;
        {{#activities}}
            &lt;a href="{{url}}" class="list-group-item list-group-item-action"&gt;
                &lt;div class="d-flex w-100 justify-content-between align-items-center"&gt;
                    &lt;div&gt;
                        &lt;h5 class="mb-1"&gt;{{name}}&lt;/h5&gt;
                        &lt;p class="mb-1"&gt;{{description}}&lt;/p&gt;
                    &lt;/div&gt;
                    &lt;div&gt;
                        &lt;span class="badge bg-{{status_color}}"&gt;{{status}}&lt;/span&gt;
                        {{#due_date}}
                            &lt;small class="text-muted"&gt;Date limite: {{due_date}}&lt;/small&gt;
                        {{/due_date}}
                    &lt;/div&gt;
                &lt;/div&gt;
            &lt;/a&gt;
        {{/activities}}
    &lt;/div&gt;
&lt;/div&gt;</code></pre>
            </div>
          </div>
        </div>

        <div id="accessibilite" class="mt-5">
          <h2>Accessibilité</h2>
          <ul class="list-group mb-4">
            <li class="list-group-item">Utilisez des éléments sémantiques appropriés (ul, li, a)</li>
            <li class="list-group-item">Assurez-vous que les liens sont clairement identifiables</li>
            <li class="list-group-item">Maintenez un contraste suffisant pour le texte</li>
            <li class="list-group-item">Fournissez des alternatives pour les badges et icônes</li>
            <li class="list-group-item">Assurez-vous que la navigation au clavier fonctionne correctement</li>
          </ul>
        </div>
      </div>
    </div>
  </div>
</div>