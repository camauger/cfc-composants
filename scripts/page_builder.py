import logging
from pathlib import Path
from utils import slugify, markdown_filter
import frontmatter
from metadata import extract_metadata


class PageBuilder:
    def __init__(self, src_path: Path, dist_path: Path, site_config: dict,
                 translations: dict, jinja_env, projects: list, post_builder=None):
        self.src_path = src_path
        self.dist_path = dist_path
        self.site_config = site_config
        self.translations = translations
        self.jinja_env = jinja_env
        self.projects = projects
        self.post_builder = post_builder

    def _build_page_translation_map(self) -> dict:
        """Construit le mapping global des pages pour chaque langue."""
        mapping = {}
        is_unilingual = len(self.site_config['languages']) == 1

        for lang in self.site_config['languages']:
            pages_dir = self.src_path / 'locales' / lang / 'pages'
            if pages_dir.exists():
                # Utiliser rglob pour chercher récursivement dans les sous-dossiers
                for page_file in pages_dir.rglob('*.md'):
                    content = page_file.read_text(encoding='utf-8')
                    metadata = extract_metadata(content)
                    tid = str(metadata.get("translation_id", page_file.stem))

                    # Construire l'URL en tenant compte du chemin relatif
                    relative_path = page_file.relative_to(pages_dir).with_suffix('')
                    if relative_path.name == 'home':
                        page_url = "/"
                    else:
                        parts = list(relative_path.parts)
                        page_url = "/" + "/".join(parts) + "/"
                        if not is_unilingual:
                            page_url = f"/{lang}{page_url}"

                    mapping.setdefault(tid, {})[lang] = page_url
        return mapping

    def _render_page(self, page_file: Path, lang: str, page_translations: dict,
                     is_unilingual: bool) -> None:
        """Rend une page en fonction de son type (blog ou standard)."""
        try:
            content = page_file.read_text(encoding='utf-8')
        except Exception as e:
            logging.error(f"Erreur lors de la lecture de {page_file}: {e}")
            return

        metadata = extract_metadata(content)
        template_name = metadata.get('template', 'pages/home.html')
        tid = str(metadata.get("translation_id", page_file.stem))
        page_trans = page_translations.get(tid, {})

        # Déterminer le chemin de sortie et l'URL custom en tenant compte des sous-dossiers
        pages_dir = self.src_path / 'locales' / lang / 'pages'
        relative_path = page_file.relative_to(pages_dir).with_suffix('')

        if is_unilingual:
            if relative_path.name == 'home':
                output_path = self.dist_path / 'index.html'
                custom_url = "/"
            else:
                parts = list(relative_path.parts)
                output_path = self.dist_path.joinpath(*parts) / 'index.html'
                custom_url = "/" + "/".join(parts) + "/"
        else:
            lang_dir = self.dist_path / lang
            if relative_path.name == 'home':
                output_path = lang_dir / 'index.html'
                custom_url = f"/{lang}/"
            else:
                parts = list(relative_path.parts)
                output_path = lang_dir.joinpath(*parts) / 'index.html'
                custom_url = f"/{lang}/" + "/".join(parts) + "/"

        # Rendu de la page
        if relative_path.name == 'blog':
            posts = self.load_posts(lang)
            pagination = {'posts': posts}
            page_metadata = {
                'title': metadata.get('title', 'Blog'),
                'description': metadata.get('description', ''),
                'lang': lang,
                'url': custom_url,
                'thumbnail': metadata.get('thumbnail', ''),
                **metadata,
                'translations': page_trans
            }
            translations_static = self.translations.get(lang, {})
            rendered = self.jinja_env.get_template(template_name).render(
                content=content,
                page=page_metadata,
                lang=lang,
                custom_url=custom_url,
                t=translations_static,
                site=self.site_config,
                projects=self.projects,
                pagination=pagination
            )
        else:
            page_metadata = {
                'lang': lang,
                'url': custom_url,
                'content_translations': page_trans,
                **metadata
            }
            translations_static = self.translations.get(lang, {})
            rendered = self.jinja_env.get_template(template_name).render(
                content=markdown_filter(frontmatter.loads(content).content),
                page=page_metadata,
                t=translations_static,
                site=self.site_config,
                projects=self.projects
            )

        output_path.parent.mkdir(parents=True, exist_ok=True)
        output_path.write_text(rendered, encoding='utf-8')

    def build_pages(self) -> None:
        """Construit l'ensemble des pages du site."""
        is_unilingual = len(self.site_config['languages']) == 1
        page_translation_map = self._build_page_translation_map()

        for lang in self.site_config['languages']:
            pages_dir = self.src_path / 'locales' / lang / 'pages'
            if pages_dir.exists():
                # Utiliser rglob pour chercher récursivement dans les sous-dossiers
                for page_file in pages_dir.rglob('*.md'):
                    self._render_page(
                        page_file, lang, page_translation_map, is_unilingual)

    def build_root_redirect(self) -> None:
        """Génère une redirection vers la page d'accueil pour la racine."""
        is_unilingual = len(self.site_config['languages']) == 1
        redirection_url = "/" if is_unilingual else f"/{self.site_config['languages'][0]}/"
        redirection_html = f"""<!DOCTYPE html>
<html lang="{self.site_config['languages'][0]}">
<head>
    <meta charset="utf-8">
    <meta http-equiv="refresh" content="0; url={redirection_url}">
    <link rel="canonical" href="{redirection_url}">
    <title>Redirection...</title>
</head>
<body>
    <p>Redirection vers <a href="{redirection_url}">la version du site</a>.</p>
</body>
</html>
"""
        (self.dist_path / "index.html").write_text(redirection_html, encoding="utf-8")

    def build_taxonomy_pages(self, taxonomy_type: str, taxonomy_dict: dict, template_name: str) -> None:
        """Construit les pages pour une taxonomie donnée (ex : catégories, mots-clés)."""
        is_unilingual = len(self.site_config.get('languages', [])) == 1

        for taxonomy_name, posts in taxonomy_dict.items():
            posts_by_lang = {}
            for post in posts:
                lang = post.get('lang', 'fr')
                posts_by_lang.setdefault(lang, []).append(post)

            for lang, posts_in_lang in posts_by_lang.items():
                slug = slugify(taxonomy_name)
                taxonomy_url_slug = self.site_config.get(
                    f"{taxonomy_type}_url", taxonomy_type)

                if is_unilingual:
                    tax_url = f"/{taxonomy_url_slug}/{slug}/"
                    output_path = self.dist_path / taxonomy_url_slug / slug / 'index.html'
                else:
                    tax_url = f"/{lang}/{taxonomy_url_slug}/{slug}/"
                    output_path = self.dist_path / lang / taxonomy_url_slug / slug / 'index.html'

                page_metadata = {
                    'title': f"{taxonomy_type.capitalize()}: {taxonomy_name}",
                    'description': f"Articles avec le {taxonomy_type} {taxonomy_name}",
                    'lang': lang,
                    'url': tax_url,
                    'taxonomy': taxonomy_name,
                }

                rendered = self.jinja_env.get_template(template_name).render(
                    posts=posts_in_lang,
                    taxonomy_name=taxonomy_name,
                    page=page_metadata,
                    site=self.site_config,
                    t=self.translations.get(lang, {})
                )

                output_path.parent.mkdir(parents=True, exist_ok=True)
                output_path.write_text(rendered, encoding='utf-8')

    def build_category_pages(self, categories: dict) -> None:
        """Construit les pages de catégories."""
        self.build_taxonomy_pages(
            'categories', categories, 'pages/category.html')

    def build_keyword_pages(self, keywords: dict) -> None:
        """Construit les pages de mots-clés."""
        self.build_taxonomy_pages('keywords', keywords, 'pages/keyword.html')

    def load_posts(self, lang: str) -> list:
        """Charge les posts via le post_builder s'il est défini."""
        return self.post_builder.load_posts(lang) if self.post_builder else []
