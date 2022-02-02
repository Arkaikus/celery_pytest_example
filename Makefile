all: with_fixtures with_worker

with_fixtures:
	pytest -vv -rA -x with_fixtures.py

with_worker:
	pytest -vv -rA -x with_worker.py

redis:
	docker compose up -d