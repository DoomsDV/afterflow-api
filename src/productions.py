from .settings import *
import os
from dotenv import load_dotenv
import dj_database_url

load_dotenv()

SECRET_KEY = os.environ.get('SECRET_KEY')

DEBUG = os.environ.get('DEBUG') == 'True'

ALLOWED_HOSTS = ['afterflow-api.onrender.com']

DATABASES = {
    'default': dj_database_url.config(
        default = os.environ.get('DB_URI'),
        conn_max_age=600
    )
}

STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
STATIC_URL = '/static/'

STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'static'),
)

MIDDLEWARE += [
    'whitenoise.middleware.WhiteNoiseMiddleware',
]

STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

CACHES = {
    "default": {
        "BACKEND": "django_redis.cache.RedisCache",
        "LOCATION": "redis://red-cl6agvquuipc73ca5b20:6379",
        "OPTIONS": {
            "CLIENT_CLASS": "django_redis.client.DefaultClient",
        }
    }
}
