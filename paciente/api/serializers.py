from rest_framework import serializers
from paciente.models import *


class PacienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Paciente
        fields = '__all__'

class DreamSeralizer(serializers.ModelSerializer):
    class Meta:
        model = Dream
        fields = '__all__'