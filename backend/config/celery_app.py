import os
import raven
import celery

from django.conf import settings
from raven.contrib.celery import register_signal, register_logger_signal


class Celery(celery.Celery):

    def on_configure(self):
        if 'dsn' in settings.RAVEN_CONFIG:
            client = raven.Client(settings.RAVEN_CONFIG['dsn'])
            # register a custom filter to filter out duplicate logs
            register_logger_signal(client)
            # hook into the Celery error handler
            register_signal(client)


# set the default Django settings module for the 'celery' program.
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "backend.settings")
app = Celery('backend')

# Using a string here means the worker doesn't have to serialize
# the configuration object to child processes.
# - namespace='CELERY' means all celery-related configuration keys
#   should have a `CELERY_` prefix.
app.config_from_object('django.conf:settings', namespace='CELERY')

# Load task modules from all registered Django app configs.
app.autodiscover_tasks()
