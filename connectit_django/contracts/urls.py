# Em: contracts/urls.py

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
    path('contracts/', ContractListView.as_view(), name='contract_list'),
    path('contracts/add/', ContractCreateView.as_view(), name='contract_add'),
    path('contracts/<int:pk>/edit/', ContractUpdateView.as_view(), name='contract_edit'),
    path('contracts/<int:pk>/delete/', ContractDeleteView.as_view(), name='contract_delete'),
    path('contracts/<int:pk>/', ContractDetailView.as_view(), name='contract_detail'),

]