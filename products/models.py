from django.db import models
from core.models import BaseModel
from django.db.models import TextChoices
from django.core.exceptions import ValidationError
from django.core.validators import MinValueValidator, RegexValidator


class Categoria(TextChoices):
    """
    Categorias possíveis para produtos do mercado.
    """
    HORTIFRUTI = 'HORTIFRUTI', 'Hortifrúti'
    CARNES = 'CARNES', 'Carnes'
    BEBIDAS = 'BEBIDAS', 'Bebidas'
    PADARIA = 'PADARIA', 'Padaria'
    LATICINIOS = 'LATICINIOS', 'Laticínios'
    MERCEARIA = 'MERCEARIA', 'Mercearia'
    LIMPEZA = 'LIMPEZA', 'Limpeza'
    HIGIENE = 'HIGIENE', 'Higiene e Beleza'
    CONGELADOS = 'CONGELADOS', 'Congelados'
    PET = 'PET', 'Pet'


class UnidadeMedida(TextChoices):
    """
    Unidades de medida válidas para os produtos.
    """
    UNIDADE = 'UN', 'Unidade'
    QUILO = 'KG', 'Quilo'
    LITRO = 'L', 'Litro'
    METRO = 'M', 'Metro'


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


class Fornecedor(BaseModel):
    """
    Modelo para representar fornecedores dos produtos.
    """
    nome = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    telefone = models.CharField(
        max_length=15,
        validators=[RegexValidator(
            regex=r'^\+?\d{9,15}$',
            message='Telefone deve conter entre 9 e 15 dígitos, podendo começar com +'
        )],
        help_text='Número de telefone com código de país, ex: +5511999999999'
    )

    class Meta:
        verbose_name = 'Fornecedor'
        verbose_name_plural = 'Fornecedores'
        ordering = ['-criacao']

    def __str__(self):
        """
        Retorna o nome do fornecedor para representação em texto.
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
    categoria = models.CharField(max_length=50, choices=Categoria.choices)
    imagem = models.ImageField(upload_to='produtos/', null=True, blank=True)
    unidade_medida = models.CharField(
        max_length=3, choices=UnidadeMedida.choices)
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

        if self.categoria not in Categoria.values:
            raise ValidationError({'categoria': 'Categoria inválida.'})

        if self.unidade_medida not in UnidadeMedida.values:
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
