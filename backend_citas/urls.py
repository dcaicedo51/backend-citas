from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from gestion.views import ServicioViewSet, CitaViewSet, UserViewSet

# El Router crea automáticamente las URLs para el CRUD (Crear, Leer, Actualizar, Borrar)
router = DefaultRouter()
router.register(r'usuarios', UserViewSet)
router.register(r'servicios', ServicioViewSet)
router.register(r'citas', CitaViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)), # Todas tus rutas empezarán con /api/
]