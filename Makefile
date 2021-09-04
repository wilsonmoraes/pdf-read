lint:
	poetry run pre-commit install && poetry run pre-commit run -a -v

deps:
	poetry install

test: deps
	poetry run pytest -vvv

run: deps
	poetry run python __main__.py
