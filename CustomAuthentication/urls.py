# Urls para el modulo de customauthentication

from django.urls import path
from .views import CustomLoginView, CustomLogin
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('login/', CustomLoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('api/login/', CustomLogin.as_view(), name='custom_login'),
]
