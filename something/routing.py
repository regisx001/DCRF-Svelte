from django.urls import re_path
from something import consumers

websocket_urlpatterns = [
    re_path(r'ws/posts/$', consumers.PostsConsumers.as_asgi())
]
