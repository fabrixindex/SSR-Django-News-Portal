from django.urls import path
from .views import getUserProfile, user_login, user_register, user_logout

urlpatterns = [
    path('profile/', getUserProfile, name='user_profile'),
    path('login/', user_login, name='login'),
    path('register/', user_register, name='register'),
    path('logout/', user_logout, name='logout')
]
