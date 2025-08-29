from django.urls import path
from . import views

urlpatterns = [
    path('inquery/',views.Inquery,name = 'inquery'),
    path('hr/<str:id>',views.HR,name ='hr'),
    path('excel_data',views.excel_data,name = 'excel_data'),
    path('table/',views.table,name = 'table'),
    path('TATA/',views.tata,name = 'TATA')
]