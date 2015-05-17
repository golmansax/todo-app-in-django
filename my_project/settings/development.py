from .base import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATES[0]['OPTIONS']['context_processors'].insert(0, 'django.template.context_processors.debug')
