from django.db.models import Q
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.generics import CreateAPIView, ListAPIView, RetrieveAPIView
from rest_framework.mixins import DestroyModelMixin, UpdateModelMixin
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly

from posts.api.pagination import PostPageNumberPagination
from posts.api.permissions import IsOwnerOrReadOnly

from comments.models import Comment
from .serializers import create_comment_serializer, CommentListSerializer, CommentDetailSerializer


class CommentCreateAPIView(CreateAPIView):
	queryset = Comment.objects.all()
	permission_classes = [IsAuthenticated]

	def get_serializer_class(self):
		model_type = self.request.GET.get('type')
		slug = self.request.GET.get('slug', None)
		parent_id = self.request.GET.get('parent_id', None)
		return create_comment_serializer(model_type, slug, parent_id, self.request.user)


class CommentListAPIView(ListAPIView):
	queryset = Comment.objects.filter()  # include child comments
	serializer_class = CommentListSerializer
	filter_backends = [SearchFilter, OrderingFilter]
	search_fields = ['content', 'user__first_name', 'user__last_name']
	pagination_class = PostPageNumberPagination

	def get_queryset(self):
		queryset_list = super(CommentListAPIView, self).get_queryset()
		query = self.request.GET.get('q')
		if query:
			queryset_list = queryset_list.filter(
				Q(content__icontains=query) |
				Q(user__first_name=query) |
				Q(user__last_name=query)
			)
		return queryset_list


class CommentDetailAPIView(DestroyModelMixin, UpdateModelMixin, RetrieveAPIView):
	permission_classes = [IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]
	queryset = Comment.objects.filter()  # include child comments
	serializer_class = CommentDetailSerializer

	def put(self, request, *args, **kwargs):
		return self.update(request, *args, **kwargs)

	def delete(self, request, *args, **kwargs):
		return  self.destroy(request, *args, **kwargs)
