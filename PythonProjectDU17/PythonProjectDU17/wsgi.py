import os
from django.core.wsgi import get_wsgi_application

# Nastavíme výchozí hodnotu pro DJANGO_SETTINGS_MODULE
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'PythonProjectDU17.settings')

# Získáme WSGI aplikaci
application = get_wsgi_application()
