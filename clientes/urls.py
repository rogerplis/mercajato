from django.urls import path

from .views import ClienteList, CarroApiView

urlpatterns = [
    path('clientes', ClienteList.as_view(), name='clientes'),
    path('carros', CarroApiView.as_view(), name='carros'),
]