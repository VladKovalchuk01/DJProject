from django.urls import path
from .views import *


urlpatterns = [
    path('', home),
    path('categories/', categories, name='cats'),
    path('login', login, name='login'),
    path('basket', basket, name="backet"),
    path('registration', registration, name='register'),
    path('mans', mans, name='mans'),
    path('womens', mans, name='womens'),
    path('child', mans, name='child'),
]