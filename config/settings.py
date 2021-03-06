
from pathlib import Path
import os

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-tymevw#byo6sf#kz-bs2coyfw(q&0yntj1o#bdgge&bbg$j&ei'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    # Axes app can be in any position in the INSTALLED_APPS list.
    'axes',
    'rest_framework',
    'rest_framework.authtoken',
    'account',
    'djoser',
    'mainapp',
    'corsheaders',
    'drugs',
 
    'django_otp.plugins.otp_static',
    'django_otp.plugins.otp_totp',

]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',

    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',


    # AxesMiddleware should be the last middleware in the MIDDLEWARE list.
    # It only formats user lockout messages and renders Axes lockout responses
    # on failed user authentication attempts from login views.
    # If you do not want Axes to override the authentication response
    # you can skip installing the middleware and use your own views.
    'axes.middleware.AxesMiddleware',
]

ROOT_URLCONF = 'config.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR/'templates'),
        os.path.join(BASE_DIR/'mainapp/templates'),
        os.path.join(BASE_DIR/'account/templates'),
        os.path.join(BASE_DIR/'drugs/templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'config.wsgi.application'
SILENCED_SYSTEM_CHECKS = ['axes.W003']
AXES_FAILURE_LIMIT = 3
AXES_LOCK_OUT_AT_FAILURE = True


# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework.authentication.BasicAuthentication',
        'rest_framework.authentication.SessionAuthentication',
        'rest_framework.authentication.TokenAuthentication',
    ),

    'DEFAULT_PERMISSION_CLASSES':(
        'rest_framework.permissions.IsAuthenticated',
        'rest_framework.permissions.IsAdminUser'
    )


}


AUTHENTICATION_BACKENDS = [
    # AxesBackend should be the first backend in the AUTHENTICATION_BACKENDS list.
    'axes.backends.AxesBackend',

    # Django ModelBackend is the default authentication backend.
    'django.contrib.auth.backends.ModelBackend',
]

# AUTH_USER_MODEL = 'authentification.User'


# DJOSER = {
#     'LOGIN_FIELD':'email',
#     "USER_CREATE_PASSWORD_RETYPE":True,
#     'SERIALIZERS':{
#         'user_create':'authentification.serializer.UserCreateSerializer',
#         'user':'authentification.serializer.UserCreateSerializer',
#         # 'current_user':'authentification.serializer.CurrentUserSerializer'
#     }
# }

CORS_ALLOW_ALL_ORIGINS = True
PASSWORD_RESET_TIMEOUT_DAYS = 1

# Password validation
# https://docs.djangoproject.com/en/3.2/ref/settings/#auth-password-validators

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


# Internationalization
# https://docs.djangoproject.com/en/3.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.2/howto/static-files/


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.2/howto/static-files/
STATIC_URL = '/static/'
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static_files'),
]

STATIC_ROOT = os.path.join('static_cdn')

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join('media_cdn')

# Default primary key field type
# https://docs.djangoproject.com/en/3.2/ref/settings/#default-auto-field
AUTH_USER_MODEL = "account.User"
# LOGIN_REDIRECT_URL = "/"
# LOGIN_URL = "/account/login/"
# LOGIN_URL = "two_factor:login"


DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

EMAIL_USE_TLS = True
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_HOST_USER = 'thomasambetsa@gmail.com'
EMAIL_HOST_PASSWORD = 'wojjleviqxakkazs'
EMAIL_PORT = 587
