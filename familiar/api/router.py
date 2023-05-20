from rest_framework.routers import DefaultRouter
from familiar.api.views import *


router_familiar = DefaultRouter()

router_familiar.register(prefix='Familiar',basename='familiares',viewset=familiarViewSet)