import os
from src import productions
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from dotenv import load_dotenv
from apps.api.views import index

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('apps.api.urls')),
    path('', index),
]
load_dotenv()

if os.environ.get('DEBUG') == 'True':
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
elif os.environ.get('DEBUG') == 'False':
    urlpatterns += static(productions.STATIC_URL, document_root=productions.STATIC_ROOT)
