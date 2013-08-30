# -*- coding:utf-8 -*-
from fabric.api import *


def dh():
    pass


def dh_bootstrap():
    """
    Prepara o ambiente para rodar uma aplicação Django.
    """
    run('mkdir -p ~/downloads')
    run("echo 'alias ll=\"ls -la --color=auto\"' >> ~/.bash_profile")
    dh_install_python()
    dh_install_setup_tools()
    dh_install_pip()
    dh_install_mysql_python()


def dh_install_python():
    """
    Instala a versão do python 2.7.3
    """
    with cd('~/downloads'):
        run('wget http://www.python.org/ftp/python/2.7.3/Python-2.7.3.tgz')
        run('tar -xzvf Python-2.7.3.tgz')
        with cd('Python-2.7.3'):
            run('./configure --prefix=$HOME/opt')
            run('make')
            run('make install')
            run("echo 'export PATH=$HOME/opt/bin:$PATH' >> ~/.bash_profile")


def dh_install_setup_tools():
    """
    Realiza a instalação do setup tools.
    """
    with cd('~/downloads'):
        run('wget http://peak.telecommunity.com/dist/ez_setup.py')
        run('python ez_setup.py')


def dh_install_pip():
    """
    Realiza a instalação do pip
    """
    with cd('~/downloads'):
        run('curl -O https://pypi.python.org/packages/source/p/pip/pip-1.4.1.tar.gz')
        run('tar -xzvf pip-1.4.1.tar.gz')
        with cd('pip-1.4.1'):
            run('python setup.py install')


def dh_install_mysql_python():
    """
    Realiza a instalação do mysql-python
    """
    with cd('~/downloads'):
        run('wget http://downloads.sourceforge.net/project/mysql-python/mysql-python/1.2.3/MySQL-python-1.2.3.tar.gz')
        run('tar -xzvf MySQL-python-1.2.3.tar.gz')
        with cd('MySQL-python-1.2.3'):
            run('python setup.py install')

