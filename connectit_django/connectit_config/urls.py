"""
URL configuration for connectit_config project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
"""

from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(('core.urls', 'core'), namespace='core')),
    path('contracts/', include(('contracts.urls', 'contracts'), namespace='contracts')),
    path('expenses/', include(('expenses.urls', 'expenses'), namespace='expenses')),
    path('tickets/', include(('tickets.urls', 'tickets'), namespace='tickets')),
]
