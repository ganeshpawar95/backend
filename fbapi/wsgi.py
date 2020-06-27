"""
WSGI config for fbapi project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/2.2/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application
import sys

sys.path.append('/var/www/djangomac')
sys.path.append('/var/www/djangomac/fbapi')

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'fbapi.settings')

application = get_wsgi_application()
