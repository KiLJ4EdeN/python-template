# python-template
python project template


## Installation
for pylance to work with poetry
```bash
poetry config virtualenvs.in-project true
```
```bash
poetry install
```


## Build dist
```bash
poetry build
```

## pytest
```bash
poetry run pytest
```

## flake8
```bash
poetry run flake8
```

## black
```bash
poetry run black python_template/app.py
```

## pre-commit
```bash
poetry run pre-commit run --all-files
```


## code cov
```bash
poetry run coverage run -m pytest -s --disable-pytest-warnings && poetry run coverage html
```

## documentation
```bash
# if its the first time
poetry run sphinx-quickstart docs
# modify conf.py accordingly
poetry run sphinx-apidoc -o docs python_template
# for repetitive creation
poetry run sphinx-build -b html docs/ docs/build/html
```


## run app
```bash
poetry run python python_template/app.py
```

refer to:


localhost:5000

localhost:5000/cov/ for code coverage report
localhost:5000/docs/ for documentation
