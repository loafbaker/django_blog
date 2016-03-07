from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse

# Create your views here.
from .models import Post

def post_create(request):
	return HttpResponse('<h1>Create</h1>')

def post_detail(request, id=None): # retrive
	instance = get_object_or_404(Post, id=id)
	context = {
		'instance': instance,
		'title': instance.title,
	}
	return render(request, 'post_detail.html', context)

def post_list(request): # list items
	if request.user.is_authenticated():
		queryset = Post.objects.all()
		context = {
			'object_list': queryset,
			'title': 'My User List',
		}
	else:
		context = {
			'title': 'List',
		}		
	return render(request, 'index.html', context)

def post_update(request):
	return HttpResponse('<h1>Update</h1>')

def post_delete(request):
	return HttpResponse('<h1>Delete</h1>')
