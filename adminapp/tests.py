from django.test import TestCase

# Create your tests here.
from django.test import Client
from django.urls import reverse

from .models import Resource, Calendar

from django.contrib.auth.models import User


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


class ViewTests(TestCase):

    def test_view_basics(self):
        """
        test_view_basics() returns True if access to view with login required is well done
        """
        self.client = Client()
        self.user = User.objects.create_user('Buzz', 'buzz@apollo11.net', 'AldrinPassword')
        login_res = self.client.login(username='Buzz', password='AldrinPassword')

        self.assertTrue(login_res)

        response = self.client.get(reverse('adminapp:searchresources'))
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'input type="reset" value="Clear fields"', response.content)

        self.client.logout()
        response = self.client.get(reverse('adminapp:searchresources'))
        self.assertEqual(response.status_code, 302)
#        self.assertIn(b'not log', response.content)
