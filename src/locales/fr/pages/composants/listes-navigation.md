---
title: Listes de navigation
description: Documentation du composant Listes de navigation de Bootstrap 5 pour Moodle
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
          <p class="lead">Les listes de navigation sont des composants qui permettent d'organiser et de naviguer entre différentes sections ou pages. Elles sont idéales pour créer des menus, des onglets ou des liens de navigation.</p>
        </div>

        <div id="exemple-base" class="mt-5">
          <h2>Exemple de base</h2>
          <p>Une liste de navigation simple avec des liens.</p>
          <div class="card mb-4">
            <div class="card-body">
              <div class="component-preview">
                <ul class="nav">
                  <li class="nav-item">
                    <a class="nav-link active" href="#">Accueil</a>
                  </li>
                  <li class="nav-item">
                    <a class="nav-link" href="#">Profil</a>
                  </li>
                  <li class="nav-item">
                    <a class="nav-link" href="#">Messages</a>
                  </li>
                  <li class="nav-item">
                    <a class="nav-link" href="#">Paramètres</a>
                  </li>
                </ul>
              </div>
            </div>
          </div>
        </div>

        <div id="styles" class="mt-5">
          <h2>Styles</h2>

          <div class="card mb-4">
            <div class="card-body">
              <h3 class="h5">Navigation avec onglets</h3>
              <p>Les listes de navigation peuvent être utilisées comme des onglets.</p>
              <div class="component-preview">
                <ul class="nav nav-tabs" id="myTab" role="tablist">
                  <li class="nav-item" role="presentation">
                    <button class="nav-link active" id="home-tab" data-bs-toggle="tab" data-bs-target="#home" type="button" role="tab" aria-controls="home" aria-selected="true">
                      Accueil
                    </button>
                  </li>
                  <li class="nav-item" role="presentation">
                    <button class="nav-link" id="profile-tab" data-bs-toggle="tab" data-bs-target="#profile" type="button" role="tab" aria-controls="profile" aria-selected="false">
                      Profil
                    </button>
                  </li>
                  <li class="nav-item" role="presentation">
                    <button class="nav-link" id="contact-tab" data-bs-toggle="tab" data-bs-target="#contact" type="button" role="tab" aria-controls="contact" aria-selected="false">
                      Contact
                    </button>
                  </li>
                </ul>

                <div class="tab-content" id="myTabContent">
                  <div class="tab-pane fade show active" id="home" role="tabpanel" aria-labelledby="home-tab">
                    Contenu de l'onglet Accueil
                  </div>
                  <div class="tab-pane fade" id="profile" role="tabpanel" aria-labelledby="profile-tab">
                    Contenu de l'onglet Profil
                  </div>
                  <div class="tab-pane fade" id="contact" role="tabpanel" aria-labelledby="contact-tab">
                    Contenu de l'onglet Contact
                  </div>
                </div>
              </div>
            </div>
          </div>

          <div class="card mb-4">
            <div class="card-body">
              <h3 class="h5">Navigation avec icônes</h3>
              <p>Les listes de navigation peuvent inclure des icônes pour plus de clarté.</p>
              <div class="component-preview">
                <ul class="nav nav-pills">
                  <li class="nav-item">
                    <a class="nav-link active" href="#">
                      <i class="fas fa-home me-2"></i>
                      Accueil
                    </a>
                  </li>
                  <li class="nav-item">
                    <a class="nav-link" href="#">
                      <i class="fas fa-user me-2"></i>
                      Profil
                    </a>
                  </li>
                  <li class="nav-item">
                    <a class="nav-link" href="#">
                      <i class="fas fa-envelope me-2"></i>
                      Messages
                    </a>
                  </li>
                  <li class="nav-item">
                    <a class="nav-link" href="#">
                      <i class="fas fa-cog me-2"></i>
                      Paramètres
                    </a>
                  </li>
                </ul>
              </div>
            </div>
          </div>

          <div class="card mb-4">
            <div class="card-body">
              <h3 class="h5">Navigation verticale</h3>
              <p>Les listes de navigation peuvent être affichées verticalement.</p>
              <div class="component-preview">
                <ul class="nav flex-column">
                  <li class="nav-item">
                    <a class="nav-link active" href="#">
                      <i class="fas fa-home me-2"></i>
                      Accueil
                    </a>
                  </li>
                  <li class="nav-item">
                    <a class="nav-link" href="#">
                      <i class="fas fa-user me-2"></i>
                      Profil
                    </a>
                  </li>
                  <li class="nav-item">
                    <a class="nav-link" href="#">
                      <i class="fas fa-envelope me-2"></i>
                      Messages
                    </a>
                  </li>
                  <li class="nav-item">
                    <a class="nav-link" href="#">
                      <i class="fas fa-cog me-2"></i>
                      Paramètres
                    </a>
                  </li>
                </ul>
              </div>
            </div>
          </div>
        </div>

        <div id="utilisation-moodle" class="mt-5">
          <h2>Utilisation dans Moodle</h2>
          <p>Dans Moodle, les listes de navigation sont utilisées pour :</p>
          <ul class="list-group mb-4">
            <li class="list-group-item">Créer des menus de navigation</li>
            <li class="list-group-item">Organiser les sections d'un cours</li>
            <li class="list-group-item">Afficher les onglets de contenu</li>
            <li class="list-group-item">Naviguer entre les différentes vues</li>
            <li class="list-group-item">Créer des menus contextuels</li>
          </ul>

          <div class="card mb-4">
            <div class="card-body">
              <h3 class="h5">Exemple d'intégration dans un template Moodle</h3>
              <pre class="bg-light p-3 rounded"><code>{{#has_nav}}
    &lt;ul class="nav {{#vertical}}flex-column{{/vertical}} {{#pills}}nav-pills{{/pills}} {{#tabs}}nav-tabs{{/tabs}}" role="tablist"&gt;
        {{#items}}
        &lt;li class="nav-item" role="presentation"&gt;
            {{#is_tab}}
            &lt;button class="nav-link {{#active}}active{{/active}}"
                    id="{{id}}-tab"
                    data-bs-toggle="tab"
                    data-bs-target="#{{id}}"
                    type="button"
                    role="tab"
                    aria-controls="{{id}}"
                    aria-selected="{{#active}}true{{/active}}{{^active}}false{{/active}}"&gt;
                {{#icon}}
                &lt;i class="fas fa-{{icon}} me-2"&gt;&lt;/i&gt;
                {{/icon}}
                {{text}}
            &lt;/button&gt;
            {{/is_tab}}
            {{^is_tab}}
            &lt;a class="nav-link {{#active}}active{{/active}}" href="{{url}}"&gt;
                {{#icon}}
                &lt;i class="fas fa-{{icon}} me-2"&gt;&lt;/i&gt;
                {{/icon}}
                {{text}}
            &lt;/a&gt;
            {{/is_tab}}
        &lt;/li&gt;
        {{/items}}
    &lt;/ul&gt;

    {{#has_tab_content}}
    &lt;div class="tab-content"&gt;
        {{#items}}
        {{#is_tab}}
        &lt;div class="tab-pane fade {{#active}}show active{{/active}}"
             id="{{id}}"
             role="tabpanel"
             aria-labelledby="{{id}}-tab"&gt;
            {{{content}}}
        &lt;/div&gt;
        {{/is_tab}}
        {{/items}}
    &lt;/div&gt;
    {{/has_tab_content}}
{{/has_nav}}</code></pre>
            </div>
          </div>
        </div>

        <div id="accessibilite" class="mt-5">
          <h2>Accessibilité</h2>
          <ul class="list-group mb-4">
            <li class="list-group-item">Utilisez des rôles ARIA appropriés (tablist, tab, tabpanel)</li>
            <li class="list-group-item">Fournissez des états actifs clairs</li>
            <li class="list-group-item">Assurez-vous que la navigation au clavier fonctionne</li>
            <li class="list-group-item">Maintenez un contraste suffisant pour le texte</li>
            <li class="list-group-item">Évitez les menus imbriqués complexes</li>
          </ul>
        </div>
      </div>
    </div>
  </div>
</div>