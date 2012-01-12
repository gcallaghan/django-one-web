from oneweb import settings

def media(request):
    '''
    Adds media related context variables to the template context
    '''
    return {'320_MEDIA_URL':settings.320_MEDIA_URL}
