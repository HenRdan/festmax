from enum import Enum

"""
Choices para os modelos do sistema.
Define opções fixas usadas em campos de modelos, para padronizar dados.
"""

"""
Lista de estados brasileiros para uso em campos de escolha.

Atributos:
    - CHOICES (list): Tuplas com sigla do estado e nome completo.
    - __str__ (str): Retorna a sigla do estado.
    - choices (list): Retorna uma lista de tuplas com sigla e nome do estado.
"""


class EstadoChoices(Enum):
    AC = ('AC', 'Acre')
    AL = ('AL', 'Alagoas')
    AP = ('AP', 'Amapá')
    AM = ('AM', 'Amazonas')
    BA = ('BA', 'Bahia')
    CE = ('CE', 'Ceará')
    DF = ('DF', 'Distrito Federal')
    ES = ('ES', 'Espírito Santo')
    GO = ('GO', 'Goiás')
    MA = ('MA', 'Maranhão')
    MT = ('MT', 'Mato Grosso')
    MS = ('MS', 'Mato Grosso do Sul')
    MG = ('MG', 'Minas Gerais')
    PA = ('PA', 'Pará')
    PB = ('PB', 'Paraíba')
    PR = ('PR', 'Paraná')
    PE = ('PE', 'Pernambuco')
    PI = ('PI', 'Piauí')
    RJ = ('RJ', 'Rio de Janeiro')
    RN = ('RN', 'Rio Grande do Norte')
    RS = ('RS', 'Rio Grande do Sul')
    RO = ('RO', 'Rondônia')
    RR = ('RR', 'Roraima')
    SC = ('SC', 'Santa Catarina')
    SP = ('SP', 'São Paulo')
    SE = ('SE', 'Sergipe')
    TO = ('TO', 'Tocantins')

    @classmethod
    def choices(cls):
        return [(member.value[0], member.value[1]) for member in cls]

    def __str__(self):
        return self.value[0]


TIPO_USUARIO_CHOICES = [
    ('FUN', 'Funcionário'),
    ('CLI', 'Cliente'),
    ('FOR', 'Fornecedor'),
]

# Choices para o sexo do usuário
SEXO_CHOICES = [
    ('M', 'Masculino'),
    ('F', 'Feminino'),
]

# Choices para o status do pagamento
STATUS_PAGAMENTO_CHOICES = [
    ('PENDENTE', 'Pendente'),
    ('PAGO', 'Pago'),
    ('CANCELADO', 'Cancelado'),
]

# Choices para formas de pagamento
FORMA_PAGAMENTO_CHOICES = [
    ('PIX', 'Pix'),
    ('BOLETO', 'Boleto'),
    ('CARTAO', 'Cartão'),
]

# Choices para o status da entrega
STATUS_ENTREGA_CHOICES = [
    ('AGUARDANDO', 'Aguardando Envio'),
    ('PENDENTE', 'Pendente'),
    ('ENTREGUE', 'Entregue'),
    ('DEVOLVIDO', 'Devolvido'),
]

# Status do pedido
STATUS_PEDIDO_CHOICES = [
    ('PENDENTE', 'Pendente'),
    ('EM_PROGRESSO', 'Em Progresso'),
    ('ENTREGUE', 'Entregue'),
    ('CANCELADO', 'Cancelado'),
]


# Categorias possíveis para produtos do mercado.
CATEGORIA_PRODUTO_CHOICES = [

    ('HORTIFRUTI', 'Hortifrúti'),
    ('CARNES', 'Carnes'),
    ('BEBIDAS', 'Bebidas'),
    ('PADARIA', 'Padaria'),
    ('LATICINIOS', 'Laticínios'),
    ('MERCEARIA', 'Mercearia'),
    ('LIMPEZA', 'Limpeza'),
    ('HIGIENE', 'Higiene e Beleza'),
    ('CONGELADOS', 'Congelados'),
    ('PET', 'Pet'),
]

# Unidades de medida válidas para os produtos.
UNIDADE_MEDIDA_CHOICES = [
    ('UN', 'Unidade'),
    ('KG', 'Quilo'),
    ('L', 'Litro'),
    ('M', 'Metro'),
]
