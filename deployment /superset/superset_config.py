import os

SECRET_KEY = os.environ["SUPERSET_SECRET_KEY"]
SQLALCHEMY_DATABASE_URI = (
    "postgresql+psycopg2://"
    f"{os.environ['SUPERSET_DB_USER']}:{os.environ['SUPERSET_DB_PASSWORD']}"
    f"@db:5432/{os.environ['SUPERSET_DB_NAME']}"
)
WTF_CSRF_ENABLED = True
SESSION_COOKIE_HTTPONLY = True
SESSION_COOKIE_SAMESITE = "Lax"
# Set True only when accessed through HTTPS at a correctly configured proxy.
SESSION_COOKIE_SECURE = False
ENABLE_PROXY_FIX = False
