# kedro-sphinx-theme

[![Documentation Status](https://readthedocs.org/projects/kedro-sphinx-theme/badge/?version=latest)](https://kedro-sphinx-theme.readthedocs.io/en/latest/?badge=latest)
[![Code style: ruff-format](https://img.shields.io/badge/code%20style-ruff_format-6340ac.svg)](https://github.com/astral-sh/ruff)
[![PyPI](https://img.shields.io/pypi/v/kedro-sphinx-theme)](https://pypi.org/project/kedro-sphinx-theme)

Sphinx theme for the Kedro ecosystem

## Installation

To install, run

```
(.venv) $ pip install kedro-sphinx-theme
```

## Development

To run style checks:

```
(.venv) $ pip install pre-commit
(.venv) $ pre-commit run -a
```
### Launch a development server locally
This outlines the steps required to run the Kedro-Sphinx-Theme locally on your machine, either with your kedro, kedro-viz or kedro-dataset. 

Before launching a development server, you'd need to have [Python](https://www.python.org/)(>=3.9) installed. We strongly recommend setting up [conda](https://docs.conda.io/en/latest/) to manage your Python versions and virtual environments. You can visit Kedro's [guide to installing conda](https://docs.kedro.org/en/latest/get_started/install.html#create-a-virtual-environment-for-your-kedro-project) for more information.

#### Steps

1. **Clone the Kedro-Sphinx-Theme Repository**
First, you need to get the Kedro-Sphinx-Theme directory on your local machine. Navigate to the directory where you have cloned the repository:

```bash
cd kedro-sphinx-theme
```

Get the location of your local repository and copy the output path for later use:

```bash
pwd
```

2. **Setup the docs build requirement in your repository**
Navigate to the directory where you want to run the documentation locally. This can be within your Kedro, Kedro-Viz, or Kedro-Dataset project:

```bash
cd path/to/your/kedro/or/kedro-viz/or/kedro-dataset
```

Ensure your Python environment is active and ready.Then navigate to the package directory

```bash
cd package
```

Install the documentation dependencies

```bash
pip install ".[docs]"
```

Use the path you copied earlier to install the kedro-sphinx-theme package

```bash
pip install -e "path/to/kedro-sphinx-theme"
```

After installing all the requirements, build the documentation from the root of the repository

```bash
cd to/your/root
```

```bash
sphinx-build -WETa --keep-going -j auto -D language=en -b html -d docs/build/doctrees docs/source docs/build
```

3. **Start a Local HTTP Server**
Finally, navigate to the docs/build directory and start a local HTTP server to view the documentation:

Navigate to the docs/build directory

```bash
cd docs/build
```

Start the server

```bash
python -m http.server
```

Once everything is successfully built and run, you can open the documentation development locally through `http://localhost:your-port`