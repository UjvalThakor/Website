from django.urls import path
from. import views

urlpatterns = [
    path('connect/',views.connect,name="connect"),
    path('showdata/',views.showdata,name="showdata"),
    path('edit/<int:id>/<str:Standard>',views.edit,name="edit"),
    path('delete/<int:id>/<str:Standard>',views.delete,name="delete"),
    path('view/<int:id>/<str:Standard',views.viewdata,name="viewdata"),
    path('view/',views.viewdata,name="viewdata")
]