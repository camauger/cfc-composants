def get_navigation():
    """
    Retourne la structure de navigation du site.
    """
    return {
        'main': [
            {
                'title': str('Accueil'),
                'url': str('/'),
            },
            {
                'title': str('Composants'),
                'url': str('/composants'),
                'children': [
                    {
                        'title': str('Accordéon'),
                        'url': str('/composants/accordeon'),
                    },
                    {
                        'title': str('Alertes'),
                        'url': str('/composants/alertes'),
                    },
                    {
                        'title': str('Boutons'),
                        'url': str('/composants/boutons'),
                    },
                    {
                        'title': str('Cartes'),
                        'url': str('/composants/cartes'),
                    },
                    {
                        'title': str('Navigation'),
                        'url': str('/composants/navigation'),
                    },
                ],
            },
            {
                'title': str('Mise en page'),
                'url': str('/mise-en-page'),
                'children': [
                    {
                        'title': str('Grille'),
                        'url': str('/mise-en-page/grille'),
                    },
                    {
                        'title': str('Conteneurs'),
                        'url': str('/mise-en-page/conteneurs'),
                    },
                ],
            },
            {
                'title': str('Utilitaires'),
                'url': str('/utilitaires'),
                'children': [
                    {
                        'title': str('Espacement'),
                        'url': str('/utilitaires/espacement'),
                    },
                    {
                        'title': str('Typographie'),
                        'url': str('/utilitaires/typographie'),
                    },
                ],
            },
        ]
    }