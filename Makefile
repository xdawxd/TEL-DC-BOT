### Poetry commands ###

poetry-install:
	poetry install

poetry-update:
	poetry update

### Linter ###

lint:
	black . && isort . && flake8
