from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Servicio, Cita, Pedido, Perfil

class PerfilSerializer(serializers.ModelSerializer):
    # Hacemos que el método de pago no sea obligatorio al registrarse
    metodo_pago_preferido = serializers.CharField(required=False, allow_blank=True, allow_null=True)

    class Meta:
        model = Perfil
        fields = ['cedula', 'telefono', 'direccion', 'metodo_pago_preferido']

class UserSerializer(serializers.ModelSerializer):
    perfil = PerfilSerializer()

    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'password', 'perfil']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        perfil_data = validated_data.pop('perfil')
        user = User.objects.create_user(**validated_data)
        Perfil.objects.create(usuario=user, **perfil_data)
        return user

class ServicioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Servicio
        fields = '__all__'

class CitaSerializer(serializers.ModelSerializer):
    paciente_nombre = serializers.ReadOnlyField(source='paciente.username')
    total_pagar = serializers.SerializerMethodField()

    class Meta:
        model = Cita
        fields = '__all__'

    def get_total_pagar(self, obj):
        return sum(servicio.precio for servicio in obj.servicios.all())

    def validate(self, data):
        fecha_solicitada = data.get('fecha_hora')
        
        # Validación de duplicados
        existe = Cita.objects.filter(fecha_hora=fecha_solicitada).exists()
        if existe:
            raise serializers.ValidationError(
                {"fecha_hora": "Este horario ya está reservado por otro paciente."}
            )
        
        # Validación de horario de oficina (8am a 6pm)
        if fecha_solicitada.hour < 8 or fecha_solicitada.hour >= 18:
            raise serializers.ValidationError(
                {"fecha_hora": "El consultorio solo atiende de 08:00 AM a 06:00 PM."}
            )

        return data