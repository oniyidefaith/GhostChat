import os
from django.core.asgi import get_asgi_application
from channels.routing import ProtocolTypeRouter, URLRouter
from channels.auth import AuthMiddlewareStack
from auths.consumers import ChatConsumer
from django.urls import path, re_path

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'anon.settings')

application = ProtocolTypeRouter({
    "http": get_asgi_application(),
    "websocket": AuthMiddlewareStack(
        URLRouter([
            re_path(r'ws/room/(?P<room_name>\w+)/$', ChatConsumer.as_asgi()),
        ])
    ),
})
