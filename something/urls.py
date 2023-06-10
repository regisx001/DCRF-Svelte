from django.urls import path
from something import views

urlpatterns = [
    path("posts/", views.ListCreatePost.as_view())
]
