from Healthcheck.celery import celery_app

@celery_app.task(bind=True)
def check_health(url = "hi"):
   print(url)