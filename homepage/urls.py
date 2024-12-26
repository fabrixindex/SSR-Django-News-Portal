from django.urls import path
from .views import inicio, about_me, soon  

urlpatterns = [
    path('', inicio, name='inicio'),
    path('about_me/', about_me, name='about_me'),
    path('soon!/', soon, name='soon!')  
]
