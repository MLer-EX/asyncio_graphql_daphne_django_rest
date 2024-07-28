# myapp/urls.py
from django.urls import path
from .views import ItemListCreate, ItemRetrieveUpdateDestroy
from django.shortcuts import render


def index(request):
    return render(request, 'chat.html')


urlpatterns = [
    path('items/', ItemListCreate.as_view(), name='item-list-create'),
    path('items/<int:pk>/', ItemRetrieveUpdateDestroy.as_view(), name='item-detail'),
    path('', index),
]
