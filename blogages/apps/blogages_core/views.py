from django.core.urlresolvers import reverse
from django.shortcuts import get_object_or_404, render_to_response
from django.utils.functional import memoize
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import TemplateView, ListView as BaseListView

from bootstrap.views import (ListView,
                             CreateView,
                             UpdateView,
                             DeleteView)

from .models import (Post,
                     Comment,
                     User)

from .forms import CommentForm


class IndexView(BaseListView):
    """
    List published posts

    """
    template_name = 'index.html'

    queryset = Post.objects.filter(state='published')


class SingleView(TemplateView):
    """
    Display a single post

    """
    template_name = 'single.html'

    def get_context_data(self, slug):
        context = super(SingleView, self).get_context_data()
        context['object'] = get_object_or_404(Post, slug=slug)

        return context


@csrf_exempt
def preview(request, template_name='preview.html'):
    """
    Post preview

    TODO: Transform into a TemplateView class

    """
    text = request.POST.get('text', '')
    data = {'text': text}

    return render_to_response(template_name, data)


class PostCreateView(CreateView):
    """
    Post creation view.

    Set the current user as post author
    If the post get updated the first author remains

    """
    def get_form(self, form_class):
        form = super(PostCreateView, self).get_form(form_class)
        form.instance.user = self.request.user
        return form

    def get_template_names(self):
        return ('post_create.html',)


class PostUpdateView(UpdateView):
    """
    Post update view

    """
    def get_template_names(self):
        return ('post_update.html',)


class PostListView(ListView):
    """
    List posts

    """
    def get_template_names(self):
        return ('post_list.html',)


class CommentMixin(object):
    """
    Common comment forms methods

    """
    def _get_post(self):
        """
        Get comment post.

        This method uses memoization for caching

        """
        return self.get_object().content_object
    get_post = memoize(_get_post, {}, 1)

    def get_success_url(self):
        post_pk = self.get_post().pk
        return reverse('blogages_core:comment_list', args=(post_pk,))


class CommentUpdateView(CommentMixin, UpdateView):
    """
    Comment update
    
    """
    form_class = CommentForm


class CommentDeleteView(CommentMixin, DeleteView):
    """
    Comment removing

    """
    model = Comment


class PostCommentMixin(CommentMixin):
    """
    Common PostComment methods

    """
    def _get_post(self):
        """
        Get comment post.

        This method uses memoization for caching

        """
        post_pk = self.kwargs.get('post_pk', 0)
        return get_object_or_404(Post, pk=post_pk)
    get_post = memoize(_get_post, {}, 1)


class CommentCreateView(PostCommentMixin, CreateView):
    """
    Comment creation right now but may be used in future
    for replying other comments.

    """

    form_class = CommentForm

    def get_form(self, form_class):
        return self.form_class(self.get_post(), **self.get_form_kwargs())


class CommentListView(PostCommentMixin, ListView):
    """
    Comment listing

    """

    template_name = 'comment_list.html'
    model = Comment

    def get_queryset(self):
        """
        Filter comments from specific post

        """
        post_pk = self.get_post().pk
        queryset = super(CommentListView, self).get_queryset()
        return queryset.filter(object_pk=post_pk)

    def _get_create_url(self):
        kwargs = {'post_pk': self.get_post().pk}
        return reverse('blogages_core:comment_form', kwargs=kwargs)


class UserListView(ListView):
    """
    User listing

    """

    model = User

    def get_queryset(self):
        queryset = super(UserListView, self).get_queryset()
        # Exclude anonymous user
        queryset = queryset.exclude(pk=-1)

        return queryset
