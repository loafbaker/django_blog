from rest_framework import serializers

from comments.models import Comment


class CommentListSerializer(serializers.ModelSerializer):
    reply_count = serializers.SerializerMethodField()
    url = serializers.HyperlinkedIdentityField(view_name='comments_api:thread', lookup_field='pk')
    class Meta:
        model = Comment
        fields = [
            'id',
            'content_type',
            'object_id',
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
    reply_count = serializers.SerializerMethodField()
    replies = serializers.SerializerMethodField()
    class Meta:
        model = Comment
        fields = [
            'id',
            'content_type',
            'object_id',
            'content',
            'timestamp',
            'reply_count',
            'replies',
        ]

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