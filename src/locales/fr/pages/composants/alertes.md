---
title: Alertes
description: Documentation du composant Alertes de Bootstrap 5 pour Moodle
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
          <p class="lead">Les alertes sont des messages contextuels qui attirent l'attention de l'utilisateur sur des informations importantes, des avertissements ou des confirmations. Elles sont idéales pour communiquer des messages de succès, d'erreur, d'avertissement ou d'information.</p>
        </div>

        <div id="exemple-base" class="mt-5">
          <h2>Exemple de base</h2>
          <p>Une alerte simple avec un message et un bouton de fermeture.</p>
          <div class="card mb-4">
            <div class="card-body">
              <div class="component-preview">
                <div class="alert alert-primary alert-dismissible fade show" role="alert">
                  Une alerte simple avec un bouton de fermeture.
                  <button type="button" class="btn-close" data-bs-dismiss="alert" aria-label="Fermer"></button>
                </div>
              </div>
            </div>
          </div>
        </div>

        <div id="styles" class="mt-5">
          <h2>Styles</h2>

          <div class="card mb-4">
            <div class="card-body">
              <h3 class="h5">Alertes de différents types</h3>
              <p>Les alertes peuvent avoir différents styles selon le type de message.</p>
              <div class="component-preview">
                <div class="alert alert-success" role="alert">
                  <strong>Succès!</strong> L'opération a été effectuée avec succès.
                </div>
                <div class="alert alert-danger" role="alert">
                  <strong>Erreur!</strong> Une erreur est survenue lors de l'opération.
                </div>
                <div class="alert alert-warning" role="alert">
                  <strong>Attention!</strong> Cette action nécessite votre attention.
                </div>
                <div class="alert alert-info" role="alert">
                  <strong>Information!</strong> Voici une information importante.
                </div>
              </div>
            </div>
          </div>

          <div class="card mb-4">
            <div class="card-body">
              <h3 class="h5">Alertes avec liens</h3>
              <p>Les alertes peuvent contenir des liens pour des actions supplémentaires.</p>
              <div class="component-preview">
                <div class="alert alert-primary" role="alert">
                  <strong>Nouvelle fonctionnalité!</strong> Découvrez notre nouvelle fonctionnalité en <a href="#" class="alert-link">cliquant ici</a>.
                </div>
              </div>
            </div>
          </div>

          <div class="card mb-4">
            <div class="card-body">
              <h3 class="h5">Alertes avec contenu riche</h3>
              <p>Les alertes peuvent contenir du contenu HTML pour une présentation plus riche.</p>
              <div class="component-preview">
                <div class="alert alert-info" role="alert">
                  <h4 class="alert-heading">Information importante</h4>
                  <p>Cette alerte contient des informations détaillées sur une nouvelle fonctionnalité.</p>
                  <hr>
                  <p class="mb-0">Vous pouvez ajouter autant de contenu que nécessaire dans une alerte.</p>
                </div>
              </div>
            </div>
          </div>
        </div>

        <div id="utilisation-moodle" class="mt-5">
          <h2>Utilisation dans Moodle</h2>
          <p>Dans Moodle, les alertes sont utilisées pour :</p>
          <ul class="list-group mb-4">
            <li class="list-group-item">Confirmer la soumission réussie d'un formulaire</li>
            <li class="list-group-item">Afficher des messages d'erreur lors de l'échec d'une opération</li>
            <li class="list-group-item">Attirer l'attention sur des informations importantes</li>
            <li class="list-group-item">Notifier les utilisateurs des changements de statut</li>
            <li class="list-group-item">Fournir des retours sur les actions effectuées</li>
          </ul>

          <div class="card mb-4">
            <div class="card-body">
              <h3 class="h5">Exemple d'intégration dans un template Moodle</h3>
              <pre class="bg-light p-3 rounded"><code>{{#has_alert}}
    &lt;div class="alert alert-{{type}} {{#dismissible}}alert-dismissible fade show{{/dismissible}}"
         role="alert"&gt;
        {{#heading}}
        &lt;h4 class="alert-heading"&gt;{{heading}}&lt;/h4&gt;
        {{/heading}}
        {{content}}
        {{#has_link}}
        &lt;a href="{{link_url}}" class="alert-link"&gt;{{link_text}}&lt;/a&gt;
        {{/has_link}}
        {{#dismissible}}
        &lt;button type="button"
                class="btn-close"
                data-bs-dismiss="alert"
                aria-label="Fermer"&gt;
        &lt;/button&gt;
        {{/dismissible}}
    &lt;/div&gt;
{{/has_alert}}</code></pre>
            </div>
          </div>
        </div>

        <div id="accessibilite" class="mt-5">
          <h2>Accessibilité</h2>
          <ul class="list-group mb-4">
            <li class="list-group-item">Utilisez des rôles ARIA appropriés (alert, status)</li>
            <li class="list-group-item">Maintenez un contraste suffisant pour le texte</li>
            <li class="list-group-item">Fournissez des alternatives pour les utilisateurs qui ne peuvent pas utiliser la souris</li>
            <li class="list-group-item">Assurez-vous que les liens sont clairement identifiables</li>
            <li class="list-group-item">Évitez d'utiliser uniquement la couleur pour transmettre l'information</li>
          </ul>
        </div>
      </div>
    </div>
  </div>
</div>
