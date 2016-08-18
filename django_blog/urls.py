"""django_blog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls import url, include
from django.conf.urls.static import static
from django.contrib import admin

from accounts import views as account_views
from .views import home

urlpatterns = [
    url(r'^$', home, name='home'),
    url(r'^comments/', include('comments.urls', namespace='comments')),
    url(r'^posts/', include('posts.urls', namespace='posts')),
    url(r'^login/$', account_views.login_view, name='login'),
    url(r'^register/$', account_views.register_view, name='register'),
    url(r'^logout/$', account_views.logout_view, name='logout'),

    # APIs
    url(r'^api/users/', include('accounts.api.urls', namespace='users_api')),
    url(r'^api/comments/', include('comments.api.urls', namespace='comments_api')),
    url(r'^api/posts/', include('posts.api.urls', namespace='posts_api')),

    # Backend
    url(r'^admin/', admin.site.urls),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
