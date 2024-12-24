from django.urls import path
from .views import get_user_profile, user_login, user_register, user_logout, edit_user_profile, change_password

urlpatterns = [
    path('profile/', get_user_profile, name='user_profile'),
    path('login/', user_login, name='login'),
    path('register/', user_register, name='register'),
    path('logout/', user_logout, name='logout'),
    path('profile/edit/', edit_user_profile, name='edit_profile'),
    path('change-password/', change_password, name='change_password')
]