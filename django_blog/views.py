from django.shortcuts import render, redirect

from rest_framework.response import Response
from rest_framework.reverse import reverse as api_reverse
from rest_framework.views import APIView

# Create your views here.

def home(request):
	return redirect('posts:list')

class APIHomeView(APIView):
	def get(self, request, format=None):
		data = {
			'users': {
				'register_url': api_reverse('users_api:register', request=request),
			},
			'posts': {
				'retrieve_url': api_reverse('posts_api:list', request=request),
				'create_url': api_reverse('posts_api:create', request=request),
			},
			'comments': {
				'retrieve_url': api_reverse('comments_api:list', request=request),
				'create_url': api_reverse('comments_api:create', request=request),
			},
		}
		return Response(data)