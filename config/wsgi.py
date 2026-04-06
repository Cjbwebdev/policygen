"""
WSGI config for PolicyGen — production deploy pipeline
"""
import os, subprocess
from pathlib import Path
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')

APP_DIR = Path(__file__).resolve().parent.parent

# 1. Run migrations at startup
subprocess.run(['python', 'manage.py', 'migrate', '--noinput', '--verbosity', '0'],
    capture_output=True, timeout=120, cwd=APP_DIR)

# 2. Collect static files if missing
STATIC_ROOT = APP_DIR / 'staticfiles'
if not STATIC_ROOT.exists():
    subprocess.run(['python', 'manage.py', 'collectstatic', '--noinput', '--verbosity', '0'],
        capture_output=True, timeout=60, cwd=APP_DIR)

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
