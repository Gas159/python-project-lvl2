install:
	poetry install
build:
	poetry build
patch:
	python3 -m pip install --user --force-reinstall dist/*.whl
lint:
	poetry run flake8 gendiff