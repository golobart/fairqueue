from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse
# from django.template import loader
from django.http import Http404
from django.shortcuts import get_object_or_404

from .models import Calendar, DaysOff, WorkingTime, Resource, CalendarDefWT, DaySpecWT

def index(request):
    return HttpResponse("Hello, world. You're at the polls index.fair queue.")


def adminPage(request):
    return render(request, 'adminapp/adminmain.html')


def resources(request):
    all_resources = Resource.objects.all()

    context = { 'all_resources': all_resources }
#    output = ', '.join([q.name for q in all_resources])
##    template = loader.get_template('adminapp/index.html')
##    return HttpResponse(template.render(context, request))
    return render(request, 'adminapp/resources.html', context)


#def resource(request, rsc_id):
#    try:
#        rsc = Resource.objects.get(pk=rsc_id)
#    except ResourceDoesNotExist:
#        raise Http404("Resource does not exist")
#
#    context = { 'rsc': rsc }
#
#    return render(request, 'adminapp/resource.html', context)

def resource(request, rsc_id):
    rsc = get_object_or_404(Resource, pk=rsc_id)

    context = { 'rsc': rsc }

    return render(request, 'adminapp/resource.html', context)


def calendar(request, testPar):
    response = "You're looking at a calendar %s."
    return HttpResponse(response % testPar)


def workingTime(request, testPar):
    response = "You're looking at a workingTime %s."
    return HttpResponse(response % testPar)
