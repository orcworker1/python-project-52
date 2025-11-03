build:
	./build.sh


render-start:
	export PATH="$$HOME/.local/bin:$$PATH"; uv run bash -lc "python manage.py migrate --noinput && python manage.py collectstatic --noinput && exec gunicorn task_manager.wsgi:application --bind 0.0.0.0:$$PORT --workers $${WEB_CONCURRENCY:-2}"


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

