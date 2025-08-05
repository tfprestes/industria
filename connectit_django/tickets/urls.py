# connectit_django/tickets/urls.py
from django.urls import path
from .views import metrics

app_name = 'tickets'

urlpatterns = [
    path('', metrics, name='metrics'),
]
