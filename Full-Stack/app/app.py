import os
import time
import redis
import psycopg2
from flask import Flask, jsonify

app = Flask(__name__)

# Connect to Redis
cache = redis.Redis(host="redis", port=6379, decode_responses=True)

def get_db():
    """Connect to PostgreSQL with retry logic for container startup."""
    for attempt in range(10):
        try:
            conn = psycopg2.connect(
                host="db",
                database=os.environ.get("POSTGRES_DB", "app_db"),
                user=os.environ.get("POSTGRES_USER", "app_user"),
                password=os.environ.get("POSTGRES_PASSWORD", "app_pass"),
            )
            return conn
        except psycopg2.OperationalError:
            time.sleep(1)
    raise Exception("Could not connect to PostgreSQL")

def init_db():
    """Create the visits table if it doesn't exist."""
    conn = get_db()
    cur = conn.cursor()
    cur.execute("""
        CREATE TABLE IF NOT EXISTS visits (
            id SERIAL PRIMARY KEY,
            count INTEGER NOT NULL,
            recorded_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    """)
    conn.commit()
    cur.close()
    conn.close()

@app.route("/")
def index():
    # Increment visit count in Redis
    count = cache.incr("hits")

    # Every 10 visits, persist the count to PostgreSQL
    if int(count) % 10 == 0:
        conn = get_db()
        cur = conn.cursor()
        cur.execute("INSERT INTO visits (count) VALUES (%s)", (count,))
        conn.commit()
        cur.close()
        conn.close()

    return jsonify(
        message="Hello from the Full-Stack Docker example!",
        visits=int(count),
    )

@app.route("/stats")
def stats():
    # Get current count from Redis
    current = cache.get("hits") or 0

    # Get persisted snapshots from PostgreSQL
    conn = get_db()
    cur = conn.cursor()
    cur.execute("SELECT count, recorded_at FROM visits ORDER BY id DESC LIMIT 5")
    rows = cur.fetchall()
    cur.close()
    conn.close()

    return jsonify(
        current_visits=int(current),
        recent_snapshots=[
            {"count": r[0], "recorded_at": r[1].isoformat()} for r in rows
        ],
    )

if __name__ == "__main__":
    init_db()
    app.run(host="0.0.0.0", port=5000)
