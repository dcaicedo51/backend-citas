import os
from pathlib import Path

# 1. Rutas del proyecto
BASE_DIR = Path(__file__).resolve().parent.parent

# 2. Configuración Crítica
SECRET_KEY = 'django-insecure-v-@7_!*#$re(01-u!f8d(_h(q%dk00)-2br1nnpz_03_key'
DEBUG = True 
ALLOWED_HOSTS = ['*']

# 3. Direccionamiento (Indispensable para Vercel)
ROOT_URLCONF = 'backend_citas.urls'
WSGI_APPLICATION = 'backend_citas.wsgi.application'

# --- NUEVA SECCIÓN: ARREGLO PARA EL ADMIN ---
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [], 
        'APP_DIRS': True, # Esto es lo que soluciona el error TemplateDoesNotExist
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]
# --------------------------------------------

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
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': '/tmp/db.sqlite3',  # Cambiamos BASE_DIR por /tmp/
    }
}

# 7. Archivos Estáticos
STATIC_URL = 'static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

# 8. Permisos de CORS para tu Frontend
CORS_ALLOW_ALL_ORIGINS = True