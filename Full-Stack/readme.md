# Full-Stack Multi-Service Docker Example

A Flask API backed by PostgreSQL and Redis, orchestrated with Docker Compose.

## Architecture

- **web** — Flask API that serves requests and tracks visits
- **db** — PostgreSQL for persistent storage (visit snapshots)
- **redis** — Redis for fast in-memory visit counting

## How It Works

1. Every request to `/` increments a visit counter in Redis
2. Every 10th visit, the count is persisted to PostgreSQL
3. The `/stats` endpoint shows the current count and recent snapshots

## Running

```bash
cd Full-Stack
docker compose up --build
```

## Endpoints

| Route    | Description                              |
|----------|------------------------------------------|
| `/`      | Returns a greeting and current visit count |
| `/stats` | Returns current count + last 5 DB snapshots |

## Stopping

```bash
docker compose down          # stop containers
docker compose down -v       # stop and remove the database volume
```
