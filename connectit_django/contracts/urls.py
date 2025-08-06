# ==============================================================================
# contracts/urls.py - v2 (Corrigido e Refatorado pelo Arquiteto de Software)
# Correção: Remoção do prefixo redundante 'contracts/' para alinhar com o
# urls.py principal do projeto.
# ==============================================================================

from django.urls import path
from .views import (
    ContractListView,
    ContractCreateView,
    ContractUpdateView,
    ContractDeleteView,
    ContractDetailView
)

app_name = 'contracts'

urlpatterns = [
    # ANTES: path('contracts/', ...)
    # AGORA: path('', ...) -> Corresponde a /contracts/
    path('', ContractListView.as_view(), name='contract_list'),

    # ANTES: path('contracts/add/', ...)
    # AGORA: path('add/', ...) -> Corresponde a /contracts/add/
    path('add/', ContractCreateView.as_view(), name='contract_add'),

    # ANTES: path('contracts/<int:pk>/', ...)
    # AGORA: path('<int:pk>/', ...) -> Corresponde a /contracts/123/
    path('<int:pk>/', ContractDetailView.as_view(), name='contract_detail'),

    # ANTES: path('contracts/<int:pk>/edit/', ...)
    # AGORA: path('<int:pk>/edit/', ...) -> Corresponde a /contracts/123/edit/
    path('<int:pk>/edit/', ContractUpdateView.as_view(), name='contract_edit'),
    
    # ANTES: path('contracts/<int:pk>/delete/', ...)
    # AGORA: path('<int:pk>/delete/', ...) -> Corresponde a /contracts/123/delete/
    path('<int:pk>/delete/', ContractDeleteView.as_view(), name='contract_delete'),
]