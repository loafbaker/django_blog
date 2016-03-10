from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib import messages

# Create your views here.
from .models import Post
from .forms import PostForm

def post_create(request):
	form = PostForm(request.POST or None)
	if form.is_valid():
		instance = form.save(commit=False)
		instance.save()
		messages.success(request, 'Successfully Created.')
		return HttpResponseRedirect(instance.get_absolute_url())
	else:
		messages.error(request, 'Fail to Create.')
	context = {
		'form': form,
	}
	return render(request, 'post_form.html', context)

def post_detail(request, id=None): # retrive
	instance = get_object_or_404(Post, id=id)
	context = {
		'instance': instance,
		'title': instance.title,
	}
	return render(request, 'post_detail.html', context)

def post_list(request): # list items
	queryset = Post.objects.all()
	context = {
		'object_list': queryset,
		'title': 'My User List',
	}
	return render(request, 'index.html', context)

def post_update(request, id=None):
	instance = get_object_or_404(Post, id=id)
	form = PostForm(request.POST or None, instance=instance)
	if form.is_valid():
		instance = form.save(commit=False)
		instance.save()
		messages.success(request, 'Item Saved.')
		return HttpResponseRedirect(instance.get_absolute_url())
	context = {
		'instance': instance,
		'title': instance.title,
		'form': form,
	}
	return render(request, 'post_form.html', context)

def post_delete(request):
	return HttpResponse('<h1>Delete</h1>')
