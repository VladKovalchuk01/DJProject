from django.shortcuts import render

from .models import *


def home(request):
    return render(request, 'goods/home.html')


def categories(request):
    posts = All_goods.objects.all()
    return render(request, 'goods/cats.html', {'posts': posts})


def login(request):
    return render(request, 'goods/login.html')


def basket(request):
    return render(request, 'goods/basket.html')


def registration(request):
    return render(request, 'goods/registration.html')

def mans(request):

    return render(request, 'goods/mans.html')

def womens(request):
    return render(request, 'goods/womens.html')

def child(request):
    return render(request, 'goods/child.html')
