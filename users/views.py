from django.shortcuts import render

def getUserProfile(request):
    return render(request, "users/profile.html")
