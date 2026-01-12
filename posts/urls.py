from django.urls import path

from . import views

app_name = 'posts'

urlpatterns = [
    path('', views.post_list, name='list'),
    path('create/', views.post_create),
    path('<slug:slug>/', views.post_detail, name='detail'),
    path('<slug:slug>/edit/', views.post_update, name='update'),
    path('<slug:slug>/delete/', views.post_delete),
]
