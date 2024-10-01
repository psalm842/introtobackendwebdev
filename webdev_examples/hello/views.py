from django.shortcuts import render
from django.http.response import HttpResponse 

def sayHello(request):
    name = request.GET.get('name', 'World')
    return render(request, 'hello/index.html', {'name': name})

def sayHelloWithName(request, name):
    return HttpResponse(f"Hello {name}!")