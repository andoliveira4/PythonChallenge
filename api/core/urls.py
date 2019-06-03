from django.urls import path
from .views import CalculaHistograma


urlpatterns = [
    path('validation/', CalculaHistograma.as_view(), name="validation")
]