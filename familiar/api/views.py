from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from familiar.models import *
from familiar.api.serializers import *


class familiarViewSet(ModelViewSet):
    permission_classes = [IsAuthenticated]
    serializer_class = familiarSerializer
    queryset = Familiar.objects.all()