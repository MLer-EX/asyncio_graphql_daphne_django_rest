import os
import django
from channels.routing import ProtocolTypeRouter, URLRouter
from channels.auth import AuthMiddlewareStack
from django.core.asgi import get_asgi_application
import my_app.routing

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'APIProject.settings')
django.setup()  # اطمینان از بارگذاری اپلیکیشن‌ها

application = ProtocolTypeRouter({
    "http": get_asgi_application(),
    "websocket": AuthMiddlewareStack(
        URLRouter(
            my_app.routing.websocket_urlpatterns
        )
    ),
})
