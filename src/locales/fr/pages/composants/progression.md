---
title: Barres de progression
description: Documentation sur l'utilisation des barres de progression Bootstrap dans Moodle, incluant les différentes variantes et options de personnalisation.
template: pages/composant.html
---

Les barres de progression sont des indicateurs visuels qui permettent aux utilisateurs de suivre l'évolution d'un processus, d'une tâche ou d'une activité. Dans Moodle, elles sont particulièrement utiles pour montrer la progression des étudiants dans un cours, l'achèvement d'activités ou le temps restant pour un quiz.

## Présentation

Une barre de progression standard de Bootstrap consiste en un conteneur `.progress` et une barre interne `.progress-bar`.

<div class="component-preview">
    <div class="progress">
        <div class="progress-bar" role="progressbar" style="width: 50%" aria-valuenow="50" aria-valuemin="0" aria-valuemax="100"></div>
    </div>
</div>

```html
<div class="progress">
  <div class="progress-bar" role="progressbar" style="width: 50%" aria-valuenow="50" aria-valuemin="0" aria-valuemax="100"></div>
</div>
```

## Variantes

### Hauteurs différentes

Vous pouvez ajuster la hauteur de vos barres de progression en utilisant la propriété CSS `height`.

<div class="preview-tabs">
    <div class="preview-tabs-headers">
        <button class="preview-tab-header active">Aperçu</button>
        <button class="preview-tab-header">Code</button>
    </div>
    <div class="preview-tab-content">
        <div class="component-preview">
            <div class="progress" style="height: 2px;">
                <div class="progress-bar" role="progressbar" style="width: 25%;" aria-valuenow="25" aria-valuemin="0" aria-valuemax="100"></div>
            </div>
            <div class="progress my-3" style="height: 5px;">
                <div class="progress-bar" role="progressbar" style="width: 50%;" aria-valuenow="50" aria-valuemin="0" aria-valuemax="100"></div>
            </div>
            <div class="progress my-3">
                <div class="progress-bar" role="progressbar" style="width: 75%;" aria-valuenow="75" aria-valuemin="0" aria-valuemax="100"></div>
            </div>
            <div class="progress" style="height: 25px;">
                <div class="progress-bar" role="progressbar" style="width: 100%;" aria-valuenow="100" aria-valuemin="0" aria-valuemax="100"></div>
            </div>
        </div>
    </div>
    <div class="preview-tab-content">
        ```html
        <div class="progress" style="height: 2px;">
            <div class="progress-bar" role="progressbar" style="width: 25%;" aria-valuenow="25" aria-valuemin="0" aria-valuemax="100"></div>
        </div>
        <div class="progress my-3" style="height: 5px;">
            <div class="progress-bar" role="progressbar" style="width: 50%;" aria-valuenow="50" aria-valuemin="0" aria-valuemax="100"></div>
        </div>
        <div class="progress my-3">
            <div class="progress-bar" role="progressbar" style="width: 75%;" aria-valuenow="75" aria-valuemin="0" aria-valuemax="100"></div>
        </div>
        <div class="progress" style="height: 25px;">
            <div class="progress-bar" role="progressbar" style="width: 100%;" aria-valuenow="100" aria-valuemin="0" aria-valuemax="100"></div>
        </div>
        ```
    </div>
</div>

### Couleurs de contexte

Bootstrap fournit différentes classes de couleur pour représenter différents types d'information.

<div class="preview-tabs">
    <div class="preview-tabs-headers">
        <button class="preview-tab-header active">Aperçu</button>
        <button class="preview-tab-header">Code</button>
    </div>
    <div class="preview-tab-content">
        <div class="component-preview">
            <div class="progress my-3">
                <div class="progress-bar bg-success" role="progressbar" style="width: 25%" aria-valuenow="25" aria-valuemin="0" aria-valuemax="100"></div>
            </div>
            <div class="progress my-3">
                <div class="progress-bar bg-info" role="progressbar" style="width: 50%" aria-valuenow="50" aria-valuemin="0" aria-valuemax="100"></div>
            </div>
            <div class="progress my-3">
                <div class="progress-bar bg-warning" role="progressbar" style="width: 75%" aria-valuenow="75" aria-valuemin="0" aria-valuemax="100"></div>
            </div>
            <div class="progress my-3">
                <div class="progress-bar bg-danger" role="progressbar" style="width: 100%" aria-valuenow="100" aria-valuemin="0" aria-valuemax="100"></div>
            </div>
        </div>
    </div>
    <div class="preview-tab-content">
        ```html
        <div class="progress my-3">
            <div class="progress-bar bg-success" role="progressbar" style="width: 25%" aria-valuenow="25" aria-valuemin="0" aria-valuemax="100"></div>
        </div>
        <div class="progress my-3">
            <div class="progress-bar bg-info" role="progressbar" style="width: 50%" aria-valuenow="50" aria-valuemin="0" aria-valuemax="100"></div>
        </div>
        <div class="progress my-3">
            <div class="progress-bar bg-warning" role="progressbar" style="width: 75%" aria-valuenow="75" aria-valuemin="0" aria-valuemax="100"></div>
        </div>
        <div class="progress my-3">
            <div class="progress-bar bg-danger" role="progressbar" style="width: 100%" aria-valuenow="100" aria-valuemin="0" aria-valuemax="100"></div>
        </div>
        ```
    </div>
</div>

### Barres avec étiquettes

Ajoutez du texte à l'intérieur de la barre de progression pour offrir plus de contexte.

<div class="component-preview">
    <div class="progress">
        <div class="progress-bar" role="progressbar" style="width: 25%;" aria-valuenow="25" aria-valuemin="0" aria-valuemax="100">25%</div>
    </div>
</div>

```html
<div class="progress">
  <div class="progress-bar" role="progressbar" style="width: 25%;" aria-valuenow="25" aria-valuemin="0" aria-valuemax="100">25%</div>
</div>
```

### Barres rayées

Ajoutez `.progress-bar-striped` pour appliquer un motif de rayures à la barre de progression.

<div class="component-preview">
    <div class="progress">
        <div class="progress-bar progress-bar-striped" role="progressbar" style="width: 40%" aria-valuenow="40" aria-valuemin="0" aria-valuemax="100"></div>
    </div>
</div>

```html
<div class="progress">
  <div class="progress-bar progress-bar-striped" role="progressbar" style="width: 40%" aria-valuenow="40" aria-valuemin="0" aria-valuemax="100"></div>
</div>
```

### Barres animées

Ajoutez `.progress-bar-animated` pour animer les rayures de droite à gauche.

<div class="component-preview">
    <div class="progress">
        <div class="progress-bar progress-bar-striped progress-bar-animated" role="progressbar" style="width: 60%" aria-valuenow="60" aria-valuemin="0" aria-valuemax="100"></div>
    </div>
</div>

```html
<div class="progress">
  <div class="progress-bar progress-bar-striped progress-bar-animated" role="progressbar" style="width: 60%" aria-valuenow="60" aria-valuemin="0" aria-valuemax="100"></div>
</div>
```

### Barres empilées

Vous pouvez placer plusieurs barres de progression dans un même conteneur pour créer une barre empilée.

<div class="component-preview">
    <div class="progress">
        <div class="progress-bar" role="progressbar" style="width: 15%" aria-valuenow="15" aria-valuemin="0" aria-valuemax="100"></div>
        <div class="progress-bar bg-success" role="progressbar" style="width: 30%" aria-valuenow="30" aria-valuemin="0" aria-valuemax="100"></div>
        <div class="progress-bar bg-info" role="progressbar" style="width: 20%" aria-valuenow="20" aria-valuemin="0" aria-valuemax="100"></div>
    </div>
</div>

```html
<div class="progress">
  <div class="progress-bar" role="progressbar" style="width: 15%" aria-valuenow="15" aria-valuemin="0" aria-valuemax="100"></div>
  <div class="progress-bar bg-success" role="progressbar" style="width: 30%" aria-valuenow="30" aria-valuemin="0" aria-valuemax="100"></div>
  <div class="progress-bar bg-info" role="progressbar" style="width: 20%" aria-valuenow="20" aria-valuemin="0" aria-valuemax="100"></div>
</div>
```

## Utilisation dans Moodle

### Avec templates Mustache

Dans Moodle, les barres de progression sont souvent générées dynamiquement via des templates Mustache :

```html
{{#progressbar}}
<div class="progress {{#classes}}{{.}} {{/classes}}">
  <div class="progress-bar {{^success}}{{^warning}}{{^danger}}bg-primary{{/danger}}{{/warning}}{{/success}}
              {{#success}}bg-success{{/success}}
              {{#warning}}bg-warning{{/warning}}
              {{#danger}}bg-danger{{/danger}}
              {{#striped}}progress-bar-striped{{/striped}}
              {{#animated}}progress-bar-animated{{/animated}}"
       role="progressbar"
       style="width: {{percentage}}%"
       aria-valuenow="{{percentage}}"
       aria-valuemin="0"
       aria-valuemax="100">
    {{#showpercentage}}{{percentage}}%{{/showpercentage}}
  </div>
</div>
{{/progressbar}}
```

### Exemple de contexte de données

Voici un exemple du format de données attendu par le template :

```javascript
{
    "progressbar": {
        "percentage": 65,
        "success": true,
        "striped": true,
        "animated": false,
        "showpercentage": true,
        "classes": ["my-3", "custom-class"]
    }
}
```

### Utilisation pour le suivi de l'achèvement de cours

Les barres de progression sont particulièrement utiles pour le suivi de l'achèvement d'un cours dans Moodle.

<div class="component-preview">
    <div class="card">
        <div class="card-body">
            <h5 class="card-title">Programmation Web Avancée</h5>
            <p class="card-text">Progression du cours</p>
            <div class="progress">
                <div class="progress-bar bg-success" role="progressbar" style="width: 42%" aria-valuenow="42" aria-valuemin="0" aria-valuemax="100">42% complété</div>
            </div>
            <div class="mt-3 d-flex justify-content-between">
                <small class="text-muted">10/24 activités terminées</small>
                <a href="#" class="btn btn-sm btn-primary">Continuer</a>
            </div>
        </div>
    </div>
</div>

```html
<div class="card">
    <div class="card-body">
        <h5 class="card-title">Programmation Web Avancée</h5>
        <p class="card-text">Progression du cours</p>
        <div class="progress">
            <div class="progress-bar bg-success" role="progressbar" style="width: 42%" aria-valuenow="42" aria-valuemin="0" aria-valuemax="100">42% complété</div>
        </div>
        <div class="mt-3 d-flex justify-content-between">
            <small class="text-muted">10/24 activités terminées</small>
            <a href="#" class="btn btn-sm btn-primary">Continuer</a>
        </div>
    </div>
</div>
```

## Mise à jour dynamique avec JavaScript

Vous pouvez modifier dynamiquement les barres de progression avec JavaScript :

```javascript
// Sélectionnez la barre de progression
const progressBar = document.querySelector('.progress-bar');

// Mettez à jour la valeur
function updateProgress(value) {
  progressBar.style.width = value + '%';
  progressBar.setAttribute('aria-valuenow', value);
  progressBar.textContent = value + '%';
}

// Exemple d'utilisation pour une progression automatique
let progress = 0;
const interval = setInterval(() => {
  progress += 10;
  updateProgress(progress);

  if (progress >= 100) {
    clearInterval(interval);
  }
}, 1000);
```

## Points importants

- **Visibilité** : Assurez-vous que la barre de progression est suffisamment grande pour être visible, surtout sur les appareils mobiles.
- **Contexte** : Utilisez les couleurs appropriées pour communiquer le contexte (ex: vert pour succès, rouge pour danger).
- **Étiquettes** : Ajoutez du texte dans la barre ou à côté pour clarifier sa signification.
- **Réactivité** : Assurez-vous que les barres de progression s'adaptent correctement à différentes tailles d'écran.
- **Feedback immédiat** : Si possible, mettez à jour la barre de progression en temps réel pour fournir un feedback visuel instantané.

## Accessibilité

Pour des barres de progression accessibles :

- Utilisez `role="progressbar"` pour identifier la fonction de l'élément.
- Incluez `aria-valuenow`, `aria-valuemin` et `aria-valuemax` pour communiquer les valeurs aux technologies d'assistance.
- Si la barre de progression n'a pas d'étiquette visible, ajoutez `aria-label` ou `aria-labelledby` pour la décrire.
- Lorsque vous mettez à jour la barre avec JavaScript, n'oubliez pas de mettre à jour les attributs ARIA.

```html
<!-- Barre de progression accessible -->
<label id="course-progress-label">Progression du cours</label>
<div class="progress">
  <div class="progress-bar" role="progressbar"
       aria-labelledby="course-progress-label"
       style="width: 75%;"
       aria-valuenow="75"
       aria-valuemin="0"
       aria-valuemax="100">
    75%
  </div>
</div>
```

## Personnalisation avancée

### Styles personnalisés

Vous pouvez personnaliser davantage vos barres de progression avec du CSS supplémentaire :

```css
/* Barre de progression avec dégradé */
.progress-bar-gradient {
  background: linear-gradient(to right, #00b09b, #96c93d);
}

/* Barre de progression avec bordure arrondie */
.progress-rounded {
  border-radius: 1rem;
}
.progress-rounded .progress-bar {
  border-radius: 1rem;
}
```

### Barres de progression circulaires

Bien que Bootstrap ne fournisse pas de barres de progression circulaires par défaut, vous pouvez en créer à l'aide de CSS et JavaScript :

```html
<div class="circular-progress" data-percentage="65">
  <svg class="circular-progress-svg" viewBox="0 0 100 100">
    <circle class="circular-progress-track" cx="50" cy="50" r="40"></circle>
    <circle class="circular-progress-bar" cx="50" cy="50" r="40"></circle>
  </svg>
  <span class="circular-progress-value">65%</span>
</div>
```

```css
.circular-progress {
  position: relative;
  width: 120px;
  height: 120px;
}
.circular-progress-svg {
  transform: rotate(-90deg);
}
.circular-progress-track {
  fill: none;
  stroke: #f0f0f0;
  stroke-width: 8;
}
.circular-progress-bar {
  fill: none;
  stroke: var(--bs-primary);
  stroke-width: 8;
  stroke-dasharray: 251.2;
  stroke-dashoffset: calc(251.2 - (251.2 * var(--percentage)) / 100);
  transition: stroke-dashoffset 0.5s ease-in-out;
}
.circular-progress-value {
  position: absolute;
  top: 50%;
  left: 50%;
  transform: translate(-50%, -50%);
  font-weight: bold;
}
```

```javascript
document.querySelectorAll('.circular-progress').forEach(progress => {
  const percentage = progress.getAttribute('data-percentage');
  progress.style.setProperty('--percentage', percentage);
});
```

## Variables de personnalisation

### Variables CSS

```css
--bs-progress-height: 1rem;
--bs-progress-font-size: 0.75rem;
--bs-progress-bg: var(--bs-secondary-bg);
--bs-progress-border-radius: var(--bs-border-radius);
--bs-progress-box-shadow: var(--bs-box-shadow-inset);
--bs-progress-bar-color: #fff;
--bs-progress-bar-bg: var(--bs-primary);
--bs-progress-bar-transition: width 0.6s ease;
```

### Variables Sass

```scss
$progress-height: 1rem;
$progress-font-size: $font-size-base * .75;
$progress-bg: var(--#{$prefix}secondary-bg);
$progress-border-radius: $border-radius;
$progress-box-shadow: $box-shadow-inset;
$progress-bar-color: $white;
$progress-bar-bg: $primary;
$progress-bar-animation-timing: 1s linear infinite;
$progress-bar-transition: width .6s ease;
$progress-bar-striped-bg-size: $spacer * 1.4 $spacer * 1.4;
```

Les barres de progression sont un puissant outil visuel pour montrer l'avancement et motiver les utilisateurs dans un environnement d'apprentissage comme Moodle. Correctement intégrées et personnalisées, elles améliorent l'expérience utilisateur en offrant un feedback visuel clair sur leur progression.