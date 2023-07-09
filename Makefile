run:
	celery -A celery_app worker --loglevel=info --concurrency=2 & python3 app.py