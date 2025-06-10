from django.contrib import admin
from .models import Cliente, Fornecedor, Funcionario


@admin.register(Cliente)
class ClienteAdmin(admin.ModelAdmin):
    list_display = ('id', 'username', 'email', 'first_name', 'last_name', 'cpf',
                    'telefone', 'endereco', 'data_nascimento', 'sexo', 'tipo_usuario')
    list_filter = ('tipo_usuario',)
    search_fields = ('username', 'email', 'first_name',
                     'last_name', 'cpf', 'telefone')
    list_per_page = 10


@admin.register(Fornecedor)
class FornecedorAdmin(admin.ModelAdmin):
    list_display = ('id', 'username', 'email', 'first_name', 'last_name', 'cnpj',
                    'telefone', 'endereco', 'tipo_usuario')
    list_filter = ('tipo_usuario',)
    search_fields = ('username', 'email', 'first_name',
                     'last_name', 'cnpj', 'telefone')
    list_per_page = 10


@admin.register(Funcionario)
class FuncionarioAdmin(admin.ModelAdmin):
    list_display = ('id', 'username', 'email', 'first_name', 'last_name', 'cpf',
                    'telefone', 'endereco', 'data_nascimento', 'sexo', 'tipo_usuario')
    list_filter = ('tipo_usuario',)
    search_fields = ('username', 'email', 'first_name',
                     'last_name', 'cpf', 'telefone')
    list_per_page = 10
