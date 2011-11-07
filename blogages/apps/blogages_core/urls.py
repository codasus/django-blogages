from django.conf.urls.defaults import patterns, url

from bootstrap.urls import (bootstrap_pattern,
                            bootstrap_list,
                            bootstrap_create,
                            bootstrap_update,
                            bootstrap_delete)

from .forms import (PostForm,
                    UserForm)

from .views import (PostListView,
                    PostCreateView,
                    PostUpdateView,
                    CommentListView,
                    CommentCreateView,
                    CommentUpdateView,
                    CommentDeleteView,
                    UserListView,
                    preview)

# Post: create, read, update, delete
urlpatterns = bootstrap_pattern(PostForm,
                                create_view=PostCreateView,
                                update_view=PostUpdateView,
                                list_view=PostListView)

# User: create, read, delete (for updating we use userena)
urlpatterns += bootstrap_pattern(UserForm,
                                 update_view=None,
                                 list_view=UserListView)

urlpatterns += patterns('',
    # comments-related views (per post)
    bootstrap_list(r'post/(?P<post_pk>[^/]+)/comments/$',
                   'comment_list',
                   view=CommentListView.as_view()),
    bootstrap_create(r'post/(?P<post_pk>[^/]+)/comments/add/$',
                     'comment_form',
                     view=CommentCreateView.as_view()),
    bootstrap_update(r'comment/(?P<pk>[^/]+)/$',
                     'comment_form',
                     view=CommentUpdateView.as_view()),
    bootstrap_delete(r'comment/(?P<pk>[^/]+)/delete/$',
                     'comment_delete',
                     view=CommentDeleteView.as_view()))

urlpatterns += patterns('',
    # post preview
    url(r'post/preview/$', preview, name='post_preview'))
