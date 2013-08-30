# -*- coding:utf-8 -*-
from fabric.api import *
from fabric.contrib.files import exists
import os
import time


def dh():
    pass


# Exemplos:
#fab producao deploy:TESTE
def deploy(tag=None):
    git_tag(tag)
    git_clone()
    git_checkout()
    copying_to_release()
    symlink_current_release()
    install_requirements()
    database_migrate()
    collectstatic()
    restart_webserver()


def git_tag(tag=None):
    if tag is None:
        tag_name = time.strftime('%Y.%m.%d_%H.%M')
        local('git tag %s' % tag_name)
        local('git push origin %s' % tag_name)
        env.tag = tag_name
    else:
        env.tag = tag


def git_clone():
    require('git_repo', provided_by=[dh])
    require('git_clone_path', provided_by=[dh])
    if not exists("%(git_clone_path)s" % env):
        run("git clone %(git_repo)s %(git_clone_path)s" % env)
        with cd("%(git_clone_path)s" % env):
            run("git submodule update --init")


def git_checkout():
    require('git_clone_path', provided_by=[dh])
    with cd("%(git_clone_path)s" % env):
        run("git fetch")
        run("git checkout %(tag)s" % env)
        run("git submodule update --init")


def copying_to_release():
    require('tag', provided_by=[dh])
    require('git_clone_path', provided_by=[dh])
    if not exists("~/releases/%(tag)s" % env):
        run('mkdir -p ~/releases/%(tag)s' % env)
        with cd("%(git_clone_path)s" % env):
            run("cp -r . ~/releases/%(tag)s" % env)


def symlink_current_release():
    require('tag', provided_by=[dh])
    run("rm %(app_link)s" % env, quiet=True)
    with cd("~"):
        run('ln -s ~/releases/%(tag)s %(app_link)s' % env)


def install_requirements():
    with cd("%(app_link)s" % env):
        run("pip install -r  requirements/production.txt", warn_only='ignore')


def database_migrate():
    require('django_settings', provided_by=[dh])
    with cd("%(app_link)s/source" % env):
        run("python manage.py syncdb --settings=%(django_settings)s" % env)


def collectstatic():
    require('django_settings', provided_by=[dh])
    with cd("~/queropagar.com.br/source"):
        run("python manage.py collectstatic --noinput --settings=%(django_settings)s" % env)


def restart_webserver():
    run('killall python2.7')


