from django.urls import path
from card_manager import views

app_name = 'card_manager'

urlpatterns = [
    path('', views.card_choice, name='card_choice'),
    path('proxy', views.ProxyView.as_view(), name='proxy'),
]