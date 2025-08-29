from django.urls import path
from .import views

urlpatterns = [
    path('emp/',views.employee,name = "emp"),
    path('view/<int:id>/',views.view,name ="view"),
    path('edit/<int:id>/',views.edit,name="edit"),
    path('delete/<int:id>/',views.delete,name="delete"),
    path('display/',views.display,name = "display")
]