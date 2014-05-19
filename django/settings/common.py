from django.conf.global_settings import TEMPLATE_CONTEXT_PROCESSORS as TCP
from configurations import Configuration


class Common(Configuration):
    MEDIA_ROOT = ''

    MEDIA_URL = ''

    DEBUG = True
    TEMPLATE_DEBUG = DEBUG
    ADMINS = (
    )
    MANAGERS = ADMINS
    ALLOWED_HOSTS = []
    TIME_ZONE = 'America/Chicago'
    LANGUAGE_CODE = 'en-au'
    SITE_ID = 1
    USE_I18N = True
    USE_L10N = True
    USE_TZ = True

    STATIC_ROOT = 'static'

    STATIC_URL = '/static/'

    STATICFILES_DIRS = (
    )
    STATICFILES_FINDERS = (
        'django.contrib.staticfiles.finders.FileSystemFinder',
        'django.contrib.staticfiles.finders.AppDirectoriesFinder'
    )

    TEMPLATE_CONTEXT_PROCESSORS = (
        'django.contrib.auth.context_processors.auth',
        'django.core.context_processors.debug',
        'django.core.context_processors.i18n',
        'django.core.context_processors.request',
        'django.core.context_processors.static',
        'django.contrib.messages.context_processors.messages',

    )

    SECRET_KEY = '-k+)^!_o5pc#ir^t$ctbalum07m_5a50xxjx8$_*+hzloblcxk'

    TEMPLATE_LOADERS = (
        'django.template.loaders.filesystem.Loader',
        'django.template.loaders.app_directories.Loader',
    )

    MIDDLEWARE_CLASSES = (
        'django.middleware.common.CommonMiddleware',
        'django.contrib.sessions.middleware.SessionMiddleware',
        'django.middleware.csrf.CsrfViewMiddleware',
        'django.contrib.auth.middleware.AuthenticationMiddleware',
        'django.contrib.messages.middleware.MessageMiddleware',
        'corsheaders.middleware.CorsMiddleware',
    )
    CORS_ORIGIN_ALLOW_ALL = True

    ROOT_URLCONF = 'main.urls'

    WSGI_APPLICATION = 'main.wsgi.application'

    TEMPLATE_DIRS = (
    )

    AUTHENTICATION_BACKENDS = (
      'django.contrib.auth.backends.ModelBackend',
    )

    INSTALLED_APPS = (
        'django.contrib.auth',
        'django.contrib.contenttypes',
        'django.contrib.sessions',
        'django.contrib.sites',
        'django.contrib.messages',
        'django.contrib.staticfiles',
        'suit',
        'rest_framework',
        'rest_framework.authtoken',
        'main',
        'south',
        'corsheaders',
        'django.contrib.admin',
    )

    AUTH_PROFILE_MODULE = 'main.UserProfile'

    TEMPLATE_CONTEXT_PROCESSORS = TCP + (
        'django.core.context_processors.request',
        )

    SESSION_SERIALIZER = 'django.contrib.sessions.serializers.JSONSerializer'

    LOGGING = {
        'version': 1,
        'disable_existing_loggers': False,
        'filters': {
            'require_debug_false': {
                '()': 'django.utils.log.RequireDebugFalse'
            }
        },
        'handlers': {
            'mail_admins': {
                'level': 'ERROR',
                'filters': ['require_debug_false'],
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

    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3', # Add 'postgresql_psycopg2', 'mysql', 'sqlite3' or 'oracle'.
            'NAME': 'ffrpg.sql',                      # Or path to database file if using sqlite3.
            # The following settings are not used with sqlite3:
            'USER': '',
            'PASSWORD': '',
            'HOST': '',                      # Empty for localhost through domain sockets or '127.0.0.1' for localhost through TCP.
            'PORT': '',                      # Set to empty string for default.
        }
    }

    REST_FRAMEWORK = {

        'PAGINATE_BY': 0,
        'DEFAULT_PAGINATION_SERIALIZER_CLASS':
            'main.jsonfix.CustomPaginationSerializer',
        'DEFAULT_RENDERER_CLASSES': (
            'main.jsonfix.CustomJSONRenderer',
            'rest_framework.renderers.BrowsableAPIRenderer',
        ),
        'DEFAULT_AUTHENTICATION_CLASSES': (
            'rest_framework.authentication.TokenAuthentication',
        ),
        'DEFAULT_FILTER_BACKENDS': ('rest_framework.filters.DjangoFilterBackend',)

    }