from django.urls import path

from rest_framework.routers import SimpleRouter
from .views import ClienteViewSet, FornecedorViewSet, FuncionarioViewSet

router = SimpleRouter()
router.register('clientes', ClienteViewSet)
router.register('fornecedores', FornecedorViewSet)
router.register('funcionarios', FuncionarioViewSet)

urlpatterns = router.urls
