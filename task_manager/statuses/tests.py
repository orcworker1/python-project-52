from django.test import TestCase
from .models import Status
from django.contrib.auth.models import User
from django.urls import reverse


class StatusCRUDtests(TestCase):
    fixtures = ['statuses.json']


    def test_create_status(self):
        status = Status.objects.create(name='new_status')
        self.assertEqual(status.name, 'new_status')
        self.assertTrue(Status.objects.filter(name="new_status").exists())

    def test_update_status(self):
        user = User.objects.get(username='test_user')
        status = Status.objects.get(name='abab')
        self.client.force_login(user)
        response = self.client.post(reverse('update', args=[status.id]),
                                    {'name':'update_name'})
        status.refresh_from_db()
        self.assertEqual(status.name, 'update_name')
        self.assertEqual(response.status_code, 302)

    def test_delete_status(self):
        status = Status.objects.get(name='aboba')
        user = User.objects.get(username='test_user')
        self.client.force_login(user)
        response = self.client.post(reverse('delete', args=[status.id]))
        self.assertFalse(Status.objects.filter(name='aboba').exists())
        self.assertEqual(response.status_code, 302)

        

# Create your tests here.
