from rest_framework import generics, filters
from django_filters.rest_framework import DjangoFilterBackend
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.apps import apps
from .forms import LoginForm
from .serializers import ItemSerializer


Item = apps.get_model('my_app', 'Item')


class ItemListCreate(generics.ListCreateAPIView):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ['name']  # فیلدهای قابل فیلتر
    search_fields = ['name', 'description']  # فیلدهای قابل جستجو
    ordering_fields = ['name', 'id']  # فیلدهای قابل مرتب‌سازی


class ItemRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer


def login_view(request):
    if request.method == "POST":
        form = LoginForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('chat')
    else:
        form = LoginForm()
    return render(request, "login.html", {"form": form})


def chat_view(request):
    return render(request, "chat.html")
