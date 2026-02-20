# Stage 1: Build the environment
FROM python:3.13-slim AS builder

ENV PYTHONUNBUFFERED=1
ENV PYTHONDONTWRITEBYTECODE=1

# Install uv
COPY --from=ghcr.io/astral-sh/uv:latest /uv /uvx /bin/

WORKDIR /build

# Copy only what's needed for dependencies first
COPY apps/pipeline/pyproject.toml apps/pipeline/uv.lock* ./

# Install dependencies into system site-packages so we don't need to copy a venv later
RUN uv pip compile pyproject.toml -o requirements.txt && \
    uv pip install --system --require-hashes -r requirements.txt || uv pip install --system .


# Stage 2: Final minimal image
FROM python:3.13-slim

ENV PYTHONUNBUFFERED=1
ENV PYTHONDONTWRITEBYTECODE=1

WORKDIR /app

# Copy system packages installed in builder stage
COPY --from=builder /usr/local/lib/python3.13/site-packages/ /usr/local/lib/python3.13/site-packages/
COPY --from=builder /usr/local/bin/ /usr/local/bin/

# Copy the actual application code and migrations
COPY apps/pipeline/src ./src
COPY apps/pipeline/alembic.ini ./alembic.ini
COPY apps/pipeline/migrations ./migrations

# Create a non-root user for security
RUN useradd -m appuser && chown -R appuser:appuser /app
USER appuser

EXPOSE 8000

# Run migrations and then uvicorn on start
CMD ["sh", "-c", "python -m alembic upgrade head && uvicorn src.main:app --host 0.0.0.0 --port 8000"]
