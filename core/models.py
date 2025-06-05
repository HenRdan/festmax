from django.db import models


class BaseModel(models.Model):
    """
    Modelo abstrato para reutilização de campos e monitoramento de atualizações.

    Campos comuns:
        - criacao: data e hora da criação (auto)
        - atualizacao: data e hora da última atualização (auto)
        - ativo: flag para controle de ativação
    """
    criacao = models.DateTimeField(auto_now_add=True)
    atualizacao = models.DateTimeField(auto_now=True)
    ativo = models.BooleanField(default=True)

    class Meta:
        abstract = True


class EnderecoModel(models.Model):
    """
    Modelo abstrato para reutilização de campos de endereço.

    Campos comuns:
        - cep, rua, numero, complemento, bairro, cidade, estado
    """
    cep = models.CharField(max_length=10)
    rua = models.CharField(max_length=255)
    numero = models.CharField(max_length=10)
    complemento = models.CharField(max_length=255, blank=True, null=True)
    bairro = models.CharField(max_length=100)
    cidade = models.CharField(max_length=100)
    estado = models.CharField(max_length=2)

    class Meta:
        abstract = True
