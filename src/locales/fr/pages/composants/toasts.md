---
title: Toasts
description: Documentation du composant Toasts de Bootstrap 5 pour Moodle
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
          <p class="lead">Les toasts sont des notifications non intrusives qui apparaissent temporairement pour informer l'utilisateur d'un événement ou d'une action. Ils sont idéaux pour les messages de confirmation, les mises à jour ou les avertissements légers.</p>
        </div>

        <div id="exemple-base" class="mt-5">
          <h2>Exemple de base</h2>
          <p>Un toast simple avec un message et un bouton de fermeture.</p>
          <div class="card mb-4">
            <div class="card-body">
              <div class="component-preview">
                <div class="toast" role="alert" aria-live="assertive" aria-atomic="true">
                  <div class="toast-header">
                    <strong class="me-auto">Notification</strong>
                    <button type="button" class="btn-close" data-bs-dismiss="toast" aria-label="Fermer"></button>
                  </div>
                  <div class="toast-body">
                    Votre action a été effectuée avec succès.
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
              <h3 class="h5">Toasts avec couleurs</h3>
              <p>Les toasts peuvent utiliser différentes couleurs pour indiquer différents types de messages.</p>
              <div class="component-preview">
                <div class="toast bg-success text-white mb-3" role="alert" aria-live="assertive" aria-atomic="true">
                  <div class="toast-header bg-success text-white">
                    <strong class="me-auto">Succès</strong>
                    <button type="button" class="btn-close btn-close-white" data-bs-dismiss="toast" aria-label="Fermer"></button>
                  </div>
                  <div class="toast-body">
                    L'opération a été effectuée avec succès.
                  </div>
                </div>

                <div class="toast bg-danger text-white mb-3" role="alert" aria-live="assertive" aria-atomic="true">
                  <div class="toast-header bg-danger text-white">
                    <strong class="me-auto">Erreur</strong>
                    <button type="button" class="btn-close btn-close-white" data-bs-dismiss="toast" aria-label="Fermer"></button>
                  </div>
                  <div class="toast-body">
                    Une erreur est survenue lors de l'opération.
                  </div>
                </div>

                <div class="toast bg-warning text-dark" role="alert" aria-live="assertive" aria-atomic="true">
                  <div class="toast-header bg-warning text-dark">
                    <strong class="me-auto">Attention</strong>
                    <button type="button" class="btn-close" data-bs-dismiss="toast" aria-label="Fermer"></button>
                  </div>
                  <div class="toast-body">
                    Veuillez vérifier vos informations avant de continuer.
                  </div>
                </div>
              </div>
            </div>
          </div>

          <div class="card mb-4">
            <div class="card-body">
              <h3 class="h5">Toasts avec icônes</h3>
              <p>Les toasts peuvent inclure des icônes pour une meilleure compréhension visuelle.</p>
              <div class="component-preview">
                <div class="toast" role="alert" aria-live="assertive" aria-atomic="true">
                  <div class="toast-header">
                    <i class="bi bi-info-circle-fill text-info me-2"></i>
                    <strong class="me-auto">Information</strong>
                    <button type="button" class="btn-close" data-bs-dismiss="toast" aria-label="Fermer"></button>
                  </div>
                  <div class="toast-body">
                    Une nouvelle mise à jour est disponible.
                  </div>
                </div>
              </div>
            </div>
          </div>

          <div class="card mb-4">
            <div class="card-body">
              <h3 class="h5">Toasts avec actions</h3>
              <p>Les toasts peuvent inclure des boutons d'action pour des interactions supplémentaires.</p>
              <div class="component-preview">
                <div class="toast" role="alert" aria-live="assertive" aria-atomic="true">
                  <div class="toast-header">
                    <strong class="me-auto">Mise à jour</strong>
                    <button type="button" class="btn-close" data-bs-dismiss="toast" aria-label="Fermer"></button>
                  </div>
                  <div class="toast-body">
                    Voulez-vous installer la mise à jour maintenant ?
                  </div>
                  <div class="toast-footer">
                    <button type="button" class="btn btn-primary btn-sm">Installer</button>
                    <button type="button" class="btn btn-secondary btn-sm" data-bs-dismiss="toast">Plus tard</button>
                  </div>
                </div>
              </div>
            </div>
          </div>
        </div>

        <div id="utilisation-moodle" class="mt-5">
          <h2>Utilisation dans Moodle</h2>
          <p>Dans Moodle, les toasts sont utilisés pour :</p>
          <ul class="list-group mb-4">
            <li class="list-group-item">Confirmer la soumission d'un formulaire</li>
            <li class="list-group-item">Notifier la sauvegarde automatique</li>
            <li class="list-group-item">Afficher des messages d'erreur non critiques</li>
            <li class="list-group-item">Indiquer la fin d'une synchronisation</li>
            <li class="list-group-item">Notifier les mises à jour de contenu</li>
          </ul>

          <div class="card mb-4">
            <div class="card-body">
              <h3 class="h5">Exemple d'intégration dans un template Moodle</h3>
              <pre class="bg-light p-3 rounded"><code>{{#show_toast}}
    &lt;div class="toast {{#color}}bg-{{color}} text-{{text_color}}{{/color}}"
         role="alert"
         aria-live="assertive"
         aria-atomic="true"&gt;
        &lt;div class="toast-header {{#color}}bg-{{color}} text-{{text_color}}{{/color}}"&gt;
            {{#icon}}
            &lt;i class="bi bi-{{icon}} me-2"&gt;&lt;/i&gt;
            {{/icon}}
            &lt;strong class="me-auto"&gt;{{title}}&lt;/strong&gt;
            &lt;button type="button"
                    class="btn-close {{#color}}btn-close-white{{/color}}"
                    data-bs-dismiss="toast"
                    aria-label="Fermer"&gt;
            &lt;/button&gt;
        &lt;/div&gt;
        &lt;div class="toast-body"&gt;
            {{message}}
        &lt;/div&gt;
        {{#has_actions}}
        &lt;div class="toast-footer"&gt;
            {{#actions}}
            &lt;button type="button"
                    class="btn btn-{{style}} btn-sm"
                    {{#dismiss}}data-bs-dismiss="toast"{{/dismiss}}&gt;
                {{text}}
            &lt;/button&gt;
            {{/actions}}
        &lt;/div&gt;
        {{/has_actions}}
    &lt;/div&gt;
{{/show_toast}}</code></pre>
            </div>
          </div>
        </div>

        <div id="accessibilite" class="mt-5">
          <h2>Accessibilité</h2>
          <ul class="list-group mb-4">
            <li class="list-group-item">Utilisez l'attribut `role="alert"`</li>
            <li class="list-group-item">Ajoutez `aria-live="assertive"` pour les messages importants</li>
            <li class="list-group-item">Utilisez `aria-atomic="true"` pour une lecture complète</li>
            <li class="list-group-item">Assurez-vous que le contraste est suffisant</li>
            <li class="list-group-item">Fournissez des alternatives pour les utilisateurs qui préfèrent réduire les animations</li>
          </ul>
        </div>
      </div>
    </div>
  </div>
</div>