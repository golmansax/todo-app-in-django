# pylint: disable=wildcard-import,unused-wildcard-import
from .base import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

template_debug = 'django.template.context_processors.debug'
TEMPLATES[0]['OPTIONS']['context_processors'].insert(0, template_debug)
