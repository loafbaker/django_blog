from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.CommentListAPIView.as_view(), name='list'),
    url(r'^(?P<pk>\d+)/$', views.CommentDetailAPIView.as_view(), name='thread'),
    # url(r'^(?P<pk>\d+)/delete/$', views.comment_delete, name='delete'),
]
