import sys, os
INTERP = "/home/fernandoe003/opt/bin/python2.7"
if sys.executable != INTERP: os.execl(INTERP, INTERP, *sys.argv)
sys.path.append(os.getcwd())
sys.path.append('/home/fernandoe003/espindola.info/source')

os.environ['DJANGO_SETTINGS_MODULE'] = 'server.settings.production'

import django.core.handlers.wsgi
application = django.core.handlers.wsgi.WSGIHandler()

