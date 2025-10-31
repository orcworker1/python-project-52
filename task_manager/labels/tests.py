from django.test import TestCase
from .models import Labels
from django.contrib.auth.models import User
from django.urls import reverse


class LabelsCRUDtests(TestCase):
    fixtures = ['tasks.json']

    def test_create_label(self):
        label = Labels.objects.create(name='new_label')
        self.assertEqual(label.name, 'new_label')
        self.assertTrue(Labels.objects.filter(name="new_label").exists())

    def test_update_label(self):
        user = User.objects.get(username='test_user')
        label = Labels.objects.get(name='test_label')
        self.client.force_login(user)
        response = self.client.post(reverse('update_label', args=[label.id]),
                                    {'name': 'updated_label'})
        label.refresh_from_db()
        self.assertEqual(label.name, 'updated_label')
        self.assertEqual(response.status_code, 302)

    def test_delete_label(self):
        label = Labels.objects.get(name='another_label')
        user = User.objects.get(username='test_user')
        self.client.force_login(user)
        response = self.client.post(reverse('delete_label', args=[label.id]))
        self.assertFalse(Labels.objects.filter(name='another_label').exists())
        self.assertEqual(response.status_code, 302)

    def test_fixture_loaded(self):
        self.assertEqual(Labels.objects.count(), 2)
        self.assertTrue(Labels.objects.filter(name='test_label').exists())

    def test_delete_label_used_in_task(self):
        label = Labels.objects.get(name='test_label')
        user = User.objects.get(username='test_user')
        self.client.force_login(user)
        response = self.client.post(reverse('delete_label', args=[label.id]))
        self.assertTrue(Labels.objects.filter(name='test_label').exists())
        self.assertEqual(response.status_code, 200)
