import os
from dotenv import load_dotenv
load_dotenv()

from django.core.asgi import get_asgi_application
if os.environ.get('DEBUG') == 'True':
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'src.settings')
else:
    os.environ.setdefault('DJANGO_SETTINGS_MODULE','src.productions')

application = get_asgi_application()
