from rest_framework.routers import DefaultRouter
from paciente.api.views import PacienteApiViewset,DreamApiViewset
paciente_router = DefaultRouter()

paciente_router.register(prefix='paciente',basename='pacientes',viewset=PacienteApiViewset)
paciente_router.register(prefix='Sueño',basename='sueños',viewset=DreamApiViewset)