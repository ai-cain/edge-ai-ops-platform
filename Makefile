DC = docker compose

.PHONY: dev down logs backend-shell backend-test docs-install docs-build docs-serve

dev:
	$(DC) up --build backend db

down:
	$(DC) down -v

logs:
	$(DC) logs -f backend db

backend-shell:
	$(DC) exec backend sh

backend-test:
	cd backend && python -m pytest tests

docs-install:
	python -m pip install -r docs/requirements.txt

docs-build:
	python -m mkdocs build --strict

docs-serve:
	python -m mkdocs serve
