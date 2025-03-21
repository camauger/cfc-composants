---
title: Tableaux
description: Documentation sur l'utilisation des tableaux Bootstrap dans Moodle, avec des exemples et des bonnes pratiques.
template: pages/composant.html
---

Les tableaux sont largement utilisés dans Moodle pour afficher des données structurées comme les listes de participants, les notes, les journaux d'activité, etc.

## Tableau de base

Le tableau de base inclut des bordures légères et un rembourrage pour les cellules.

=== "Aperçu"
    <div class="bd-example">
      <table class="table">
        <thead>
          <tr>
            <th scope="col">#</th>
            <th scope="col">Nom</th>
            <th scope="col">Prénom</th>
            <th scope="col">Note</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <th scope="row">1</th>
            <td>Dubois</td>
            <td>Marie</td>
            <td>85%</td>
          </tr>
          <tr>
            <th scope="row">2</th>
            <td>Martin</td>
            <td>Pierre</td>
            <td>92%</td>
          </tr>
          <tr>
            <th scope="row">3</th>
            <td>Bernard</td>
            <td>Julie</td>
            <td>78%</td>
          </tr>
        </tbody>
      </table>
    </div>

=== "HTML"
    ```html
    <table class="table">
      <thead>
        <tr>
          <th scope="col">#</th>
          <th scope="col">Nom</th>
          <th scope="col">Prénom</th>
          <th scope="col">Note</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <th scope="row">1</th>
          <td>Dubois</td>
          <td>Marie</td>
          <td>85%</td>
        </tr>
        <tr>
          <th scope="row">2</th>
          <td>Martin</td>
          <td>Pierre</td>
          <td>92%</td>
        </tr>
        <tr>
          <th scope="row">3</th>
          <td>Bernard</td>
          <td>Julie</td>
          <td>78%</td>
        </tr>
      </tbody>
    </table>
    ```

## Variantes de style

### Tableau avec rayures

Ajoutez `.table-striped` pour des rayures alternées.

=== "Aperçu"
    <div class="bd-example">
      <table class="table table-striped">
        <thead>
          <tr>
            <th scope="col">Activité</th>
            <th scope="col">Date</th>
            <th scope="col">Statut</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td>Devoir 1</td>
            <td>2024-01-15</td>
            <td>Complété</td>
          </tr>
          <tr>
            <td>Quiz 1</td>
            <td>2024-01-20</td>
            <td>En attente</td>
          </tr>
          <tr>
            <td>Forum</td>
            <td>2024-01-25</td>
            <td>En cours</td>
          </tr>
        </tbody>
      </table>
    </div>

=== "HTML"
    ```html
    <table class="table table-striped">
      <thead>
        <tr>
          <th scope="col">Activité</th>
          <th scope="col">Date</th>
          <th scope="col">Statut</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <td>Devoir 1</td>
          <td>2024-01-15</td>
          <td>Complété</td>
        </tr>
        <tr>
          <td>Quiz 1</td>
          <td>2024-01-20</td>
          <td>En attente</td>
        </tr>
        <tr>
          <td>Forum</td>
          <td>2024-01-25</td>
          <td>En cours</td>
        </tr>
      </tbody>
    </table>
    ```

### Tableau avec bordures

Utilisez `.table-bordered` pour des bordures sur tous les côtés.

=== "Aperçu"
    <div class="bd-example">
      <table class="table table-bordered">
        <thead>
          <tr>
            <th scope="col">Module</th>
            <th scope="col">Description</th>
            <th scope="col">Durée</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td>Introduction</td>
            <td>Présentation du cours</td>
            <td>1h</td>
          </tr>
          <tr>
            <td>Chapitre 1</td>
            <td>Concepts de base</td>
            <td>2h</td>
          </tr>
          <tr>
            <td>Chapitre 2</td>
            <td>Applications pratiques</td>
            <td>3h</td>
          </tr>
        </tbody>
      </table>
    </div>

### Tableau avec survol

Ajoutez `.table-hover` pour un effet de survol sur les lignes.

=== "Aperçu"
    <div class="bd-example">
      <table class="table table-hover">
        <thead>
          <tr>
            <th scope="col">Étudiant</th>
            <th scope="col">Participation</th>
            <th scope="col">Progression</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td>Alice Dupont</td>
            <td>Active</td>
            <td>75%</td>
          </tr>
          <tr>
            <td>Bob Martin</td>
            <td>Modérée</td>
            <td>45%</td>
          </tr>
          <tr>
            <td>Claire Bernard</td>
            <td>Très active</td>
            <td>90%</td>
          </tr>
        </tbody>
      </table>
    </div>

## Utilisation dans Moodle

Dans Moodle, les tableaux sont souvent utilisés avec des templates Mustache :

```html
{{#table}}
<table class="table {{#striped}}table-striped{{/striped}} {{#hover}}table-hover{{/hover}}">
  <thead>
    <tr>
      {{#headers}}
      <th scope="col">{{.}}</th>
      {{/headers}}
    </tr>
  </thead>
  <tbody>
    {{#rows}}
    <tr>
      {{#cells}}
      <td>{{{.}}}</td>
      {{/cells}}
    </tr>
    {{/rows}}
  </tbody>
  {{#hasfooter}}
  <tfoot>
    <tr>
      {{#footers}}
      <td>{{.}}</td>
      {{/footers}}
    </tr>
  </tfoot>
  {{/hasfooter}}
</table>
{{/table}}
```

## Tableaux responsifs

Enveloppez les tableaux dans `.table-responsive{-sm|-md|-lg|-xl|-xxl}` pour les rendre défilables horizontalement.

```html
<div class="table-responsive">
  <table class="table">
    ...
  </table>
</div>
```

## Accessibilité

Pour des tableaux accessibles :

- Utilisez des en-têtes de tableau appropriés (`<th>`)
- Ajoutez `scope="col"` pour les en-têtes de colonnes
- Ajoutez `scope="row"` pour les en-têtes de lignes
- Incluez des légendes descriptives avec `<caption>`
- Évitez les tableaux complexes avec des cellules fusionnées

## Personnalisation

### Variables CSS

```css
--bs-table-color: var(--bs-body-color);
--bs-table-bg: var(--bs-body-bg);
--bs-table-border-color: var(--bs-border-color);
--bs-table-accent-bg: transparent;
--bs-table-striped-color: var(--bs-body-color);
--bs-table-striped-bg: rgba(0, 0, 0, 0.05);
--bs-table-active-color: var(--bs-body-color);
--bs-table-active-bg: rgba(0, 0, 0, 0.1);
--bs-table-hover-color: var(--bs-body-color);
--bs-table-hover-bg: rgba(0, 0, 0, 0.075);
```

### Variables Sass

```scss
$table-cell-padding-y:        .5rem;
$table-cell-padding-x:        .5rem;
$table-cell-padding-y-sm:     .25rem;
$table-cell-padding-x-sm:     .25rem;
$table-cell-vertical-align:   top;
$table-color:                 var(--#{$prefix}body-color);
$table-bg:                    var(--#{$prefix}body-bg);
$table-accent-bg:             transparent;
$table-striped-color:         $table-color;
$table-striped-bg-factor:     .05;
$table-striped-bg:            rgba($black, $table-striped-bg-factor);
$table-active-color:          $table-color;
$table-active-bg-factor:      .1;
$table-active-bg:             rgba($black, $table-active-bg-factor);
$table-hover-color:           $table-color;
$table-hover-bg-factor:       .075;
$table-hover-bg:              rgba($black, $table-hover-bg-factor);
```