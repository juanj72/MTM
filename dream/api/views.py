from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from dream.models import *
from dream.api.serializers import * 

# Create your views here.


class ModelDreamViewSet(ModelViewSet):
    permission_classes = [IsAuthenticated]
    serializer_class = dreamSerializer
    queryset = Dream.objects.all()


class ModelTipoViewSet(ModelViewSet):
    permission_classes = [IsAuthenticated]
    serializer_class = tipoSerializer
    queryset = Tipo.objects.all()