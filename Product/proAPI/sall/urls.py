from django.urls import path
from .import views

urlpatterns = [
    path('json_data/',views.json_data,name = "json_data"),
    path('shop/',views.shop,name = "shop")
]