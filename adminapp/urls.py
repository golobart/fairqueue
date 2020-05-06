from django.urls import path

from . import views

app_name = 'adminapp'

urlpatterns = [
    # ex: /adminapp/
    path('', views.adminPage, name='adminPage'),
    # ex: /adminapp/rscs/
    path('rscs/', views.resources, name='resources'),
    # ex: /adminapp/rsc/5/
    path('rsc/<int:rsc_id>/', views.resource, name='resource'),
    # path('rsc/', views.resource, name='resource'),
    # ex: /adminapp/cals/
    path('cals/', views.calendar, name='calendars'),
    # ex: /adminapp/cal/5/
    path('cal/<int:testPar>/', views.calendar, name='calendar'),
    # ex: /adminapp/wts/
    path('wts/', views.workingTime, name='workingTimes'),
    # ex: /adminapp/wt/5/
    path('wt/<int:testPar>/', views.workingTime, name='workingTime'),
    # ex: /adminapp/searchrscs/
    path('searchrscs/', views.search_resources, name='searchresources'),
    # ex: /adminapp/searchrscsdo/
    path('searchrscsdo/', views.search_resources_do, name='searchresourcesdo'),
]
