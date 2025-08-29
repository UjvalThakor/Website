from django.urls import path

from . import views

urlpatterns = [
    path('body/',views.Body,name = 'body'),
    path('body/<str:id>',views.Bodyid,name = 'Bodyid'),
    path('Company/',views.compnay,name = 'Company')
]