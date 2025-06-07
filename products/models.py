from django.db import models

from core.models import BaseModel
from accounts.models import Fornecedor
from core.choices import CATEGORIA_PRODUTO_CHOICES, UNIDADE_MEDIDA_CHOICES

from django.core.exceptions import ValidationError
from django.core.validators import MinValueValidator


class Marca(BaseModel):
    """
    Modelo para representar marcas dos produtos fornecidos.
    """
    nome = models.CharField(max_length=255)

    class Meta:
        verbose_name = 'Marca'
        verbose_name_plural = 'Marcas'
        ordering = ['-criacao']

    def __str__(self):
        """
        Retorna o nome da marca para representação em texto.
        """
        return self.nome


class Produto(BaseModel):
    """
    Modelo que representa um produto vendido no mercado.
    """
    nome = models.CharField(max_length=255)
    descricao = models.TextField()
    preco = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        validators=[MinValueValidator(
            0.01, message='O preço deve ser maior que zero')]
    )
    categoria = models.CharField(
        max_length=50, choices=CATEGORIA_PRODUTO_CHOICES)
    imagem = models.ImageField(upload_to='produtos/', null=True, blank=True)
    unidade_medida = models.CharField(
        max_length=3, choices=UNIDADE_MEDIDA_CHOICES)
    marca = models.ForeignKey(Marca, on_delete=models.CASCADE)
    fornecedor = models.ForeignKey(Fornecedor, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Produto'
        verbose_name_plural = 'Produtos'
        ordering = ['-criacao']

    def clean(self):
        """
        Validações customizadas para o produto.
        Garante que o preço é positivo e que a categoria e unidade de medida sejam válidas.
        """
        super().clean()

        if self.preco <= 0:
            raise ValidationError(
                {'preco': 'O preço não pode ser menor ou igual a zero.'})

        if self.categoria not in [choice[0] for choice in CATEGORIA_PRODUTO_CHOICES]:
            raise ValidationError({'categoria': 'Categoria inválida.'})

        if self.unidade_medida not in [choice[0] for choice in UNIDADE_MEDIDA_CHOICES]:
            raise ValidationError(
                {'unidade_medida': 'Unidade de medida inválida.'})

    def save(self, *args, **kwargs):
        """
        Sobrescreve o método save para validar antes de salvar.
        """
        self.clean()
        super().save(*args, **kwargs)

    def __str__(self):
        """
        Retorna o nome do produto para representação em texto.
        """
        return self.nome
