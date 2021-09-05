lint:
	poetry run isort --diff --check-only --settings-path pyproject.toml ./
	poetry run black --diff --check --config pyproject.toml ./
	poetry run darglint --verbosity 2 pdf_read tests
	poetry run pre-commit install && poetry run pre-commit run -a -v

safety:
	poetry check
	poetry run safety check --full-report

deps:
	poetry install

test: deps
	poetry run pytest -vvv


run: deps
	poetry run python __main__.py
