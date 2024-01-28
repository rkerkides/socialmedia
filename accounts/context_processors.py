from django.conf import settings

def add_login_redirect_url(request):
    return {'LOGIN_REDIRECT_URL': settings.LOGIN_REDIRECT_URL}
