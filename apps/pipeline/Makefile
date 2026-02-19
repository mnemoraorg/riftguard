.PHONY: install dev run lint format test clean migrate-new migrate-up

# Variables
PYTHON := uv run python
ALEMBIC := uv run alembic

install:
	uv sync

dev:
	$(PYTHON) -m src.main serve --reload

run:
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
# Usages: 
# 1. make migrate-new msg="create_earthquake_table"
# 2. make migrate-up
migrate-new:
	$(ALEMBIC) revision --autogenerate -m "$(msg)"

migrate-up:
	$(ALEMBIC) upgrade head
