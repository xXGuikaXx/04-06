from django.core.exceptions import ValidationError
from django.utils import timezone

def valida_data(data_transacao):

    if data_transacao.year <= timezone.now().year -1 or data_transacao.year >= timezone.now().year +1:
        raise ValidationError("A transação deve ser feita com o ano atual")