---
title: Listes
description: Documentation du composant Listes de Bootstrap 5 pour Moodle
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
          <p class="lead">Les listes sont des composants essentiels pour organiser et présenter des informations de manière structurée. Elles permettent d'afficher des éléments dans un format facilement lisible.</p>
        </div>

        <div id="exemple-base" class="mt-5">
          <h2>Exemple de base</h2>
          <p>Une liste simple avec des éléments.</p>
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
              <h3 class="h5">Listes avec actions</h3>
              <p>Les listes peuvent inclure des éléments interactifs.</p>
              <div class="component-preview">
                <div class="list-group">
                  <a href="#" class="list-group-item list-group-item-action active">
                    Élément actif
                  </a>
                  <a href="#" class="list-group-item list-group-item-action">
                    Élément cliquable
                  </a>
                  <button type="button" class="list-group-item list-group-item-action">
                    Bouton liste
                  </button>
                </div>
              </div>
            </div>
          </div>

          <div class="card mb-4">
            <div class="card-body">
              <h3 class="h5">Listes avec badges</h3>
              <p>Les listes peuvent inclure des badges pour plus d'information.</p>
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
              <h3 class="h5">Listes personnalisées</h3>
              <p>Les listes peuvent avoir des styles personnalisés.</p>
              <div class="component-preview">
                <ul class="list-group">
                  <li class="list-group-item list-group-item-primary">Élément principal</li>
                  <li class="list-group-item list-group-item-secondary">Élément secondaire</li>
                  <li class="list-group-item list-group-item-success">Élément succès</li>
                  <li class="list-group-item list-group-item-danger">Élément erreur</li>
                  <li class="list-group-item list-group-item-warning">Élément avertissement</li>
                  <li class="list-group-item list-group-item-info">Élément information</li>
                  <li class="list-group-item list-group-item-light">Élément clair</li>
                  <li class="list-group-item list-group-item-dark">Élément sombre</li>
                </ul>
              </div>
            </div>
          </div>

          <div class="card mb-4">
            <div class="card-body">
              <h3 class="h5">Listes avec contenu personnalisé</h3>
              <p>Les éléments de liste peuvent contenir du contenu HTML personnalisé.</p>
              <div class="component-preview">
                <div class="list-group">
                  <a href="#" class="list-group-item list-group-item-action">
                    <div class="d-flex w-100 justify-content-between">
                      <h5 class="mb-1">Titre de l'élément</h5>
                      <small>Il y a 3 jours</small>
                    </div>
                    <p class="mb-1">Description détaillée de l'élément de la liste.</p>
                    <small>Informations supplémentaires</small>
                  </a>
                  <a href="#" class="list-group-item list-group-item-action">
                    <div class="d-flex w-100 justify-content-between">
                      <h5 class="mb-1">Autre élément</h5>
                      <small>Il y a 5 jours</small>
                    </div>
                    <p class="mb-1">Description d'un autre élément de la liste.</p>
                    <small>Autres informations</small>
                  </a>
                </div>
              </div>
            </div>
          </div>
        </div>

        <div id="utilisation-moodle" class="mt-5">
          <h2>Utilisation dans Moodle</h2>
          <p>Dans Moodle, les listes sont utilisées pour :</p>
          <ul class="list-group mb-4">
            <li class="list-group-item">Afficher les activités d'un cours</li>
            <li class="list-group-item">Présenter les participants d'un cours</li>
            <li class="list-group-item">Montrer les notifications et messages</li>
            <li class="list-group-item">Organiser les ressources pédagogiques</li>
            <li class="list-group-item">Afficher les résultats et notes</li>
          </ul>

          <div class="card mb-4">
            <div class="card-body">
              <h3 class="h5">Exemple d'intégration dans un template Moodle</h3>
              <pre class="bg-light p-3 rounded"><code>{{#has_items}}
    &lt;div class="list-group"&gt;
        {{#items}}
        &lt;a href="{{url}}"
           class="list-group-item list-group-item-action {{#active}}active{{/active}} {{#disabled}}disabled{{/disabled}}"&gt;
            {{#has_badge}}
            &lt;div class="d-flex w-100 justify-content-between align-items-center"&gt;
                &lt;div&gt;
                    &lt;h5 class="mb-1"&gt;{{title}}&lt;/h5&gt;
                    &lt;p class="mb-1"&gt;{{description}}&lt;/p&gt;
                    &lt;small&gt;{{additional_info}}&lt;/small&gt;
                &lt;/div&gt;
                &lt;span class="badge bg-{{badge_style}} {{#rounded}}rounded-pill{{/rounded}}"&gt;
                    {{badge_text}}
                &lt;/span&gt;
            &lt;/div&gt;
            {{/has_badge}}
            {{^has_badge}}
            &lt;div&gt;
                &lt;h5 class="mb-1"&gt;{{title}}&lt;/h5&gt;
                &lt;p class="mb-1"&gt;{{description}}&lt;/p&gt;
                &lt;small&gt;{{additional_info}}&lt;/small&gt;
            &lt;/div&gt;
            {{/has_badge}}
        &lt;/a&gt;
        {{/items}}
    &lt;/div&gt;
{{/has_items}}</code></pre>
            </div>
          </div>
        </div>

        <div id="accessibilite" class="mt-5">
          <h2>Accessibilité</h2>
          <ul class="list-group mb-4">
            <li class="list-group-item">Utilisez des listes sémantiques (ul, ol) pour une meilleure structure</li>
            <li class="list-group-item">Fournissez des textes descriptifs pour les liens</li>
            <li class="list-group-item">Maintenez un contraste suffisant pour le texte</li>
            <li class="list-group-item">Assurez-vous que les listes sont accessibles au clavier</li>
            <li class="list-group-item">Utilisez des badges et des icônes de manière appropriée</li>
          </ul>
        </div>
      </div>
    </div>
  </div>
</div>