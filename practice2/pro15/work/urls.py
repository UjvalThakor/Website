from django.urls import path

from .import views

urlpatterns = [
    path('',views.Practice,name = 'practice')
]