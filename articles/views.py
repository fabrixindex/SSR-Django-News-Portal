from django.shortcuts import render, redirect, get_object_or_404
from django.utils.timezone import now
from .models import Article

def getArticles(request):
    articles = Article.objects.all()  
    return render(request, "articles/articles_list.html", {"articles": articles})

def getArticleDetail(request, id):
    article = get_object_or_404(Article, id=id)
    return render(request, "articles/article_detail.html", {"article": article})

def createArticle(request):
    if request.method == "POST":
        title = request.POST.get("title")
        author = request.POST.get("author")
        content = request.POST.get("content")
        publication_date = request.POST.get("publication_date")
        
        article = Article(
            title=title,
            author=author,
            content=content,
            publication_date=publication_date,
            last_updated=now()
        )
        article.save()

        return redirect("article_list")
    else:
        return render(request, "articles/create_article.html")


def searchArticle(request):
    query = request.GET.get('q', '').strip()  
    
    if query:
        articles = Article.objects.filter(title__icontains=query)  
    else:
        articles = Article.objects.all()  
    return render(request, "articles/articles_list.html", {"articles": articles, "query": query})