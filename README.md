# Celery error handling
Simple project where is shown how to catch errors raised in celery tasks

1. launch celery: celery -A proj worker --app=proj.celery_app:app --loglevel=debug
2. execute the launcher.py file: python launcher.py

Other launching options:
 - launch celery logging in file: celery -A proj worker --app=proj.celery_app:app --loglevel=debug --logfile=celery.log
 
 

