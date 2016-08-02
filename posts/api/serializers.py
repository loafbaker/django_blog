from rest_framework import serializers

from posts.models import Post


class PostListSerializer(serializers.ModelSerializer):
	url = serializers.HyperlinkedIdentityField(view_name='posts_api:detail', lookup_field='slug')
	class Meta:
		model = Post
		fields = [
			'title',
			'slug',
			'content',
			'publish',
			'url',
		]

class PostCreateUpdateSerializer(serializers.ModelSerializer):
	class Meta:
		model = Post
		fields = [
			'title',
			'content',
			'publish',
		]

class PostDetailSerializer(serializers.ModelSerializer):
	class Meta:
		model = Post
		fields = [
			'id',
			'title',
			'slug',
			'content',
			'publish',
		]

