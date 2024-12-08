from django.shortcuts import render, redirect
from .models import Article

def articles(request):
    if request.method == "POST":
        title = request.POST["title"]
        author = request.POST["author"]
        content = request.POST["content"]
        publication_date = request.POST["publication_date"]
        last_updated = request.POST["last_updated"]

        article = Article(
            title=title,
            author=author,
            content=content,
            publication_date=publication_date,
            last_updated=last_updated
        )
        article.save()

        return redirect("inicio")
    else:
        return render(request, "articles/article.html")

def searchArticle(request):
    query = request.GET.get('q', '').strip()  
    
    if query:
        articles = Article.objects.filter(title__icontains=query)  
    else:
        articles = Article.objects.all()  
    return render(request, "articles/article.html", {"articles": articles, "query": query})