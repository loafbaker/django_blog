from rest_framework.generics import ListAPIView, CreateAPIView, RetrieveAPIView, RetrieveUpdateAPIView, DestroyAPIView
from rest_framework.permissions import IsAuthenticated

from posts.models import Post
from .permissions import IsOwnerOrReadOnly
from .serializers import PostCreateUpdateSerializer, PostDetailSerializer, PostListSerializer

class PostListAPIView(ListAPIView):
	queryset = Post.objects.all()
	serializer_class = PostListSerializer

class PostCreateAPIView(CreateAPIView):
	permission_classes = [IsAuthenticated]
	queryset = Post.objects.all()
	serializer_class = PostCreateUpdateSerializer

	def perform_create(self, serializer):
		serializer.save(user=self.request.user)

class PostDetailAPIView(RetrieveAPIView):
	queryset = Post.objects.all()
	serializer_class = PostDetailSerializer
	lookup_field = 'slug'

class PostUpdateAPIView(RetrieveUpdateAPIView):
	permission_classes = [IsOwnerOrReadOnly]
	queryset = Post.objects.all()
	serializer_class = PostCreateUpdateSerializer
	lookup_field = 'slug'

class PostDeleteAPIView(DestroyAPIView):
	permission_classes = [IsOwnerOrReadOnly]
	queryset = Post.objects.all()
	serializer_class = PostListSerializer
	lookup_field = 'slug'