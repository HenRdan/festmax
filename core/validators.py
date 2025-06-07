import re
from django.core.exceptions import ValidationError


def cep_validator(value):
    """
    Validador para CEP.
    Formato: 99999-999
    """
    if not re.match(r'^\d{5}-\d{3}$', value):
        raise ValidationError('CEP deve estar no formato 99999-999')


def cpf_validator(value):
    """
    Validador para CPF.
    Formato: 999.999.999-99
    """
    if not re.match(r'^\d{3}\.\d{3}\.\d{3}-\d{2}$', value):
        raise ValidationError('CPF deve estar no formato 999.999.999-99')


def cnpj_validator(value):
    """
    Validador para CNPJ.
    """
    if not re.match(r'^\d{2}\.\d{3}\.\d{3}\/\d{4}-\d{2}$', value):
        raise ValidationError('CNPJ deve estar no formato 99.999.999/9999-99')


def telefone_validator(value):
    """
    Validador para telefone.
    """
    if not re.match(r'^\+?\d{9,15}$', value):
        raise ValidationError(
            'Telefone deve conter entre 9 e 15 dígitos, podendo começar com +')
