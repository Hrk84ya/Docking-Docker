# Stage 1: Build
FROM golang:1.22-alpine AS build
WORKDIR /src
COPY main.go .
RUN go build -o /app main.go

# Stage 2: Run
FROM alpine:3.19
RUN apk add --no-cache curl
COPY --from=build /app /app

EXPOSE 8080

# Health check: runs every 10s, allows 3s per check, 
# waits 5s before first check, fails after 3 consecutive failures
HEALTHCHECK --interval=10s --timeout=3s --start-period=5s --retries=3 \
  CMD curl -f http://localhost:8080/health || exit 1

CMD ["/app"]
