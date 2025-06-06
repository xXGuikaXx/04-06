from django.core.validators import ValidationError

def valida_status(status):

    if status == 'E' or status == 'P':
        raise ValidationError('Este valor deve ser do tipo de transacao.')