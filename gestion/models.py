from django.db import models
from django.contrib.auth.models import User

# --- 1. EXTENSIÓN DEL USUARIO (PERFIL) ---
# Se coloca aquí arriba para que esté disponible para los demás
class Perfil(models.Model):
    METODOS_PAGO = [
        ('EFECTIVO', 'Efectivo'),
        ('TRANSFERENCIA', 'Transferencia'),
        ('PAGO_MOVIL', 'Pago Móvil / Zelle'),
        ('TARJETA', 'Tarjeta'),
    ]

    usuario = models.OneToOneField(User, on_delete=models.CASCADE, related_name='perfil')
    cedula = models.CharField(max_length=20, unique=True)
    telefono = models.CharField(max_length=20)
    direccion = models.CharField(max_length=255, blank=True, null=True)
    metodo_pago_preferido = models.CharField(
        max_length=20, 
        choices=METODOS_PAGO, 
        default='EFECTIVO',
        blank=True,  # Permite que el formulario lo deje vacío
        null=True    # Permite que la base de datos guarde un valor nulo
    )

    def __str__(self):
        return f"{self.usuario.username} - {self.cedula}"

# --- 2. SERVICIOS ---
class Servicio(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField(blank=True, null=True)
    precio = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.nombre

# --- 3. CITAS ---
class Cita(models.Model):
    ESTADOS = [
        ('PENDIENTE', 'Pendiente'),
        ('CONFIRMADA', 'Confirmada'),
        ('COMPLETADA', 'Completada'),
        ('CANCELADA', 'Cancelada'),
    ]
    
    paciente = models.ForeignKey(User, on_delete=models.CASCADE, related_name='mis_citas')
    fecha_hora = models.DateTimeField()
    servicios = models.ManyToManyField(Servicio) 
    notas_medicas = models.TextField(blank=True, null=True)
    estado = models.CharField(max_length=20, choices=ESTADOS, default='PENDIENTE')

    def __str__(self):
        return f"Cita {self.id} - {self.paciente.username}"

# --- 4. PEDIDOS ---
class Pedido(models.Model):
    paciente = models.ForeignKey(User, on_delete=models.CASCADE)
    producto = models.CharField(max_length=100)
    cantidad = models.PositiveIntegerField(default=1)
    pagado = models.BooleanField(default=False)
    fecha_creacion = models.DateTimeField(auto_now_add=True)