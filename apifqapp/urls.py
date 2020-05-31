from django.urls import path, include

from . import views

# Create a router and register our viewsets with it.
from rest_framework.routers import DefaultRouter

app_name = 'apifqapp'

router = DefaultRouter()
router.register(r'calendar', views.CalendarViewSet)
router.register(r'resource', views.ResourceViewSet)
router.register(r'daysoff', views.DaysOffViewSet)

# The API URLs are now determined automatically by the router.
urlpatterns = [
    path('', include(router.urls)),
]