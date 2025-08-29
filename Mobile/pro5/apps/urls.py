from django.urls import path
from . import views

urlpatterns = [
    path('signup/',views.signUp,name = "signUp"),
    path('otp/',views.otp,name = "otp"),
    path('login/',views.Login,name="Login"),
    path('viewdata/',views.viewdata,name ="viewdata"),
    path('edit/<int:id>/',views.edit,name="edit"),
    path('delete/<int:id>/',views.delete,name="delete"),
    path('view/<int:id>/',views.view,name="view")
]