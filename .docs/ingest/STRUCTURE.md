# Ingest Service Structure (Python)

This document outlines the file structure for the `apps/ingest` service, designed as a production-grade Python data pipeline for fetching and processing USGS earthquake data. Using Python aligns well with data science and AI engineering workflows.

## Overview

The service is structured to support two primary modes of operation using a unified entry point:

1.  **Backfill (CLI Mode):** Run ad-hoc commands to fetch historical data.
2.  **Daemon (Cron/Service Mode):** Long-running process for scheduled ingestion.

## Directory Structure

We follow the "src layout" which is a best practice for Python application packaging, ensuring that import paths are clean and tests run against the installed package, not the local folder by accident.

```plaintext
apps/ingest/
├── src/
│   └── ingest/             # Main package source
│       ├── __init__.py
│       ├── main.py         # Entry point (Typer/Click CLI app)
│       ├── config.py       # Pydantic settings management
│       ├── constants.py    # Global constants
│       ├── adapters/       # Interfaces to external systems
│       │   ├── __init__.py
│       │   ├── usgs.py     # USGS API Client
│       │   └── database.py # Database interactions (SQLAlchemy/AsyncPG)
│       ├── domain/         # Domain models and business schemas
│       │   ├── __init__.py
│       │   └── models.py   # Pydantic models (e.g., Earthquake, Feature)
│       └── services/       # Business logic layer
│           ├── __init__.py
│           ├── pipeline.py # Core orchestration (fetching -> cleaning -> saving)
│           └── scheduler.py# Daemon loop logic (e.g., using APScheduler)
├── tests/                  # Test suite
│   ├── __init__.py
│   ├── conftest.py         # Pytest fixtures
│   ├── integration/        # Integration tests
│   └── unit/               # Unit tests
├── pyproject.toml          # Project metadata and dependencies (Modern standard)
├── uv.lock                 # Lock file (assuming 'uv' or 'poetry' for fast management)
├── Dockerfile              # Container definition
├── Makefile                # Automation commands
└── README.md               # Documentation
```

## Detailed Explanation

### `src/ingest/`

The core application code.

- **`main.py`**: The application entry point. We'll use **Typer** (built on Click) to creating a CLI with subcommands.
  - `python -m ingest backfill --start 2023-01-01 --end 2023-01-31`
  - `python -m ingest serve` (starts the scheduler/daemon)

- **`config.py`**: Uses **Pydantic Settings** (`BaseSettings`) to load configuration from environment variables (`.env`). This ensures type safety for your config (e.g., DB credentials, API keys).

- **`domain/models.py`**: Defines the data structures using **Pydantic**. This gives you automatic validation when parsing the USGS GeoJSON response. This is a stepping stone to AI engineering (structured data handling).

- **`adapters/`**:
  - **`usgs.py`**: Contains the logic to make HTTP requests to USGS. It returns Pydantic models, not raw JSON.
  - **`database.py`**: Handles database connections. For production, **SQLAlchemy (Async)** or **Prisma Client Python** are good choices.

- **`services/`**:
  - **`pipeline.py`**: Contains the `run_ingest(start_date, end_date)` function. This is the pure business logic that the CLI and Scheduler both call.
  - **`scheduler.py`**: Sets up a lightweight scheduler (like `APScheduler` or a simple infinite loop with `time.sleep`) to call `run_ingest` periodically.

### `tests/`

Separated from the source code.

- **`conftest.py`**: Define fixtures here, like a mock USGS client or an in-memory database session.

### `pyproject.toml`

The modern way to manage Python projects. It replaces `requirements.txt` and `setup.py`. It works great with tools like `uv` (extremely fast pip replacement) or `poetry`.

## Recommended Stack for AI/Data Engineering Focus

- **Language**: Python 3.12+
- **CLI**: Typer (User friendly, type-hint based)
- **Config**: Pydantic Settings
- **Data Validation**: Pydantic (Standard in the LLM/AI world)
- **HTTP Client**: Httpx (Async support)
- **Database**: SQLAlchemy 2.0 (Async) or Prisma
- **Package Manager**: `uv` (written in Rust, instant installs)

## Usage Scenarios

### 1. Backfill (CLI)

```bash
# Fetch data for a specific month
uv run python -m ingest backfill --start "2024-01-01" --end "2024-02-01"
```

### 2. Service/Daemon

```bash
# Run the scheduler
uv run python -m ingest start-server
```
