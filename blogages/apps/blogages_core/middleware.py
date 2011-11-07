"""
Thankfully taken from:
http://djangosnippets.org/snippets/1179/
"""

from django.http import HttpResponseRedirect
from django.conf import settings
from django.contrib.auth.models import User

from re import compile

EXEMPT_URLS = [compile(settings.LOGIN_URL.lstrip('/'))]

if hasattr(settings, 'LOGIN_EXEMPT_URLS'):
    EXEMPT_URLS += [compile(expr) for expr in settings.LOGIN_EXEMPT_URLS]

if hasattr(settings, 'LOGIN_REQUIRED_URLS'):
    LOGIN_REQUIRED_URLS = [compile(expr) for expr in settings.LOGIN_REQUIRED_URLS]

class LoginRequiredMiddleware:
    """
    Middleware that requires a user to be authenticated to view any page other
    than LOGIN_URL. Exemptions to this requirement can optionally be specified
    in settings via a list of regular expressions in LOGIN_EXEMPT_URLS (which
    you can copy from your urls.py).

    Requires authentication middleware and template context processors to be
    loaded. You'll get an error if they aren't.
    """
    def process_request(self, request):
        assert hasattr(request, 'user'), "The Login Required middleware\
 requires authentication middleware to be installed. Edit your\
 MIDDLEWARE_CLASSES setting to insert\
 'django.contrib.auth.middlware.AuthenticationMiddleware'. If that doesn't\
 work, ensure your TEMPLATE_CONTEXT_PROCESSORS setting includes\
 'django.core.context_processors.auth'."
        path = request.path_info.lstrip('/')
        
        if any(m.match(path) for m in LOGIN_REQUIRED_URLS):
            if not any(m.match(path) for m in EXEMPT_URLS):
                if User.objects.filter(is_staff=True).count() == 0:
                    return HttpResponseRedirect(settings.SIGNUP_URL)

                if not request.user.is_authenticated():
                    return HttpResponseRedirect(settings.LOGIN_URL)
