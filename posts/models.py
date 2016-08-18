from __future__ import unicode_literals

from django.db import models
from django.conf import settings
from django.contrib.contenttypes.models import ContentType
from django.core.urlresolvers import reverse
from django.utils import timezone
from django.utils.safestring import mark_safe

from markdown_deux import markdown

# Create your models here.

from comments.models import Comment

class PostManager(models.Manager):
	def active(self, *args, **kwargs):
		return super(PostManager, self).filter(draft=False).filter(publish__lte=timezone.now())


def upload_location(instance, filename):
	return '%s/%s' % (instance.id, filename)

class Post(models.Model):
	user = models.ForeignKey(settings.AUTH_USER_MODEL)
	title = models.CharField(max_length=120)
	slug = models.SlugField(unique=True)
	image = models.ImageField(upload_to=upload_location,
		                      null=True, blank=True,
		                      width_field='width_field',
		                      height_field='height_field')
	width_field = models.IntegerField(default=0)
	height_field = models.IntegerField(default=0)
	content = models.TextField()
	read_time = models.TimeField(null=True, blank=True)
	draft = models.BooleanField(default=False)
	publish = models.DateTimeField(auto_now=False, auto_now_add=False)
	timestamp = models.DateTimeField(auto_now=False, auto_now_add=True)
	updated = models.DateTimeField(auto_now=True, auto_now_add=False)

	objects = PostManager()

	def __unicode__(self):
		return self.title

	def __str__(self):
		return self.title

	def get_absolute_url(self):
		return reverse('posts:detail', kwargs={'slug': self.slug})

	def get_api_url(self):
		return reverse('posts_api:detail', kwargs={'slug': self.slug})

	def get_markdown(self):
		content = self.content
		markdown_html = markdown(content)
		return mark_safe(markdown_html)

	@property
	def comments(self):
		qs = Comment.objects.filter_by_instance(self)
		return qs

	@property
	def get_content_type(self):
		content_type = ContentType.objects.get_for_model(self.__class__)
		return content_type

	@property
	def read_time_in_minutes(self):
		minutes = int(self.read_time.strftime('%-M'))
		if minutes == 1:
			result_str = '< 1 minute'
		else:
			result_str = '%s minutes' % (minutes)
		return result_str

	class Meta:
		ordering = ['-timestamp', '-updated']