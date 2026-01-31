import os
from pathlib import Path

# 1. Rutas del proyecto
BASE_DIR = Path(__file__).resolve().parent.parent

# 2. Configuración Crítica (¡Esto es lo que faltaba!)
# La SECRET_KEY es obligatoria para que Django arranque.
SECRET_KEY = 'django-insecure-v-@7_!*#$re(01-u!f8d(_h(q%dk00)-2br1nnpz_03_key'
DEBUG = True 
ALLOWED_HOSTS = ['*']

# 3. Direccionamiento (Indispensable para Vercel)
# Sin esto, Django no sabe qué URLs cargar.
ROOT_URLCONF = 'backend_citas.urls'
WSGI_APPLICATION = 'backend_citas.wsgi.application'

# 4. Definición de Aplicaciones
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',
    'corsheaders',
    'gestion',
]

# 5. Capas de Seguridad y Procesamiento
MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware', # Siempre debe ir primero
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

# 6. Base de Datos (SQLite para pruebas en Vercel)
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# 7. Archivos Estáticos (Necesario para ver el Admin de Django)
STATIC_URL = 'static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

# 8. Permisos de CORS para tu Frontend
CORS_ALLOW_ALL_ORIGINS = True