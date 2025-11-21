# Nginx Static Web Server

A simple Nginx web server serving a responsive login page using Alpine Linux for minimal image size.

## Features
- Lightweight Alpine-based Nginx container
- Responsive login form interface
- Bootstrap styling with custom CSS
- Minimal resource footprint

## Build & Run

```bash
# Build the image
docker build -t nginx-login .

# Run the container
docker run -p 8080:80 nginx-login
```

Access the application at `http://localhost:8080`

## Files
- `Dockerfile`: Alpine Nginx configuration
- `index.html`: Bootstrap login form
- `Procedure.md`: Detailed setup instructions

## Port Configuration
- Container port: 80
- Host port: 8080 (configurable)