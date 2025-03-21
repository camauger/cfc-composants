---
title: Fil d'Ariane (Breadcrumb)
description: Documentation sur l'utilisation du fil d'Ariane dans Bootstrap et son intégration dans Moodle, y compris sa configuration dans MkDocs Material.
template: pages/composant.html
---

Le fil d'Ariane est un élément essentiel de navigation qui permet aux utilisateurs de visualiser leur position actuelle dans la hiérarchie du site et de naviguer facilement vers les niveaux supérieurs. Il est particulièrement important dans un environnement d'apprentissage comme Moodle où la structure hiérarchique peut être complexe.

## Présentation

Dans un contexte d'interface utilisateur, le fil d'Ariane est une représentation visuelle du chemin de navigation de l'utilisateur, affichant généralement une série de liens menant de la page d'accueil à la page actuelle.

<div class="component-preview">
    <nav aria-label="breadcrumb">
        <ol class="breadcrumb">
            <li class="breadcrumb-item"><a href="#">Accueil</a></li>
            <li class="breadcrumb-item"><a href="#">Catégorie</a></li>
            <li class="breadcrumb-item"><a href="#">Cours</a></li>
            <li class="breadcrumb-item active" aria-current="page">Activité</li>
        </ol>
    </nav>
</div>

```html
<nav aria-label="breadcrumb">
  <ol class="breadcrumb">
    <li class="breadcrumb-item"><a href="#">Accueil</a></li>
    <li class="breadcrumb-item"><a href="#">Catégorie</a></li>
    <li class="breadcrumb-item"><a href="#">Cours</a></li>
    <li class="breadcrumb-item active" aria-current="page">Activité</li>
  </ol>
</nav>
```

## Variantes de style

Le fil d'Ariane peut être adapté à différents styles selon les besoins spécifiques de votre thème.

<div class="preview-tabs">
    <div class="preview-tabs-headers">
        <button class="preview-tab-header active">Standard</button>
        <button class="preview-tab-header">Avec diviseurs personnalisés</button>
        <button class="preview-tab-header">Avec fond</button>
    </div>
    <div class="preview-tab-content">
        <nav aria-label="breadcrumb">
            <ol class="breadcrumb">
                <li class="breadcrumb-item"><a href="#">Accueil</a></li>
                <li class="breadcrumb-item"><a href="#">Catégorie</a></li>
                <li class="breadcrumb-item active" aria-current="page">Cours</li>
            </ol>
        </nav>

        ```html
        <nav aria-label="breadcrumb">
          <ol class="breadcrumb">
            <li class="breadcrumb-item"><a href="#">Accueil</a></li>
            <li class="breadcrumb-item"><a href="#">Catégorie</a></li>
            <li class="breadcrumb-item active" aria-current="page">Cours</li>
          </ol>
        </nav>
        ```
    </div>
    <div class="preview-tab-content">
        <nav style="--bs-breadcrumb-divider: '>';" aria-label="breadcrumb">
            <ol class="breadcrumb">
                <li class="breadcrumb-item"><a href="#">Accueil</a></li>
                <li class="breadcrumb-item"><a href="#">Catégorie</a></li>
                <li class="breadcrumb-item active" aria-current="page">Cours</li>
            </ol>
        </nav>

        ```html
        <nav style="--bs-breadcrumb-divider: '>';" aria-label="breadcrumb">
          <ol class="breadcrumb">
            <li class="breadcrumb-item"><a href="#">Accueil</a></li>
            <li class="breadcrumb-item"><a href="#">Catégorie</a></li>
            <li class="breadcrumb-item active" aria-current="page">Cours</li>
          </ol>
        </nav>
        ```
    </div>
    <div class="preview-tab-content">
        <nav aria-label="breadcrumb">
            <ol class="breadcrumb p-3 bg-light rounded">
                <li class="breadcrumb-item"><a href="#">Accueil</a></li>
                <li class="breadcrumb-item"><a href="#">Catégorie</a></li>
                <li class="breadcrumb-item active" aria-current="page">Cours</li>
            </ol>
        </nav>

        ```html
        <nav aria-label="breadcrumb">
          <ol class="breadcrumb p-3 bg-light rounded">
            <li class="breadcrumb-item"><a href="#">Accueil</a></li>
            <li class="breadcrumb-item"><a href="#">Catégorie</a></li>
            <li class="breadcrumb-item active" aria-current="page">Cours</li>
          </ol>
        </nav>
        ```
    </div>
</div>

## Utilisation dans Moodle

### Intégration avec les templates Mustache

Dans Moodle, le fil d'Ariane est typiquement généré dynamiquement via des templates Mustache :

```html
<nav aria-label="{{#str}}breadcrumb, theme_boost{{/str}}">
    <ol class="breadcrumb">
        {{#breadcrumbs}}
        <li class="breadcrumb-item {{#isactive}}active{{/isactive}}">
            {{^isactive}}
            <a href="{{{url}}}" {{#title}}title="{{title}}"{{/title}}>
                {{{text}}}
            </a>
            {{/isactive}}
            {{#isactive}}
            <span {{#title}}title="{{title}}"{{/title}} aria-current="page">
                {{{text}}}
            </span>
            {{/isactive}}
        </li>
        {{/breadcrumbs}}
    </ol>
</nav>
```

Ce code génère automatiquement le fil d'Ariane approprié en fonction de l'emplacement actuel de l'utilisateur dans la hiérarchie de Moodle.

### Exemple de contexte de données

Voici un exemple du format de données attendu par le template :

```javascript
{
    "breadcrumbs": [
        {
            "text": "Accueil",
            "url": "/",
            "title": "Retour à la page d'accueil",
            "isactive": false
        },
        {
            "text": "Sciences",
            "url": "/category/1",
            "title": "Catégorie Sciences",
            "isactive": false
        },
        {
            "text": "Physique 101",
            "url": "/course/2",
            "title": "Cours d'introduction à la physique",
            "isactive": false
        },
        {
            "text": "Devoir 1",
            "title": "Premier devoir du cours",
            "isactive": true
        }
    ]
}
```

## Utilisation dans MkDocs Material

Si vous utilisez Material for MkDocs pour générer votre documentation, vous pouvez activer le fil d'Ariane de façon native en ajoutant une fonctionnalité dans votre fichier `mkdocs.yml` :

```yaml
theme:
  name: material
  features:
    - navigation.path
```

Cette configuration permet d'afficher automatiquement un fil d'Ariane en haut de chaque page, reflétant la structure de navigation définie dans votre fichier `mkdocs.yml`.

### Configuration de la navigation dans MkDocs

La structure de navigation dans MkDocs, qui alimente également le fil d'Ariane, est définie dans le fichier `mkdocs.yml` :

```yaml
site_name: Ma Documentation
nav:
  - Accueil: index.md
  - Sections:
    - Introduction: sections/introduction.md
    - Composants:
      - Présentation: sections/composants/index.md
      - Boutons: sections/composants/boutons.md
      - Formulaires: sections/composants/formulaires.md
```

Le fil d'Ariane reflétera cette hiérarchie, permettant aux utilisateurs de facilement naviguer entre les niveaux de votre documentation.

## Points importants

- **Séparateurs** : Par défaut, Bootstrap utilise le caractère `/` comme séparateur, mais vous pouvez le personnaliser avec la variable CSS `--bs-breadcrumb-divider`
- **Hiérarchie** : Respectez la hiérarchie logique du site, du plus général au plus spécifique
- **Élément actif** : Le dernier élément doit toujours avoir la classe `active` et l'attribut `aria-current="page"`
- **Taille maximale** : Limitez le nombre d'éléments à 4-5 pour éviter de surcharger l'interface
- **Cohérence** : Utilisez le fil d'Ariane de manière cohérente sur toutes les pages du site

## Accessibilité

Pour un fil d'Ariane accessible :

- Utilisez l'élément `<nav>` avec `aria-label="breadcrumb"` pour identifier clairement la fonction
- Ajoutez `aria-current="page"` sur l'élément actif
- Assurez un contraste suffisant entre le texte et l'arrière-plan
- Préservez la navigabilité au clavier entre les éléments du fil d'Ariane

```html
<!-- Fil d'Ariane accessible -->
<nav aria-label="breadcrumb">
  <ol class="breadcrumb">
    <li class="breadcrumb-item"><a href="#" tabindex="0">Accueil</a></li>
    <li class="breadcrumb-item"><a href="#" tabindex="0">Catégorie</a></li>
    <li class="breadcrumb-item active" aria-current="page">Page actuelle</li>
  </ol>
</nav>
```

## Personnalisation avancée

### Modification des séparateurs

Vous pouvez personnaliser le séparateur du fil d'Ariane de plusieurs façons :

```css
/* Utiliser un caractère différent */
.breadcrumb-item + .breadcrumb-item::before {
  content: ">";
}

/* Ou utiliser la variable CSS */
:root {
  --bs-breadcrumb-divider: '>';
}

/* Ou directement dans le HTML */
<nav style="--bs-breadcrumb-divider: '>';" aria-label="breadcrumb">
```

### Adaptations responsives

Pour les écrans mobiles, vous pouvez adapter le fil d'Ariane pour qu'il reste lisible :

```css
@media (max-width: 576px) {
  /* Réduire la taille de police sur mobile */
  .breadcrumb {
    font-size: 0.875rem;
  }

  /* Option: masquer certains éléments intermédiaires */
  .breadcrumb-item:not(:first-child):not(:last-child):not(:nth-last-child(2)) {
    display: none;
  }

  /* Ajouter des points de suspension pour les éléments masqués */
  .breadcrumb-item:nth-last-child(2)::before {
    content: "...";
  }
}
```

### Intégration avec des icônes

Vous pouvez améliorer visuellement votre fil d'Ariane avec des icônes :

```html
<nav aria-label="breadcrumb">
  <ol class="breadcrumb">
    <li class="breadcrumb-item">
      <a href="#"><i class="fa fa-home" aria-hidden="true"></i> Accueil</a>
    </li>
    <li class="breadcrumb-item"><a href="#">Catégorie</a></li>
    <li class="breadcrumb-item active" aria-current="page">Page actuelle</li>
  </ol>
</nav>
```

## Variables de personnalisation

### Variables CSS

```css
/* Variables pour le fil d'Ariane */
--bs-breadcrumb-padding-x: 0;
--bs-breadcrumb-padding-y: 0;
--bs-breadcrumb-margin-bottom: 1rem;
--bs-breadcrumb-bg: transparent;
--bs-breadcrumb-border-radius: 0.375rem;
--bs-breadcrumb-divider-color: var(--bs-secondary-color);
--bs-breadcrumb-item-padding-x: 0.5rem;
--bs-breadcrumb-item-active-color: var(--bs-secondary-color);
--bs-breadcrumb-divider: '/';
```

### Variables Sass

```scss
/* Breadcrumbs */
$breadcrumb-font-size: null;
$breadcrumb-padding-y: 0;
$breadcrumb-padding-x: 0;
$breadcrumb-item-padding-x: .5rem;
$breadcrumb-margin-bottom: 1rem;
$breadcrumb-bg: null;
$breadcrumb-divider-color: var(--#{$prefix}secondary-color);
$breadcrumb-active-color: var(--#{$prefix}secondary-color);
$breadcrumb-divider: quote("/");
$breadcrumb-divider-flipped: $breadcrumb-divider;
$breadcrumb-border-radius: null;
```

## Considérations pour MkDocs

### Pages d'index

Dans MkDocs, les pages index (`index.md` ou `README.md`) jouent un rôle important dans la navigation. Ces pages servent de points d'entrée pour les sections et affectent la structure du fil d'Ariane.

Selon la documentation officielle de MkDocs, quand deux fichiers `index.md` et `README.md` existent dans le même répertoire, `index.md` est utilisé et `README.md` est ignoré. Cette connaissance est utile pour structurer correctement votre documentation.

### Mise à jour du mkdocs.yml

Pour que votre fil d'Ariane reflète correctement la structure de votre documentation, assurez-vous que votre fichier `mkdocs.yml` contient une configuration `nav` bien structurée :

```yaml
site_name: Documentation Bootstrap 5 pour Moodle
nav:
  - Accueil: index.md
  - Composants:
    - Accordéon: components/accordeon.md
    - Alertes: components/alertes.md
    - Fil d'Ariane: components/ariane.md
    - Badges: components/badges.md
    - Boutons: components/boutons.md
    - Cartes: components/cartes.md
    - Carrousel: components/carrousel.md
    - Formulaires: components/formulaires.md
    - Modales: components/modales.md
    - Navigation: components/navigation.md
    - Tableaux: components/tableaux.md
```

Le fil d'Ariane est un élément essentiel de l'expérience utilisateur, offrant orientation et contexte aux utilisateurs navigant dans une plateforme complexe comme Moodle ou un site de documentation. Une implémentation soignée améliore considérablement l'utilisabilité et l'accessibilité du site.