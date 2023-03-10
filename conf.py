# -*- coding: utf-8 -*-
#
# Godot Engine documentation build configuration file

import sys
import os

# -- General configuration ------------------------------------------------

needs_sphinx = "1.3"

# Sphinx extension module names and templates location
sys.path.append(os.path.abspath("_extensions"))
extensions = [
    "gdscript",
    "godot_descriptions",
]
templates_path = ["_templates"]

# You can specify multiple suffix as a list of string: ['.rst', '.md']
source_suffix = ".rst"
source_encoding = "utf-8-sig"

# The master toctree document
master_doc = "index"

# General information about the project
project = "Godot Engine"
copyright = (
    "2014-2018, Juan Linietsky, Ariel Manzur and the Godot community (CC-BY 3.0)"
)
author = "Juan Linietsky, Ariel Manzur and the Godot community"

# Version info for the project, acts as replacement for |version| and |release|
# The short X.Y version
version = os.getenv("READTHEDOCS_VERSION", "2.1")
# The full version, including alpha/beta/rc tags
release = version

# Language / i18n

supported_languages = {
    "en": "Godot Engine (%s) documentation in English",
    "de": "Godot Engine (%s) Dokumentation auf Deutsch",
    "es": "Documentación de Godot Engine (%s) en español",
    "fr": "Documentation de Godot Engine (%s) en français",
    "fi": "Godot Engine (%s) dokumentaatio suomeksi",
    "it": "Godot Engine (%s) documentazione in italiano",
    "ja": "Godot Engine (%s)の日本語のドキュメント",
    "ko": "Godot Engine (%s) 문서 (한국어)",
    "pl": "Dokumentacja Godot Engine (%s) w języku polskim",
    "pt_BR": "Documentação da Godot Engine (%s) em Português Brasileiro",
    "ru": "Документация Godot Engine (%s) на русском языке",
    "uk": "Документація до Godot Engine (%s) українською мовою",
    "zh_CN": "Godot Engine (%s) 简体中文文档",
}

language = os.getenv("READTHEDOCS_LANGUAGE", "en")
if not language in supported_languages.keys():
    print("Unknown language: " + language)
    print("Supported languages: " + ", ".join(supported_languages.keys()))
    print(
        "The configured language is either wrong, or it should be added to supported_languages in conf.py. Falling back to 'en'."
    )
    language = "en"

exclude_patterns = ["_build"]

# fmt: off
# These imports should *not* be moved to the start of the file,
# they depend on the sys.path.append call registering "extensions".
from gdscript import GDScriptLexer
from sphinx.highlighting import lexers

lexers['gdscript'] = GDScriptLexer()
# fmt: on

# Pygments (syntax highlighting) style to use
pygments_style = "sphinx"
highlight_language = "gdscript"

# -- Options for HTML output ----------------------------------------------

# on_rtd is whether we are on readthedocs.org, this line of code grabbed from docs.readthedocs.org
on_rtd = os.environ.get("READTHEDOCS", None) == "True"

import sphinx_rtd_theme

html_theme = "sphinx_rtd_theme"
html_theme_path = [sphinx_rtd_theme.get_html_theme_path()]
if on_rtd:
    using_rtd_theme = True

# Theme options
html_theme_options = {
    # 'typekit_id': 'hiw1hhg',
    # 'analytics_id': '',
    # 'sticky_navigation': True  # Set to False to disable the sticky nav while scrolling.
    "logo_only": True,  # if we have a html_logo below, this shows /only/ the logo with no title text
    "collapse_navigation": False,  # Collapse navigation (False makes it tree-like)
    # 'display_version': True,  # Display the docs version
    # 'navigation_depth': 4,  # Depth of the headers shown in the navigation bar
}

html_title = supported_languages[language] % version

# VCS options: https://docs.readthedocs.io/en/latest/vcs.html#github
html_context = {
    "display_github": True,  # Integrate GitHub
    "github_user": "godotengine",  # Username
    "github_repo": "godot-docs",  # Repo name
    "github_version": "master",  # Version
    "conf_py_path": "/",  # Path in the checkout to the docs root
    "godot_inject_language_links": True,
    "godot_docs_supported_languages": list(supported_languages.keys()),
    "godot_docs_basepath": "https://docs.godotengine.org/",
    "godot_docs_suffix": ".html",
    "godot_default_lang": "en",
    "godot_canonical_version": "stable",
    # Distinguish local development website from production website.
    # This prevents people from looking for changes on the production website after making local changes :)
    "godot_title_prefix": "" if on_rtd else "(DEV) ",
}

html_logo = "img/docs_logo.png"

# Output file base name for HTML help builder
htmlhelp_basename = "GodotEnginedoc"

# -- Options for reStructuredText parser ----------------------------------

# Enable directives that insert the contents of external files
file_insertion_enabled = False

# -- Options for LaTeX output ---------------------------------------------

# Grouping the document tree into LaTeX files. List of tuples
# (source start file, target name, title,
#  author, documentclass [howto, manual, or own class]).
latex_documents = [
    (
        master_doc,
        "GodotEngine.tex",
        "Godot Engine Documentation",
        "Juan Linietsky, Ariel Manzur and the Godot community",
        "manual",
    ),
]
