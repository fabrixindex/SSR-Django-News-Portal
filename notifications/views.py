from django.shortcuts import render
from django.http import HttpResponse

def notification_view(request):
    return render(request, "notifications/notification_view.html")