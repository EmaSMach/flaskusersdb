# --*-- encoding: utf-8 --*--
from __future__ import unicode_literals
import os


class DevelopementConfig(object):
    """
    Configurations for the development stage.
    """
    APPLICATION_DIR = os.path.dirname(os.path.realpath(__file__))
    DEBUG = True
    SQlALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(APPLICATION_DIR, 'db.sqlite3')
    WTF_CSRF_ENABLED = True
    SECRET_KEY = 'dev'
