from django.urls import re_path

from . import views

app_name = 'comments'

urlpatterns = [
    re_path(r'^(?P<id>\d+)/$', views.comment_thread, name='thread'),
    re_path(r'^(?P<id>\d+)/delete/$', views.comment_delete, name='delete'),
]
