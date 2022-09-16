install:
	poetry install
build:
	poetry build
pre-commit:
	poetry run pre-commit run --all-files
fmt-black:
	poetry run black python_template/ tests/
lint-black:
	poetry run black --check python_template/ tests/
lint-flake8:
	poetry run flake8 python_template/ tests/
lint-mypy:
	poetry run mypy python_template/ tests/
lint: lint-black lint-flake8 lint-mypy
create-cov:
	poetry run coverage run -m pytest -s --disable-pytest-warnings && poetry run coverage html
create-doc:
	poetry run sphinx-build -b html docs/ docs/build/html
start:
	poetry run python python_template/app.py
test:
	poetry run pytest
.PHONY: install build pre-commit fmt-black lint-black lint-flake8 lint-mypy lint test
