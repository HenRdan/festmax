from rest_framework import viewsets
from rest_framework.response import Response

from .models import EnderecoModel
from .serializers import EnderecoSerializer


class EnderecoViewSet(viewsets.ModelViewSet):
    """
    ViewSet para gerenciar os endereços
    Permite criar, listar, atualizar e deletar endereços, de acordo com o id
    """
    queryset = EnderecoModel.objects.all().order_by('-id')
    serializer_class = EnderecoSerializer

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)
