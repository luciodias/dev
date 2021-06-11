"""
WSGI config for hello project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/howto/deployment/wsgi/
"""

import os, sys

# edit your username below
sys.path.append("/home/luciod/public_html/hello")

from django.core.wsgi import get_wsgi_application

os.environ['DJANGO_SETTINGS_MODULE'] = 'hello.settings'

application = get_wsgi_application()