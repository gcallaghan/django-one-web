from oneweb import settings

def media(request):
    '''
    Adds media related context variables to the template context
    '''
    return {'ONEWEB_MEDIA_URL':settings.ONEWEB_MEDIA_URL}

