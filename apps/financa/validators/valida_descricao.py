from django.core.exceptions import ValidationError

def valida_descricao(descricao):
    if len(descricao) < 3:
        raise ValidationError("Descrição deve conter pelo menos 3 caracteres")