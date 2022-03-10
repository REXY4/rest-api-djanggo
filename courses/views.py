from django.http import HttpResponse

def index(request):
    return HttpResponse("Hellp world, toure at the polls index!")