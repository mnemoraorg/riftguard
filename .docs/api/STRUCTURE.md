# Production-Grade Go API Structure

This document outlines the directory structure for the `apps/api` service. It follows the standard [Go Project Layout](https://github.com/golang-standards/project-layout) and adopts a "Clean Architecture" approach to ensure maintainability, testability, and scalability.

## Directory Structure

```text
apps/api/
├── cmd/
│   └── server/
│       └── main.go           # Entry point: Initializes config, DB, and starts the server
├── internal/
│   ├── api/
│   │   ├── handler/          # HTTP handlers (Gin-specific)
│   │   ├── middleware/       # Custom Gin middlewares (Auth, Logger, CORS)
│   │   └── router/           # Route registration and grouping
│   ├── config/
│   │   └── config.go         # Configuration loading (environment variables)
│   ├── domain/
│   │   ├── model/            # Business entities (Plain Go structs)
│   │   └── repository/       # Repository interfaces (abstraction layer)
│   ├── infra/
│   │   ├── database/         # Database connection and GORM initialization
│   │   └── repository/       # GORM implementations of domain interfaces
│   └── service/              # Business logic (Usecases) - Orchestrates domain and infra
├── pkg/                      # Shared utility code that could be used by other projects
├── scripts/                  # Development scripts (e.g., database migrations)
├── .air.toml                 # Configuration for live-reloading during development
├── Dockerfile                # Multi-stage production Docker build
├── Makefile                  # Automation for build, run, and test tasks
└── go.mod                    # Go dependencies
```

## Key Principles

### 1. Separation of Concerns

- **Domain**: Contains the core business logic and entities. It should not depend on any external frameworks (like Gin or GORM).
- **Service**: Orchestrates the flow of data. It depends on `domain` and `repository` interfaces.
- **API**: Handles the HTTP request/response cycle. It depends on `service`.
- **Infra**: Handles the technical details (GORM, PostgreSQL). It implements `domain/repository` interfaces.

### 2. Dependency Injection

Dependencies are passed into constructors (e.g., `NewUserService(repo)`). This makes the code highly testable as you can easily swap real database implementations with mocks.

### 3. Interface Segregation

The `domain/repository` defines _what_ the application needs from the database, while `infra/repository` defines _how_ it's implemented.

### 4. Production Readiness

- **Config**: Loads from the environment with sensible defaults.
- **Graceful Shutdown**: The server should handle `SIGINT` and `SIGTERM` to close database connections cleanly.
- **Logging**: Uses structured logging (e.g., `zap` or `slog`).
- **Migrations**: Uses a migration tool (e.g., `golang-migrate` or GORM AutoMigrate) to manage schema changes.
