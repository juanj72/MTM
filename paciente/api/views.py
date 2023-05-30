from rest_framework.viewsets import ModelViewSet
from rest_framework.views import APIView
from paciente.models import *
from paciente.api.serializers import PacienteSerializer
from paciente.api.serializers import PacientePadrinoSerializer
from paciente.api.serializers import PacienteFamiliarSerializer
from rest_framework.permissions import IsAuthenticated

class PacienteApiViewset(ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = Paciente.objects.all()
    serializer_class = PacienteSerializer
    # permission_classes = [IsAuthenticated]

class PacientePadrinoApiViewset(ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = padrino.objects.all()
    serializer_class = PacientePadrinoSerializer
    # permission_classes = [IsAuthenticated]

class PacienteFamiliarApiViewset(ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = familiar.objects.all()
    serializer_class = PacienteFamiliarSerializer
    # permission_classes = [IsAuthenticated]