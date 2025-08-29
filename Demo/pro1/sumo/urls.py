from django.urls import path
from . import views

urlpatterns = [
    path('final/',views.final,name="final"),
    path('showdata/',views.showdata,name="showdata"),
    path('edit/<int:id>/',views.edit,name="edit"),
    path('delete/<int:id>/',views.delete,name="delete"),
    path('view/<int:id>/',views.viewdata,name="viewdata"),
]