---
title: Formulaires
description: Documentation du composant Formulaires de Bootstrap 5 pour Moodle
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
          <p class="lead">Les formulaires sont des composants essentiels pour la saisie de données. Ils permettent aux utilisateurs d'interagir avec l'interface en saisissant des informations.</p>
        </div>

        <div id="exemple-base" class="mt-5">
          <h2>Exemple de base</h2>
          <p>Un formulaire simple avec des champs de saisie.</p>
          <div class="card mb-4">
            <div class="card-body">
              <div class="component-preview">
                <form>
                  <div class="mb-3">
                    <label for="email" class="form-label">Adresse courriel</label>
                    <input type="email" class="form-control" id="email" placeholder="nom@exemple.com">
                  </div>
                  <div class="mb-3">
                    <label for="password" class="form-label">Mot de passe</label>
                    <input type="password" class="form-control" id="password">
                  </div>
                  <button type="submit" class="btn btn-primary">Connexion</button>
                </form>
              </div>
            </div>
          </div>
        </div>

        <div id="styles" class="mt-5">
          <h2>Styles</h2>

          <div class="card mb-4">
            <div class="card-body">
              <h3 class="h5">Types de champs</h3>
              <p>Les formulaires peuvent contenir différents types de champs.</p>
              <div class="component-preview">
                <form>
                  <div class="mb-3">
                    <label for="text" class="form-label">Champ texte</label>
                    <input type="text" class="form-control" id="text">
                  </div>
                  <div class="mb-3">
                    <label for="textarea" class="form-label">Zone de texte</label>
                    <textarea class="form-control" id="textarea" rows="3"></textarea>
                  </div>
                  <div class="mb-3">
                    <label for="select" class="form-label">Liste déroulante</label>
                    <select class="form-select" id="select">
                      <option selected>Choisir une option</option>
                      <option value="1">Option 1</option>
                      <option value="2">Option 2</option>
                      <option value="3">Option 3</option>
                    </select>
                  </div>
                  <div class="mb-3">
                    <label for="file" class="form-label">Fichier</label>
                    <input type="file" class="form-control" id="file">
                  </div>
                </form>
              </div>
            </div>
          </div>

          <div class="card mb-4">
            <div class="card-body">
              <h3 class="h5">Cases à cocher et boutons radio</h3>
              <p>Les formulaires peuvent inclure des cases à cocher et des boutons radio.</p>
              <div class="component-preview">
                <form>
                  <div class="mb-3">
                    <div class="form-check">
                      <input class="form-check-input" type="checkbox" id="checkbox1">
                      <label class="form-check-label" for="checkbox1">
                        Case à cocher 1
                      </label>
                    </div>
                    <div class="form-check">
                      <input class="form-check-input" type="checkbox" id="checkbox2">
                      <label class="form-check-label" for="checkbox2">
                        Case à cocher 2
                      </label>
                    </div>
                  </div>
                  <div class="mb-3">
                    <div class="form-check">
                      <input class="form-check-input" type="radio" name="radio" id="radio1">
                      <label class="form-check-label" for="radio1">
                        Bouton radio 1
                      </label>
                    </div>
                    <div class="form-check">
                      <input class="form-check-input" type="radio" name="radio" id="radio2">
                      <label class="form-check-label" for="radio2">
                        Bouton radio 2
                      </label>
                    </div>
                  </div>
                </form>
              </div>
            </div>
          </div>

          <div class="card mb-4">
            <div class="card-body">
              <h3 class="h5">Validation</h3>
              <p>Les formulaires peuvent inclure des messages de validation.</p>
              <div class="component-preview">
                <form class="needs-validation" novalidate>
                  <div class="mb-3">
                    <label for="validation" class="form-label">Champ requis</label>
                    <input type="text" class="form-control" id="validation" required>
                    <div class="invalid-feedback">
                      Veuillez remplir ce champ.
                    </div>
                  </div>
                  <button type="submit" class="btn btn-primary">Valider</button>
                </form>
              </div>
            </div>
          </div>

          <div class="card mb-4">
            <div class="card-body">
              <h3 class="h5">Champs groupés</h3>
              <p>Les champs peuvent être groupés pour une meilleure organisation.</p>
              <div class="component-preview">
                <form>
                  <div class="input-group mb-3">
                    <span class="input-group-text">@</span>
                    <input type="text" class="form-control" placeholder="Nom d'utilisateur">
                  </div>
                  <div class="input-group mb-3">
                    <input type="text" class="form-control" placeholder="URL">
                    <span class="input-group-text">.com</span>
                  </div>
                  <div class="input-group">
                    <span class="input-group-text">$</span>
                    <input type="text" class="form-control" placeholder="Montant">
                    <span class="input-group-text">.00</span>
                  </div>
                </form>
              </div>
            </div>
          </div>
        </div>

        <div id="utilisation-moodle" class="mt-5">
          <h2>Utilisation dans Moodle</h2>
          <p>Dans Moodle, les formulaires sont utilisés pour :</p>
          <ul class="list-group mb-4">
            <li class="list-group-item">Connexion des utilisateurs</li>
            <li class="list-group-item">Configuration des cours</li>
            <li class="list-group-item">Soumission des devoirs</li>
            <li class="list-group-item">Création de quiz</li>
            <li class="list-group-item">Paramètres utilisateur</li>
          </ul>

          <div class="card mb-4">
            <div class="card-body">
              <h3 class="h5">Exemple d'intégration dans un template Moodle</h3>
              <pre class="bg-light p-3 rounded"><code>{{#form}}
    &lt;form {{#id}}id="{{id}}"{{/id}} {{#action}}action="{{action}}"{{/action}} {{#method}}method="{{method}}"{{/method}}&gt;
        {{#fields}}
        &lt;div class="mb-3"&gt;
            &lt;label for="{{id}}" class="form-label"&gt;{{label}}&lt;/label&gt;
            {{#type}}
            &lt;input type="{{type}}"
                   class="form-control {{#validation}}is-{{validation}}{{/validation}}"
                   id="{{id}}"
                   {{#required}}required{{/required}}
                   {{#placeholder}}placeholder="{{placeholder}}"{{/placeholder}}&gt;
            {{/type}}
            {{#textarea}}
            &lt;textarea class="form-control"
                      id="{{id}}"
                      rows="{{rows}}"
                      {{#required}}required{{/required}}
                      {{#placeholder}}placeholder="{{placeholder}}"{{/placeholder}}&gt;&lt;/textarea&gt;
            {{/textarea}}
            {{#select}}
            &lt;select class="form-select"
                    id="{{id}}"
                    {{#required}}required{{/required}}&gt;
                {{#options}}
                &lt;option value="{{value}}" {{#selected}}selected{{/selected}}&gt;{{text}}&lt;/option&gt;
                {{/options}}
            &lt;/select&gt;
            {{/select}}
            {{#validation_message}}
            &lt;div class="invalid-feedback"&gt;
                {{validation_message}}
            &lt;/div&gt;
            {{/validation_message}}
        &lt;/div&gt;
        {{/fields}}
        {{#submit}}
        &lt;button type="submit" class="btn btn-{{style}}"&gt;{{text}}&lt;/button&gt;
        {{/submit}}
    &lt;/form&gt;
{{/form}}</code></pre>
            </div>
          </div>
        </div>

        <div id="accessibilite" class="mt-5">
          <h2>Accessibilité</h2>
          <ul class="list-group mb-4">
            <li class="list-group-item">Associez chaque champ à son label</li>
            <li class="list-group-item">Fournissez des messages d'erreur clairs</li>
            <li class="list-group-item">Maintenez un contraste suffisant</li>
            <li class="list-group-item">Assurez-vous que les formulaires sont accessibles au clavier</li>
          </ul>
        </div>
      </div>
    </div>
  </div>
</div>