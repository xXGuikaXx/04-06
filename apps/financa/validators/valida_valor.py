from django.core.validators import ValidationError

def valida_valor(valor):

    if valor <= 0:
        raise ValidationError("O valor não pode ser negativo ou zero")

