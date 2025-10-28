from django.test import TestCase
from django.contrib.auth.models import User
from django.urls import reverse


class UserCRUDtests(TestCase):
    fixtures = ['users.json']


    def test_create_user(self):
        start_count_user = User.objects.count()
        response = self.client.post(reverse('create'), {
            'username': 'babushka',
            'first_name':'lala',
            'last_name': 'lolo',
            'password1': 'akaka23',
            'password2': 'akaka23',
        })
        self.assertEqual(User.objects.count(), start_count_user + 1 )
        self.assertTrue(User.objects.filter(username='babushka').exists())
        self.assertRedirects(response, reverse('login'))

    def test_fixture_loaded(self):
        self.assertEqual(User.objects.count(), 2)
        self.assertTrue(User.objects.filter(username='test_user').exists())

    def test_update_user(self):
        user = User.objects.get(username='test_user')
        self.client.force_login(user)
        response = self.client.post(reverse('update', args=[user.id]),
                    {'first_name': 'new_name', 'last_name': 'new_last'})
        user.refresh_from_db()
        self.assertEqual(user.first_name, 'new_name')
        self.assertEqual(user.last_name, 'new_last')
        self.assertEqual(response.status_code, 302)

    def test_delete_user(self):
        user = User.objects.get(username='second_user')
        self.client.force_login(user)
        response = self.client.post(reverse('delete', args=[user.id]))
        self.assertFalse(User.objects.filter(username='second_user').exists())
        self.assertEqual(response.status_code, 302)














# Create your tests here.
