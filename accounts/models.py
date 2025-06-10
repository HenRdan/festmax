from django.db import models
from core.models import BaseModel, UserBaseModel, EnderecoModel
from core.choices import SEXO_CHOICES, TIPO_USUARIO_CHOICES, EstadoChoices
from core.validators import cpf_validator, cnpj_validator


class Cliente(BaseModel, UserBaseModel):
    """
    Modelo para representar um cliente do sistema.
    """
    cpf = models.CharField("CPF", max_length=14, validators=[
                           cpf_validator], unique=True, null=False, blank=False)
    data_nascimento = models.DateField("Data de Nascimento")
    sexo = models.CharField("Sexo", max_length=1, choices=SEXO_CHOICES)
    endereco = models.ForeignKey(
        EnderecoModel, on_delete=models.SET_NULL, null=True, blank=True)

    class Meta:
        verbose_name = 'Cliente'
        verbose_name_plural = 'Clientes'
        ordering = ['-criacao']


class Fornecedor(BaseModel, UserBaseModel):
    """
    Modelo para representar um fornecedor do sistema.
    """
    cnpj = models.CharField("CNPJ", max_length=18, validators=[
                            cnpj_validator], unique=True, null=False, blank=False)
    endereco = models.ForeignKey(
        EnderecoModel, on_delete=models.SET_NULL, null=True, blank=True)

    class Meta:
        verbose_name = 'Fornecedor'
        verbose_name_plural = 'Fornecedores'
        ordering = ['-criacao']


class Funcionario(BaseModel, UserBaseModel):
    """
    Modelo para representar um funcionário do sistema.
    """
    cpf = models.CharField(max_length=14, validators=[
        cpf_validator], unique=True, null=False, blank=False)
    data_nascimento = models.DateField("Data de Nascimento")
    cargo = models.CharField("Cargo", max_length=255)
    salario = models.DecimalField("Salário", max_digits=10, decimal_places=2)
    sexo = models.CharField("Sexo", max_length=1, choices=SEXO_CHOICES)
    endereco = models.ForeignKey(
        EnderecoModel, on_delete=models.SET_NULL, null=True, blank=True)

    class Meta:
        verbose_name = 'Funcionario'
        verbose_name_plural = 'Funcionarios'
        ordering = ['-criacao']
