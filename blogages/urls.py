from django.conf.urls.defaults import patterns, include, url
from django.views.generic.simple import redirect_to
from django.conf import settings

from userena.views import profile_edit

from apps.blogages_core.forms import EditProfileForm
from apps.blogages_core.views import IndexView, SingleView

profile_dict = {'edit_profile_form': EditProfileForm}

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()


urlpatterns = patterns('',
    # Overrides default userena view for editing accounts
    # specifying a custom ProfileForm
    url(r'^admin/accounts/(?P<username>[.\w]+)/edit/$', profile_edit,
                                                        profile_dict,
                                                        name='userena_profile_edit'),

    # Userena urls
    url(r'^admin/accounts/', include('userena.urls')),

    # Blogages administration
    url(r'^admin/?$', redirect_to, {'url': '/admin/post/'}, name='home'),
    url(r'^admin/', include('apps.blogages_core.urls',
                            namespace='blogages_core')),
)

urlpatterns += patterns('',
    # Django comments framework urls
    url(r'^comments/', include('django.contrib.comments.urls')))

urlpatterns += patterns('apps.blogages_core.views',
    # List posts
    url(r'^$', IndexView.as_view(), name='index'),
    # Show post
    url(r'^(?P<slug>[^/]+)/?$', SingleView.as_view(), name='single'))


if settings.DEBUG and getattr(settings, 'DEVELOPMENT', False):
    from django.contrib.staticfiles.urls import staticfiles_urlpatterns
    urlpatterns += staticfiles_urlpatterns()
else:
    urlpatterns += patterns('',
        url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {
            'document_root': settings.MEDIA_ROOT,
        }),
        url(r'^static/(?P<path>.*)$', 'django.views.static.serve', {
            'document_root': settings.STATIC_ROOT,
        }))
