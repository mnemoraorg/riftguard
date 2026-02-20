# Pipeline Database & Migrations

The `apps/pipeline` service uses PostgreSQL (v17) and Alembic for database schema migrations. Because the service is containerized using Docker, all migration commands must be executed within the context of the running Docker container to ensure they have access to the correct environment variables, models, and the database network.

## Automatic Migrations on Startup

The Docker container is configured to automatically run database migrations every time it starts up.

If you look in the `docker-compose.yml` (and `.infra/pipeline/Dockerfile`), the start command includes:

```bash
python -m alembic upgrade head
```

This guarantees that your database schema is always up-to-date with the latest code before the `uvicorn` server begins accepting requests.

## Workflow: Updating the Database Schema

When you modify or create new database models in `apps/pipeline/src/domain`, you need to generate a new migration script and apply it to the database.

Handy shortcut scripts have been provided in `apps/pipeline/package.json`.

**Requirement:** Your Docker compose network (e.g., `bun turbo dev`) must be actively running before executing these commands!

### Step 1: Generate a New Migration

After saving changes to your Python models, generate a new migration script describing the change:

```bash
cd apps/pipeline
bun run db:generate "add_user_profile_table"
```

_What this does:_ This runs `docker compose exec` to run Alembic _inside_ the container. Alembic analyzes your Python models, compares them to the tables currently in the Docker database, and automatically creates a new SQL migration file in `apps/pipeline/migrations/versions/`.

### Step 2: Apply the Migration

You can apply this new migration to your database in one of two ways:

**Option A (Automatic Application):**
Simply stop your dev server (`Ctrl+C`) and start it again (`bun turbo dev`). The container's startup script will automatically detect the new migration file and apply it before booting the API.

**Option B (Manual Application):**
To apply the changes immediately without having to restart the development server, run:

```bash
cd apps/pipeline
bun run db:migrate
```

_What this does:_ This runs `python -m alembic upgrade head` directly against the running database, executing the migration files and officially altering your PostgreSQL schema.
