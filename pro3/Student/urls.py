from django.urls import path
from. import views

urlpatterns = [
    path('connect/',views.connect,name="connect"),
    path('delete/<int:id>/<int:Standard>/',views.delete,name="delete"),
    path('viewdata/<int:id>/<int:Standard>/',views.viewdata,name="viewdata"),
    path('showdata/',views.showdata,name="showdata"),
    path('edit/<int:id>/<int:Standard>/',views.edit,name="edit")
    ]