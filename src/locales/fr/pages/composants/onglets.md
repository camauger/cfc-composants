---
title: Onglets
description: Documentation du composant Onglets de Bootstrap 5 pour Moodle
template: pages/composant.html
---

<div class="container py-4">
  <div class="row">
    <div class="col-lg-3">
      <nav id="navbar-example3" class="h-100 flex-column align-items-stretch pe-4 border-end">
        <nav class="nav nav-pills flex-column">
          <a class="nav-link" href="#description">Description</a>
          <a class="nav-link" href="#exemple-base">Exemple de base</a>
          <a class="nav-link" href="#styles">Styles d'onglets</a>
          <a class="nav-link" href="#utilisation-moodle">Utilisation dans Moodle</a>
          <a class="nav-link" href="#accessibilite">Accessibilité</a>
        </nav>
      </nav>
    </div>

    <div class="col-lg-9">
      <div data-bs-spy="scroll" data-bs-target="#navbar-example3" data-bs-smooth-scroll="true" class="scrollspy-example-2" tabindex="0">
        <div id="description">
          <h2>Description</h2>
          <p class="lead">Les onglets permettent d'organiser le contenu en sections distinctes, accessibles via des onglets cliquables. Ils sont utiles pour réduire la complexité visuelle et organiser le contenu de manière logique.</p>
        </div>

        <div id="exemple-base" class="mt-5">
          <h2>Exemple de base</h2>
          <p>Un exemple simple d'onglets avec contenu.</p>
          <div class="card mb-4">
            <div class="card-body">
              <div class="component-preview">
                <ul class="nav nav-tabs" id="myTab" role="tablist">
                  <li class="nav-item" role="presentation">
                    <button class="nav-link active" id="home-tab" data-bs-toggle="tab" data-bs-target="#home" type="button" role="tab" aria-controls="home" aria-selected="true">Accueil</button>
                  </li>
                  <li class="nav-item" role="presentation">
                    <button class="nav-link" id="profile-tab" data-bs-toggle="tab" data-bs-target="#profile" type="button" role="tab" aria-controls="profile" aria-selected="false">Profil</button>
                  </li>
                  <li class="nav-item" role="presentation">
                    <button class="nav-link" id="contact-tab" data-bs-toggle="tab" data-bs-target="#contact" type="button" role="tab" aria-controls="contact" aria-selected="false">Contact</button>
                  </li>
                </ul>
                <div class="tab-content" id="myTabContent">
                  <div class="tab-pane fade show active" id="home" role="tabpanel" aria-labelledby="home-tab">
                    Contenu de l'onglet Accueil
                  </div>
                  <div class="tab-pane fade" id="profile" role="tabpanel" aria-labelledby="profile-tab">
                    Contenu de l'onglet Profil
                  </div>
                  <div class="tab-pane fade" id="contact" role="tabpanel" aria-labelledby="contact-tab">
                    Contenu de l'onglet Contact
                  </div>
                </div>
              </div>
            </div>
          </div>
        </div>

        <div id="styles" class="mt-5">
          <h2>Styles d'onglets</h2>

          <div class="card mb-4">
            <div class="card-body">
              <h3 class="h5">Onglets avec icônes</h3>
              <p>Ajoutez des icônes aux onglets pour améliorer la compréhension visuelle.</p>
              <div class="component-preview">
                <ul class="nav nav-tabs" id="iconTab" role="tablist">
                  <li class="nav-item" role="presentation">
                    <button class="nav-link active" id="home-icon-tab" data-bs-toggle="tab" data-bs-target="#home-icon" type="button" role="tab" aria-controls="home-icon" aria-selected="true">
                      <i class="fas fa-home"></i> Accueil
                    </button>
                  </li>
                  <li class="nav-item" role="presentation">
                    <button class="nav-link" id="profile-icon-tab" data-bs-toggle="tab" data-bs-target="#profile-icon" type="button" role="tab" aria-controls="profile-icon" aria-selected="false">
                      <i class="fas fa-user"></i> Profil
                    </button>
                  </li>
                </ul>
                <div class="tab-content" id="iconTabContent">
                  <div class="tab-pane fade show active" id="home-icon" role="tabpanel" aria-labelledby="home-icon-tab">
                    Contenu avec icône
                  </div>
                  <div class="tab-pane fade" id="profile-icon" role="tabpanel" aria-labelledby="profile-icon-tab">
                    Contenu avec icône
                  </div>
                </div>
              </div>
            </div>
          </div>

          <div class="card mb-4">
            <div class="card-body">
              <h3 class="h5">Onglets verticaux</h3>
              <p>Organisez les onglets verticalement pour une meilleure utilisation de l'espace.</p>
              <div class="component-preview">
                <div class="row">
                  <div class="col-3">
                    <div class="nav flex-column nav-pills" id="v-pills-tab" role="tablist">
                      <button class="nav-link active" id="v-pills-home-tab" data-bs-toggle="pill" data-bs-target="#v-pills-home" type="button" role="tab" aria-controls="v-pills-home" aria-selected="true">Accueil</button>
                      <button class="nav-link" id="v-pills-profile-tab" data-bs-toggle="pill" data-bs-target="#v-pills-profile" type="button" role="tab" aria-controls="v-pills-profile" aria-selected="false">Profil</button>
                      <button class="nav-link" id="v-pills-messages-tab" data-bs-toggle="pill" data-bs-target="#v-pills-messages" type="button" role="tab" aria-controls="v-pills-messages" aria-selected="false">Messages</button>
                    </div>
                  </div>
                  <div class="col-9">
                    <div class="tab-content" id="v-pills-tabContent">
                      <div class="tab-pane fade show active" id="v-pills-home" role="tabpanel" aria-labelledby="v-pills-home-tab">
                        Contenu de l'onglet Accueil
                      </div>
                      <div class="tab-pane fade" id="v-pills-profile" role="tabpanel" aria-labelledby="v-pills-profile-tab">
                        Contenu de l'onglet Profil
                      </div>
                      <div class="tab-pane fade" id="v-pills-messages" role="tabpanel" aria-labelledby="v-pills-messages-tab">
                        Contenu de l'onglet Messages
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
          <p>Dans Moodle, les onglets sont particulièrement utiles pour :</p>
          <ul class="list-group mb-4">
            <li class="list-group-item">Organiser le contenu des cours par sections</li>
            <li class="list-group-item">Séparer les différentes parties d'une activité</li>
            <li class="list-group-item">Créer des interfaces de navigation complexes</li>
            <li class="list-group-item">Gérer les paramètres de configuration</li>
          </ul>

          <div class="card mb-4">
            <div class="card-body">
              <h3 class="h5">Exemple d'intégration dans un template Moodle</h3>
              <pre class="bg-light p-3 rounded"><code>{{#course}}
    &lt;ul class="nav nav-tabs" id="courseTab" role="tablist"&gt;
        &lt;li class="nav-item" role="presentation"&gt;
            &lt;button class="nav-link active" id="overview-tab" data-bs-toggle="tab" data-bs-target="#overview" type="button" role="tab" aria-controls="overview" aria-selected="true"&gt;
                Vue d'ensemble
            &lt;/button&gt;
        &lt;/li&gt;
        &lt;li class="nav-item" role="presentation"&gt;
            &lt;button class="nav-link" id="content-tab" data-bs-toggle="tab" data-bs-target="#content" type="button" role="tab" aria-controls="content" aria-selected="false"&gt;
                Contenu
            &lt;/button&gt;
        &lt;/li&gt;
        &lt;li class="nav-item" role="presentation"&gt;
            &lt;button class="nav-link" id="progress-tab" data-bs-toggle="tab" data-bs-target="#progress" type="button" role="tab" aria-controls="progress" aria-selected="false"&gt;
                Progression
            &lt;/button&gt;
        &lt;/li&gt;
    &lt;/ul&gt;

    &lt;div class="tab-content" id="courseTabContent"&gt;
        &lt;div class="tab-pane fade show active" id="overview" role="tabpanel" aria-labelledby="overview-tab"&gt;
            &lt;div class="course-overview"&gt;
                {{&gt; course_overview}}
            &lt;/div&gt;
        &lt;/div&gt;
        &lt;div class="tab-pane fade" id="content" role="tabpanel" aria-labelledby="content-tab"&gt;
            &lt;div class="course-content"&gt;
                {{&gt; course_content}}
            &lt;/div&gt;
        &lt;/div&gt;
        &lt;div class="tab-pane fade" id="progress" role="tabpanel" aria-labelledby="progress-tab"&gt;
            &lt;div class="course-progress"&gt;
                {{&gt; course_progress}}
            &lt;/div&gt;
        &lt;/div&gt;
    &lt;/div&gt;
{{/course}}</code></pre>
            </div>
          </div>
        </div>

        <div id="accessibilite" class="mt-5">
          <h2>Accessibilité</h2>
          <ul class="list-group mb-4">
            <li class="list-group-item">Utilisez des libellés clairs et descriptifs pour les onglets</li>
            <li class="list-group-item">Assurez-vous que la navigation au clavier fonctionne correctement</li>
            <li class="list-group-item">Maintenez une structure cohérente entre les onglets</li>
            <li class="list-group-item">Fournissez des indicateurs visuels clairs pour l'onglet actif</li>
            <li class="list-group-item">Testez la navigation avec des lecteurs d'écran</li>
          </ul>
        </div>
      </div>
    </div>
  </div>
</div>