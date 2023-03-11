# file:Makefile

brain-games:
	poetry run brain-games

brain-even:
	poetry run brain-even

brain-calc:
	poetry run brain-calc

lint:
	poetry run flake8 brain_games

build:
	poetry build

publish:
	poetry publish --dry-run

install:
	poetry install

package-install:
	python3 -m pip install --user dist/*.whl

