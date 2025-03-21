from config_loader import ConfigLoader
from gallery_builder import GalleryBuilder
from glossary_builder import GlossaryBuilder
from jinja2 import Environment, FileSystemLoader, select_autoescape
from page_builder import PageBuilder
from pathlib import Path
from post_builder import PostBuilder
from static_file_manager import StaticFileManager
from utils import markdown_filter, format_date_filter, slugify
import sys
import logging
import argparse
import pprint
import json

sys.path.append(str(Path(__file__).parent.parent / 'src'))
from config.navigation import get_navigation

sys.stdout.reconfigure(encoding='utf-8')

logging.basicConfig(
    level=logging.INFO,
    format='[%(asctime)s] %(levelname)s: %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S'
)

ICON_START = "🚀"
ICON_CLEAN = "🧹"
ICON_COPY = "📋"
ICON_BUILD = "📝"
ICON_GLOSSARY = "📖"
ICON_CATEGORY = "📂"
ICON_REDIRECT = "🔀"
ICON_SUCCESS = "✨"
ICON_ERROR = "❌"

def force_string(value):
    """Force la conversion en chaîne de caractères."""
    if value is None:
        return ''
    if hasattr(value, '__str__'):
        return value.__str__()
    return str(value)

class SiteBuilder:
    def __init__(self):
        self.base_path = Path(__file__).parent.parent
        self.src_path = self.base_path / 'src'
        self.dist_path = self.base_path / 'dist'

        config_loader = ConfigLoader(self.src_path)
        self.translations = config_loader.load_translations()
        self.projects = config_loader.load_projects()
        self.site_config = config_loader.load_site_config()

        # Charger les traductions
        translations_file = self.src_path / 'locales' / 'fr' / 'translations.json'
        with open(translations_file, 'r', encoding='utf-8') as f:
            translations = json.load(f)

        self.jinja_env = Environment(
            loader=FileSystemLoader(str(self.src_path / 'templates')),
            autoescape=select_autoescape(['html', 'xml'])
        )
        self.jinja_env.filters['date'] = format_date_filter
        self.jinja_env.filters['markdown'] = markdown_filter
        self.jinja_env.filters['slugify'] = slugify
        self.jinja_env.filters['pprint'] = pprint.pformat
        self.jinja_env.filters['string'] = force_string

        # Ajouter les traductions à l'environnement global
        self.jinja_env.globals['t'] = translations

        # Chargement de la navigation
        try:
            nav = get_navigation()
            logging.info(f"Navigation brute chargée: {nav}")

            def process_nav_item(item):
                """Traite un élément de navigation et ses enfants."""
                if not isinstance(item, dict):
                    logging.warning(f"Item de navigation invalide (pas un dict): {item}")
                    return {'title': '', 'url': '#'}

                # Forcer la conversion en chaîne de caractères
                title = force_string(item.get('title', ''))
                url = force_string(item.get('url', '#'))

                processed = {
                    'title': title,
                    'url': url
                }

                if 'children' in item and isinstance(item['children'], list):
                    processed['children'] = [process_nav_item(child) for child in item['children']]

                logging.info(f"Item traité: {processed}")
                return processed

            # Traiter la navigation principale
            if isinstance(nav, dict) and 'main' in nav and isinstance(nav['main'], list):
                main_nav = [process_nav_item(item) for item in nav['main']]
                self.jinja_env.globals['navigation'] = {'main': main_nav}
                logging.info("Navigation traitée avec succès")
            else:
                raise ValueError("Format de navigation invalide")

        except Exception as e:
            logging.error(f"Erreur lors du chargement de la navigation: {e}", exc_info=True)
            self.jinja_env.globals['navigation'] = {'main': []}

        self.jinja_env.globals['is_multilingual'] = len(self.site_config.get('languages', [])) > 1
        self.jinja_env.globals['is_unilingual'] = not len(self.site_config.get('languages', [])) > 1

        self.static_manager = StaticFileManager(self.src_path, self.dist_path)
        self.post_builder = PostBuilder(self.src_path, self.dist_path, self.site_config,
                                      self.translations, self.jinja_env, self.projects)
        self.glossary_builder = GlossaryBuilder(self.src_path, self.dist_path, self.site_config,
                                              self.translations, self.jinja_env, self.projects)
        self.page_builder = PageBuilder(self.src_path, self.dist_path, self.site_config,
                                      self.translations, self.jinja_env, self.projects,
                                      post_builder=self.post_builder)

    def build(self):
        try:
            logging.info(f"{ICON_START} Début de la construction du site...")
            logging.info(f"{ICON_CLEAN} Nettoyage du dossier de sortie...")
            self.static_manager.setup_output_dir()
            logging.info(f"{ICON_COPY} Copie des fichiers statiques...")
            self.static_manager.copy_static_files()

            gallery_builder = GalleryBuilder(self.src_path, self.dist_path, self.jinja_env,
                                             self.site_config, self.translations)
            gallery_builder.build_gallery()

            logging.info(f"{ICON_BUILD} Génération des pages...")
            self.page_builder.build_pages()
            logging.info(f"{ICON_BUILD} Génération des posts...")
            posts = self.post_builder.build_posts()
            logging.info(f"{ICON_GLOSSARY} Génération du glossaire...")
            self.glossary_builder.build_terms()
            logging.info(
                f"{ICON_CATEGORY} Regroupement des posts pour les catégories et mots-clés...")
            categories = {}
            keywords = {}
            for post in posts:
                for category in post.get('categories', []):
                    categories.setdefault(category, []).append(post)
                for keyword in post.get('meta_keywords', []):
                    keywords.setdefault(keyword, []).append(post)

            self.page_builder.build_category_pages(categories)
            self.page_builder.build_keyword_pages(keywords)

            logging.info(
                f"{ICON_CATEGORY} Génération des pages pour les catégories...")
            self.page_builder.build_category_pages(categories)
            logging.info(
                f"{ICON_CATEGORY} Génération des pages pour les mots-clés...")
            self.page_builder.build_keyword_pages(keywords)
            logging.info(
                f"{ICON_REDIRECT} Création de la redirection racine...")

            logging.info(f"{ICON_SUCCESS} Site construit avec succès!")
        except Exception as e:
            logging.error(
                f"{ICON_ERROR} Erreur durant la construction du site: {e}", exc_info=True)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Site Builder CLI options")
    parser.add_argument("--build", action="store_true", help="Build the site")

    args = parser.parse_args()
    if args.build:
        builder = SiteBuilder()
        builder.build()
    else:
        parser.print_help()
