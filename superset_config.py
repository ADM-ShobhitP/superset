import os
from flask_cors import CORS
from celery.schedules import crontab
import smtplib
ROW_LIMIT = 5000

ENABLE_CORS = True
TALISMAN_ENABLED = False
HTTP_HEADERS = {}
CORS_OPTIONS = {
    "supports_credentials": True,
    "allow_headers":[ "*"],
    "resources": ["*"],
    "origins": ["http://localhost:3000", "http://10.1.15.88:3000"]
}

def apply_cors(app):
    CORS(app, **CORS_OPTIONS)

SECRET_KEY = '04f8996da763b7a969b1028ee3007569eaf3a635486ddab211d512c85b9df8fb'

SQLALCHEMY_DATABASE_URI = os.environ.get(
    'SUPERSET_DB_URI',
    'postgresql://postgres:password@localhost:5432/superset'
)

SESSION_COOKIE_SECURE = True
# Flask-WTF flag for CSRF
WTF_CSRF_ENABLED = False
# Add endpoints that need to be exempt from CSRF protection
WTF_CSRF_EXEMPT_LIST = ["/api/v1/security/csrf_token/"]
# A CSRF token that expires in 1 year
WTF_CSRF_TIME_LIMIT = 60 * 60 * 24 * 365

MAPBOX_API_KEY = ''


FEATURE_FLAGS = {
    "EMBEDDED_SUPERSET": True,
    "ALERT_REPORTS": True,
}


ENABLE_GUEST_TOKEN = True
GUEST_ROLE_NAME = 'embed_dashboard'
GUEST_TOKEN_JWT_SECRET = "0d7e28a46511d33e9251c69dbadcdddd4f77760732f1725ab9fc1914918a615e"
GUEST_TOKEN_JWT_EXP_SECONDS = 3600

ENABLE_TEMPLATE_PROCESSING = True
JINJA_CONTEXT_ADDONS = {
    'custom_id_visit_date_filter': lambda id, visit_date: f"{id} -- {visit_date}"
}




class CeleryConfig:
    BROKER_URL = "redis://localhost:6379/0"
    CELERY_IMPORTS = ("superset.sql_lab",)
    CELERY_RESULT_BACKEND = "redis://localhost:6379/0"
    CELERYD_PREFETCH_MULTIPLIER = 10
    CELERY_ACKS_LATE = True
    CELERY_ANNOTATIONS = {"tasks.add": {"rate_limit": "10/s"}}
    CELERYBEAT_SCHEDULE = {
        "email_reports": {
            "task": "superset.tasks.email_reports",
            "schedule": crontab(minute="*/10"),  # Runs every 10 minutes
        }
    }

CELERY_CONFIG = CeleryConfig

SCREENSHOT_LOCATE_WAIT = 100
SCREENSHOT_LOAD_WAIT = 600


EMAIL_NOTIFICATIONS = True
SMTP_HOST = "smtp.gmail.com"
SMTP_PORT = 587
SMTP_STARTTLS = True
SMTP_SSL = False
SMTP_USER = "shobhitprakash8@gmail.com"
SMTP_PASSWORD = "okfaxuzxzmmbkxum"
SMTP_MAIL_FROM = "shobhitprakash8@gmail.com"
EMAIL_REPORTS_SUBJECT_PREFIX = "[Superset] "

WEBDRIVER_TYPE = "chrome"
WEBDRIVER_OPTION_ARGS = [
    "--force-device-scale-factor=2.0",
    "--high-dpi-support=2.0",
    "--headless",
    "--disable-gpu",
    "--disable-dev-shm-usage",
    "--no-sandbox",
    "--disable-setuid-sandbox",
    "--disable-extensions",
]

WEBDRIVER_BASEURL = "http://localhost:8088"
WEBDRIVER_BASEURL_USER_FRIENDLY = "http://localhost:8088"

