from django.urls import path
from .views import usuario

urlpatterns = [
    path('', usuario, name='usuario'),
]
