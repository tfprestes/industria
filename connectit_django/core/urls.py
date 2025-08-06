# ==============================================================================
# core/urls.py - Código Validado pelo Arquiteto de Software
# Nenhuma correção necessária. O arquivo segue os padrões RESTful e do Django.
# ==============================================================================
from django.urls import path
from .views import AssetListView, AssetCreateView, AssetUpdateView, AssetDeleteView, DashboardView

app_name = 'core'

urlpatterns = [
    # Mapeia a raiz do app para o Dashboard principal
    path('', DashboardView.as_view(), name='dashboard'),
    
    # URLs para o CRUD de Ativos (Assets)
    path('assets/', AssetListView.as_view(), name='asset_list'),
    path('assets/add/', AssetCreateView.as_view(), name='asset_add'),
    path('assets/<int:pk>/edit/', AssetUpdateView.as_view(), name='asset_edit'),
    path('assets/<int:pk>/delete/', AssetDeleteView.as_view(), name='asset_delete'),
    
    # Outras URLs do app virão aqui...
]