from django.urls import path
from .views import getUserProfile

urlpatterns = [
    path('profile/', getUserProfile, name='user_profile'),
]
