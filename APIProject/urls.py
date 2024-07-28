# myproject/urls.py
from django.contrib import admin
from django.urls import path, include
from django.views.decorators.csrf import csrf_exempt
from graphene_django.views import GraphQLView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('my_app.urls')),
    path('o/', include('oauth2_provider.urls', namespace='oauth2_provider')),
    path('graphql/', csrf_exempt(GraphQLView.as_view(graphiql=True))),
]
