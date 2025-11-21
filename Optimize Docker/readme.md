# Optimized Docker Build

Multi-stage Docker build demonstrating optimization techniques for Python applications.

## Optimization Features
- Multi-stage build to reduce final image size
- Alpine Linux base for minimal footprint
- No-cache pip installation
- Separate build and runtime stages

## Build & Run

```bash
# Build the optimized image
docker build -t python-optimized .

# Run the container
docker run python-optimized
```

## Files
- `Dockerfile`: Multi-stage build configuration
- `main.py`: Simple pandas data processing script
- `readme.md`: Additional documentation

## Optimization Techniques
- Build stage: Install dependencies and prepare application
- Runtime stage: Copy only necessary files
- `--no-cache-dir`: Prevents pip cache storage
- Alpine base: Minimal Linux distribution