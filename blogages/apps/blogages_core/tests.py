from django.test import TestCase

from django_fsm.db.fields import TransitionNotAllowed

from apps.blogages_core.models import Post


class WorkflowTest(TestCase):
    def test_post_workflow(self):
        # create post (default state: draft)
        post = Post.objects.create(title='Post Title',
                                   text='Some long text')
        self.assertEqual(post.state, 'draft')

        # publish post
        post.publish()
        self.assertEqual(post.state, 'published')

        # post can not be published again
        self.assertRaises(TransitionNotAllowed, post.publish)
