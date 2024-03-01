"""Sphinx theme for the Kedro ecosystem."""

from __future__ import annotations

import os
import typing as t

if t.TYPE_CHECKING:
    from sphinx.application import Sphinx

__version__ = "2024.3.0"


def setup(app: Sphinx):
    """Register theme."""
    app.add_html_theme("kedro-sphinx-theme", os.path.abspath(os.path.dirname(__file__)))
