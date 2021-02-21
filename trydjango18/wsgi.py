"""
WSGI config for trydjango18 project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.8/howto/deployment/wsgi/
"""

from django.core.wsgi import get_wsgi_application
import os
#print ('after import django wsgi')

#from whitenoise.django import DjangoWhiteNoise
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "trydjango18.settings")
#os.environ['DJANGO_SETTINGS_MODULE'] = 'trydjango18.settings'

#print ('after os.environ.set.default...blah')

# disable whitenoise temp for FIST
#from whitenoise.django import DjangoWhiteNoise
#print ('after import whitenoiseh')

application = get_wsgi_application()
#print ('after get wsgi application')

# disable whitenoise temp for FIST
# application = DjangoWhiteNoise(application)
#print ('after Djangowhitenoise application')
