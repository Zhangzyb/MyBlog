from celery import Celery
import os
import django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Blog.settings')
django.setup()

celery_app = Celery('Blog')
celery_app.config_from_object('celery_tasks.config')
celery_app.autodiscover_tasks(['celery_tasks.email'])