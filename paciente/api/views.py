from rest_framework.viewsets import ModelViewSet
from rest_framework.views import APIView
from paciente.models import *
from paciente.api.serializers import PacienteSerializer,DreamSeralizer
from rest_framework.permissions import IsAuthenticated

class PacienteApiViewset(ModelViewSet):
    queryset = Paciente.objects.all()
    serializer_class = PacienteSerializer
    # permission_classes = [IsAuthenticated]

class DreamApiViewset(ModelViewSet):
    queryset = Dream.objects.all()
    serializer_class = DreamSeralizer