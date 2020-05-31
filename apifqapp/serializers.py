from rest_framework import serializers
from adminapp.models import Calendar, Resource, DaysOff
from django.contrib.auth.models import User


class CalendarSerializer(serializers.HyperlinkedModelSerializer):
    #owner = serializers.ReadOnlyField(source='owner.username')
    #highlight = serializers.HyperlinkedIdentityField(view_name='snippet-highlight', format='html')

    class Meta:
        model = Calendar
        fields = ['id', 'owner', 'name', 'description', 'year', 'ini_day',
                  'end_day', 'template', 'next', 'prev', 'open']


class ResourceSerializer(serializers.HyperlinkedModelSerializer):
    #snippets = serializers.HyperlinkedRelatedField(many=True, view_name='snippet-detail', read_only=True)

    class Meta:
        model = Resource
        fields = ['id', 'name', 'description', 'text_title',
                  'calendar']


class DaysOffSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = DaysOff
        fields = ['id', 'name', 'description', 'type', 'day', 'end_day', 'week_day',
                  'month_day', 'month', 'from_day', 'to_day']