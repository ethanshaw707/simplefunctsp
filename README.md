# Simple Functions for Senior Project (SP) practice `simplefunctsp`

This practice package repository is for our class to go through the process of;

1. Creating a function
2. Building documentation for the function
3. Submitting a pull request


###  Python Installation

We will use [uv](https://docs.astral.sh/uv/guides/install-python/)

### Installing uv and python

1. Follow [uv's installation scripts](https://docs.astral.sh/uv/getting-started/installation/#installation-methods)
2. Now run `uv python install --default`.
  - You can see your available Python versions with `uv python list`.
  - If you want a specific version of Python, you can run `uv python install 3.12,` for example.
  - You can upgrade to the latest supported patch release for each version with `uv python upgrade`.

## mkdocs-material

1. mkdocs-material with `uv pip install mkdocs-material --system`
2. [Guide on mkdocs-material](https://www.youtube.com/watch?v=xlABhbnNrfI) and his [companion website for this video](https://jameswillett.dev/getting-started-with-material-for-mkdocs/)
 - However, we are using `uv` and will use `uv run mkdocs new .` instead of `mkdocs new .`

## Handy `uv` commands 

### Installing the package in development into the Python environment 

The `--editable` allows us to create an installation that points back to your project directory instead of copying the code into site-packages. With this, we can now edit the source files, and the installed package in the environment is automatically updated.

```bash
uv sync --editable
```

With this run you can now run the following command to evaluate the package within the package specific Python that has the package installed

```bash
uv run python
```

### Examining the Documentation

Because of the `WATCH:` options in the `mkdocs.yml` we can now make edits to our function details and see the edits in real time with

```bash
uv run mkdocs serve
```

After you have the docs as you want you will need to build them to the `docs` folder for Github.

```bash
uv run mkdocs build
```

### Install a package from Github repository

```bash
uv pip install "git+https://github.com/byuirpytooling/simplefunctsp.git@main"
```

## Directory structure

```bash
pypackage_template
├── .readthedocs.yml           ┐
├── CHANGELOG.md               │
├── CONDUCT.md                 │
├── CONTRIBUTING.md            │
├── docs                       │
│   ├── changelog.md           │
│   ├── conduct.md             │
│   ├── conf.py                │ 
│   ├── contributing.md        │ Package documentation
│   ├── example.ipynb          │
│   ├── index.md               │
│   ├── make.bat               │
│   ├── Makefile               │
│   └── requirements.txt       │
├── LICENSE                    │
├── README.md                  ┘
├── pyproject.toml             ┐ 
├── src                        │
│   └── pypackage_template     │ Package source code, metadata,
│       ├── __init__.py        │ and build instructions 
│       └── pycounts.py        ┘
└── tests                      ┐
    └── test_pycounts.py       ┘ Package tests
```
