# -*- coding:utf-8 -*-
from server.settings.base import *

DEBUG = True
TEMPLATE_DEBUG = DEBUG
ALLOWED_HOSTS = ["127.0.0.1",]

DATABASES = {
    'default' : {
        'ENGINE'   : 'django.db.backends.mysql',
        'NAME'     : 'blog',
        'USER'     : 'root',
        'PASSWORD' : '',
        'HOST'     : '',
        'PORT'     : '',
        'OPTIONS': {
           'init_command': 'SET storage_engine=MyISAM',
        }
    },
}

