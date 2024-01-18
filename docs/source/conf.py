#파이썬 프로젝트를 문서화하는 sphinx를 사용하는 'Openfootmanager' 프로젝트의 문서를 생성하기 위한 Sphinx의 설정을 정의하는 코드
# Configuration file for the Sphinx documentation builder.
#
# This file only contains a selection of the most football options. For a full
# list see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html
import sphinx

# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
# import os
# import sys
# sys.path.insert(0, os.path.abspath('.'))


# -- Project information -----------------------------------------------------

project = "Openfootmanager"
copyright = "2023, Pedrenrique G. Guimaraes"
author = "Pedrenrique G. Guimaraes"

# The full version, including alpha/beta/rc tags
release = "0.1.0-alpha"


# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    sphinx.ext.viewcode,
]

# Add any paths that contain templates here, relative to this directory.
templates_path = ["_templates"]

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = []


# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = "alabaster"

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ["_static"]
