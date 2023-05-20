from rest_framework import serializers
from familiar.models import *


class familiarSerializer(serializers.ModelSerializer):
    class Meta:
        model = Familiar
        fields = '__all__'