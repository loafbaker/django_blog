from django.db.models import Q
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.generics import ListAPIView, CreateAPIView, RetrieveAPIView, RetrieveUpdateAPIView, DestroyAPIView
from rest_framework.permissions import IsAuthenticated

from posts.models import Post
from .pagination import PostPageNumberPagination
from .permissions import IsOwnerOrReadOnly
from .serializers import PostCreateUpdateSerializer, PostDetailSerializer, PostListSerializer

class PostListAPIView(ListAPIView):
	queryset = Post.objects.all()
	serializer_class = PostListSerializer
	filter_backends = [SearchFilter, OrderingFilter]
	search_fields = ['title', 'content', 'user__first_name', 'user__last_name']
	pagination_class = PostPageNumberPagination

	def get_queryset(self):
		queryset_list = super(PostListAPIView, self).get_queryset()
		query = self.request.GET.get('q')
		if query:
			queryset_list = queryset_list.filter(
				Q(title__icontains=query) |
				Q(content__icontains=query) |
				Q(user__first_name=query) |
				Q(user__last_name=query)
			)
		return queryset_list

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