DC = docker compose

.PHONY: dev down logs backend-shell frontend-shell backend-lint backend-test frontend-install frontend-build docs-install docs-build docs-serve ci-local

dev:
	$(DC) up --build frontend backend db

down:
	$(DC) down -v

logs:
	$(DC) logs -f frontend backend db

backend-shell:
	$(DC) exec backend sh

frontend-shell:
	$(DC) exec frontend sh

backend-lint:
	cd backend && python -m ruff check app tests

backend-test:
	cd backend && python -m pytest tests

frontend-install:
	cd frontend && npm install

frontend-build:
	cd frontend && npm run build

docs-install:
	python -m pip install -r docs/requirements.txt

docs-build:
	python -m mkdocs build --strict

docs-serve:
	python -m mkdocs serve

ci-local:
	$(MAKE) backend-lint
	$(MAKE) backend-test
	$(MAKE) frontend-build
	$(MAKE) docs-build
	$(DC) config
