from rest_framework import serializers
from core.serializers import BaseUserSerializer
from .models import Cliente, Fornecedor, Funcionario


class ClienteSerializer(BaseUserSerializer):
    class Meta:
        model = Cliente
        fields = '__all__'


class FornecedorSerializer(BaseUserSerializer):
    class Meta:
        model = Fornecedor
        fields = '__all__'


class FuncionarioSerializer(BaseUserSerializer):
    class Meta:
        model = Funcionario
        fields = '__all__'
