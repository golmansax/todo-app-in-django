# pylint: disable=wildcard-import,unused-wildcard-import
from .base import *  # noqa

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

DEBUG_PROCESSOR = 'django.template.context_processors.debug'
TEMPLATES[0]['OPTIONS']['context_processors'].insert(0, DEBUG_PROCESSOR)
