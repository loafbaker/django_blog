from __future__ import unicode_literals

from django.conf import settings
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.core.urlresolvers import reverse
from django.db import models

# Create your models here.

class CommentManager(models.Manager):
	def all(self):
		content_type = ContentType.objects.get(model='post')
		qs = super(CommentManager, self).filter(content_type=content_type)
		return qs

	def filter_by_instance(self, instance):
		content_type = ContentType.objects.get_for_model(instance.__class__)
		obj_id = instance.id
		qs = super(CommentManager, self).filter(content_type=content_type, object_id=obj_id)
		return qs

class Comment(models.Model):
	user = models.ForeignKey(settings.AUTH_USER_MODEL, null=True, blank=True) # Allow Anonymous user

	content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
	object_id = models.PositiveIntegerField()
	content_object = GenericForeignKey('content_type', 'object_id')

	content = models.TextField()
	timestamp = models.DateTimeField(auto_now=False, auto_now_add=True)

	objects = CommentManager()

	def __unicode__(self):
		return self.get_user_name  # str(self.user.username)

	def __str__(self):
		return self.get_user_name  # str(self.user.username)

	class Meta:
		ordering = ['-timestamp']

	def get_absolute_url(self):
		return reverse('comments:thread', kwargs={'id': self.id})

	@property
	def get_user_name(self):
		if self.user:
			return self.user.username
		else:
			return 'Anonymous User'

	@property
	def get_content_type(self):
		content_type = ContentType.objects.get_for_model(self.__class__)
		return content_type

	# Replies to this comment
	def children(self):
		return Comment.objects.filter_by_instance(self)

	# If the instance's parent is a post,
	# then the instance is the root comment
	def first_layered(self):
		return self.content_type.model == 'post'

	@property
	def parent(self):
		if self.first_layered():
			return None
		else:
			return self.content_object
