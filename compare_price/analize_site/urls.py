from django.urls import path
from . import views

app_name="analize_site"

urlpatterns = [
    path('', views.controler_two_price, name="conroler_price"),
]