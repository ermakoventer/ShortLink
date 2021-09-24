from django.http import request
from django.shortcuts import render

def home(request):
    return render(request, 'main/home.html',{'title': 'Главная страница'})

def about(request):
    return render(request, 'main/about.html',{'title': 'Страница про нас'})