from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from .forms.users.forms import UserForm

def getUserProfile(request):
    user = request.user
    return render(request, "users/profile.html", {"user": user})

def user_login(request):
    if request.method == 'POST':  
        username = request.POST.get('username')  
        password = request.POST.get('password') 
        
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            login(request, user)  
            return redirect("inicio")  
        else:
            return redirect("login") 
    else:
        return render(request, "users/login.html")  

def user_logout(request):
    logout(request)
    return redirect("login")

def user_register(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()  
            return redirect("inicio") 
    else:
        form = UserForm()

    return render(request, "users/register.html", {"form": form})