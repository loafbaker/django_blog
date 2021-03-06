from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.contenttypes.models import ContentType
from django.http import HttpResponseRedirect, HttpResponse, Http404
from django.shortcuts import render

# Create your views here.

from .forms import CommentForm
from .models import Comment

def comment_thread(request, id):
	try:
		comment = Comment.objects.get(id=id)
	except Comment.DoesNotExist:
		raise Http404

	# Render form only when the comment is a first-layered one
	if comment.first_layered():
		initial_data = {
			'content_type': comment.get_content_type,
			'object_id': comment.id,
		}
		form = CommentForm(request.POST or None, initial=initial_data)
		if request.method == 'POST' and form.is_valid():
			# Gather usual data
			c_type = form.cleaned_data.get('content_type')
			content_type = ContentType.objects.get(model=c_type)
			obj_id = form.cleaned_data.get('object_id')
			content_data = form.cleaned_data.get('content')

			if request.user.is_authenticated():
				new_comment = Comment.objects.create(
						user=request.user,
						content_type=content_type,
						object_id=obj_id,
						content=content_data,
					)
			else:
				new_comment = Comment.objects.create(
						content_type=content_type,
						object_id=obj_id,
						content=content_data,
					)
			return HttpResponseRedirect(new_comment.content_object.get_absolute_url())
		context = {
			'comment': comment,
			'form': form,
		}
	else:
		context = {
			'comment': comment,
		}
	return render(request, 'comment_thread.html', context)

@login_required()
def comment_delete(request, id):
	try:
		comment = Comment.objects.get(id=id)
	except Comment.DoesNotExist:
		raise Http404

	if comment.user != request.user or not comment.user:
		response = HttpResponse('You do not have permission to delete this.')
		response.status_code = 403
		return response

	if request.method == 'POST':
		parent_obj_url = comment.content_object.get_absolute_url()
		children = comment.children()
		if children.count() > 0:
			for child in children:
				child.delete()
		comment.delete()
		messages.success(request, 'This comment has been deleted.')
		return HttpResponseRedirect(parent_obj_url)
	context = {
		'comment': comment,
	}
	return render(request, 'confirm_delete.html', context)