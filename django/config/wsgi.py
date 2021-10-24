"""
WSGI config for config project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

# os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')

# check running on docker
if not os.path.exists("/.dockerenv"):
    from dotenv import load_dotenv

    from .settings.base import BASE_DIR

    load_dotenv(os.path.join(str(BASE_DIR), "django.env"))

envstate = os.environ.get("ENV_STATE")
if envstate == "production":
    # settings/production.py
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings.production")
elif envstate == "staging":
    # settings/staging.py
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings.staging")
else:
    # settings/local.py
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings.local")


application = get_wsgi_application()
