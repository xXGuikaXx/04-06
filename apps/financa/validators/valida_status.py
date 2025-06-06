from django.core.validators import ValidationError

def valida_status(status):

    if status != 'E' or status != 'P':
        raise ValidationError('Status invalido.')