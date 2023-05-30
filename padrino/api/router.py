from rest_framework.routers import DefaultRouter
from padrino.api.views import PadrinoViewSet

router_padrino = DefaultRouter()

router_padrino.register(prefix='padrino',basename='padrinos',viewset=PadrinoViewSet)
