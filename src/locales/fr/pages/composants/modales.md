---
title: Modales
description: Documentation du composant Modales de Bootstrap 5 pour Moodle
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
          <p class="lead">Les modales sont des fenêtres contextuelles qui apparaissent au centre de l'écran avec un fond semi-transparent. Elles sont idéales pour afficher des formulaires, des confirmations ou des contenus importants qui nécessitent l'attention de l'utilisateur.</p>
        </div>

        <div id="exemple-base" class="mt-5">
          <h2>Exemple de base</h2>
          <p>Une modale simple avec un titre, un contenu et des boutons d'action.</p>
          <div class="card mb-4">
            <div class="card-body">
              <div class="component-preview">
                <button type="button" class="btn btn-primary" data-bs-toggle="modal" data-bs-target="#exampleModal">
                  Ouvrir la modale
                </button>

                <div class="modal fade" id="exampleModal" tabindex="-1" aria-labelledby="exampleModalLabel" aria-hidden="true">
                  <div class="modal-dialog">
                    <div class="modal-content">
                      <div class="modal-header">
                        <h5 class="modal-title" id="exampleModalLabel">Titre de la modale</h5>
                        <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Fermer"></button>
                      </div>
                      <div class="modal-body">
                        Contenu de la modale
                      </div>
                      <div class="modal-footer">
                        <button type="button" class="btn btn-secondary" data-bs-dismiss="modal">Fermer</button>
                        <button type="button" class="btn btn-primary">Enregistrer</button>
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
              <h3 class="h5">Modales de différentes tailles</h3>
              <p>Les modales peuvent avoir différentes tailles selon le contenu.</p>
              <div class="component-preview">
                <div class="d-flex gap-3 justify-content-center">
                  <button type="button" class="btn btn-primary" data-bs-toggle="modal" data-bs-target="#smallModal">
                    Petite
                  </button>
                  <button type="button" class="btn btn-primary" data-bs-toggle="modal" data-bs-target="#defaultModal">
                    Par défaut
                  </button>
                  <button type="button" class="btn btn-primary" data-bs-toggle="modal" data-bs-target="#largeModal">
                    Grande
                  </button>
                  <button type="button" class="btn btn-primary" data-bs-toggle="modal" data-bs-target="#extraLargeModal">
                    Extra grande
                  </button>
                </div>

                <div class="modal fade" id="smallModal" tabindex="-1" aria-labelledby="smallModalLabel" aria-hidden="true">
                  <div class="modal-dialog modal-sm">
                    <div class="modal-content">
                      <div class="modal-header">
                        <h5 class="modal-title" id="smallModalLabel">Petite modale</h5>
                        <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Fermer"></button>
                      </div>
                      <div class="modal-body">
                        Contenu de la petite modale
                      </div>
                    </div>
                  </div>
                </div>

                <div class="modal fade" id="defaultModal" tabindex="-1" aria-labelledby="defaultModalLabel" aria-hidden="true">
                  <div class="modal-dialog">
                    <div class="modal-content">
                      <div class="modal-header">
                        <h5 class="modal-title" id="defaultModalLabel">Modale par défaut</h5>
                        <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Fermer"></button>
                      </div>
                      <div class="modal-body">
                        Contenu de la modale par défaut
                      </div>
                    </div>
                  </div>
                </div>

                <div class="modal fade" id="largeModal" tabindex="-1" aria-labelledby="largeModalLabel" aria-hidden="true">
                  <div class="modal-dialog modal-lg">
                    <div class="modal-content">
                      <div class="modal-header">
                        <h5 class="modal-title" id="largeModalLabel">Grande modale</h5>
                        <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Fermer"></button>
                      </div>
                      <div class="modal-body">
                        Contenu de la grande modale
                      </div>
                    </div>
                  </div>
                </div>

                <div class="modal fade" id="extraLargeModal" tabindex="-1" aria-labelledby="extraLargeModalLabel" aria-hidden="true">
                  <div class="modal-dialog modal-xl">
                    <div class="modal-content">
                      <div class="modal-header">
                        <h5 class="modal-title" id="extraLargeModalLabel">Extra grande modale</h5>
                        <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Fermer"></button>
                      </div>
                      <div class="modal-body">
                        Contenu de l'extra grande modale
                      </div>
                    </div>
                  </div>
                </div>
              </div>
            </div>
          </div>

          <div class="card mb-4">
            <div class="card-body">
              <h3 class="h5">Modales avec scrolling</h3>
              <p>Les modales peuvent avoir un défilement indépendant.</p>
              <div class="component-preview">
                <button type="button" class="btn btn-primary" data-bs-toggle="modal" data-bs-target="#scrollableModal">
                  Ouvrir la modale avec défilement
                </button>

                <div class="modal fade" id="scrollableModal" tabindex="-1" aria-labelledby="scrollableModalLabel" aria-hidden="true">
                  <div class="modal-dialog modal-dialog-scrollable">
                    <div class="modal-content">
                      <div class="modal-header">
                        <h5 class="modal-title" id="scrollableModalLabel">Modale avec défilement</h5>
                        <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Fermer"></button>
                      </div>
                      <div class="modal-body">
                        <p>Contenu avec défilement...</p>
                        <p>Ligne après ligne...</p>
                        <p>Pour tester le défilement...</p>
                        <p>Ajoutez beaucoup de contenu...</p>
                        <p>Jusqu'à ce que la barre de défilement apparaisse...</p>
                      </div>
                    </div>
                  </div>
                </div>
              </div>
            </div>
          </div>

          <div class="card mb-4">
            <div class="card-body">
              <h3 class="h5">Modales avec formulaires</h3>
              <p>Les modales peuvent contenir des formulaires pour la saisie de données.</p>
              <div class="component-preview">
                <button type="button" class="btn btn-primary" data-bs-toggle="modal" data-bs-target="#formModal">
                  Ouvrir le formulaire
                </button>

                <div class="modal fade" id="formModal" tabindex="-1" aria-labelledby="formModalLabel" aria-hidden="true">
                  <div class="modal-dialog">
                    <div class="modal-content">
                      <div class="modal-header">
                        <h5 class="modal-title" id="formModalLabel">Formulaire dans une modale</h5>
                        <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Fermer"></button>
                      </div>
                      <div class="modal-body">
                        <form>
                          <div class="mb-3">
                            <label for="email" class="form-label">Email</label>
                            <input type="email" class="form-control" id="email">
                          </div>
                          <div class="mb-3">
                            <label for="password" class="form-label">Mot de passe</label>
                            <input type="password" class="form-control" id="password">
                          </div>
                        </form>
                      </div>
                      <div class="modal-footer">
                        <button type="button" class="btn btn-secondary" data-bs-dismiss="modal">Annuler</button>
                        <button type="button" class="btn btn-primary">Connexion</button>
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
          <p>Dans Moodle, les modales sont utilisées pour :</p>
          <ul class="list-group mb-4">
            <li class="list-group-item">Afficher des formulaires de connexion</li>
            <li class="list-group-item">Confirmer des actions importantes</li>
            <li class="list-group-item">Montrer des détails sur les activités</li>
            <li class="list-group-item">Afficher des messages d'erreur</li>
            <li class="list-group-item">Fournir des options de configuration</li>
          </ul>

          <div class="card mb-4">
            <div class="card-body">
              <h3 class="h5">Exemple d'intégration dans un template Moodle</h3>
              <pre class="bg-light p-3 rounded"><code>{{#has_modal}}
    &lt;button type="button"
            class="btn {{#style}}btn-{{style}}{{/style}}"
            data-bs-toggle="modal"
            data-bs-target="#{{id}}"&gt;
        {{button_text}}
    &lt;/button&gt;

    &lt;div class="modal fade"
         id="{{id}}"
         tabindex="-1"
         aria-labelledby="{{id}}Label"
         aria-hidden="true"&gt;
        &lt;div class="modal-dialog {{#size}}modal-{{size}}{{/size}} {{#scrollable}}modal-dialog-scrollable{{/scrollable}}"&gt;
            &lt;div class="modal-content"&gt;
                &lt;div class="modal-header"&gt;
                    &lt;h5 class="modal-title" id="{{id}}Label"&gt;{{title}}&lt;/h5&gt;
                    &lt;button type="button"
                            class="btn-close"
                            data-bs-dismiss="modal"
                            aria-label="Fermer"&gt;
                    &lt;/button&gt;
                &lt;/div&gt;
                &lt;div class="modal-body"&gt;
                    {{content}}
                &lt;/div&gt;
                {{#has_footer}}
                &lt;div class="modal-footer"&gt;
                    {{#footer_buttons}}
                    &lt;button type="button"
                            class="btn btn-{{style}}"
                            {{#dismiss}}data-bs-dismiss="modal"{{/dismiss}}&gt;
                        {{text}}
                    &lt;/button&gt;
                    {{/footer_buttons}}
                &lt;/div&gt;
                {{/has_footer}}
            &lt;/div&gt;
        &lt;/div&gt;
    &lt;/div&gt;
{{/has_modal}}</code></pre>
            </div>
          </div>
        </div>

        <div id="accessibilite" class="mt-5">
          <h2>Accessibilité</h2>
          <ul class="list-group mb-4">
            <li class="list-group-item">Utilisez des attributs ARIA appropriés</li>
            <li class="list-group-item">Gérez correctement le focus lors de l'ouverture/fermeture</li>
            <li class="list-group-item">Maintenez un contraste suffisant pour le texte</li>
            <li class="list-group-item">Fournissez des alternatives pour les utilisateurs qui ne peuvent pas utiliser la souris</li>
            <li class="list-group-item">Assurez-vous que le contenu est accessible au clavier</li>
          </ul>
        </div>
      </div>
    </div>
  </div>
</div>