import json
import os

from beret_utils import get_config
from beret_utils.config import bool_value, EnvValue
from beret_utils import PathData

base_dir = PathData.main()

DEFAULT_CONFIG = (
    ('PROJECT_NAME', 'todo'),
    ('POSTGRES_ENGINE', 'django.db.backends.postgresql'),
    ('POSTGRES_DB', 'todo'),
    ('POSTGRES_USER', 'beret'),
    ('POSTGRES_PASSWORD', '6649beret'),
    ('POSTGRES_HOST', '127.0.0.1'),
    ('POSTGRES_PORT', ''),
    ('PROJECT_APP', base_dir.name),
    ('SECRET_KEY', "django-insecure-aj#exo2bw$h%ps^hr4o+ch)e_u2ao1j19rd6z0q)l1o#e!9rn5"),
    ("DJANGO_SECRET_KEY", EnvValue('SECRET_KEY')),
    ('DJANGO_DEBUG', True, bool_value),
    ('DJANGO_EMAIL_BACKEND', "django.core.mail.backends.console.EmailBackend"),
    ("DJANGO_ALLOWED_HOSTS", "ala.hipisi.org.pl eskape.marysia.app localhost"),
    ('APP_HOST', '127.0.0.1'),
    ('APP_PORT', '8085'),

)

ENV_FILES = (
    '.env',
    '.local.env',
)

Config = get_config(DEFAULT_CONFIG, ENV_FILES)
config = Config()

if __name__ == '__main__':
    print(config)
