from django.shortcuts import render, redirect, get_object_or_404
from django.utils.timezone import now
from .models import Article
from .forms.articles.forms import ArticleForm

def getArticles(request):
    articles = Article.objects.all()  
    return render(request, "articles/articles_list.html", {"articles": articles})

def getArticleDetail(request, id):
    article = get_object_or_404(Article, id=id)
    return render(request, "articles/article_detail.html", {"article": article})

def createArticle(request):
    if request.method == "POST":
        form = ArticleForm(request.POST)
        if form.is_valid():
            article = form.save(commit=False)
            article.publication_date = form.cleaned_data.get('publication_date', now())
            article.last_updated = now()
            article.save()
            return redirect("articles")
    else:
        form = ArticleForm()

    return render(request, "articles/create_article.html", {"form": form})


def searchArticle(request):
    query = request.GET.get('q', '').strip()  
    
    if query:
        articles = Article.objects.filter(title__icontains=query)  
    else:
        articles = Article.objects.all()  
    return render(request, "articles/articles_list.html", {"articles": articles, "query": query})

def deleteArticle(request, id):
    article = Article.objects.get(id=id)
    article.delete()
    return redirect("articles")

def updateArticle(request, id):
    article = get_object_or_404(Article, id=id)
    
    if request.method == "POST":
        article_form = ArticleForm(request.POST, instance=article)
        
        if article_form.is_valid():
            article_form.save()
            return redirect('article_detail', id=article.id)  

    else:
        article_form = ArticleForm(instance=article)

    return render(request, "articles/update_article.html", {"form": article_form, "article": article})