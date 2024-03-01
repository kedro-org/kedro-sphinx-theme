"""Sphinx theme for the Kedro ecosystem."""

from __future__ import annotations

from pathlib import Path

from sphinx.application import Sphinx

__version__ = "2024.3.0"

THEME_PATH = (Path(__file__).parent / "theme" / "kedro-sphinx-theme").resolve()


def setup(app: Sphinx):
    """Register theme."""
    app.add_html_theme("kedro-sphinx-theme", THEME_PATH)
