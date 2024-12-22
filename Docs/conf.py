# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

#import sys
#from pathlib import Path
#sys.path.insert(0, str(Path('..', 'src').resolve()))

project = "lockmgr"
copyright = '2023-present, Gene C'
author = 'Gene C'
release = '1.5.2'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

#extensions = ['myst_parser']
#         'sphinx.ext.autodoc',
extensions = ['sphinx.ext.autodoc', 'autoapi.extension']

autoapi_dirs = ['../src/lockmgr']
autoapi_options = ['members']
#autodoc_typehints = 'description'

templates_path = ['_templates']
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']



# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'alabaster'
html_static_path = ['_static']
