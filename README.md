## celery_pytest_example

celery test example with pytest-celery

- Create virtualenv
- Install requirements `pip install -r requirements.txt`
- Run redis `make redis`
- Run tests with `make` or
  - `make with_fixtures`
  - `make with_worker`
  - `pytest -vv -rA -x with_fixtures.py`
  - `pytest -vv -rA -x with_worker.py`

## django troubleshooting

- https://stackoverflow.com/a/46564964
- https://medium.com/@solankiarpit1997/testing-celery-tasks-a8a3568d0213