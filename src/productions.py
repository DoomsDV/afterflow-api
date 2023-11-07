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
        default='postgres://afterflowdb_user:jP7G7t77qloOlhvOAcz2vp4x2R40tGPO@dpg-cl17peis1bgc73fo7mo0-a.oregon-postgres.render.com/afterflowdb',
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