from django.contrib.contenttypes.models import ContentType
from django.contrib.auth import get_user_model

from rest_framework import serializers

from comments.models import Comment


User = get_user_model()


def create_comment_serializer(model_type='post', slug=None, parent_id=None, user=None):
    class CommentCreateSerializer(serializers.ModelSerializer):
        class Meta:
            model = Comment
            fields = [
                'id',
                'content',
                'timestamp',
            ]

        def __init__(self, *args, **kwargs):
            self.model_type = model_type
            # For the post
            if slug:
                self.slug = slug
            else:
                self.slug = None
            # For the comment
            if parent_id:
                self.parent_id = parent_id
            else:
                self.parent_id = None
            return super(CommentCreateSerializer, self).__init__(*args, **kwargs)

        def validate(self, data):
            data_valid = False
            model_type = self.model_type
            try:
                model = ContentType.objects.get(model=model_type)
            except:
                raise serializers.ValidationError('This is not a valid content type.')
            some_model = model.model_class()
            # Case 1: model type is post
            if model_type == 'post':
                try:
                    object = some_model.objects.get(slug=self.slug)
                    data_valid = True
                except:
                    raise serializers.ValidationError('This is not a valid slug for the post object.')
            # Case 2: model type is comment
            elif model_type == 'comment':
                try:
                    ## If allow multi-layer comment thread,
                    # object = some_model.objects.get(id=parent_id)
                    ##  otherwise,
                    object = some_model.objects.all().get(id=parent_id)
                    data_valid = True
                except:
                    raise serializers.ValidationError('This is not a valid parent id for the comment object.')
            if data_valid:
                return data
            else:
                raise serializers.ValidationError('No slug or parent id provided.')

        def create(self, validated_data):
            content = validated_data.get('content')
            model_type = self.model_type
            slug = self.slug
            parent_id = self.parent_id
            if user:
                comment = Comment.objects.create_by_model_type(model_type, slug, parent_id, content, user)
            else:
                comment = Comment.objects.create_by_model_type(model_type, slug, parent_id, content)
            return comment

    return CommentCreateSerializer

class CommentListSerializer(serializers.ModelSerializer):
    reply_count = serializers.SerializerMethodField()
    url = serializers.HyperlinkedIdentityField(view_name='comments_api:thread', lookup_field='pk')
    class Meta:
        model = Comment
        fields = [
            'id',
            'content',
            'timestamp',
            'reply_count',
            'url',
        ]

    def get_reply_count(self, obj):
        if obj.first_layered():
            return obj.children().count()
        else:
            return 0

class CommentChildSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = [
            'content',
            'timestamp',
        ]

class CommentDetailSerializer(serializers.ModelSerializer):
    content_object_url = serializers.SerializerMethodField()
    reply_count = serializers.SerializerMethodField()
    replies = serializers.SerializerMethodField()
    class Meta:
        model = Comment
        fields = [
            'id',
            'content_object_url',
            'content',
            'timestamp',
            'reply_count',
            'replies',
        ]
        read_only_fields = [
            'timestamp',
            'reply_count',
            'replies',
        ]

    def get_content_object_url(self, obj):
        url = obj.content_object.get_api_url()
        return self.context['request'].build_absolute_uri(url)

    def get_reply_count(self, obj):
        if obj.first_layered():
            return obj.children().count()
        else:
            return 0

    def get_replies(self, obj):
        if obj.first_layered():
            return CommentChildSerializer(obj.children(), many=True).data
        else:
            return None