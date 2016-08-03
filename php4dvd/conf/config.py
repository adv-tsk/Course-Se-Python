# -*- coding: utf-8 -*-

import os
import inspect

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe()))))

BASE_URL = ''

DEFAULT_BROWSER = 'firefox'

USER = ''
PASSWORD = ''


try:
    from .local_config import *
except ImportError:
    pass