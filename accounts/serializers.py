from rest_framework import serializers
from core.serializers import BaseUserSerializer
from .models import Cliente, Fornecedor, Funcionario


class ClienteSerializer(BaseUserSerializer):
    class Meta:
        model = Cliente
        fields = [
            'id',
            'username',
            'email',
            'first_name',
            'last_name',
            'password',
            'cpf',
            'telefone',
            'endereco',
            'data_nascimento',
            'sexo',
            'tipo_usuario',
        ]
    extra_kwargs = {
        'username': {'required': True, 'write_only': True},
        'cpf': {'required': True, 'write_only': True},
        'password': {'required': True, 'write_only': True},
        'email': {'required': True, 'write_only': True},
        'first_name': {'required': True},
        'last_name': {'required': True},
        'tipo_usuario': {'required': True},
    }


class FornecedorSerializer(BaseUserSerializer):
    class Meta:
        model = Fornecedor
        fields = [
            'id',
            'username',
            'email',
            'first_name',
            'last_name',
            'password',
            'cnpj',
            'telefone',
            'endereco',
            'tipo_usuario',
        ]
    extra_kwargs = {
        'username': {'required': True, 'write_only': True},
        'cnpj': {'required': True, 'write_only': True},
        'password': {'required': True, 'write_only': True},
        'email': {'required': True, 'write_only': True},
        'first_name': {'required': True},
        'last_name': {'required': True},
        'tipo_usuario': {'required': True},
    }


class FuncionarioSerializer(BaseUserSerializer):
    class Meta:
        model = Funcionario
        fields = [
            'id',
            'username',
            'email',
            'first_name',
            'last_name',
            'password',
            'cpf',
            'telefone',
            'endereco',
            'tipo_usuario',
        ]
    extra_kwargs = {
        'username': {'required': True, 'write_only': True},
        'cpf': {'required': True, 'write_only': True},
        'password': {'required': True, 'write_only': True},
        'email': {'required': True, 'write_only': True},
        'first_name': {'required': True},
        'last_name': {'required': True},
        'tipo_usuario': {'required': True},
    }
