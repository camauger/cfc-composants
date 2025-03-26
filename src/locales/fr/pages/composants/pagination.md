---
title: Pagination
description: Documentation du composant Pagination de Bootstrap 5 pour Moodle
template: pages/composant.html
---

<div class="container py-4">
  <div class="row">
    <div class="col-lg-3">
      <nav id="navbar-example3" class="h-100 flex-column align-items-stretch pe-4 border-end">
        <nav class="nav nav-pills flex-column">
          <a class="nav-link" href="#description">Description</a>
          <a class="nav-link" href="#exemple-base">Exemple de base</a>
          <a class="nav-link" href="#styles">Styles de pagination</a>
          <a class="nav-link" href="#utilisation-moodle">Utilisation dans Moodle</a>
          <a class="nav-link" href="#accessibilite">Accessibilité</a>
        </nav>
      </nav>
    </div>

    <div class="col-lg-9">
      <div data-bs-spy="scroll" data-bs-target="#navbar-example3" data-bs-smooth-scroll="true" class="scrollspy-example-2" tabindex="0">
        <div id="description">
          <h2>Description</h2>
          <p class="lead">La pagination est un composant de navigation qui permet aux utilisateurs de naviguer entre les pages d'un ensemble de résultats. Elle est particulièrement utile pour les listes longues de contenu.</p>
        </div>

        <div id="exemple-base" class="mt-5">
          <h2>Exemple de base</h2>
          <p>Une pagination simple avec des liens vers les pages précédentes et suivantes.</p>
          <div class="card mb-4">
            <div class="card-body">
              <div class="component-preview">
                <nav aria-label="Navigation des pages">
                  <ul class="pagination">
                    <li class="page-item disabled">
                      <a class="page-link" href="#" tabindex="-1" aria-disabled="true">Précédent</a>
                    </li>
                    <li class="page-item active"><a class="page-link" href="#">1</a></li>
                    <li class="page-item"><a class="page-link" href="#">2</a></li>
                    <li class="page-item"><a class="page-link" href="#">3</a></li>
                    <li class="page-item">
                      <a class="page-link" href="#">Suivant</a>
                    </li>
                  </ul>
                </nav>
              </div>
            </div>
          </div>
        </div>

        <div id="styles" class="mt-5">
          <h2>Styles de pagination</h2>

          <div class="card mb-4">
            <div class="card-body">
              <h3 class="h5">Pagination avec icônes</h3>
              <p>Utilisez des icônes pour les boutons précédent/suivant.</p>
              <div class="component-preview">
                <nav aria-label="Navigation des pages avec icônes">
                  <ul class="pagination">
                    <li class="page-item disabled">
                      <a class="page-link" href="#" tabindex="-1" aria-disabled="true">
                        <i class="fas fa-chevron-left"></i>
                      </a>
                    </li>
                    <li class="page-item active"><a class="page-link" href="#">1</a></li>
                    <li class="page-item"><a class="page-link" href="#">2</a></li>
                    <li class="page-item"><a class="page-link" href="#">3</a></li>
                    <li class="page-item">
                      <a class="page-link" href="#">
                        <i class="fas fa-chevron-right"></i>
                      </a>
                    </li>
                  </ul>
                </nav>
              </div>
            </div>
          </div>

          <div class="card mb-4">
            <div class="card-body">
              <h3 class="h5">Pagination avec ellipsis</h3>
              <p>Utilisez des points de suspension pour les longues listes de pages.</p>
              <div class="component-preview">
                <nav aria-label="Navigation des pages avec ellipsis">
                  <ul class="pagination">
                    <li class="page-item">
                      <a class="page-link" href="#">
                        <i class="fas fa-chevron-left"></i>
                      </a>
                    </li>
                    <li class="page-item active"><a class="page-link" href="#">1</a></li>
                    <li class="page-item"><a class="page-link" href="#">2</a></li>
                    <li class="page-item"><a class="page-link" href="#">3</a></li>
                    <li class="page-item disabled">
                      <span class="page-link">...</span>
                    </li>
                    <li class="page-item"><a class="page-link" href="#">8</a></li>
                    <li class="page-item">
                      <a class="page-link" href="#">
                        <i class="fas fa-chevron-right"></i>
                      </a>
                    </li>
                  </ul>
                </nav>
              </div>
            </div>
          </div>

          <div class="card mb-4">
            <div class="card-body">
              <h3 class="h5">Pagination avec taille personnalisée</h3>
              <p>Utilisez les classes de taille pour modifier l'apparence de la pagination.</p>
              <div class="component-preview">
                <nav aria-label="Navigation des pages de grande taille">
                  <ul class="pagination pagination-lg">
                    <li class="page-item disabled">
                      <a class="page-link" href="#" tabindex="-1" aria-disabled="true">Précédent</a>
                    </li>
                    <li class="page-item active"><a class="page-link" href="#">1</a></li>
                    <li class="page-item"><a class="page-link" href="#">2</a></li>
                    <li class="page-item"><a class="page-link" href="#">3</a></li>
                    <li class="page-item">
                      <a class="page-link" href="#">Suivant</a>
                    </li>
                  </ul>
                </nav>
              </div>
            </div>
          </div>
        </div>

        <div id="utilisation-moodle" class="mt-5">
          <h2>Utilisation dans Moodle</h2>
          <p>Dans Moodle, la pagination est particulièrement utile pour :</p>
          <ul class="list-group mb-4">
            <li class="list-group-item">Naviguer dans les listes de cours</li>
            <li class="list-group-item">Parcourir les résultats des activités</li>
            <li class="list-group-item">Accéder aux différentes sections d'un cours</li>
            <li class="list-group-item">Naviguer dans les forums et discussions</li>
          </ul>

          <div class="card mb-4">
            <div class="card-body">
              <h3 class="h5">Exemple d'intégration dans un template Moodle</h3>
              <pre class="bg-light p-3 rounded"><code>{{#courses}}
    &lt;div class="courses-list"&gt;
        {{#items}}
            &lt;div class="course-item"&gt;
                {{&gt; course_card}}
            &lt;/div&gt;
        {{/items}}

        &lt;nav aria-label="Navigation des cours"&gt;
            &lt;ul class="pagination justify-content-center"&gt;
                {{#pagination}}
                    &lt;li class="page-item {{#active}}active{{/active}} {{#disabled}}disabled{{/disabled}}"&gt;
                        &lt;a class="page-link" href="{{url}}" {{#disabled}}tabindex="-1" aria-disabled="true"{{/disabled}}&gt;
                            {{#icon}}
                                &lt;i class="fas fa-{{icon}}"&gt;&lt;/i&gt;
                            {{/icon}}
                            {{^icon}}
                                {{text}}
                            {{/icon}}
                        &lt;/a&gt;
                    &lt;/li&gt;
                {{/pagination}}
            &lt;/ul&gt;
        &lt;/nav&gt;
    &lt;/div&gt;
{{/courses}}</code></pre>
            </div>
          </div>
        </div>

        <div id="accessibilite" class="mt-5">
          <h2>Accessibilité</h2>
          <ul class="list-group mb-4">
            <li class="list-group-item">Utilisez l'attribut `aria-label` pour décrire la navigation</li>
            <li class="list-group-item">Assurez-vous que la navigation au clavier fonctionne correctement</li>
            <li class="list-group-item">Fournissez des libellés clairs pour les boutons précédent/suivant</li>
            <li class="list-group-item">Indiquez clairement la page active</li>
            <li class="list-group-item">Maintenez un contraste suffisant pour les liens</li>
          </ul>
        </div>
      </div>
    </div>
  </div>
</div>