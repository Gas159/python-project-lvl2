install:
	poetry install
build:
	poetry build
publish:
	poetry publish --dry-run
patch:
	python3 -m pip install --user --force-reinstall dist/*.whl
patch1:
	python3 -m pip install --user dist/*.whl
lint:
	poetry run flake8 gendiff
test:
	poetry run pytest -v
test_cov:
	poetry run pytest --cov=gendiff


fast-check:
	poetry install
	poetry build
	python -m pip install --user --force-reinstall dist/*.whl
	poetry run flake8 gendiff
	poetry run pytest -s
	poetry run pytest --cov=gendiff

fast-check1:
	echo "\n\n ! Build process...\n"
	make build
	echo "\n\n\n ! Package-force-reinstall process...\n"
	make patch
	echo "\n\n\n ! Lint checkup process...\n"
	make lint
	echo "\n\n\n ! Test checkup process...\n"
	make test