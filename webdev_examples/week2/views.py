from django.shortcuts import render
from django.http.response import HttpResponse 

def sayHello(request):
    name = request.GET.get('name', 'World')
    return HttpResponse(f"Hello {name}!")

def sayHelloWithName(request, name):
    return HttpResponse(f"Hello {name}!")