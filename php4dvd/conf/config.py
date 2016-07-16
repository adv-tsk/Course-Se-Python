# -*- coding: utf-8 -*-


BASE_URL = ''

USER = ''
PASSWORD = ''


try:
    from .local_config import *
except ImportError:
    pass