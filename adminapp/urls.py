from django.urls import path

from . import views

app_name = 'adminapp'

urlpatterns = [
    # ex: /adminapp/
    path('', views.adminPage, name='adminPage'),

    # TODO eliminar ex: /adminapp/rscs/ TODO eliminar, substituit per searchresources
    path('rscs/', views.resources, name='resources'),
    # ex: /adminapp/rsc/5/
    path('rsc/<int:rsc_id>/', views.resource, name='resource'),
    # ex: /adminapp/delrsc/5/
    path('delrsc/<int:rsc_id>/', views.delete_resource, name='deleteresource'),
    # ex: /adminapp/delrscs/
    path('delrscs/', views.delete_resources, name='deleteresources'),
    # ex: /adminapp/crersc/
    path('crersc/', views.create_resource, name='createresource'),
    # ex: /adminapp/crerscdo/
    path('crerscdo/', views.create_resource_do, name='createresourcedo'),
    # ex: /adminapp/searchrscs/
    path('searchrscs/', views.search_resources, name='searchresources'),
    # ex: /adminapp/searchrscsdo/
    path('searchrscsdo/', views.search_resources_do, name='searchresourcesdo'),


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
    # ex: /adminapp/searchcals/
    path('searchcals/', views.search_calendars, name='searchcalendars'),
    # ex: /adminapp/searchcalsdo/
    path('searchcalsdo/', views.search_calendars_do, name='searchcalendarsdo'),

    # ex: /adminapp/wt/5/
    path('wt/<int:id>/', views.workingtime, name='workingtime'),
    # ex: /adminapp/delwt/5/
    path('delwt/<int:id>/', views.delete_workingtime, name='deleteworkingtime'),
    # ex: /adminapp/delwts/
    path('delwts/', views.delete_workingtimes, name='deleteworkingtimes'),
    # ex: /adminapp/crewt/
    path('crewt/', views.create_workingtime, name='createworkingtime'),
    # ex: /adminapp/crewtdo/
    path('crewtdo/', views.create_workingtime_do, name='createworkingtimedo'),
    # ex: /adminapp/searchwts/
    path('searchwts/', views.search_workingtimes, name='searchworkingtimes'),
    # ex: /adminapp/searchwtsdo/
    path('searchwtsdo/', views.search_workingtimes_do, name='searchworkingtimesdo'),

    # ex: /adminapp/dof/5/
    path('dof/<int:id>/', views.daysoff, name='daysoff'),
    # ex: /adminapp/deldof/5/
    path('deldof/<int:id>/', views.delete_daysoff, name='deletedaysoff'),
    # ex: /adminapp/deldofs/
    path('deldofs/', views.delete_daysoffs, name='deletedaysoffs'),
    # ex: /adminapp/credof/
    path('credof/', views.create_daysoff, name='createdaysoff'),
    # ex: /adminapp/credofdo/
    path('credofdo/', views.create_daysoff_do, name='createdaysoffdo'),
    # ex: /adminapp/searchdofs/
    path('searchdofs/', views.search_daysoffs, name='searchdaysoffs'),
    # ex: /adminapp/searchdofsdo/
    path('searchdofsdo/', views.search_daysoffs_do, name='searchdaysoffsdo'),
]
