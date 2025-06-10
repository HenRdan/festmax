from django.urls import path
from rest_framework.routers import SimpleRouter
from .views import EnderecoViewSet

router = SimpleRouter()
router.register('enderecos', EnderecoViewSet)

urlpatterns = router.urls
