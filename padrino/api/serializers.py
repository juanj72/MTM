from rest_framework import serializers
from padrino.models import *



class PadrinoSerializer(serializers.ModelSerializer):
    class Meta :
        model = Padrino
        fields = '__all__'

        