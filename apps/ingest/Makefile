.PHONY: install dev run lint format test clean migrate-new migrate-up

# Variables
PYTHON := uv run python
ALEMBIC := uv run alembic

install:
	uv sync

dev:
	# Run the daemon/server in development mode
	$(PYTHON) -m src.main serve --reload

run:
	# Example: make run cmd="backfill --start 2024-01-01"
	$(PYTHON) -m src.main $(cmd)

lint:
	uv run ruff check .
	uv run mypy src

format:
	uv run ruff check --fix .
	uv run ruff format .

test:
	uv run pytest

clean:
	find . -type d -name "__pycache__" -exec rm -rf {} +
	find . -type f -name "*.pyc" -delete

# Database Migrations
migrate-new:
	# Usage: make migrate-new msg="create_earthquake_table"
	$(ALEMBIC) revision --autogenerate -m "$(msg)"

migrate-up:
	$(ALEMBIC) upgrade head
