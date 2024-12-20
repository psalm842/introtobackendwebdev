"""
URL configuration for webdev_examples project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from hello import views as hello_views
from quizzer import views as quizzer_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', hello_views.home),
    path('hello/', hello_views.sayHello),
    path('hello/<str:name>/', hello_views.sayHelloWithName),
    path('quiz', quizzer_views.quiz),
    path('results', quizzer_views.results),
    path('history', quizzer_views.history),
]
