from django.contrib import admin
from apps.financa.models.transacao import Transacao

@admin.register(Transacao)
class TransacaoAdmin(admin.ModelAdmin):
    list_display = ['tipo_transacao','descricao','valor','data_transacao','status']
    list_filter = ['tipo_transacao','status']
    search_fields = ['descricao','valor']
    list_per_page = 20
    readonly_fields = ['criado_em','atualizado_em']
    fieldsets = [
        ('Infomações sobre Transação',
         {
             'fields': ['tipo_transacao','descricao','valor','data_transacao','status']
         }
        ),

        ('Informações Extras',
         {
             "classes": ["collapse"],
             "fields": ['criado_em','atualizado_em']
         }
        )
    ]