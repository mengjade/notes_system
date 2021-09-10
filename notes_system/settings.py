import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'rha7*we-io_dbhnf$k)%wum_i=-fct9+n^j+@5j9p*$z01lzj1'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

from django.contrib.messages import constants as message_constants
MESSAGE_LEVEL = message_constants.DEBUG

ALLOWED_HOSTS = ['mengjade.pythonanywhere.com', '127.0.0.1']

# Application definition

INSTALLED_APPS = [
    'notes_system',
    'notes',
    'food',
    'redir',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]

HIGHLIGHTJS = {
# The URL to the jQuery JavaScript file
'jquery_url': '//code.jquery.com/jquery.min.js',
# The highlight.js base URL
'base_url': '//cdnjs.cloudflare.com/ajax/libs/highlight.js/8.3/highlight.min.js',
# The complete URL to the highlight.js CSS file
'css_url': '//cdnjs.cloudflare.com/ajax/libs/highlight.js/8.3/styles/{0}.min.css',
# Include jQuery with highlight.js JavaScript (affects django-highlightjs template tags)
'include_jquery': False,
# The default used style.
'style': 'monokai_sublime',
}

HIGHLIGHTJS = {
'style': 'github',
}

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
#    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware'
]

ROOT_URLCONF = 'notes_system.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': ["notes_system/templates"],
        'APP_DIRS': True,
        'OPTIONS': {
            'debug': DEBUG,
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'notes.static_var_import_processor.disqus',
                'food.static_var_import_processor.disqus',
                'redir.static_var_import_processor.disqus',
                'notes_system.static_var_import_processor.disqus',
            ],
        },
    },
]

WSGI_APPLICATION = 'notes_system.wsgi.application'

# Database
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

# Password validation
AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

import os
SETTINGS_PATH = os.path.dirname(os.path.dirname(__file__))

TEMPLATE_DIRS = (
    os.path.join(SETTINGS_PATH, 'templates'),
)

# Internationalization
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_L10N = True
USE_TZ = True

# Static files (CSS, JavaScript, Images)
STATICFILES_FINDERS = [
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
]
STATIC_URL = '/static/'
STATICFILES_DIRS = ( BASE_DIR, os.path.join(BASE_DIR, 'static'), )

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

#CUR_URL = "http://mengjade.pythonanywhere.com/"
#CUR_PATH = "/home/mengjade/newweb/myweb/"

CUR_URL = "http://127.0.0.1:8080/"
CUR_PATH = "C:/Users/peiyi/OneDrive/Desktop/newweb/myweb/"
