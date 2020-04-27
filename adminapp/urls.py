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
    # ex: /adminapp/cal/5/
    path('cal/<int:testPar>/', views.calendar, name='calendar'),
    # ex: /adminapp/wt/5/
    path('wt/<int:testPar>/', views.workingTime, name='workingTime'),
]
