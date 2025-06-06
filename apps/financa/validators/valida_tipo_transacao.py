from django.core.exceptions import ValidationError

def valida_tipo_transacao(tipo_transacao):

    if tipo_transacao != 'R' or tipo_transacao != 'D':
        raise ValidationError('Tipo de transacao invalido')