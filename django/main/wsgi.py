import os
import sys

sys.path.append(os.path.dirname(os.path.abspath(__file__)) + '/..' )
sys.path.append(os.path.dirname(os.path.abspath(__file__)) + '/../main')

os.environ["DJANGO_SETTINGS_MODULE"] = "settings.live"
os.environ["DJANGO_CONFIGURATION"] = "Live"

from configurations.wsgi import get_wsgi_application
application = get_wsgi_application()