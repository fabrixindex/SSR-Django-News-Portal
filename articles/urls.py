from django.urls import path
from .views import getArticles, createArticle, searchArticle, getArticleDetail, deleteArticle, updateArticle

urlpatterns = [
    path('', getArticles, name='articles'),
    path('create/', createArticle, name='create_article'),
    path('<int:id>/', getArticleDetail, name='article_detail'),
    path('search/', searchArticle, name='search_article'),
    path('delete/<int:id>/', deleteArticle, name='delete_article'),
    path('update/<int:id>/', updateArticle, name='update_article'),
]
