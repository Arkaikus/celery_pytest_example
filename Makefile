all:
	pytest -vv -rA -x main.py
redis:
	docker compose up -d