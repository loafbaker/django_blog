from rest_framework import serializers

from accounts.api.serializers import UserDetailSerializer
from comments.api.serializers import CommentListSerializer

from posts.models import Post


class PostListSerializer(serializers.ModelSerializer):
	user = UserDetailSerializer(read_only=True)
	image = serializers.SerializerMethodField()
	url = serializers.HyperlinkedIdentityField(view_name='posts_api:detail', lookup_field='slug')
	class Meta:
		model = Post
		fields = [
			'title',
			'slug',
			'user',
			'content',
			'image',
			'publish',
			'url',
		]

	def get_image(self, obj):
		if obj.image:
			return obj.image.url
		else:
			return None

class PostCreateUpdateSerializer(serializers.ModelSerializer):
	class Meta:
		model = Post
		fields = [
			'title',
			'content',
			'publish',
		]

class PostDetailSerializer(serializers.ModelSerializer):
	user = UserDetailSerializer(read_only=True)
	html = serializers.SerializerMethodField()
	image = serializers.SerializerMethodField()
	comments = serializers.SerializerMethodField()
	class Meta:
		model = Post
		fields = [
			'id',
			'title',
			'slug',
			'user',
			'content',
			'html',
			'image',
			'publish',
			'comments',
		]

	def get_html(self, obj):
		return obj.get_markdown()

	def get_image(self, obj):
		if obj.image:
			return obj.image.url
		else:
			return None

	def get_comments(self, obj):
		return CommentListSerializer(obj.comments, many=True, context={'request': self.context['request']}).data

