# 
# Docs/conf.py
#
import os
import sys
import subprocess

# --------------------------------------------
# Set up
#
def read_version() -> str:
    """ 
    Get package version from version.txt file
    """
    file = '../../version.txt'
    if os.path.exists(file):
        with open(file, 'r') as fob:
            proj_vers = fob.readlines()[0]
    else:
        proj_vers = '0.1.0-unknown'
    return proj_vers

docs_root = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.abspath("../../"))
#abs_lib_path = os.path.abspath(os.path.join(docs_root, 'lib'))

# --------------------------------------------
# project
# 
project = "cidrtools"
author = 'Gene C'
latex_engine = 'xelatex'

release = read_version()

extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.imgconverter',
    "hawkmoth",                  # Core Hawkmoth C-Autodoc engine
]

primary_domain = 'c'
hawkmoth_clang_c = [
    "-std=c23",
    "-Ilib",
]

# Tell Sphinx's code highlighter not to emit visible/literal unicode whitespace symbols
# sphinx = baseline, tango = corp color, friendly - brighter, colorful - more so
# Options: sphinx, friendly, tango
pygments_style = 'sphinx'

latex_elements = {
    'papersize': 'letterpaper',
    'pointsize': '10pt',

    'preamble': r'''
        \usepackage{microtype}
        \usepackage{parskip}
        \usepackage{needspace}
        \usepackage{fontspec}

        \usepackage{newunicodechar}
        \newunicodechar{␣}{\textvisiblespace}
        \tracinglostchars=0

        \makeatletter
        \renewcommand{\subsection}[1]{\par\bigskip\needspace{14\baselineskip}\textbf{#1}}
        %\renewcommand{\subsection}{\par\bigskip\needspace{14\baselineskip}}
        \makeatother

        ''',

    'fontpkg': r'''
        \setmainfont{Fira Sans}           % Ultra-modern geometric sans font
        \setsansfont{Fira Sans}
        \setmonofont{Fira Mono}[ Scale=0.9] % Premium look for C function signatures
    ''',

}

# Grouping the document tree into a single LaTeX document manual volume.
# Tuple structure: (source start file, target name, title, author, documentclass)
latex_documents = [
    (
        'index',
        'lockmgr.tex',
        'lockmgr API Reference',
        'Gene C',
        'manual'
    ),
]
