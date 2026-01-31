import os
from django.core.wsgi import get_wsgi_application

# Asegúrate de que el nombre coincida con tu carpeta de configuración
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'backend_citas.settings')

application = get_wsgi_application()

# Variable necesaria para Vercel
app = application