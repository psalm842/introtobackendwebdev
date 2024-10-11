from django.shortcuts import render
from django.http.response import HttpResponse 

def home(request):
    return render(request, 'hello/index.html', {})

def sayHello(request):
    name = request.GET.get('name', 'World')
    title = request.GET.get('title', '')
    return render(request, 'hello/hello.html', {'name': name, 'title': title})

def sayHelloWithName(request, name):
    return HttpResponse(f"Hello {name}!")