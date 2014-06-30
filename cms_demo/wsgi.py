"""
WSGI config for cms_demo project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.6/howto/deployment/wsgi/
"""

import os
import sys
import site

ALLDIRS = ['/home/andre/env/lib/python2.6/site-packages']

# Remember original sys.path.
#prev_sys_path = list(sys.path) 

# Add each new site-packages directory.
for directory in ALLDIRS:
  site.addsitedir(directory)

#sys.path.append('/home/andre/cms')
#sys.path.append('/home/andre/cms/cms_demo')
#sys.path.append('/var/websites')
#sys.path.append('/var/websites/museum_analytics')

# Reorder sys.path so new directories at the front.
#new_sys_path = [] 
#for item in list(sys.path): 
#    if item not in prev_sys_path: 
#        new_sys_path.append(item) 
#        sys.path.remove(item) 
#sys.path[:0] = new_sys_path

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "cms_demo.settings")

#activate_env = os.path.expanduser("/home/andre/env/bin/activate_this.py")
#execfile(activate_env, dict(__file__=activate_env))

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()

