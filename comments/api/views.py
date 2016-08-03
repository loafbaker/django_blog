from django.db.models import Q
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.generics import ListAPIView, RetrieveAPIView

from posts.api.pagination import PostPageNumberPagination

from comments.models import Comment
from .serializers import CommentListSerializer, CommentDetailSerializer

class CommentListAPIView(ListAPIView):
	queryset = Comment.objects.all()
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


class CommentDetailAPIView(RetrieveAPIView):
	queryset = Comment.objects.all()
	serializer_class = CommentDetailSerializer
