from django.urls import path
from .views import inicio_view, SesionView

urlpatterns = [
    path('', inicio_view, name='inicio'),  
    path('sesion/', SesionView.as_view(), name='sesion'),  
]