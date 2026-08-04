from django.http import HttpResponse

def hello(request):
    return HttpResponse("Hello Django from the station dev environment")
