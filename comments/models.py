from __future__ import unicode_literals

from django.conf import settings
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.db import models

# Create your models here.

class CommentManager(models.Manager):
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

	@property
	def get_user_name(self):
		if self.user:
			return self.user.username
		else:
			return 'Anonymous User'
