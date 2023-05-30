from rest_framework import serializers
from paciente.models import *


class PacienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Paciente
        fields = '__all__'

class PacientePadrinoSerializer(serializers.ModelSerializer):
    class Meta:
        model = padrino
        fields = '__all__'

class PacienteFamiliarSerializer(serializers.ModelSerializer):
    class Meta:
        model = familiar
        fields = '__all__'