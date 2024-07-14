import os
import sys
sys.path.insert(0, os.path.abspath('../'))
sys.path.insert(0, os.path.abspath('../Funciones_objetivo'))

project = 'Optimización_UX21II070'
author = 'Angel Ortega Martínez'
release = '1.0'

extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.napoleon',
]

source_suffix = '.rst'
master_doc = 'index'

templates_path = ['_templates']
exclude_patterns = []

html_theme = 'alabaster'
html_static_path = ['_static']

def setup(app):
    app.add_css_file('custom.css')

autodoc_default_options = {
    'members': True,
    'undoc-members': True,
    'show-inheritance': True,
    'inherited-members': True,
}

# Orden de los miembros basado en el orden de aparición en el código
autodoc_member_order = 'bysource'