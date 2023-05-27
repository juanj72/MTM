from rest_framework.viewsets import ModelViewSet
from rest_framework.views import APIView
from paciente.models import *
from paciente.api.serializers import PacienteSerializer
from rest_framework.permissions import IsAuthenticated

class PacienteApiViewset(ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = Paciente.objects.all()
    serializer_class = PacienteSerializer
    # permission_classes = [IsAuthenticated]
