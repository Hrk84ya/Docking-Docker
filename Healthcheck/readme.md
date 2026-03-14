# Docker HEALTHCHECK Example

A minimal Go app that demonstrates the `HEALTHCHECK` Dockerfile instruction.

## How It Works

The app simulates a slow startup — it returns `503 Service Unavailable` on `/health` for the first 5 seconds, then switches to `200 OK`. Docker's health check mechanism detects this and reports the container status accordingly.

### HEALTHCHECK flags explained

```dockerfile
HEALTHCHECK --interval=10s --timeout=3s --start-period=5s --retries=3 \
  CMD curl -f http://localhost:8080/health || exit 1
```

| Flag             | Meaning                                              |
|------------------|------------------------------------------------------|
| `--interval=10s` | Run the check every 10 seconds                       |
| `--timeout=3s`   | Fail if the check takes longer than 3 seconds        |
| `--start-period=5s` | Grace period before checks count as failures      |
| `--retries=3`    | Mark unhealthy after 3 consecutive failures          |

## Running

```bash
cd Healthcheck
docker build -t healthcheck-demo .
docker run -d --name hc-demo -p 8080:8080 healthcheck-demo
```

## Watching the health status

```bash
# Check container health status
docker inspect --format='{{.State.Health.Status}}' hc-demo

# Watch it transition from "starting" → "healthy"
watch -n 2 'docker inspect --format="{{.State.Health.Status}}" hc-demo'
```

## Endpoints

| Route     | Description                          |
|-----------|--------------------------------------|
| `/`       | Simple greeting                      |
| `/health` | Returns 200 when healthy, 503 when starting |

## Cleanup

```bash
docker stop hc-demo && docker rm hc-demo
```
