"""
WSGI config for 22 project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.2/howto/deployment/wsgi/
"""

import os
from dotenv import load_dotenv
from django.core.wsgi import get_wsgi_application
import rollbar

load_dotenv()

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'task_manager.settings')

rollbar.init(
    os.environ.get('rollbar_access_token'),
    environment='development' if os.environ.get('DEBUG', 'False').lower() == 'true' else 'production',
)

application = get_wsgi_application()