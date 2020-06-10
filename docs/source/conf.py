# Configuration file for the Sphinx documentation builder.
#
# This file only contains a selection of the most common options. For a full
# list see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
import os
import sys

sys.path.insert(0, os.path.abspath('../../.'))
sys.path.insert(0, os.path.abspath('../../rec_to_nwb'))
sys.path.insert(0, os.path.abspath('../../rec_to_nwb/processing'))
sys.path.insert(0, os.path.abspath('../../rec_to_nwb/processing/exceptions'))
sys.path.insert(0, os.path.abspath('../../rec_to_nwb/processing/header'))
sys.path.insert(0, os.path.abspath('../../rec_to_nwb/processing/metadata'))
sys.path.insert(0, os.path.abspath('../../rec_to_nwb/processing/nwb'))
sys.path.insert(0, os.path.abspath('../../rec_to_nwb/processing/time'))
sys.path.insert(0, os.path.abspath('../../rec_to_nwb/processing/tools'))

# -- Project information -----------------------------------------------------
# from setup import version

project = 'rec_to_nwb'
copyright = '2020, Novela'
author = 'Novela'

# The full version, including alpha/beta/rc tags
release = "0.1.012"

# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    'sphinx.ext.autodoc',
    'recommonmark',
    'autoapi.extension',
    'sphinx.ext.napoleon'
]

autoapi_add_toctree_entry = False
autoapi_type = 'python'
autoapi_dirs = ['../../rec_to_nwb/processing']
add_module_names = False


# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = []


# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = 'sphinx_rtd_theme'

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']

