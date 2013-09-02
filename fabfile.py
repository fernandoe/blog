# -*- coding:utf-8 -*-
from fabric.api import *
from fabric_knife.dreamhost import *
from fabric_knife.deploy import *
import os

def dh():
    """
    Configura informações para deploy no dreamhost.
    """
    user     = os.environ.get('DH_USER')
    password = os.environ.get('DH_PASSWORD')
    host     = os.environ.get('DH_HOST')

    env.forward_agent = True
    env.hosts         = [host]
    env.user          = user
    env.password      = password

    env.git_repo        = 'git@github.com:fernandoe/blog.git'
    env.git_clone_path  = "~/blog.git"
    env.django_settings = 'server.settings.production'
    env.app_link        = '~/espindola.info'

#     env.tag = "2013.08.27_22.26"


