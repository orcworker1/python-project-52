build:
	./build.sh


render-start:
	uv run gunicorn task_manager.wsgi


install:
	uv sync


start:
	uv run python manage.py runserver

migrate:
	python manage.py migrate

