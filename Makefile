build:
	./build.sh


render-start:
	uv run gunicorn task_manager.wsgi


install:
	uv sync


start:
	uv run python manage.py runserver 0.0.0.0:8000
