import os
from celery import Celery

redis_url = "redis://localhost:6380"
app = Celery(
    "app",
    broker_url=redis_url,
    result_backend=redis_url,
)
