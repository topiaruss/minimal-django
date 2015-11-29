from django.http import HttpResponse
import datetime


def index(request):
    now = datetime.datetime.now().isoformat()
    return HttpResponse("Hello, world. It's the index page at %s" % now)
