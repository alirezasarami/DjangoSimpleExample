from user.models import Log
from django.http import HttpResponse

def log(fn):
    def wrapper(request):
        user = request.user
        action = fn.__name__
        browser = request.META['HTTP_USER_AGENT'] if 'HTTP_USER_AGENT' in request.META else None
        try:
            Log.objects.create(user = user , action = action ,  browser = browser)
            return fn(request)
        except Exception as error:
            return HttpResponse('Error:' ,error)
    return wrapper
