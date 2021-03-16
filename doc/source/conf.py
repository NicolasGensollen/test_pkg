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
sys.path.insert(0, os.path.abspath('../..'))
sys.setrecursionlimit(1500)


# -- Project information -----------------------------------------------------

project = 'Toy_pkg'
copyright = '2021, Nicolas Gensollen'
author = 'Nicolas Gensollen'

# The full version, including alpha/beta/rc tags
import toy_pkg
release = toy_pkg.__version__

# If extensions (or modules to document with autodoc) are in another
# directory, add these directories to sys.path here. If the directory
# is relative to the documentation root, use os.path.abspath to make it
# absolute, like shown here.
sys.path.insert(0, os.path.abspath('sphinxext'))
import sphinx_gallery


# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = ['sphinx_gallery.gen_gallery',
              'sphinx.ext.autodoc',
              'sphinx.ext.autosummary',
              'sphinx.ext.imgmath',
              'sphinx.ext.intersphinx',
              'sphinx.ext.napoleon',
              ]

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# The suffix of source filenames.
source_suffix = '.rst'

# Generate the plots for the gallery
plot_gallery = 'True'

# The master toctree document.
master_doc = 'index'

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = []

# List of directories, relative to source directory, that shouldn't be
# searched for source files.
exclude_trees = ['_build', 'templates', 'includes']

# If true, '()' will be appended to :func: etc. cross-reference text.
add_function_parentheses = False

# The name of the Pygments (syntax highlighting) style to use.
pygments_style = 'sphinx'

# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = 'pydata_sphinx_theme'

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']

# The name for this set of Sphinx documents.  If None, it defaults to
# "<project> v<release> documentation".
html_title = "Useless toy package"

# A shorter title for the navigation bar.  Default is the same as html_title.
html_short_title = 'toy_pkg'

_python_doc_base = 'https://docs.python.org/3.6'

# Example configuration for intersphinx: refer to the Python standard library.
intersphinx_mapping = {
    'python': (_python_doc_base, None),
    'numpy': ('https://docs.scipy.org/doc/numpy', None),
}

extlinks = {
    'simple': (_python_doc_base + '/reference/simple_stmts.html#%s', ''),
    'compound': (_python_doc_base + '/reference/compound_stmts.html#%s', ''),
}

sphinx_gallery_conf = {
    'doc_module': 'toy_pkg',
    'backreferences_dir': os.path.join('modules', 'generated'),
    'reference_url': {'toy_pkg': None},
    'junit': '../../test-results/sphinx-gallery/junit.xml',
    'examples_dirs': '../../examples',
    'gallery_dirs': 'auto_examples',
    # Ignore the function signature leftover by joblib
    'ignore_pattern': 'func_code\.py',
    'binder': {
        'org': 'toy_pkg',
        'repo': 'toy_pkg.github.io',
        'binderhub_url': 'https://mybinder.org',
        'branch': 'main',
        'dependencies': ['../../requirements-build-docs.txt',
                         '../binder/requirements.txt'],
        'notebooks_dir': 'examples'
    }
}


