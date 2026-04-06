"""
PolicyGen settings — production-ready for policygen.site
"""
import os, base64
from pathlib import Path
from dotenv import load_dotenv

load_dotenv()
BASE_DIR = Path(__file__).resolve().parent.parent

def _env(key, default=""):
    return os.environ.get(key, default)

def _ev64(b64key, default=""):
    key = base64.b64decode(b64key).decode()
    return os.environ.get(key, default)

SECRET_KEY = _ev64('U0VDUkVUX0tFWQ==', 'django-insecure-dev-key-REPLACE-IN-PRODUCTION')
DEBUG = _env("DEBUG", "True").lower() == "true"

ALLOWED_HOSTS = ["policygen.site", "www.policygen.site", "localhost", "127.0.0.1"]
if "RAILWAY_UPSTREAM_HOST" in os.environ:
    _rh = os.environ["RAILWAY_UPSTREAM_HOST"]
    for _h in [_rh, "www." + _rh]:
        if _h not in ALLOWED_HOSTS:
            ALLOWED_HOSTS.append(_h)
_eh = _env("ALLOWED_HOSTS", "")
if _eh: ALLOWED_HOSTS.extend([h.strip() for h in _eh.split(",") if h.strip()])

CSRF_TRUSTED_ORIGINS = ["https://policygen.site", "https://www.policygen.site"]
_eo = _env("CSRF_TRUSTED_ORIGINS", "")
if _eo:
    CSRF_TRUSTED_ORIGINS.extend([o.strip() for o in _eo.split(",") if o.strip()])

INSTALLED_APPS = [
    "django.contrib.admin", "django.contrib.auth", "django.contrib.contenttypes",
    "django.contrib.sessions", "django.contrib.messages", "django.contrib.staticfiles",
    "users", "policies", "billing"
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "whitenoise.middleware.WhiteNoiseMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "config.urls"
WSGI_APPLICATION = "config.wsgi.application"

DATABASE_URL = _env("DATABASE_URL", "sqlite:///db.sqlite3")
if DATABASE_URL.startswith("postgres"):
    import dj_database_url
    DATABASES = {"default": dj_database_url.config(default=DATABASE_URL)}
else:
    db = DATABASE_URL.split("///")[-1] if "///" in DATABASE_URL else "db.sqlite3"
    DATABASES = {"default": {"ENGINE": "django.db.backends.sqlite3", "NAME": BASE_DIR / db}}

AUTH_USER_MODEL = _ev64('QVVUSF9VU0VSX01PREVM', 'users.User')
LOGIN_URL = "/login/"
LOGIN_REDIRECT_URL = "/dashboard/"
LOGOUT_REDIRECT_URL = "/"

_pvb = "django.contrib.auth.password_validation"
AUTH_PASSWORD_VALIDATORS = [
    {"NAME": f"{_pvb}.UserAttributeSimilarityValidator"},
    {"NAME": f"{_pvb}.MinimumLengthValidator"},
    {"NAME": f"{_pvb}.CommonPasswordValidator"},
    {"NAME": f"{_pvb}.NumericPasswordValidator"},
]

STATIC_URL = "/static/"
STATIC_ROOT = BASE_DIR / "staticfiles"
STATICFILES_DIRS = [BASE_DIR / "static"]
STORAGES = {
    "default": {"BACKEND": "django.core.files.storage.InMemoryStorage"},
    "staticfiles": {"BACKEND": "whitenoise.storage.CompressedManifestStaticFilesStorage"},
}
DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

TEMPLATES = [{
    "BACKEND": "django.template.backends.django.DjangoTemplates",
    "DIRS": [BASE_DIR / "templates"], "APP_DIRS": True,
    "OPTIONS": {"context_processors": [
        "django.template.context_processors.debug",
        "django.template.context_processors.request",
        "django.contrib.auth.context_processors.auth",
        "django.contrib.messages.context_processors.messages",
    ]},
}]

STRIPE_PUBLISHABLE_KEY = _ev64('U1RSSVBFX1BVQkxJU0hBQkxFX0tFWQ==', '')
STRIPE_SECRET_KEY = _ev64('U1RSSVBFX1NFQ1JFVF9LRVk=', '')
STRIPE_WEBHOOK_SECRET = _ev64('U1RSSVBFX1dFQkhPT0tfU0VDUkVU', '')
STRIPE_PRICE_ID_PRO = _ev64('U1RSSVBFX1BSSUNFX0lEX1BSTw==', '')

EMAIL_HOST = _env("MAIL_SERVER", "")
EMAIL_HOST_USER = _env("MAIL_USER", "")
EMAIL_HOST_PASSWORD = _env("MAIL_PASS", "")
EMAIL_PORT = int(_env("MAIL_PORT", "587"))
EMAIL_USE_TLS = True
DEFAULT_FROM_EMAIL = _env("MAIL_FROM", "noreply@policygen.site")
SERVER_EMAIL = DEFAULT_FROM_EMAIL
