import os
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

# SEGURIDAD: Permite que Vercel sirva tu app
ALLOWED_HOSTS = ['*']

# APPS: Verifica que solo esté una vez 'corsheaders'
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

# MIDDLEWARE: CorsMiddleware debe ir arriba
MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

# BASE DE DATOS: Asegúrate de que use BASE_DIR
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# ARCHIVOS ESTÁTICOS: Necesario para el panel de Admin en la nube
STATIC_URL = 'static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

CORS_ALLOW_ALL_ORIGINS = True