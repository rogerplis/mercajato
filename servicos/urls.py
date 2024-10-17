from django.urls import path

from .views import ServicoList, OrcamentoList, ItemOrcamentoList, OrdemServicoList

urlpatterns = [
    path('servicos', ServicoList.as_view(), name='servicos'),
    path('orcamentos', OrcamentoList.as_view(), name='orcamentos'),
    path('itensorcamentos', ItemOrcamentoList.as_view(), name='itensorcamentos'),
    path('ordensservicos', OrdemServicoList.as_view(), name='ordensservicos'),
]