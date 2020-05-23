from django.urls import path

from . import views

app_name = 'adminapp'

urlpatterns = [
    # ex: /adminapp/
    path('', views.adminPage, name='adminPage'),
    # ex: /adminapp/rscs/ TODO eliminar, substituit per searchresources
    path('rscs/', views.resources, name='resources'),
    # ex: /adminapp/rsc/5/
    path('rsc/<int:rsc_id>/', views.resource, name='resource'),
    # path('rsc/', views.resource, name='resource'),
    # ex: /adminapp/delrsc/5/
    path('delrsc/<int:rsc_id>/', views.delete_resource, name='deleteresource'),
    # ex: /adminapp/delrscs/
    path('delrscs/', views.delete_resources, name='deleteresources'),
    # ex: /adminapp/crersc/
    path('crersc/', views.create_resource, name='createresource'),
    # ex: /adminapp/crerscdo/
    path('crerscdo/', views.create_resource_do, name='createresourcedo'),
    # ex: /adminapp/searchcals/
    path('searchcals/', views.search_calendars, name='searchcalendars'),
    # ex: /adminapp/searchcalsdo/
    path('searchcalsdo/', views.search_calendars_do, name='searchcalendarsdo'),
    # ex: /adminapp/cal/5/
    path('cal/<int:cal_id>/', views.calendar, name='calendar'),
    # ex: /adminapp/delcal/5/
    path('delcal/<int:cal_id>/', views.delete_calendar, name='deletecalendar'),
    # ex: /adminapp/delcals/
    path('delcals/', views.delete_calendars, name='deletecalendars'),
    # ex: /adminapp/crecal/
    path('crecal/', views.create_calendar, name='createcalendar'),
    # ex: /adminapp/crecaldo/
    path('crecaldo/', views.create_calendar_do, name='createcalendardo'),
    # ex: /adminapp/wts/
    path('wts/', views.workingTime, name='workingTimes'),
    # ex: /adminapp/wt/5/
    path('wt/<int:testPar>/', views.workingTime, name='workingTime'),
    # ex: /adminapp/searchrscs/
    path('searchrscs/', views.search_resources, name='searchresources'),
    # ex: /adminapp/searchrscsdo/
    path('searchrscsdo/', views.search_resources_do, name='searchresourcesdo'),
]
