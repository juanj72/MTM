from rest_framework.routers import DefaultRouter
from dream.api.views import *


router_dream=DefaultRouter()

router_dream.register(prefix='Sueños',basename='Sueño',viewset=ModelDreamViewSet)
router_dream.register(prefix='Tipos',basename='Tipo',viewset=ModelTipoViewSet)
