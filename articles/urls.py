from django.urls import path
from .views import articles, searchArticle

urlpatterns = [
    path('', articles, name='articles'),
    path('search/', searchArticle, name='search_article'),
]
