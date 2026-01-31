from rest_framework import viewsets, permissions
from django.contrib.auth.models import User
from .models import Servicio, Cita, Pedido
from .serializers import ServicioSerializer, CitaSerializer, UserSerializer
from rest_framework.decorators import action
from rest_framework.response import Response

# ViewSet de Usuarios (Registro y Listado)
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    # Por ahora permitimos que cualquiera se registre (AllowAny)
    permission_classes = [permissions.AllowAny]

# ViewSet de Servicios
class ServicioViewSet(viewsets.ModelViewSet):
    queryset = Servicio.objects.all()
    serializer_class = ServicioSerializer

# ViewSet de Citas
class CitaViewSet(viewsets.ModelViewSet):
    queryset = Cita.objects.all()
    serializer_class = CitaSerializer

    @action(detail=False, methods=['get'])
    def ocupadas(self, request):
        fecha = request.query_params.get('fecha') # Ejemplo: /api/citas/ocupadas/?fecha=2026-02-15
        if fecha:
            citas = Cita.objects.filter(fecha_hora__date=fecha)
            horas_ocupadas = [c.fecha_hora.strftime('%H:%M') for c in citas]
            return Response(horas_ocupadas)
        return Response({"error": "Debes proporcionar una fecha"}, status=400)

    