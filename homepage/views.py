from django.shortcuts import render
from django.http import HttpResponse
import requests
from articles.models import Article

def inicio(request):
    articles = Article.objects.all()[:3]
    while len(articles) < 3:
        articles.append(None)  
    return render(request, 'homepage/index.html', {'articles': articles})

def get_github_avatar(username):
    url = f"https://api.github.com/users/{username}"
    try:
        response = requests.get(url)
        response.raise_for_status()  
        data = response.json()
        return data.get("avatar_url", "")
    except requests.RequestException:
        return None

def about_me(request):
    username = "fabrixindex"  
    avatar_url = get_github_avatar(username)
    return render(request, 'homepage/about_me.html', {"avatar_url": avatar_url})

def soon(request):
    return render(request, 'homepage/soon.html')
