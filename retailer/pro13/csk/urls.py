from django.urls import path,re_path
from .import views


urlpatterns = [
    path('home/',views.home,name = 'home'),
    path('Product/',views.Product,name = 'Product'),
    re_path(r'^cart/(?:(?P<userid>\d+)/)?$', views.cart, name='cart'),
    path('login/',views.login,name="login"),
    path('signup/',views.signup,name="signup"),
    path('otp/',views.otp,name = "otp")
]