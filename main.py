import pytest
import logging
from .tasks import debug_task, mul
from .app import redis_url

# Only works this way
@pytest.mark.celery(broker_url=redis_url, result_backend=redis_url)
# Worker initialized per test
@pytest.mark.usefixtures("celery_worker")
class TestCelery:
    def test_debug(self):
        logging.info("Debug task")
        response = debug_task.delay()
        assert response.get(timeout=10)

    def test_mul(self):
        logging.info("Mul task")
        response = mul.delay(2, 3)
        assert response.get(timeout=10) == 6
