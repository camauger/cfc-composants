---
title: Accordéon
description: Guide d'utilisation du composant accordéon de Bootstrap 5 dans Moodle
template: pages/composant.html
---


L'accordéon est un composant interactif qui permet d'afficher du contenu de manière expansible/réductible. Il est particulièrement utile pour organiser du contenu dense en sections distinctes dans Moodle.

## Utilisation de base

L'accordéon de base utilise les classes `accordion` et `accordion-item` pour créer une liste d'éléments expansibles.

<div class="example-preview">
  <div class="accordion" id="accordionExample">
    <div class="accordion-item">
      <h2 class="accordion-header">
        <button class="accordion-button" type="button" data-bs-toggle="collapse" data-bs-target="#collapseOne" aria-expanded="true" aria-controls="collapseOne">
          Section 1
        </button>
      </h2>
      <div id="collapseOne" class="accordion-collapse collapse show" data-bs-parent="#accordionExample">
        <div class="accordion-body">
          Contenu de la première section
        </div>
      </div>
    </div>
    <div class="accordion-item">
      <h2 class="accordion-header">
        <button class="accordion-button collapsed" type="button" data-bs-toggle="collapse" data-bs-target="#collapseTwo" aria-expanded="false" aria-controls="collapseTwo">
          Section 2
        </button>
      </h2>
      <div id="collapseTwo" class="accordion-collapse collapse" data-bs-parent="#accordionExample">
        <div class="accordion-body">
          Contenu de la deuxième section
        </div>
      </div>
    </div>
  </div>
</div>

## Utilisation dans Moodle

Dans Moodle, l'accordéon est particulièrement utile pour :

1. **Organisation des sections de cours**
   - Regrouper les ressources par thème
   - Masquer/afficher les activités optionnelles
   - Présenter des informations complémentaires

2. **Présentation des consignes**
   - Structurer les étapes d'une activité
   - Fournir des détails supplémentaires à la demande
   - Organiser les critères d'évaluation

3. **FAQ et support**
   - Répondre aux questions fréquentes
   - Fournir de l'aide contextuelle
   - Présenter des tutoriels étape par étape

## Options de personnalisation

### Flush

L'option `accordion-flush` supprime les bordures externes de l'accordéon.

<div class="accordion accordion-flush" id="accordionFlushExample">
  <!-- ... contenu de l'accordéon ... -->
</div>

### Always open

Par défaut, un seul élément peut être ouvert à la fois. Pour permettre l'ouverture simultanée de plusieurs éléments, retirez l'attribut `data-bs-parent`.

<div class="accordion" id="accordionNoParent">
  <div class="accordion-item">
    <!-- Notez l'absence de data-bs-parent -->
    <div id="collapseOne" class="accordion-collapse collapse show">
      <!-- ... contenu ... -->
    </div>
  </div>
</div>

## Accessibilité

Pour garantir l'accessibilité de vos accordéons :

1. **Structure HTML**
   - Utilisez des balises `<h2>` pour les en-têtes
   - Maintenez une hiérarchie logique des titres
   - Préservez l'ordre sémantique du contenu

2. **Attributs ARIA**
   - `aria-expanded` : indique l'état d'expansion
   - `aria-controls` : associe le bouton à son contenu
   - `aria-labelledby` : lie le contenu à son en-tête

3. **Navigation au clavier**
   - Tab : navigation entre les boutons
   - Enter/Space : ouvre/ferme la section
   - Les boutons sont naturellement focusables

## Bonnes pratiques

1. **Organisation du contenu**
   - Limitez le nombre de sections (maximum 5-7)
   - Utilisez des titres descriptifs et concis
   - Évitez de masquer des informations critiques

2. **Performance**
   - Évitez les accordéons imbriqués
   - Ne surchargez pas les sections de contenu
   - Utilisez des images optimisées

3. **Expérience utilisateur**
   - Indiquez clairement le contenu de chaque section
   - Maintenez une cohérence dans la structure
   - Préservez l'état des sections lors de la navigation

## Personnalisation CSS

Vous pouvez personnaliser l'apparence de l'accordéon avec les variables CSS de Bootstrap :

```scss
// Variables personnalisables
$accordion-padding-y: 1rem;
$accordion-padding-x: 1.25rem;
$accordion-color: $body-color;
$accordion-bg: $body-bg;
$accordion-border-width: $border-width;
$accordion-border-color: var(--#{$prefix}border-color);
$accordion-border-radius: $border-radius;
$accordion-inner-border-radius: subtract($accordion-border-radius, $accordion-border-width);

// États et interactions
$accordion-button-active-bg: tint-color($component-active-bg, 90%);
$accordion-button-active-color: shade-color($primary, 10%);
$accordion-button-focus-border-color: $input-focus-border-color;
$accordion-button-focus-box-shadow: $btn-focus-box-shadow;
```

## Exemples d'utilisation dans Moodle

### Sections de cours

<div class="accordion" id="courseContent">
  <div class="accordion-item">
    <h2 class="accordion-header">
      <button class="accordion-button" type="button" data-bs-toggle="collapse" data-bs-target="#module1">
        Module 1 : Introduction
      </button>
    </h2>
    <div id="module1" class="accordion-collapse collapse show" data-bs-parent="#courseContent">
      <div class="accordion-body">
        <ul class="list-unstyled">
          <li><i class="fas fa-book"></i> Lecture : Introduction au cours</li>
          <li><i class="fas fa-tasks"></i> Quiz : Évaluation initiale</li>
          <li><i class="fas fa-comments"></i> Forum : Présentations</li>
        </ul>
      </div>
    </div>
  </div>
</div>

### FAQ dynamique

<div class="accordion accordion-flush" id="faqAccordion">
  <div class="accordion-item">
    <h2 class="accordion-header">
      <button class="accordion-button collapsed" type="button" data-bs-toggle="collapse" data-bs-target="#faq1">
        Comment soumettre un devoir ?
      </button>
    </h2>
    <div id="faq1" class="accordion-collapse collapse" data-bs-parent="#faqAccordion">
      <div class="accordion-body">
        <ol>
          <li>Accédez à la section du devoir</li>
          <li>Cliquez sur "Ajouter un travail"</li>
          <li>Téléversez votre fichier</li>
          <li>Cliquez sur "Enregistrer"</li>
        </ol>
      </div>
    </div>
  </div>
</div>

## Dépannage

### Problèmes courants

1. **L'accordéon ne s'ouvre pas**
   - Vérifiez que le JavaScript de Bootstrap est chargé
   - Confirmez que les IDs sont uniques
   - Assurez-vous que les attributs data-bs-* sont corrects

2. **Conflits de style**
   - Inspectez les styles avec les outils de développement
   - Vérifiez la spécificité CSS
   - Utilisez !important avec parcimonie

3. **Problèmes d'accessibilité**
   - Testez la navigation au clavier
   - Vérifiez les contrastes de couleur
   - Validez les attributs ARIA

## Bonnes pratiques

### Pour les développeurs

1. **Accessibilité** :
   - Utilisez des en-têtes (`<h2>`, `<h3>`, etc.) appropriés
   - Assurez-vous que les boutons ont un texte descriptif
   - Maintenez une hiérarchie logique du contenu
   - Utilisez les attributs ARIA appropriés (`aria-expanded`, `aria-controls`)

2. **Performance** :
   - Évitez de surcharger l'accordéon avec trop de contenu
   - Utilisez des images optimisées dans le contenu
   - Préchargez le contenu important

### Pour les non-développeurs

#### Quand utiliser un accordéon

L'accordéon est un excellent choix dans les situations suivantes :

- **Contenu dense** : Lorsque vous avez beaucoup d'informations à présenter mais souhaitez éviter le défilement excessif
- **Informations hiérarchiques** : Pour organiser du contenu en catégories distinctes
- **FAQ** : Pour présenter des questions et réponses de manière organisée
- **Structuration de cours** : Pour organiser les sections ou modules d'un cours
- **Consignes d'activités** : Pour décomposer des instructions complexes en étapes logiques

En revanche, évitez d'utiliser un accordéon quand :

- Le contenu est court et peut être affiché directement
- L'information est critique et ne devrait pas être masquée
- Tous les éléments doivent être consultés dans un ordre spécifique
- Le contenu est fréquemment consulté et sa dissimulation créerait une friction inutile

#### Organisation efficace du contenu

1. **Hiérarchie logique** :
   - Organisez les sections de l'accordéon dans un ordre logique
   - Placez les informations les plus importantes ou les plus fréquemment consultées en haut
   - Regroupez les contenus thématiquement cohérents

2. **Équilibre du contenu** :
   - Répartissez le contenu de manière équilibrée entre les sections
   - Évitez une section très longue suivie de sections très courtes
   - Idéalement, chaque section devrait pouvoir être lue en 1-2 minutes maximum

3. **Rédaction des titres** :
   - Utilisez des titres courts mais descriptifs (5-10 mots maximum)
   - Commencez par les mots-clés importants
   - Soyez cohérent dans la formulation des titres (questions, affirmations, etc.)
   - Évitez le jargon technique sauf si votre public le comprend parfaitement

#### Cas d'utilisation dans Moodle

1. **Page de cours** :
   - Organisez les sujets/semaines du cours en accordéons pour une navigation facile
   - Utilisez un accordéon pour regrouper les ressources complémentaires
   - Présentez les consignes d'évaluation en sections distinctes

2. **Documentation pédagogique** :
   - Structurez les guides d'utilisation par thématiques
   - Présenter les étapes d'un processus (par exemple, soumettre un devoir)
   - Regrouper différents scénarios d'utilisation

3. **Activités interactives** :
   - Organisez les étapes d'un exercice complexe
   - Présentez plusieurs cas d'étude ou exemples
   - Structurez des critères d'évaluation détaillés

#### Conseils ergonomiques

1. **Visibilité des contrôles** :
   - Assurez-vous que les boutons d'ouverture/fermeture sont facilement identifiables
   - Utilisez des icônes reconnaissables (flèche vers le bas/haut) en plus du texte
   - Maintenez une taille suffisante pour faciliter l'interaction sur appareils tactiles

2. **Retour visuel** :
   - Assurez-vous que l'état ouvert/fermé est clairement visible
   - Utilisez des animations sobres pour signaler les transitions
   - Envisagez d'utiliser des couleurs différentes pour les sections actives

3. **Considérations mobiles** :
   - Testez l'accordéon sur petits écrans pour vérifier la lisibilité
   - Assurez-vous que les boutons sont suffisamment grands pour être touchés
   - Vérifiez que le contenu déplié s'affiche correctement sur mobile

#### Exemples concrets dans Moodle

**Exemple 1 : FAQ du cours**

<div class="accordion" id="faqAccordion">
  <div class="accordion-item">
    <h2 class="accordion-header">
      <button class="accordion-button collapsed" type="button" data-bs-toggle="collapse" data-bs-target="#faq1">
        Comment soumettre mon devoir ?
      </button>
    </h2>
    <div id="faq1" class="accordion-collapse collapse" data-bs-parent="#faqAccordion">
      <div class="accordion-body">
        <p>Pour soumettre votre devoir :</p>
        <ol>
          <li>Cliquez sur l'activité "Devoir" dans votre cours</li>
          <li>Cliquez sur le bouton "Ajouter un travail"</li>
          <li>Déposez votre fichier ou rédigez votre texte</li>
          <li>Cliquez sur "Enregistrer"</li>
        </ol>
      </div>
    </div>
  </div>
  <!-- Autres questions... -->
</div>


**Exemple 2 : Plan de cours structuré**

<div class="accordion" id="courseModules">
  <div class="accordion-item">
    <h2 class="accordion-header">
      <button class="accordion-button" type="button" data-bs-toggle="collapse" data-bs-target="#module1">
        Module 1 : Introduction au sujet
      </button>
    </h2>
    <div id="module1" class="accordion-collapse collapse show" data-bs-parent="#courseModules">
      <div class="accordion-body">
        <h3>Objectifs d'apprentissage</h3>
        <ul>
          <li>Comprendre les concepts fondamentaux</li>
          <li>Savoir appliquer les principes de base</li>
        </ul>

        <h3>Ressources</h3>
        <ul>
          <li><a href="#">Présentation du cours</a></li>
          <li><a href="#">Lecture obligatoire</a></li>
        </ul>
      </div>
    </div>
  </div>
  <!-- Autres modules... -->
</div>


#### Complémentarité avec d'autres composants

Les accordéons fonctionnent bien en combinaison avec :

- **Onglets** : Utilisez des onglets pour les catégories principales et des accordéons pour les sous-catégories
- **Boutons** : Ajoutez des boutons d'action à l'intérieur des sections d'accordéon
- **Cartes** : Intégrez des accordéons dans des cartes pour une organisation visuelle plus claire
- **Badges** : Ajoutez des badges aux titres d'accordéon pour indiquer des statuts (nouveau, obligatoire, etc.)

## Intégration dans Moodle

Pour utiliser l'accordéon dans Moodle, assurez-vous que le JavaScript de Bootstrap est correctement chargé. Exemple d'utilisation dans un template Moodle :

```php
<?php
// Template Moodle
$context = context_system::instance();
?>

<div class="accordion" id="moodleAccordion">
    {{#sections}}
    <div class="accordion-item">
        <h2 class="accordion-header">
            <button class="accordion-button" type="button" data-bs-toggle="collapse" data-bs-target="#collapse{{id}}">
                {{{title}}}
            </button>
        </h2>
        <div id="collapse{{id}}" class="accordion-collapse collapse" data-bs-parent="#moodleAccordion">
            <div class="accordion-body">
                {{{content}}}
            </div>
        </div>
    </div>
    {{/sections}}
</div>
```

### Exemple avec plusieurs sections


<div class="accordion" id="courseSections">
  <div class="accordion-item">
    <h2 class="accordion-header">
      <button class="accordion-button" type="button" data-bs-toggle="collapse" data-bs-target="#section1">
        Section 1 : Introduction
      </button>
    </h2>
    <div id="section1" class="accordion-collapse collapse show" data-bs-parent="#courseSections">
      <div class="accordion-body">
        <h3>Objectifs du cours</h3>
        <ul>
          <li>Objectif 1</li>
          <li>Objectif 2</li>
        </ul>
      </div>
    </div>
  </div>
  <div class="accordion-item">
    <h2 class="accordion-header">
      <button class="accordion-button collapsed" type="button" data-bs-toggle="collapse" data-bs-target="#section2">
        Section 2 : Contenu du cours
      </button>
    </h2>
    <div id="section2" class="accordion-collapse collapse" data-bs-parent="#courseSections">
      <div class="accordion-body">
        Contenu de la section 2...
      </div>
    </div>
  </div>
</div>

## Considérations d'accessibilité

- Utilisez des attributs ARIA appropriés :

  <button class="accordion-button"
          aria-expanded="true"
          aria-controls="collapseOne">

- Assurez-vous que l'accordéon est navigable au clavier
- Fournissez des retours visuels clairs pour les états focus et hover
- Maintenez un contraste suffisant pour les éléments interactifs
- Utilisez des textes descriptifs pour les boutons
- Évitez de masquer du contenu essentiel dans les accordéons