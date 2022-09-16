# python-template
python project template


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


## code cov
```bash
make create-cov
```

## documentation
```bash
make create-doc
```


## run app
```bash
make start
```

refer to:


localhost:5000

localhost:5000/cov/ for code coverage report

localhost:5000/docs/ for documentation
