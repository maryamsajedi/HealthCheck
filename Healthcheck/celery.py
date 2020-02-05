from __future__ import absolute_import, unicode_literals

import os
from celery import Celery


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Healthcheck.settings')

celery_app = Celery('Healthcheck')
celery_app.config_from_object('django.conf:settings', namespace='CELERY')
celery_app.autodiscover_tasks(['services.check_health'])