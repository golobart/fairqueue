from django.shortcuts import render


# Create your views here.

# ----------- API views

from rest_framework import viewsets, permissions
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import renderers

from .serializers import CalendarSerializer, ResourceSerializer, DaysOffSerializer
from adminapp.models import Resource, Calendar, DaysOff


class CalendarViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides `list`, `create`, `retrieve`,
    `update` and `destroy` actions.

    Additionally we also provide an extra `highlight` action.
    """
    queryset = Calendar.objects.all()
    serializer_class = CalendarSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, ]
                          # IsOwnerOrReadOnly]

    @action(detail=True, renderer_classes=[renderers.StaticHTMLRenderer])
    def highlight(self, request, *args, **kwargs):
        calendar = self.get_object()
        return Response(calendar.highlighted)

    # def perform_create(self, serializer):
    #     serializer.save(owner=self.request.user)


class ResourceViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides `list`, `create`, `retrieve`,
    `update` and `destroy` actions.

    Additionally we also provide an extra `highlight` action.
    """
    queryset = Resource.objects.all()
    serializer_class = ResourceSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, ]
                          # IsOwnerOrReadOnly]

    @action(detail=True, renderer_classes=[renderers.StaticHTMLRenderer])
    def highlight(self, request, *args, **kwargs):
        resource = self.get_object()
        return Response(resource.highlighted)


class DaysOffViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides `list`, `create`, `retrieve`,
    `update` and `destroy` actions.

    Additionally we also provide an extra `highlight` action.
    """
    queryset = DaysOff.objects.all()
    serializer_class = DaysOffSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, ]
                         # IsOwnerOrReadOnly]

    # @action(detail=True, renderer_classes=[renderers.StaticHTMLRenderer])
    # def highlight(self, request, *args, **kwargs):
    #     daysoff = self.get_object()
    #     return Response(daysoff.highlighted)