build:
	./build.sh

render-start:
	gunicorn task_manager.wsgi


install:
	uv sync


dev:
	python manage.py runserver
