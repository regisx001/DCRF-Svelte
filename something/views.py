from rest_framework.generics import ListCreateAPIView
from something.serializers import PostSerializer
from something.models import Post


class ListCreatePost(ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
