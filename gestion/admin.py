from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User
from .models import Perfil, Servicio, Cita, Pedido

# Esto hace que el perfil aparezca dentro de la edición del usuario
class PerfilInline(admin.StackedInline):
    model = Perfil
    can_delete = False
    verbose_name_plural = 'Información de Perfil'

# Personalizamos el admin de Usuario
class UserAdmin(BaseUserAdmin):
    inlines = (PerfilInline,)

# Re-registramos el modelo User con el nuevo diseño
admin.site.unregister(User)
admin.site.register(User, UserAdmin)

# Registramos el resto de los modelos para que aparezcan en el menú
admin.site.register(Servicio)
admin.site.register(Cita)
admin.site.register(Pedido)
admin.site.register(Perfil) # También lo registramos solo por si quieres verlo aparte