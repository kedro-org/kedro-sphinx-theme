import glob
import shutil  # Import shutil for high-level file operations
import subprocess
import zipfile

import pytest


# Define a fixture for setup and cleanup
@pytest.fixture
def cleanup():
    # Setup can be done here if needed
    yield  # This yields control to the test function
    # Cleanup: Remove the wheel_contents directory after the test
    shutil.rmtree("wheel_contents", ignore_errors=True)
    shutil.rmtree("dist", ignore_errors=True)


# Use the fixture in your test by including it as a parameter
def test_built_wheel_contains_expected_files(cleanup):
    # Build the project
    subprocess.run(["uv", "build"], check=True)

    # Find the wheel file
    wheel_files = glob.glob("dist/*.whl")
    assert wheel_files, "No wheel files found in dist/"
    wheel_file = wheel_files[0]

    # Unzip the wheel file using Python's zipfile module
    with zipfile.ZipFile(wheel_file, "r") as zip_ref:
        zip_ref.extractall("wheel_contents")

    # Check for the existence of CSS files in /assets/ folder
    css_files = glob.glob("wheel_contents/kedro_sphinx_theme/assets/styles/*.css")
    assert css_files, "CSS files missing in /assets/"

    # Check for the existence of HTML files and theme.conf in /theme folder
    html_files = glob.glob(
        "wheel_contents/kedro_sphinx_theme/theme/kedro-sphinx-theme/*.html"
    )
    theme_conf_file = glob.glob(
        "wheel_contents/kedro_sphinx_theme/theme/kedro-sphinx-theme/theme.conf"
    )

    # Assert that HTML files and theme.conf exist
    assert html_files, "HTML files missing in /theme/kedro-sphinx-theme/"
    assert theme_conf_file, "theme.conf missing in /theme/kedro-sphinx-theme/"
