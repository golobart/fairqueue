from django.test import TestCase

# Create your tests here.

from .models import Resource, Calendar


class ResourceModelTests(TestCase):

    def test_resource_basics(self):
        """
        resource_basics() returns True if insertion is well done
        """
        calendar = Calendar(owner="oowwnneerr", name="ccaall__nnaammee",
                            ini_day="2019-04-17", end_day="2020-12-14",
                            template=True, open=True)
        resource = Resource(name="tteesstt__nnaammee", calendar=calendar)
        self.assertEqual(resource.name, "tteesstt__nnaammee")
        self.assertEqual(resource.calendar, calendar)
        self.assertEqual(calendar.name, "ccaall__nnaammee")