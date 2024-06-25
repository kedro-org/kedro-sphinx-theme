"""Sphinx configuration."""

from importlib.metadata import metadata

# -- Project information

_metadata = metadata("kedro-sphinx-theme")

project = _metadata["Name"]
author = _metadata["Author-email"].split("<", 1)[0].strip()
copyright = f"2024, {author}"

version = _metadata["Version"]
release = ".".join(version.split(".")[:2])


# -- General configuration

extensions = [
    "myst_parser",
    "sphinx_copybutton",
]

favicons = [
    "https://kedro.org/images/favicon.ico",
]

# Add the relative path from your conf.py file to the assets directory to html_static_path
html_static_path = ['_static']

# Include custom.js in the HTML output
html_js_files = [
    'custom.js',
]

templates_path = ["_templates"]

exclude_patterns = [
    "Thumbs.db",
    ".DS_Store",
    ".ipynb_checkpoints",
]

# -- Options for HTML output

html_theme = "kedro-sphinx-theme"
html_static_path = ["_static"]
