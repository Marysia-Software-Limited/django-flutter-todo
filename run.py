#!/usr/bin/env python

import os
from config import config, base_dir

args = f"--dart-entrypoint-args {config.APP_HOST}:{config.APP_PORT}"
app_dir = base_dir('frontend')

os.chdir(app_dir)
os.system(f'flutter run {args}')
