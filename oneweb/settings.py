from django.conf import settings

DEFAULT_ONEWEB_MEDIA_URL = '%soneweb/' % settings.STATIC_URL

ONEWEB_MEDIA_URL = getattr( settings, 'ONEWEB_MEDIA_URL', DEFAULT_ONEWEB_MEDIA_URL )


