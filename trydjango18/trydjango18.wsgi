import os
import sys
import site

# change /var/www/html/sear_project to local
print ('wsgi')
local_path = '/media/My_Files/Dropbox/UCL_Projects/FIST/FIST_project'
# Add the site-packages of the chosen virtualenv to work with
site.addsitedir(local_path + '/lib/python2.7/site-packages')
# Add the app's directory to the PYTHONPATH
sys.path.append(local_path)
sys.path.append(local_path + '/src')
os.environ['DJANGO_SETTINGS_MODULE'] = 'trydjango18.settings'
# Activate your virtual env
activate_env=os.path.expanduser(local_path + "/bin/activate_this.py")
execfile(activate_env, dict(__file__=activate_env))
from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
