from rest_framework.viewsets import ModelViewSet
from rest_framework.views import APIView
from padrino.api.serializers import *
from padrino.models import *
from rest_framework.permissions import IsAuthenticated


class PadrinoViewSet(ModelViewSet):
    queryset = Padrino.objects.all()
    serializer_class = PadrinoSerializer