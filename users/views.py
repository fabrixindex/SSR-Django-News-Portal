from django.shortcuts import render
from django.http import HttpResponse

def usuario(request):
    return HttpResponse("Bienvenidos a la app de users!")
