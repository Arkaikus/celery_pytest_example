import logging
from .app import app
from .tasks import debug_task, mul
from celery.contrib.testing.worker import start_worker


class TestCelery:
    def setup_class(cls):
        logging.info("Setup celery worker")
        cls.worker = start_worker(app, perform_ping_check=False)
        cls.worker.__enter__()

    def teardown_class(cls):
        logging.info("Teardown celery worker")
        cls.worker.__exit__(None, None, None)

    def test_debug(self):
        logging.info("Debug task")
        response = debug_task.delay()
        assert response.get(timeout=10)

    def test_mul(self):
        logging.info("Mul task")
        response = mul.delay(2, 3)
        assert response.get(timeout=10) == 6
