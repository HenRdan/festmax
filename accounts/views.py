from rest_framework import generics
from rest_framework import status
from rest_framework import viewsets, mixins
from rest_framework.response import Response

from .models import Cliente, Fornecedor, Funcionario
from .serializers import ClienteSerializer, FornecedorSerializer, FuncionarioSerializer


class ClienteViewSet(viewsets.ModelViewSet):
    """
    ViewSet para gerenciar os clientes
    Permite criar, listar, atualizar e deletar clientes, de acordo com o id
    """
    queryset = Cliente.objects.all().order_by('-id')
    serializer_class = ClienteSerializer

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)


class FornecedorViewSet(viewsets.ModelViewSet):
    """
    ViewSet para gerenciar os fornecedores
    Permite criar, listar, atualizar e deletar fornecedores, de acordo com o id
    """
    queryset = Fornecedor.objects.all().order_by('-id')
    serializer_class = FornecedorSerializer

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)


class FuncionarioViewSet(viewsets.ModelViewSet):
    """
    ViewSet para gerenciar os funcionarios
    Permite criar, listar, atualizar e deletar funcionarios, de acordo com o id
    """
    queryset = Funcionario.objects.all().order_by('-id')
    serializer_class = FuncionarioSerializer

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)
