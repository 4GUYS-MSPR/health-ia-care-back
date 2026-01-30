import os
import sys

from django.core.wsgi import get_wsgi_application

from logs.logger import logger

def handle_exception(exc_type, exc_value, exc_traceback):
    if issubclass(exc_type, KeyboardInterrupt):
        sys.__excepthook__(exc_type, exc_value, exc_traceback)
        return
    logger.log.exception("Uncaught exception", exc_info=(exc_type, exc_value, exc_traceback))

sys.excepthook = handle_exception

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'healthIA.settings')

application = get_wsgi_application()
