from rest_framework import serializers
from dream.models import *


class dreamSerializer(serializers.ModelSerializer):
    class Meta:
        model = Dream
        fields = '__all__'


class tipoSerializer(serializers.ModelSerializer):
    class Meta :
        model = Tipo
        fields = '__all__'