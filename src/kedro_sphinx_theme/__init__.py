"""Sphinx theme for the Kedro ecosystem."""

from __future__ import annotations

import os
from pathlib import Path

from sphinx.application import Sphinx

__version__ = "2024.10.2"

THEME_PATH = (Path(__file__).parent / "theme" / "kedro-sphinx-theme").resolve()


def env_override(default_appid: str) -> str:
    """Override Heap ID based on the build version."""
    build_version = os.getenv("READTHEDOCS_VERSION")

    if build_version == "latest":
        return os.environ["HEAP_APPID_QA"]
    if build_version == "stable":
        return os.environ["HEAP_APPID_PROD"]

    return default_appid  # default to Development for local builds


def _add_jinja_filters(app: Sphinx) -> None:
    # https://github.com/crate/crate/issues/10833
    from sphinx.builders.latex import LaTeXBuilder
    from sphinx.builders.linkcheck import CheckExternalLinksBuilder

    # LaTeXBuilder is used in the PDF docs build,
    # and it doesn't have attribute 'templates'
    if not (isinstance(app.builder, (LaTeXBuilder, CheckExternalLinksBuilder))):
        app.builder.templates.environment.filters["env_override"] = env_override


def _override_permalinks_icon(app: Sphinx) -> None:
    # https://github.com/readthedocs/sphinx_rtd_theme/issues/98#issuecomment-1503211439
    app.config.html_permalinks_icon = "¶"  # type: ignore


def setup(app: Sphinx) -> None:
    """Register theme."""
    app.add_html_theme("kedro-sphinx-theme", THEME_PATH.as_posix())

    app.connect("builder-inited", _add_jinja_filters)
    app.connect("builder-inited", _override_permalinks_icon)
