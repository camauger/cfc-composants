---
title: Accordéons
description: Documentation du composant Accordéons de Bootstrap 5 pour Moodle
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
          <p class="lead">Les accordéons sont des composants qui permettent d'afficher du contenu de manière organisée et interactive. Ils sont idéaux pour présenter des informations détaillées tout en gardant une interface claire et concise.</p>
        </div>

        <div id="exemple-base" class="mt-5">
          <h2>Exemple de base</h2>
          <p>Un accordéon simple avec trois sections.</p>
          <div class="card mb-4">
            <div class="card-body">
              <div class="component-preview">
                <div class="accordion" id="basicAccordion">
                  <div class="accordion-item">
                    <h2 class="accordion-header" id="headingOne">
                      <button class="accordion-button" type="button" data-bs-toggle="collapse" data-bs-target="#collapseOne" aria-expanded="true" aria-controls="collapseOne">
                        Première section
                      </button>
                    </h2>
                    <div id="collapseOne" class="accordion-collapse collapse show" aria-labelledby="headingOne" data-bs-parent="#basicAccordion">
                      <div class="accordion-body">
                        Contenu de la première section
                      </div>
                    </div>
                  </div>
                  <div class="accordion-item">
                    <h2 class="accordion-header" id="headingTwo">
                      <button class="accordion-button collapsed" type="button" data-bs-toggle="collapse" data-bs-target="#collapseTwo" aria-expanded="false" aria-controls="collapseTwo">
                        Deuxième section
                      </button>
                    </h2>
                    <div id="collapseTwo" class="accordion-collapse collapse" aria-labelledby="headingTwo" data-bs-parent="#basicAccordion">
                      <div class="accordion-body">
                        Contenu de la deuxième section
                      </div>
                    </div>
                  </div>
                  <div class="accordion-item">
                    <h2 class="accordion-header" id="headingThree">
                      <button class="accordion-button collapsed" type="button" data-bs-toggle="collapse" data-bs-target="#collapseThree" aria-expanded="false" aria-controls="collapseThree">
                        Troisième section
                      </button>
                    </h2>
                    <div id="collapseThree" class="accordion-collapse collapse" aria-labelledby="headingThree" data-bs-parent="#basicAccordion">
                      <div class="accordion-body">
                        Contenu de la troisième section
                      </div>
                    </div>
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
              <h3 class="h5">Accordéon avec icônes</h3>
              <p>Les accordéons peuvent inclure des icônes pour plus de clarté.</p>
              <div class="component-preview">
                <div class="accordion" id="iconAccordion">
                  <div class="accordion-item">
                    <h2 class="accordion-header" id="iconHeadingOne">
                      <button class="accordion-button" type="button" data-bs-toggle="collapse" data-bs-target="#iconCollapseOne" aria-expanded="true" aria-controls="iconCollapseOne">
                        <i class="fas fa-info-circle me-2"></i>
                        Section avec icône
                      </button>
                    </h2>
                    <div id="iconCollapseOne" class="accordion-collapse collapse show" aria-labelledby="iconHeadingOne" data-bs-parent="#iconAccordion">
                      <div class="accordion-body">
                        Contenu de la section avec icône
                      </div>
                    </div>
                  </div>
                </div>
              </div>
            </div>
          </div>

          <div class="card mb-4">
            <div class="card-body">
              <h3 class="h5">Accordéon avec contenu riche</h3>
              <p>Les accordéons peuvent contenir différents types de contenu.</p>
              <div class="component-preview">
                <div class="accordion" id="richAccordion">
                  <div class="accordion-item">
                    <h2 class="accordion-header" id="richHeadingOne">
                      <button class="accordion-button" type="button" data-bs-toggle="collapse" data-bs-target="#richCollapseOne" aria-expanded="true" aria-controls="richCollapseOne">
                        Section avec contenu riche
                      </button>
                    </h2>
                    <div id="richCollapseOne" class="accordion-collapse collapse show" aria-labelledby="richHeadingOne" data-bs-parent="#richAccordion">
                      <div class="accordion-body">
                        <h5>Sous-titre</h5>
                        <p>Un paragraphe de texte...</p>
                        <ul class="list-group">
                          <li class="list-group-item">Premier élément</li>
                          <li class="list-group-item">Deuxième élément</li>
                          <li class="list-group-item">Troisième élément</li>
                        </ul>
                      </div>
                    </div>
                  </div>
                </div>
              </div>
            </div>
          </div>

          <div class="card mb-4">
            <div class="card-body">
              <h3 class="h5">Accordéon avec fond coloré</h3>
              <p>Les accordéons peuvent avoir un fond coloré pour plus d'impact visuel.</p>
              <div class="component-preview">
                <div class="accordion" id="coloredAccordion">
                  <div class="accordion-item bg-primary text-white">
                    <h2 class="accordion-header" id="coloredHeadingOne">
                      <button class="accordion-button bg-primary text-white" type="button" data-bs-toggle="collapse" data-bs-target="#coloredCollapseOne" aria-expanded="true" aria-controls="coloredCollapseOne">
                        Section colorée
                      </button>
                    </h2>
                    <div id="coloredCollapseOne" class="accordion-collapse collapse show" aria-labelledby="coloredHeadingOne" data-bs-parent="#coloredAccordion">
                      <div class="accordion-body bg-primary text-white">
                        Contenu de la section colorée
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
          <p>Dans Moodle, les accordéons sont utilisés pour :</p>
          <ul class="list-group mb-4">
            <li class="list-group-item">Organiser les sections d'un cours</li>
            <li class="list-group-item">Afficher les détails des activités</li>
            <li class="list-group-item">Présenter les critères d'évaluation</li>
            <li class="list-group-item">Montrer les instructions détaillées</li>
            <li class="list-group-item">Organiser les FAQ</li>
          </ul>

          <div class="card mb-4">
            <div class="card-body">
              <h3 class="h5">Exemple d'intégration dans un template Moodle</h3>
              <pre class="bg-light p-3 rounded"><code>{{#has_accordion}}
    &lt;div class="accordion" id="{{accordion_id}}"&gt;
        {{#items}}
        &lt;div class="accordion-item {{#color}}bg-{{color}} text-{{text_color}}{{/color}}"&gt;
            &lt;h2 class="accordion-header" id="{{heading_id}}"&gt;
                &lt;button class="accordion-button {{#color}}bg-{{color}} text-{{text_color}}{{/color}} {{#expanded}}show{{/expanded}}"
                        type="button"
                        data-bs-toggle="collapse"
                        data-bs-target="#{{collapse_id}}"
                        aria-expanded="{{#expanded}}true{{/expanded}}{{^expanded}}false{{/expanded}}"
                        aria-controls="{{collapse_id}}"&gt;
                    {{#icon}}
                    &lt;i class="fas fa-{{icon}} me-2"&gt;&lt;/i&gt;
                    {{/icon}}
                    {{title}}
                &lt;/button&gt;
            &lt;/h2&gt;

            &lt;div id="{{collapse_id}}"
                 class="accordion-collapse collapse {{#expanded}}show{{/expanded}}"
                 aria-labelledby="{{heading_id}}"
                 data-bs-parent="#{{../accordion_id}}"&gt;
                &lt;div class="accordion-body {{#color}}bg-{{color}} text-{{text_color}}{{/color}}"&gt;
                    {{{content}}}
                &lt;/div&gt;
            &lt;/div&gt;
        &lt;/div&gt;
        {{/items}}
    &lt;/div&gt;
{{/has_accordion}}</code></pre>
            </div>
          </div>
        </div>

        <div id="accessibilite" class="mt-5">
          <h2>Accessibilité</h2>
          <ul class="list-group mb-4">
            <li class="list-group-item">Utilisez des en-têtes appropriés pour chaque section</li>
            <li class="list-group-item">Fournissez des attributs ARIA appropriés</li>
            <li class="list-group-item">Assurez-vous que la navigation au clavier fonctionne</li>
            <li class="list-group-item">Maintenez un contraste suffisant pour le texte</li>
            <li class="list-group-item">Évitez les informations essentielles uniquement dans les sections fermées</li>
          </ul>
        </div>
      </div>
    </div>
  </div>
</div>