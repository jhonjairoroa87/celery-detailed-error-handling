from __future__ import absolute_import

from celery import Celery

app = Celery('proj', broker='redis://localhost:6379')

app.conf.update(
    CELERY_TASK_RESULT_EXPIRES=3600,
    CELERY_IMPORTS=("proj.tasks", )
)
