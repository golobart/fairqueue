
from django.shortcuts import render, redirect

#  Create your views here.

from django.http import HttpResponse
# from django.template import loader
from django.http import Http404
from django.shortcuts import get_object_or_404
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required

from .models import Calendar, DaysOff, WorkingTime, Resource, CalendarDefWT, DaySpecWT
from .forms import SearchRscsForm, ResourceForm

def index(request):
    return HttpResponse("Hello, world. You're at the polls index.fair queue.")


def adminPage(request):
    return render(request, 'adminapp/adminmain.html')

# TODO eliminar
def resources(request):
    all_resources = Resource.objects.all()

    context = { 'all_resources': all_resources }
#    output = ', '.join([q.name for q in all_resources])
##    template = loader.get_template('adminapp/index.html')
##    return HttpResponse(template.render(context, request))
    return render(request, 'adminapp/resources.html', context)

@login_required
def search_resources(request):
    # Presenta el formulari per cercar recursos
    form = SearchRscsForm()
    context = { 'form': form,
                'activemenu': 'resource',}
    return render(request, 'adminapp/searchresources.html', context)

@login_required
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
        if 'ord_name' in req_dict:
            ord_name = req_dict.get('ord_name')
            if ord_name == 'asc':
                rscs_qset = rscs_qset.order_by('name')
            elif ord_name == 'des':
                rscs_qset = rscs_qset.order_by('-name')
        if 'ord_desc' in req_dict:
            ord_desc = req_dict.get('ord_desc')
            if ord_desc == 'asc':
                rscs_qset = rscs_qset.order_by('description')
            elif ord_desc == 'des':
                rscs_qset = rscs_qset.order_by('-description')
        if 'ord_cal_name' in req_dict:
            ord_cal_name = req_dict.get('ord_cal_name')
            if ord_cal_name == 'asc':
                rscs_qset = rscs_qset.order_by('calendar')
            elif ord_cal_name == 'des':
                rscs_qset = rscs_qset.order_by('-calendar')

        paginator = Paginator(rscs_qset, 5)  # 5 per page.
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)

        # url params except 'page'
        url_pars = ''
        for par in req_dict:
            if par != 'page':
                url_pars += par + '=' + req_dict[par] + '&'

    context = {
        'form': form,
        'req_dict': req_dict, # query params TODO remove innecessary
        'results': rscs_qset, # search results TODO remove innecessary
        'page_obj': page_obj,
        'paginator': paginator,
        'activemenu': 'resource',
        'url_pars': url_pars,
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

@login_required
def resource(request, rsc_id):
    rsc = get_object_or_404(Resource, pk=rsc_id)
    if request.method == "POST":
        form = ResourceForm(request.POST, instance=rsc)
        if form.is_valid():
            rsc = form.save(commit=False)
            # post.author = request.user
            # post.published_date = timezone.now()
            rsc.save()
            return redirect('adminapp:searchresources')
            # return redirect('adminapp:resources', pk=rsc.pk)
    else:
        form = ResourceForm(instance=rsc)

    context = { 'rsc': rsc,
                'form': form,
                'activemenu': 'resource',}

    return render(request, 'adminapp/resource.html', context)


@login_required
def delete_resource(request, rsc_id):
    rsc = get_object_or_404(Resource, pk=rsc_id)
    rsc.delete()
    return redirect('adminapp:searchresources')


@login_required
def create_resource(request):
    if request.method == "GET":
        #form = ResourceForm(request.GET) intentava poblar els camps èr defecte amb el que venia del search, pero dona errors de validacio
        form = ResourceForm()
    else:
        form = ResourceForm()
    context = {'form': form,
               'activemenu': 'resource',}
    return render(request, 'adminapp/createresource.html', context)


@login_required
def create_resource_do(request):
    if request.method == "POST":
        form = ResourceForm(request.POST)
        if form.is_valid():
            rsc = form.save(commit=False)
            rsc.save()
            return redirect('adminapp:createresource')
            # return redirect('adminapp:searchresources')
        else:
            context = {'form': form}
            return render(request, 'adminapp/createresource.html', context)
    form = ResourceForm()
    context = {'form': form,
               'activemenu': 'resource',}
    return render(request, 'adminapp/createresource.html', context)


def calendar(request, testPar):
    response = "You're looking at a calendar %s."
    return HttpResponse(response % testPar)


def workingTime(request, testPar):
    response = "You're looking at a workingTime %s."
    return HttpResponse(response % testPar)
