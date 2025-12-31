from django.urls import path, re_path

from . import views

app_name = 'comments'

urlpatterns = [
    path('', views.CommentListAPIView.as_view(), name='list'),
    path('create/', views.CommentCreateAPIView.as_view(), name='create'),
    re_path(r'^(?P<pk>\d+)/$', views.CommentDetailAPIView.as_view(), name='thread'),
    # url(r'^(?P<pk>\d+)/delete/$', views.comment_delete, name='delete'),
]
