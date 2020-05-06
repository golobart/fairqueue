from django.shortcuts import render, redirect

#  Create your views here.

from django.http import HttpResponse
# from django.template import loader
from django.http import Http404
from django.shortcuts import get_object_or_404
from django.core.paginator import Paginator

from .models import Calendar, DaysOff, WorkingTime, Resource, CalendarDefWT, DaySpecWT
from .forms import SearchRscsForm, ResourceForm

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


def search_resources(request):
    # Presenta el formulari per cercar recursos
    form = SearchRscsForm()
    context = { 'form': form }
    return render(request, 'adminapp/searchresources.html', context)

def search_resources_do(request):
    # Es una request tipus GET
    if request.method == "GET":
        form = SearchRscsForm(request.GET)
        rscs_qset = Resource.objects.all()
        req_dict = request.GET
        if 'rsc_name' in req_dict:
            rsc_name = req_dict.get('rsc_name')
            rscs_qset = rscs_qset.filter(name__icontains=rsc_name)
        if 'rsc_desc' in req_dict:
            rsc_desc = req_dict.get('rsc_desc')
            rscs_qset = rscs_qset.filter(description__icontains=rsc_desc)
        if 'cal_name' in req_dict:
            cal_name = req_dict.get('cal_name')
            rscs_qset = rscs_qset.filter(calendar__name__icontains=cal_name)
        paginator = Paginator(rscs_qset.order_by('name'), 5)  # 5 per page.
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)

    # TODO eliminar
    if request.method == "POST":
        form = SearchRscsForm(request.POST) #if no files
        #if form.is_valid():
            # TODO fer la gravacio de recursos

    context = {
        'form': form,
        'req_dict': req_dict, # query params TODO remove innecessary
        'results': rscs_qset, # search results TODO remove innecessary
        'page_obj': page_obj,
        'paginator': paginator,
    }
    return render(request, 'adminapp/searchresourcesdo.html', context)

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
    if request.method == "POST":
        form = ResourceForm(request.POST, instance=rsc)
        if form.is_valid():
            rsc = form.save(commit=False)
            # post.author = request.user
            # post.published_date = timezone.now()
            rsc.save()
            return redirect('resource', pk=rsc.pk)
    else:
        form = ResourceForm(instance=rsc)

    context = { 'rsc': rsc, 'form': form }

    return render(request, 'adminapp/resource.html', context)


def calendar(request, testPar):
    response = "You're looking at a calendar %s."
    return HttpResponse(response % testPar)


def workingTime(request, testPar):
    response = "You're looking at a workingTime %s."
    return HttpResponse(response % testPar)
