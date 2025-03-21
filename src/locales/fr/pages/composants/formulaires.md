---
title: Formulaires
description: Documentation sur l'utilisation des formulaires Bootstrap dans Moodle, avec des exemples et des bonnes pratiques.
template: pages/composant.html
---

Les formulaires sont des éléments essentiels dans Moodle, utilisés pour la saisie de données, les questionnaires, les paramètres de cours et bien plus encore. Bootstrap fournit des styles et des composants qui permettent de créer des formulaires élégants et fonctionnels.

## Formulaire de base

Voici un exemple de formulaire de base avec les styles Bootstrap :

=== "Aperçu"
    <div class="bd-example">
      <form>
        <div class="mb-3">
          <label for="exampleInputEmail1" class="form-label">Adresse courriel</label>
          <input type="email" class="form-control" id="exampleInputEmail1" aria-describedby="emailHelp">
          <div id="emailHelp" class="form-text">Nous ne partagerons jamais votre courriel.</div>
        </div>
        <div class="mb-3">
          <label for="exampleInputPassword1" class="form-label">Mot de passe</label>
          <input type="password" class="form-control" id="exampleInputPassword1">
        </div>
        <div class="mb-3 form-check">
          <input type="checkbox" class="form-check-input" id="exampleCheck1">
          <label class="form-check-label" for="exampleCheck1">Se souvenir de moi</label>
        </div>
        <button type="submit" class="btn btn-primary">Soumettre</button>
      </form>
    </div>

=== "HTML"
    ```html
    <form>
      <div class="mb-3">
        <label for="exampleInputEmail1" class="form-label">Adresse courriel</label>
        <input type="email" class="form-control" id="exampleInputEmail1" aria-describedby="emailHelp">
        <div id="emailHelp" class="form-text">Nous ne partagerons jamais votre courriel.</div>
      </div>
      <div class="mb-3">
        <label for="exampleInputPassword1" class="form-label">Mot de passe</label>
        <input type="password" class="form-control" id="exampleInputPassword1">
      </div>
      <div class="mb-3 form-check">
        <input type="checkbox" class="form-check-input" id="exampleCheck1">
        <label class="form-check-label" for="exampleCheck1">Se souvenir de moi</label>
      </div>
      <button type="submit" class="btn btn-primary">Soumettre</button>
    </form>
    ```

## Contrôles de formulaire

### Champs de texte

Les champs de texte sont les éléments de formulaire les plus courants. Utilisez la classe `.form-control` pour styliser les champs de texte.

=== "Aperçu"
    <div class="bd-example">
      <div class="mb-3">
        <label for="exampleFormControlInput1" class="form-label">Titre de l'activité</label>
        <input type="text" class="form-control" id="exampleFormControlInput1" placeholder="Entrez le titre">
      </div>
      <div class="mb-3">
        <label for="exampleFormControlTextarea1" class="form-label">Description</label>
        <textarea class="form-control" id="exampleFormControlTextarea1" rows="3"></textarea>
      </div>
    </div>

=== "HTML"
    ```html
    <div class="mb-3">
      <label for="exampleFormControlInput1" class="form-label">Titre de l'activité</label>
      <input type="text" class="form-control" id="exampleFormControlInput1" placeholder="Entrez le titre">
    </div>
    <div class="mb-3">
      <label for="exampleFormControlTextarea1" class="form-label">Description</label>
      <textarea class="form-control" id="exampleFormControlTextarea1" rows="3"></textarea>
    </div>
    ```

### Cases à cocher et boutons radio

Les cases à cocher et les boutons radio sont utilisés pour les choix multiples ou uniques.

=== "Aperçu"
    <div class="bd-example">
      <div class="mb-3">
        <div class="form-check">
          <input class="form-check-input" type="checkbox" value="" id="flexCheckDefault">
          <label class="form-check-label" for="flexCheckDefault">
            Option par défaut
          </label>
        </div>
        <div class="form-check">
          <input class="form-check-input" type="checkbox" value="" id="flexCheckChecked" checked>
          <label class="form-check-label" for="flexCheckChecked">
            Option cochée
          </label>
        </div>
      </div>
      <div class="mb-3">
        <div class="form-check">
          <input class="form-check-input" type="radio" name="flexRadioDefault" id="flexRadioDefault1">
          <label class="form-check-label" for="flexRadioDefault1">
            Bouton radio par défaut
          </label>
        </div>
        <div class="form-check">
          <input class="form-check-input" type="radio" name="flexRadioDefault" id="flexRadioDefault2" checked>
          <label class="form-check-label" for="flexRadioDefault2">
            Bouton radio sélectionné
          </label>
        </div>
      </div>
    </div>

=== "HTML"
    ```html
    <div class="form-check">
      <input class="form-check-input" type="checkbox" value="" id="flexCheckDefault">
      <label class="form-check-label" for="flexCheckDefault">
        Option par défaut
      </label>
    </div>
    <div class="form-check">
      <input class="form-check-input" type="checkbox" value="" id="flexCheckChecked" checked>
      <label class="form-check-label" for="flexCheckChecked">
        Option cochée
      </label>
    </div>

    <div class="form-check">
      <input class="form-check-input" type="radio" name="flexRadioDefault" id="flexRadioDefault1">
      <label class="form-check-label" for="flexRadioDefault1">
        Bouton radio par défaut
      </label>
    </div>
    <div class="form-check">
      <input class="form-check-input" type="radio" name="flexRadioDefault" id="flexRadioDefault2" checked>
      <label class="form-check-label" for="flexRadioDefault2">
        Bouton radio sélectionné
      </label>
    </div>
    ```

## Validation des formulaires

Bootstrap inclut une validation de formulaire native et personnalisée.

=== "Aperçu"
    <div class="bd-example">
      <form class="needs-validation" novalidate>
        <div class="mb-3">
          <label for="validationCustom01" class="form-label">Nom du cours</label>
          <input type="text" class="form-control" id="validationCustom01" value="" required>
          <div class="valid-feedback">
            Parfait !
          </div>
          <div class="invalid-feedback">
            Veuillez entrer un nom de cours.
          </div>
        </div>
        <div class="mb-3">
          <label for="validationCustom02" class="form-label">Code du cours</label>
          <input type="text" class="form-control" id="validationCustom02" value="" required>
          <div class="valid-feedback">
            Parfait !
          </div>
          <div class="invalid-feedback">
            Veuillez entrer un code de cours.
          </div>
        </div>
        <button class="btn btn-primary" type="submit">Valider</button>
      </form>
    </div>

=== "HTML"
    ```html
    <form class="needs-validation" novalidate>
      <div class="mb-3">
        <label for="validationCustom01" class="form-label">Nom du cours</label>
        <input type="text" class="form-control" id="validationCustom01" value="" required>
        <div class="valid-feedback">
          Parfait !
        </div>
        <div class="invalid-feedback">
          Veuillez entrer un nom de cours.
        </div>
      </div>
      <div class="mb-3">
        <label for="validationCustom02" class="form-label">Code du cours</label>
        <input type="text" class="form-control" id="validationCustom02" value="" required>
        <div class="valid-feedback">
          Parfait !
        </div>
        <div class="invalid-feedback">
          Veuillez entrer un code de cours.
        </div>
      </div>
      <button class="btn btn-primary" type="submit">Valider</button>
    </form>
    ```

=== "JavaScript"
    ```javascript
    // Example starter JavaScript for disabling form submissions if there are invalid fields
    (function () {
      'use strict'

      // Fetch all the forms we want to apply custom Bootstrap validation styles to
      var forms = document.querySelectorAll('.needs-validation')

      // Loop over them and prevent submission
      Array.prototype.slice.call(forms)
        .forEach(function (form) {
          form.addEventListener('submit', function (event) {
            if (!form.checkValidity()) {
              event.preventDefault()
              event.stopPropagation()
            }

            form.classList.add('was-validated')
          }, false)
        })
    })()
    ```

## Utilisation dans Moodle

Dans Moodle, les formulaires sont généralement créés à l'aide de la classe `mform` (Moodle Forms). Voici comment intégrer les styles Bootstrap avec les formulaires Moodle :

```php
class mod_mymodule_mod_form extends moodleform {
    public function definition() {
        $mform = $this->_form;

        // Ajouter un champ texte
        $mform->addElement('text', 'name', get_string('name'), array('class' => 'form-control'));
        $mform->setType('name', PARAM_TEXT);

        // Ajouter une zone de texte
        $mform->addElement('textarea', 'description', get_string('description'),
            array('class' => 'form-control', 'rows' => 3));

        // Ajouter des cases à cocher
        $mform->addElement('advcheckbox', 'option1', get_string('option1'), '',
            array('class' => 'form-check-input'));
    }
}
```

## Personnalisation

### Variables CSS

```css
--bs-form-control-bg: #fff;
--bs-form-control-disabled-bg: #e9ecef;
--bs-form-control-border-color: #ced4da;
--bs-form-control-border-width: 1px;
--bs-form-control-border-radius: 0.375rem;
--bs-form-control-focus-border-color: #86b7fe;
--bs-form-control-focus-box-shadow: 0 0 0 0.25rem rgba(13, 110, 253, 0.25);
```

### Variables Sass

```scss
$input-bg:                              $white;
$input-disabled-bg:                     $gray-200;
$input-border-color:                    $gray-400;
$input-border-width:                    $border-width;
$input-border-radius:                   $border-radius;
$input-focus-border-color:              tint-color($component-active-bg, 50%);
$input-focus-box-shadow:                $component-active-shadow;
$input-placeholder-color:               $gray-600;
$input-plaintext-color:                 $body-color;
```