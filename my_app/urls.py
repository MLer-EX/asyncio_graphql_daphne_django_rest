# myapp/urls.py
from django.urls import path
from .views import ItemListCreate, ItemRetrieveUpdateDestroy
from .views import login_view, chat_view


urlpatterns = [
    path('items/', ItemListCreate.as_view(), name='item-list-create'),
    path('items/<int:pk>/', ItemRetrieveUpdateDestroy.as_view(), name='item-detail'),
    path('login/', login_view, name='login'),
    path('chat/', chat_view, name='chat'),
]