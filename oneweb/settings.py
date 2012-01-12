from django.conf import settings

DEFAULT_320_MEDIA_URL = '%s/django-one-web/' % settings.STATIC_URL

320_MEDIA_URL = getattr( settings, 'ONE_WEB_MEDIA_URL', DEFAULT_320_MEDIA_URL )


