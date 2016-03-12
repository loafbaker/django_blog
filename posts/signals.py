from __future__ import unicode_literals

from django.db.models.signals import pre_save
from django.utils.text import slugify

from .models import Post


def create_slug(instance, slug_id=0):
    slug = slugify(instance.title)
    if slug_id != 0:
        slug = '%s-%s' % (slug, slug_id)
    exists = Post.objects.filter(slug=slug).exists()
    if exists:
        return create_slug(instance, slug_id+1)
    return slug


def pre_save_post_receiver(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = create_slug(instance)


pre_save.connect(pre_save_post_receiver, sender=Post)