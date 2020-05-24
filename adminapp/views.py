from django.shortcuts import render, redirect

#  Create your views here.

from django.http import HttpResponse
# from django.template import loader
from django.http import Http404
from django.shortcuts import get_object_or_404
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required, permission_required, user_passes_test
from django.db.models import Q
from django.utils.translation import ugettext_lazy as _

from .models import Calendar, DaysOff, WorkingTime, Resource, CalendarDefWT, DaySpecWT
from .forms import SearchRscsForm, ResourceForm, SearchCalsForm, CalendarForm, SearchWTsForm, WorkingTimeForm

# TODO eliminar
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


# ----- RESOURCES VIEWS

def change_or_view_resource(user):
    return user.has_perm('adminapp.change_resource') or user.has_perm('adminapp.view_resource')

@login_required
@user_passes_test(change_or_view_resource)
def resource(request, rsc_id):
    rsc = get_object_or_404(Resource, pk=rsc_id)
    readonly = ''
    resultmessage = ''
    if request.method == "POST":
        form = ResourceForm(request.POST, instance=rsc)
        if request.user.has_perm('adminapp.change_resource'):
            if form.is_valid():
                rsc = form.save(commit=False)
                # post.author = request.user
                # post.published_date = timezone.now()
                rsc.save()
                resultmessage = _('Resource updated.')
                # return redirect('adminapp:searchresources')
                # return redirect('adminapp:resources', pk=rsc.pk)
    else:
        form = ResourceForm(instance=rsc)
        if request.GET.get('rd', '') != '':
            readonly = 'readonly'
            #for theField in form.fields:
            #    theField.attrs['readonly'] = True
            # considerar tb crispy-forms especialment en form.as_p

    context = { 'rsc': rsc,
                'form': form,
                'readonly': readonly,
                'resultmessage': resultmessage,
                'activemenu': 'resource',}

    return render(request, 'adminapp/resource.html', context)


@login_required
@permission_required('adminapp.delete_resource', raise_exception=True)
def delete_resource(request, rsc_id):
    rsc = get_object_or_404(Resource, pk=rsc_id)
    rsc.delete()
    return redirect('adminapp:searchresources')



@login_required
@permission_required('adminapp.delete_resource', raise_exception=True)
def delete_resources(request):
    if request.method == "POST":
        req_dict = request.POST
        if 'rectodel' in req_dict:
            for par in req_dict.getlist('rectodel'):
                if par != '':
                    cal = get_object_or_404(Resource, pk=par)
                    cal.delete()
    return redirect('adminapp:searchresources')


@login_required
@permission_required('adminapp.add_resource', raise_exception=True)
def create_resource(request):
    resultmessage = ''
    if request.method == "GET":
        #form = ResourceForm(request.GET) intentava poblar els camps èr defecte amb el que venia del search, pero dona errors de validacio
        form = ResourceForm()
    else:
        form = ResourceForm()
    context = {'form': form,
               'resultmessage': resultmessage,
               'activemenu': 'resource',}
    return render(request, 'adminapp/createresource.html', context)


@login_required
@permission_required('adminapp.add_resource', raise_exception=True)
def create_resource_do(request):
    resultmessage = ''
    if request.method == "POST":
        form = ResourceForm(request.POST)
        if form.is_valid():
            rsc = form.save(commit=False)
            rsc.save()
            resultmessage = _('Resource created.')
            # return redirect('adminapp:createresource')
            # return redirect('adminapp:searchresources')
        else:
            context = {'form': form}
            return render(request, 'adminapp/createresource.html', context)
    form = ResourceForm()
    context = {'form': form,
               'resultmessage': resultmessage,
               'activemenu': 'resource',}
    return render(request, 'adminapp/createresource.html', context)


@login_required
def search_resources(request):
    # Presenta el formulari per cercar recursos
    resultmessage = ''
    form = SearchRscsForm()
    context = { 'form': form,
                'resultmessage': resultmessage,
                'activemenu': 'resource',}
    return render(request, 'adminapp/searchresources.html', context)


@login_required
def search_resources_do(request):
    # Es una request tipus GET
    resultmessage = ''
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
        'resultmessage': resultmessage,
        'url_pars': url_pars,
    }
    return render(request, 'adminapp/searchresourcesdo.html', context)


# ----- CALENDARS VIEWS

def change_or_view_calendar(user):
    return user.has_perm('adminapp.change_calendar') or user.has_perm('adminapp.view_calendar')


@login_required
@user_passes_test(change_or_view_calendar)
def calendar(request, cal_id):
    cal = get_object_or_404(Calendar, pk=cal_id)
    readonly = ''
    resultmessage = ''
    if request.method == "POST":
        form = CalendarForm(request.POST, instance=cal)
        # TODO test form.has_changed()
        if request.user.has_perm('adminapp.change_calendar'):
            if form.is_valid():
                cal = form.save(commit=False)
                # post.author = request.user
                # post.published_date = timezone.now()
                cal.save()
                resultmessage = _('Calendar updated.')
                # return redirect('adminapp:searchcalendars')
                # return redirect('adminapp:calendars', pk=cal.pk)
    else:
        form = CalendarForm(instance=cal)
        if request.GET.get('rd', '') != '':
            readonly = 'readonly'
            #for theField in form.fields:
            #    theField.attrs['readonly'] = True
            # considerar tb crispy-forms especialment en form.as_p

    context = { 'cal': cal,
                'form': form,
                'readonly': readonly,
                'resultmessage': resultmessage,
                'activemenu': 'calendar',}

    return render(request, 'adminapp/calendar.html', context)


@login_required
@permission_required('adminapp.delete_calendar', raise_exception=True)
def delete_calendar(request, cal_id):
    cal = get_object_or_404(Calendar, pk=cal_id)
    cal.delete()
    return redirect('adminapp:searchcalendars')

@login_required
@permission_required('adminapp.delete_calendar', raise_exception=True)
def delete_calendars(request):
    if request.method == "POST":
        req_dict = request.POST
        if 'rectodel' in req_dict:
            for par in req_dict.getlist('rectodel'):
                if par != '':
                    cal = get_object_or_404(Calendar, pk=par)
                    cal.delete()
    return redirect('adminapp:searchcalendars')


@login_required
@permission_required('adminapp.add_calendar', raise_exception=True)
def create_calendar(request):
    if request.method == "GET":
        #form = ResourceForm(request.GET) intentava poblar els camps èr defecte amb el que venia del search, pero dona errors de validacio
        form = CalendarForm()
    else:
        form = CalendarForm()
    context = {'form': form,
               'activemenu': 'calendar',}
    return render(request, 'adminapp/createcalendar.html', context)


@login_required
@permission_required('adminapp.add_calendar', raise_exception=True)
def create_calendar_do(request):
    resultmessage = ''
    if request.method == "POST":
        form = CalendarForm(request.POST)
        if form.is_valid():
            cal = form.save(commit=False)
            cal.save()
            resultmessage = _('Calendar created.')
            # return redirect('adminapp:createcalendar')
            # return redirect('adminapp:searchcalendars')
        else:
            context = {'form': form}
            return render(request, 'adminapp/createcalendar.html', context)
    form = CalendarForm()
    context = {'form': form,
               'resultmessage': resultmessage,
               'activemenu': 'calendar',}
    return render(request, 'adminapp/createcalendar.html', context)


@login_required
def search_calendars(request):
    # Presenta el formulari per cercar calendaris
    resultmessage = ''
    form = SearchCalsForm()
    context = { 'form': form,
                'resultmessage': resultmessage,
                'activemenu': 'calendar',}
    return render(request, 'adminapp/searchcalendars.html', context)


@login_required
def search_calendars_do(request):
    # Es una request tipus GET
    resultmessage = ''
    if request.method == "GET":
        form = SearchCalsForm(request.GET)
        cals_qset = Calendar.objects.all()
        req_dict = request.GET
        if 'cal_owner' in req_dict:
            cal_owner = req_dict.get('cal_owner')
            if cal_owner != '':
                cals_qset = cals_qset.filter(owner__icontains=cal_owner)
        if 'cal_name' in req_dict:
            cal_name = req_dict.get('cal_name')
            if cal_name != '':
                cals_qset = cals_qset.filter(name__icontains=cal_name)
        if 'cal_desc' in req_dict:
            cal_desc = req_dict.get('cal_desc')
            if cal_desc != '':
                cals_qset = cals_qset.filter(description__icontains=cal_desc)
            #else: el camp pot estar buit, llavors no es posa cap filtre
                #cals_qset = cals_qset.filter(description__isnull=True) | cals_qset.filter(description__exact='')
                #cals_qset = cals_qset.filter(Q(description__isnull=True) | Q(description__exact=''))
        if 'cal_year' in req_dict:
            cal_year = req_dict.get('cal_year')
            if cal_year != '':
                cals_qset = cals_qset.filter(year__icontains=cal_year)

        if 'ord_owner' in req_dict:
            ord_owner = req_dict.get('ord_owner')
            if ord_owner == 'asc':
                cals_qset = cals_qset.order_by('owner')
            elif ord_owner == 'des':
                cals_qset = cals_qset.order_by('-owner')
        if 'ord_name' in req_dict:
            ord_name = req_dict.get('ord_name')
            if ord_name == 'asc':
                cals_qset = cals_qset.order_by('name')
            elif ord_name == 'des':
                cals_qset = cals_qset.order_by('-name')
        if 'ord_desc' in req_dict:
            ord_desc = req_dict.get('ord_desc')
            if ord_desc == 'asc':
                cals_qset = cals_qset.order_by('description')
            elif ord_desc == 'des':
                cals_qset = cals_qset.order_by('-description')
        if 'ord_year' in req_dict:
            ord_year = req_dict.get('ord_year')
            if ord_year == 'asc':
                cals_qset = cals_qset.order_by('year')
            elif ord_year == 'des':
                cals_qset = cals_qset.order_by('-year')

        paginator = Paginator(cals_qset, 5)  # 5 per page.
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
        'results': cals_qset, # search results TODO remove innecessary
        'page_obj': page_obj,
        'paginator': paginator,
        'activemenu': 'calendar',
        'resultmessage': resultmessage,
        'url_pars': url_pars,
    }
    return render(request, 'adminapp/searchcalendarsdo.html', context)


# ----- WORKING TIME VIEWS

def change_or_view_workingtime(user):
    return user.has_perm('adminapp.change_workingtime') or user.has_perm('adminapp.view_workingtime')


@login_required
@user_passes_test(change_or_view_workingtime)
def workingtime(request, id):
    wt = get_object_or_404(WorkingTime, pk=id)
    readonly = ''
    resultmessage = ''
    if request.method == "POST":
        form = WorkingTimeForm(request.POST, instance=wt)
        # TODO test form.has_changed()
        if request.user.has_perm('adminapp.change_calendar'):
            if form.is_valid():
                wt = form.save(commit=False)
                # post.author = request.user
                # post.published_date = timezone.now()
                wt.save()
                resultmessage = _('WorkingTime updated.')
                # return redirect('adminapp:searchcalendars')
                # return redirect('adminapp:calendars', pk=cal.pk)
    else:
        form = WorkingTimeForm(instance=wt)
        if request.GET.get('rd', '') != '':
            readonly = 'readonly'
            #for theField in form.fields:
            #    theField.attrs['readonly'] = True
            # considerar tb crispy-forms especialment en form.as_p

    context = { 'wt': wt,
                'form': form,
                'readonly': readonly,
                'resultmessage': resultmessage,
                'activemenu': 'workingtime',}

    return render(request, 'adminapp/workingtime.html', context)


@login_required
@permission_required('adminapp.delete_workingtime', raise_exception=True)
def delete_workingtime(request, id):
    wt = get_object_or_404(Calendar, pk=id)
    wt.delete()
    return redirect('adminapp:searchworkingtimes')

@login_required
@permission_required('adminapp.delete_workingtime', raise_exception=True)
def delete_workingtimes(request):
    if request.method == "POST":
        req_dict = request.POST
        if 'rectodel' in req_dict:
            for par in req_dict.getlist('rectodel'):
                if par != '':
                    wt = get_object_or_404(WorkingTime, pk=par)
                    wt.delete()
    return redirect('adminapp:searchworkingtimes')


@login_required
@permission_required('adminapp.add_workingtime', raise_exception=True)
def create_workingtime(request):
    if request.method == "GET":
        #form = ResourceForm(request.GET) intentava poblar els camps èr defecte amb el que venia del search, pero dona errors de validacio
        form = WorkingTimeForm()
    else:
        form = WorkingTimeForm()
    context = {'form': form,
               'activemenu': 'calendar',}
    return render(request, 'adminapp/createworkingtime.html', context)


@login_required
@permission_required('adminapp.add_workingtime', raise_exception=True)
def create_workingtime_do(request):
    resultmessage = ''
    if request.method == "POST":
        form = WorkingTimeForm(request.POST)
        if form.is_valid():
            wt = form.save(commit=False)
            wt.save()
            resultmessage = _('WorkingTime created.')
            # return redirect('adminapp:createcalendar')
            # return redirect('adminapp:searchcalendars')
        else:
            context = {'form': form}
            return render(request, 'adminapp/createworkingtime.html', context)
    form = WorkingTimeForm()
    context = {'form': form,
               'resultmessage': resultmessage,
               'activemenu': 'workingtime',}
    return render(request, 'adminapp/createworkingtime.html', context)


@login_required
def search_workingtimes(request):
    # Presenta el formulari per cercar calendaris
    resultmessage = ''
    form = SearchWTsForm()
    context = { 'form': form,
                'resultmessage': resultmessage,
                'activemenu': 'workingtime',}
    return render(request, 'adminapp/searchworkingtimes.html', context)


@login_required
def search_workingtimes_do(request):
    # Es una request tipus GET
    resultmessage = ''
    if request.method == "GET":
        form = SearchWTsForm(request.GET)
        qset = WorkingTime.objects.all()
        req_dict = request.GET
        if 'xxxcal_owner' in req_dict:
            xxxcal_owner = req_dict.get('xxxcal_owner')
            if xxxcal_owner != '':
                qset = qset.filter(owner__icontains=xxxcal_owner)


        if 'ord_xxxowner' in req_dict:
            ord_xxxowner = req_dict.get('ord_xxxowner')
            if ord_xxxowner == 'asc':
                qset = qset.order_by('owner')
            elif ord_xxxowner == 'des':
                qset = qset.order_by('-owner')


        paginator = Paginator(qset, 5)  # 5 per page.
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
        'results': qset, # search results TODO remove innecessary
        'page_obj': page_obj,
        'paginator': paginator,
        'activemenu': 'workingtime',
        'resultmessage': resultmessage,
        'url_pars': url_pars,
    }
    return render(request, 'adminapp/searchworkingtimesdo.html', context)
