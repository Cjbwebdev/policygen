#!/bin/bash
# Entrypoint script for Railway
set -e

echo "Starting PolicyGen on port $PORT..."

# Create a .railway_up flag file
touch /app/.railway_up

# Start healthcheck server in background (pure Python, no Django dependency)
python3 << 'PYEOF' &
import http.server
import socketserver
import threading
import time
import urllib.request

class HealthHandler(http.server.BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == '/health/':
            self.send_response(200)
            self.send_header('Content-Type', 'application/json')
            self.end_headers()
            self.wfile.write(b'{"status": "ok"}')
        else:
            self.send_response(302)
            self.send_header('Location', '/health/')
            self.end_headers()
    def log_message(self, format, *args):
        pass  # silence

PORT = int(__import__('os').environ.get('PORT', '8000'))
with socketserver.TCPServer(("", PORT), HealthHandler) as httpd:
    httpd.serve_forever()
PYEOF

HEALTH_PID=$!
echo "Healthcheck server running on PID $HEALTH_PID"

# Run migrations
echo "Running migrations..."
python manage.py migrate --noinput 2>&1 || echo "Migration warning (may be first run)"

# Start Django
echo "Starting Django server..."
gunicorn config.wsgi:application --bind 0.0.0.0:$PORT --timeout 120
