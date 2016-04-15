from django.contrib import messages
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.db.models import Q
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone

# Create your views here.
from comments.models import Comment
from .models import Post
from .forms import PostForm

def post_create(request):
	if not (request.user.is_staff or request.user.is_superuser):
		raise Http404
	form = PostForm(request.POST or None, request.FILES or None)
	if form.is_valid():
		instance = form.save(commit=False)
		instance.user = request.user
		instance.save()
		messages.success(request, 'Successfully Created.')
		return HttpResponseRedirect(instance.get_absolute_url())
	context = {
		'form': form,
		'button': 'Create Post',
	}
	return render(request, 'post_form.html', context)

def post_detail(request, slug=None): # retrive
	instance = get_object_or_404(Post, slug=slug)
	if not (request.user.is_staff or request.user.is_superuser):
		if instance.draft or instance.publish > timezone.now():
			raise Http404
	context = {
		'instance': instance,
		'title': instance.title,
	}
	return render(request, 'post_detail.html', context)

def post_list(request): # list items
	if request.user.is_staff or request.user.is_superuser:
		queryset_list = Post.objects.all()
	else:
		queryset_list = Post.objects.active()
	today = timezone.now()
	query = request.GET.get('q')
	if query:
		queryset_list = queryset_list.filter(
			Q(title__icontains=query) |
			Q(content__icontains=query) |
			Q(user__first_name=query) |
			Q(user__last_name=query)
			)
	paginator = Paginator(queryset_list, 10) # Show 10 posts per page
	page_request_token = 'page'
	page = request.GET.get(page_request_token)
	try:
		queryset = paginator.page(page)
	except PageNotAnInteger:
		# If page is not an integer, deliver first page.
		queryset = paginator.page(1)
	except EmptyPage:
		# If page is out of range (e.g. 9999), deliver last page of results.
		queryset = paginator.page(paginator.num_pages)
	context = {
		'object_list': queryset,
		'title': 'Post List',
		'page_request_token': page_request_token,
		'today': today,
	}
	return render(request, 'post_list.html', context)

def post_update(request, slug=None):
	if not (request.user.is_staff or request.user.is_superuser):
		raise Http404
	instance = get_object_or_404(Post, slug=slug)
	if instance.user != request.user:
		raise Http404
	form = PostForm(request.POST or None, request.FILES or None, instance=instance)
	if form.is_valid():
		instance = form.save(commit=False)
		instance.user = request.user
		instance.save()
		messages.success(request, 'Item Saved.')
		return HttpResponseRedirect(instance.get_absolute_url())
	context = {
		'instance': instance,
		'title': instance.title,
		'form': form,
		'button': 'Update Post',
	}
	return render(request, 'post_form.html', context)

def post_delete(request, slug=None):
	if not (request.user.is_staff or request.user.is_superuser):
		raise Http404
	instance = get_object_or_404(Post, slug=slug)
	if instance.user != request.user:
		raise Http404
	instance.delete()
	messages.success(request, 'Successfully Deleted.')
	return redirect('posts:list')
