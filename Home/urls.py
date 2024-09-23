from django.urls import path
from .views import inicio_view, SesionView, AcercaView, ContactoView

urlpatterns = [
    path('', inicio_view, name='inicio'),  
    path('sesion/', SesionView.as_view(), name='sesion'),  
    path('about/', AcercaView.as_view(), name='about'),
    path('contact/', ContactoView.as_view(), name='contact'),
]