# python-template
python project template

[![awesome](https://cdn.rawgit.com/sindresorhus/awesome/d7305f38d29fed78fa85652e3a63e154dd8e8829/media/badge.svg)](https://github.com/KiLJ4EdeN/)
[![License](https://img.shields.io/github/license/KiLJ4EdeN/python-template)](https://img.shields.io/github/license/KiLJ4EdeN/python-template) [![Version](https://img.shields.io/github/v/tag/KiLJ4EdeN/python-template)](https://img.shields.io/github/v/tag/KiLJ4EdeN/python-template) [![Code size](https://img.shields.io/github/languages/code-size/KiLJ4EdeN/python-template)](https://img.shields.io/github/languages/code-size/KiLJ4EdeN/python-template) [![Repo size](https://img.shields.io/github/repo-size/KiLJ4EdeN/python-template)](https://img.shields.io/github/repo-size/KiLJ4EdeN/python-template) [![Issue open](https://img.shields.io/github/issues/KiLJ4EdeN/python-template)](https://img.shields.io/github/issues/KiLJ4EdeN/python-template)
![Issue closed](https://img.shields.io/github/issues-closed/KiLJ4EdeN/python-template)

## install
for pylance to work with poetry
```bash
poetry config virtualenvs.in-project true
```
```bash
make install
```

## dist
```bash
make build
```

## bump
```bash
# or major or minor or patch
make bump-prerelease
```

## pytest
```bash
make test
```

## flake8
```bash
make lint-flake8
```

## black
```bash
make lint-black
```

## mypy
```bash
make lint-mypy
```

## pre-commit
```bash
make pre-commit
```

## documentation
```bash
make create-doc
```

## code cov
```bash
make create-cov
```

## run app
```bash
make start
```

refer to:


localhost:5000

localhost:5000/cov/ for code coverage report

localhost:5000/docs/ for documentation

## docker
```bash
make docker-build
make docker-up
make docker-down
```

## structure
```
├── python_template
│   ├── app.py
│   └── __init__.py
├── tests
│   ├── __init__.py
│   ├── test_app.py
│   └── test_version.py
├── LICENSE
├── Makefile
├── MANIFEST.in
├── mkdocs.yml
├── poetry.lock
├── pyproject.toml
├── README.md
├── requirements.txt
└── docs
    ├── explanation.md
    ├── how-to-guides.md
    ├── index.md
    ├── reference.md
    └── tutorials.md
```
