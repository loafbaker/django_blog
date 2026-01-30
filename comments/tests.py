from django.test import TestCase
from django.utils import timezone
from django.contrib.auth import get_user_model

from comments.api.serializers import create_comment_serializer
from posts.models import Post
from comments.models import Comment


User = get_user_model()


class CommentReplySerializerTests(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username='reply_tester',
            email='reply_tester@example.com',
            password='testpass1234',
        )
        self.post = Post.objects.create(
            user=self.user,
            title='Test Post',
            slug='test-post',
            content='Test content',
            publish=timezone.now(),
        )
        self.root_comment = Comment.objects.create_by_model_type(
            model_type='post',
            slug=self.post.slug,
            parent_id=None,
            content='Root comment',
            user=self.user,
        )

    def test_reply_serializer_accepts_parent_comment(self):
        serializer_cls = create_comment_serializer(
            model_type='comment',
            parent_id=self.root_comment.id,
            user=self.user,
        )
        serializer = serializer_cls(data={'content': 'Reply comment'})
        self.assertTrue(serializer.is_valid(), serializer.errors)
        reply = serializer.save()
        self.assertEqual(reply.parent, self.root_comment)
