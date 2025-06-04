from django.test import TestCase
from apps.financa.models.transacao import Transacao
from datetime import datetime

class TestTransacao(TestCase):

    def setUp(self):
        self.receita = Transacao.objects.create(
            descricao = 'salario',
            valor = 10000,
            tipo_transacao = 'R',
            status = 'E',
            data_transacao = datetime.strptime('2025-01-01 00:00:00', '%Y-%m-%d %H:%M:%S')
        )
        self.despesa = Transacao.objects.create(
            descricao = 'Aluguel',
            valor = 3000,
            tipo_transacao = 'D',
            status = 'E',
            data_transacao = datetime.strptime('2025-01-01 00:00:00', '%Y-%m-%d %H:%M:%S')
        )

    def test_velida_a_criacao_das_transacoes(self):

        self.assertEqual(self.receita.descricao, 'salario')
        self.assertEqual(self.receita.valor, 10000)
        self.assertEqual(self.receita.tipo_transacao, 'R')
        self.assertEqual(self.receita.status, 'E')
        self.assertEqual(self.receita.data_transacao, datetime.strptime('2025-01-01 00:00:00', '%Y-%m-%d %H:%M:%S'))

        self.assertEqual(self.despesa.descricao, 'Aluguel')
        self.assertEqual(self.despesa.valor, 3000)
        self.assertEqual(self.despesa.tipo_transacao, 'D')
        self.assertEqual(self.despesa.status, 'E')
        self.assertEqual(self.despesa.data_transacao, datetime.strptime('2025-01-01 00:00:00', '%Y-%m-%d %H:%M:%S'))
