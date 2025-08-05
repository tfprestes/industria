# Em: core/urls.py
from django.urls import path
from .views import AssetListView, AssetCreateView, AssetUpdateView, AssetDeleteView, DashboardView

app_name = 'core'

urlpatterns = [
    path('', DashboardView.as_view(), name='dashboard'),
    path('assets/', AssetListView.as_view(), name='asset_list'),
    path('assets/add/', AssetCreateView.as_view(), name='asset_add'),
    path('assets/<int:pk>/edit/', AssetUpdateView.as_view(), name='asset_edit'),
    path('assets/<int:pk>/delete/', AssetDeleteView.as_view(), name='asset_delete'),
    # Outras URLs do app virão aqui...
]