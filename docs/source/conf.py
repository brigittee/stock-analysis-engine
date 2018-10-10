# -*- coding: utf-8 -*-
#
# Configuration file for the Sphinx documentation builder.
#
# This file does only contain a selection of the most common options. For a
# full list see the documentation:
# http://www.sphinx-doc.org/en/master/config

# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
# import os
# import sys
# sys.path.insert(0, os.path.abspath('.'))


# -- Project information -----------------------------------------------------

import os
import sys
from unittest.mock import MagicMock
from recommonmark.parser import CommonMarkParser
from pprint import pprint

# Using working source code sphinx conf.py on read the docs:
# https://github.com/mahmoud/boltons/blob/master/docs/conf.py#L20

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
CUR_PATH = os.path.dirname(os.path.abspath(__file__))
PROJECT_PATH = os.path.abspath(CUR_PATH + '/../')
CUR_PACKAGE_PATH = os.path.abspath(CUR_PATH + '/../')
PACKAGE_PATH_FROM_DOCS = os.path.abspath('../')
sys.path.insert(0, PROJECT_PATH)

source_code_dirs = [
    'analysis_engine/iex/',
    'analysis_engine/mocks/',
    'analysis_engine/scripts/',
    'analysis_engine/work_tasks/',
    'analysis_engine/yahoo/'
]

for source_code_dir_name in source_code_dirs:
    sys.path.insert(0, '{}/{}'.format(
        CUR_PACKAGE_PATH,
        source_code_dir_name))
    sys.path.insert(0, '{}/../{}'.format(
        PACKAGE_PATH_FROM_DOCS,
        source_code_dir_name))

print('----------------------')
print('environment variables:')
pprint(os.environ)
print('cur path: {}'.format(
    CUR_PATH))
print('paths:')
pprint(sys.path)
print('cur dir files:')
os.system('ls -l {}'.format(
    PACKAGE_PATH_FROM_DOCS))
print('two dirs up:')
os.system('ls -l .. {}'.format(
    PACKAGE_PATH_FROM_DOCS))
os.system('ls -l {}/../latest/'.format(
print('two dirs up:')
os.system('ls -l {}/../..'.format(
    PACKAGE_PATH_FROM_DOCS))
print('two dirs up:')
os.system('ls -l {}/../..'.format(
    PACKAGE_PATH_FROM_DOCS))
os.system('ls -l {}/../../latest/'.format(
print('----------------------')

project = 'Stock Analysis Engine'
copyright = '2018, Jay Johnson'
author = 'Jay Johnson'

html_theme_options = {}
if os.getenv("READTHEDOCS", "") != "":

    class Mock(MagicMock):
        @classmethod
        def __getattr__(cls, name):
            return MagicMock()

    MOCK_MODULES = [
    ]
    sys.modules.update((mod_name, Mock()) for mod_name in MOCK_MODULES)

    html_theme_options = {
        'canonical_url': '',
        'logo_only': False,
        'display_version': True,
        'prev_next_buttons_location': 'bottom',
        # Toc options
        'collapse_navigation': False,
        'sticky_navigation': True,
        'navigation_depth': 4
    }
# if on readthedocs

# -- Project information -----------------------------------------------------

project = 'Stock Analysis Engine'
copyright = '2018, Jay Johnson'
author = 'Jay Johnson'


# The short X.Y version
version = ''
# The full version, including alpha/beta/rc tags
release = '1.0.0'

# -- General configuration ---------------------------------------------------

# If your documentation needs a minimal Sphinx version, state it here.
#
# needs_sphinx = '1.0'

autosummary_generate = True

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.autosummary',
    'sphinx.ext.doctest',
    'sphinx.ext.intersphinx',
    'sphinx.ext.coverage',
    'sphinx.ext.viewcode',
    'celery.contrib.sphinx',
]

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# The suffix(es) of source filenames.
# You can specify multiple suffix as a list of string:
#
source_suffix = ['.rst', '.md']

source_parsers = {
    '.md': CommonMarkParser,
}

# The master toctree document.
master_doc = 'index'

# The language for content autogenerated by Sphinx. Refer to documentation
# for a list of supported languages.
#
# This is also used if you do content translation via gettext catalogs.
# Usually you set "language" from the command line for these cases.
language = None

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path .
exclude_patterns = ['_build']

# The name of the Pygments (syntax highlighting) style to use.
pygments_style = 'sphinx'

# Example configuration for intersphinx: refer to the Python standard library.
intersphinx_mapping = {'python': ('https://docs.python.org/2.7', None)}


# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = os.getenv(
    "DOC_THEME",
    "sphinx_rtd_theme")

# Theme options are theme-specific and customize the look and feel of a theme
# further.  For a list of options available for each theme, see the
# documentation.
#
# html_theme_options = {}

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']

# Custom sidebar templates, must be a dictionary that maps document names
# to template names.
#
# The default sidebars (for documents that don't match any pattern) are
# defined by theme itself.  Builtin themes are using these templates by
# default: ``['localtoc.html', 'relations.html', 'sourcelink.html',
# 'searchbox.html']``.
#
# html_sidebars = {}


# -- Options for HTMLHelp output ---------------------------------------------

# Output file base name for HTML help builder.
htmlhelp_basename = 'StockAnalysisEnginedoc'


# -- Options for LaTeX output ------------------------------------------------

latex_elements = {
    # The paper size ('letterpaper' or 'a4paper').
    #
    # 'papersize': 'letterpaper',

    # The font size ('10pt', '11pt' or '12pt').
    #
    # 'pointsize': '10pt',

    # Additional stuff for the LaTeX preamble.
    #
    # 'preamble': '',

    # Latex figure (float) alignment
    #
    # 'figure_align': 'htbp',
}

# Grouping the document tree into LaTeX files. List of tuples
# (source start file, target name, title,
#  author, documentclass [howto, manual, or own class]).
latex_documents = [
    (master_doc,
     'StockAnalysisEngine.tex',
     'Stock Analysis Engine Documentation',
     'Jay Johnson',
     'manual'),
]


# -- Options for manual page output ------------------------------------------

# One entry per manual page. List of tuples
# (source start file, name, description, authors, manual section).
man_pages = [
    (master_doc, 'stockanalysisengine', 'Stock Analysis Engine Documentation',
     [author], 1)
]


# -- Options for Texinfo output ----------------------------------------------

# Grouping the document tree into Texinfo files. List of tuples
# (source start file, target name, title, author,
#  dir menu entry, description, category)
texinfo_documents = [
    (master_doc,
     'StockAnalysisEngine',
     'Stock Analysis Engine Documentation',
     author,
     'StockAnalysisEngine',
     'One line description of project.',
     'Miscellaneous'),
]


# -- Extension configuration -------------------------------------------------

# -- Options for intersphinx extension ---------------------------------------

# Example configuration for intersphinx: refer to the Python standard library.
intersphinx_mapping = {'https://docs.python.org/': None}

# -- Options for todo extension ----------------------------------------------

# If true, `todo` and `todoList` produce output, else they produce nothing.
todo_include_todos = True
