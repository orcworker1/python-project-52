build:
	./build.sh


render-start:
	uv run bash -lc


install:
	uv sync


start:
	uv run python manage.py runserver

migrate:
	python manage.py migrate

shell:
	python manage.py shell

test:
	uv run python manage.py test

