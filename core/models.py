from django.db import models
from core.choices import TIPO_USUARIO_CHOICES, EstadoChoices
from django.contrib.auth.models import AbstractUser
from core.validators import cep_validator, telefone_validator, cpf_validator, cnpj_validator


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


class UserBaseModel(AbstractUser):
    """
    Modelo abstrato para reutilização de campos de usuário.

    Campos comuns:
        - first_name: primeiro nome do usuário
        - last_name: último nome do usuário
        - email: email do usuário
        - senha: senha do usuário
        - telefone: telefone do usuário
        - tipo_usuario: tipo de usuário
    """
    telefone = models.CharField(
        max_length=15,
        validators=[telefone_validator],
        help_text='Número de telefone com código de país, ex: +5511999999999'
    )
    tipo_usuario = models.CharField(max_length=3, choices=TIPO_USUARIO_CHOICES)

    class Meta:
        abstract = True

    @property
    def nome_completo(self):
        """
        Retorna o nome completo do usuário.
        """
        return f"{self.first_name or ''} {self.last_name or ''}".strip()


class EnderecoModel(BaseModel):
    """
    Modelo para representar um endereço.

    Campos comuns:
        - cep, rua, numero, complemento, bairro, cidade, estado
    """
    cep = models.CharField(
        max_length=10,
        validators=[cep_validator]
    )
    rua = models.CharField(max_length=255)
    numero = models.CharField(max_length=10)
    complemento = models.CharField(max_length=255, blank=True, null=True)
    bairro = models.CharField(max_length=100)
    cidade = models.CharField(max_length=100)
    estado = models.CharField(max_length=2, choices=EstadoChoices.choices())

    class Meta:
        verbose_name = 'Endereço'
        verbose_name_plural = 'Endereços'
        ordering = ['-criacao']

    def __str__(self):
        return f"{self.rua}, {self.numero} - {self.bairro} - {self.cidade}/{self.estado}"
