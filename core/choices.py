"""
Choices para os modelos do sistema.
Define opções fixas usadas em campos de modelos, para padronizar dados.
"""


class EstadoChoices:
    """
    Lista de estados brasileiros para uso em campos de escolha.

    Atributos:
        CHOICES (list): Tuplas com sigla do estado e nome completo.
    """
    AC = 'AC'
    AL = 'AL'
    AP = 'AP'
    AM = 'AM'
    BA = 'BA'
    CE = 'CE'
    DF = 'DF'
    ES = 'ES'
    GO = 'GO'
    MA = 'MA'
    MT = 'MT'
    MS = 'MS'
    MG = 'MG'
    PA = 'PA'
    PB = 'PB'
    PR = 'PR'
    PE = 'PE'
    PI = 'PI'
    RJ = 'RJ'
    RN = 'RN'
    RS = 'RS'
    RO = 'RO'
    RR = 'RR'
    SC = 'SC'
    SP = 'SP'
    SE = 'SE'
    TO = 'TO'

    CHOICES = [
        (AC, 'Acre'),
        (AL, 'Alagoas'),
        (AP, 'Amapá'),
        (AM, 'Amazonas'),
        (BA, 'Bahia'),
        (CE, 'Ceará'),
        (DF, 'Distrito Federal'),
        (ES, 'Espírito Santo'),
        (GO, 'Goiás'),
        (MA, 'Maranhão'),
        (MT, 'Mato Grosso'),
        (MS, 'Mato Grosso do Sul'),
        (MG, 'Minas Gerais'),
        (PA, 'Pará'),
        (PB, 'Paraíba'),
        (PR, 'Paraná'),
        (PE, 'Pernambuco'),
        (PI, 'Piauí'),
        (RJ, 'Rio de Janeiro'),
        (RN, 'Rio Grande do Norte'),
        (RS, 'Rio Grande do Sul'),
        (RO, 'Rondônia'),
        (RR, 'Roraima'),
        (SC, 'Santa Catarina'),
        (SP, 'São Paulo'),
        (SE, 'Sergipe'),
        (TO, 'Tocantins'),
    ]


# Choices para o sexo do usuário
SEXO_CHOICES = [
    ('M', 'Masculino'),
    ('F', 'Feminino'),
]

# Choices para o tipo de usuário
TIPO_USUARIOS_CHOICES = [
    ('FUN', 'Funcionário'),
    ('CLI', 'Cliente'),
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
