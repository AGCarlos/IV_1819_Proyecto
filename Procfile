web: flask db upgrade; flask translate compile; gunicorn app:app --log-file=-
worker: rq worker -u $REDIS_URL filecnc
