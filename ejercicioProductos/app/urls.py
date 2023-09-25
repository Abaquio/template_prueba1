from django.urls import path
from .views import index, productos

urlpatterns = [
    path('',index,name='index'),
    path('productos/', productos, name='productos'),
    path('productos/<str:categoria>/',productos,name='productos_categoria')
]
