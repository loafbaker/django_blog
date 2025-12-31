from django.urls import path, re_path

from . import views

app_name = 'posts'

urlpatterns = [
    path('', views.PostListAPIView.as_view(), name='list'),
    path('create/', views.PostCreateAPIView.as_view(), name='create'),
    re_path(r'^(?P<slug>[\w-]+)/$', views.PostDetailAPIView.as_view(), name='detail'),
    re_path(r'^(?P<slug>[\w-]+)/edit/$', views.PostUpdateAPIView.as_view(), name='update'),
    re_path(r'^(?P<slug>[\w-]+)/delete/$', views.PostDeleteAPIView.as_view(), name='delete'),
]
