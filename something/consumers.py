from djangochannelsrestframework.generics import GenericAsyncAPIConsumer
from djangochannelsrestframework.mixins import ListModelMixin, CreateModelMixin
from something.serializers import PostSerializer
from something.models import Post


class PostsConsumers(ListModelMixin, CreateModelMixin, GenericAsyncAPIConsumer):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
