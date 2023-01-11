import os

from beret_utils import get_config
from beret_utils.config import bool_value, EnvValue
from beret_utils import PathData

base_dir = PathData.main()

DEFAULT_CONFIG = (
    ('PROJECT_NAME', 'todo'),
    ('DB_ENGINE', 'django.db.backends.sqlite3'),
    ('DB_NAME', base_dir('db.sqlite3').path),
    ('DB_USER', ''),
    ('DB_PASSWORD', ''),
    ('DB_HOST', ''),
    ('DB_PORT', ''),
    ('PROJECT_APP', base_dir.name),
    ('SECRET_KEY', "very_secret"),
    ("DJANGO_SECRET_KEY", EnvValue('SECRET_KEY')),
    ('DJANGO_DEBUG', True, bool_value),
    ('DJANGO_EMAIL_BACKEND', "django.core.mail.backends.console.EmailBackend"),
    ("DJANGO_ALLOWED_HOSTS", "ala.hipisi.org.pl eskape.marysia.app localhost"),
    ('APP_HOST', '127.0.0.1'),
    ('APP_PORT', '8085'),

)

ENV_FILES = (
    '.local.env',
    '.env',
)

Config = get_config(DEFAULT_CONFIG, ENV_FILES)
config = Config()

if __name__ == '__main__':
    for key, value in config.items():
        print(f"{key}={value}")
