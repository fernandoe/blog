# -*- coding:utf-8 -*-
from server.settings.base import *
import os

#===================================================================================================
# ===============[ DJANGO ]===============
#===================================================================================================
db_name     = os.environ.get('DB_NAME')
db_user     = os.environ.get('DB_USER')
db_password = os.environ.get('DB_PASSWORD')
db_host     = os.environ.get('DB_HOST')

DEBUG = False
TEMPLATE_DEBUG = DEBUG
ALLOWED_HOSTS = [
    '.espindola.info'
]
STATIC_URL  = 'http://static.espindola.info/'
STATIC_ROOT = '/home/fernandoe003/static.espindola.info'
DATABASES = {
    'default' : {
        'ENGINE'   : 'django.db.backends.mysql',
        'NAME'     : db_name,
        'USER'     : db_user,
        'PASSWORD' : db_password,
        'HOST'     : db_host,
        'PORT'     : '',
        'OPTIONS': {
           'init_command': 'SET storage_engine=MyISAM',
        }
    },
}

