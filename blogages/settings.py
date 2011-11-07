# Django settings for blogages project.
from os.path import abspath, dirname, join
from sys import path as sys_path

# Project root
PROJECT_ROOT = dirname(abspath(join(__file__)))

# Thirdy-party libraries
sys_path.insert(0, join(PROJECT_ROOT, 'libs'))

# djangoappengine settings
from djangoappengine.settings_base import *

ADMINS = (
    # ('Your Name', 'your_email@example.com'),
)

MANAGERS = ADMINS

# For more details about the code below, take a look at:
# http://groups.google.com/group/django-non-relational/msg/d324fb578daf0c1d
#DATABASES['native'] = { 
#    'ENGINE': 'djangoappengine.db', 
#    'HIGH_REPLICATION': False, 
#    'DEV_APPSERVER_OPTIONS': { 
#        'high_replication' : False, 
#        'use_sqlite': False,
#    } 
#} 

#DATABASES['native'] = DATABASES['default']
#DATABASES['default'] = {'ENGINE': 'dbindexer', 'TARGET': 'native'}

DBINDEXER_SITECONF = 'dbindexes'

# Local time zone for this installation. Choices can be found here:
# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
# although not all choices may be available on all operating systems.
# On Unix systems, a value of None will cause Django to use the same
# timezone as the operating system.
# If running in a Windows environment this must be set to the same as your
# system time zone.
TIME_ZONE = 'America/Chicago'

# Language code for this installation. All choices can be found here:
# http://www.i18nguy.com/unicode/language-identifiers.html
LANGUAGE_CODE = 'en-us'

SITE_ID = 5023

# If you set this to False, Django will make some optimizations so as not
# to load the internationalization machinery.
USE_I18N = True

# If you set this to False, Django will not format dates, numbers and
# calendars according to the current locale
USE_L10N = False

# Absolute filesystem path to the directory that will hold user-uploaded files.
# Example: "/home/media/media.lawrence.com/media/"
MEDIA_ROOT = join(PROJECT_ROOT, 'media', '')

# URL that handles the media served from MEDIA_ROOT. Make sure to use a
# trailing slash.
# Examples: "http://media.lawrence.com/media/", "http://example.com/media/"
MEDIA_URL = '/media/'

# Absolute path to the directory static files should be collected to.
# Don't put anything in this directory yourself; store your static files
# in apps' "static/" subdirectories and in STATICFILES_DIRS.
# Example: "/home/media/media.lawrence.com/static/"
STATIC_ROOT = join(PROJECT_ROOT, 'static', '')

# URL prefix for static files.
# Example: "http://media.lawrence.com/static/"
STATIC_URL = '/static/'

# URL prefix for admin static files -- CSS, JavaScript and images.
# Make sure to use a trailing slash.
# Examples: "http://foo.com/static/admin/", "/static/admin/".
ADMIN_MEDIA_PREFIX = '/static/admin/'

# Additional locations of static files
STATICFILES_DIRS = (
    # Put strings here, like "/home/html/static" or "C:/www/django/static".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
)

# List of finder classes that know how to find static files in
# various locations.
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
#    'django.contrib.staticfiles.finders.DefaultStorageFinder',
)

# Make this unique, and don't share it with anybody.
SECRET_KEY = 'psd3d)^$%1b)am$j41+p9q0wm3ev2n#@-kf!5!14t!_8smn*3+'

# List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
#     'django.template.loaders.eggs.Loader',
)

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'apps.blogages_core.middleware.LoginRequiredMiddleware',
)

ROOT_URLCONF = 'urls'

TEMPLATE_DIRS = (
    # Put strings here, like "/home/html/django_templates" or "C:/www/django/templates".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
    join(PROJECT_ROOT, 'templates'),
)

INSTALLED_APPS = (
    # theme
    'themes.default_theme',

    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.comments',
    'django.contrib.markup',
    # Uncomment the next line to enable the admin:
    # 'django.contrib.admin',
    # Uncomment the next line to enable admin documentation:
    # 'django.contrib.admindocs',

    # apps
    'apps.blogages_core',
    'apps.input_mask',

    # libs
    'bootstrap',
    'userena',

    # appengine specific
    'djangotoolbox',
    'autoload',
    'dbindexer',
    'djangoappengine',
)

# A sample logging configuration. The only tangible logging
# performed by this configuration is to send an email to
# the site admins on every HTTP 500 error.
# See http://docs.djangoproject.com/en/dev/topics/logging for
# more details on how to customize your logging configuration.
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'mail_admins': {
            'level': 'ERROR',
            'class': 'django.utils.log.AdminEmailHandler'
        }
    },
    'loggers': {
        'django.request': {
            'handlers': ['mail_admins'],
            'level': 'ERROR',
            'propagate': True,
        },
    }
}

DATE_INPUT_FORMATS = ('%m/%d/%Y',)

TEMPLATE_CONTEXT_PROCESSORS = (
    "django.contrib.auth.context_processors.auth",
    "django.core.context_processors.debug",
    "django.core.context_processors.i18n",
    "django.core.context_processors.media",
    "django.core.context_processors.static",
    "django.contrib.messages.context_processors.messages",
    "django.contrib.auth.context_processors.auth",
    "django.core.context_processors.auth",
)

AUTHENTICATION_BACKENDS = (
    'userena.backends.UserenaAuthenticationBackend',
    'django.contrib.auth.backends.ModelBackend',
)

LOGIN_REDIRECT_URL = '/admin/'
LOGIN_URL = '/admin/accounts/signin/'
SIGNUP_URL = '/admin/accounts/signup/'
LOGOUT_URL = '/admin/accounts/signout/'

LOGIN_REQUIRED_URLS = ('^admin/',)
LOGIN_EXEMPT_URLS = ('^admin/accounts/signin/$',
                     '^admin/accounts/signup/$')

ANONYMOUS_USER_ID = -1
AUTH_PROFILE_MODULE = 'blogages_core.Profile'

USERENA_DISABLE_PROFILE_LIST = True
USERENA_SIGNIN_REDIRECT_URL = LOGIN_REDIRECT_URL

GAE_SETTINGS_MODULES = (
    'apps.blogages_core.gae_settings',
)

try:
    from local_settings import *
except:
    pass
