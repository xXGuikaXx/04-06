from django.db import models
from core.model import BaseModel
from ..validators.valida_descricao import valida_descricao
from ..validators.valida_valor import valida_valor
from ..validators.valida_data import valida_data
from ..validators.valida_tipo_transacao import valida_tipo_transacao
from ..validators.valida_status import valida_status


class Transacao(BaseModel):

    TIPO_CHOICES = (
    ('R','Receita'),
    ('D', 'Despesa')
    )

    STATUS_CHOICES = (
    ('E','Efetivado'),
    ('P','Pendente')
    )

    descricao = models.CharField(
        max_length=200,
        verbose_name="Descrição",
        help_text='Descrição da Transação',
        validators=[valida_descricao]
    )

    valor = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        verbose_name="Valor",
        help_text='Valor da Transação',
        validators=[valida_valor]
    )

    tipo_transacao = models.CharField(
    max_length=1,
    choices=TIPO_CHOICES,
    verbose_name="Tipo de Transacao",
    help_text='receita ou despesa',
    validators=[valida_tipo_transacao]
    )

    status = models.CharField(
        max_length=1,
        choices=STATUS_CHOICES,
        verbose_name="Status da Transacao",
        help_text='Pendente ou Efetivado',
        validators=[valida_status]
    )
    data_transacao = models.DateField(
        verbose_name="Data de Transacao",
        help_text='xx/xx/xxxx',
        validators=[valida_data]
    )


    class Meta:
        verbose_name = "Transação"
        verbose_name_plural = "Transações"
        ordering = ['data_transacao']