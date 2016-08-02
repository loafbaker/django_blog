from rest_framework.generics import ListAPIView, RetrieveAPIView, RetrieveUpdateAPIView, DestroyAPIView

from posts.models import Post
from .permissions import IsOwnerOrReadOnly
from .serializers import PostDetailSerializer, PostListSerializer

class PostListAPIView(ListAPIView):
	queryset = Post.objects.all()
	serializer_class = PostListSerializer

class PostDetailAPIView(RetrieveAPIView):
	queryset = Post.objects.all()
	serializer_class = PostDetailSerializer
	lookup_field = 'slug'

class PostUpdateAPIView(RetrieveUpdateAPIView):
	permission_classes = [IsOwnerOrReadOnly]
	queryset = Post.objects.all()
	serializer_class = PostListSerializer
	lookup_field = 'slug'

class PostDeleteAPIView(DestroyAPIView):
	permission_classes = [IsOwnerOrReadOnly]
	queryset = Post.objects.all()
	serializer_class = PostListSerializer
	lookup_field = 'slug'