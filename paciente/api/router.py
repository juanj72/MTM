from rest_framework.routers import DefaultRouter
from paciente.api.views import PacienteApiViewset
from paciente.api.views import PacientePadrinoApiViewset
from paciente.api.views import PacienteFamiliarApiViewset

paciente_router = DefaultRouter()

paciente_router.register(prefix='paciente',basename='pacientes',viewset=PacienteApiViewset)

paciente_router.register(prefix='paciente_padrino',basename='paciente_padrino',viewset=PacientePadrinoApiViewset)

paciente_router.register(prefix='paciente_familiar',basename='paciente_familiar',viewset=PacienteFamiliarApiViewset)
