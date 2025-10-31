from django.test import TestCase
from .models import Task
from django.contrib.auth.models import User
from django.urls import reverse
from task_manager.statuses.models import Status
from task_manager.labels.models import Labels


class TaskCRUDtests(TestCase):
    fixtures = ['tasks.json']

    def test_create_task(self):
        user = User.objects.get(username='test_user')
        status = Status.objects.get(name='test_status')
        self.client.force_login(user)
        
        start_count_task = Task.objects.count()
        response = self.client.post(reverse('create_task'), {
            'name': 'new_task',
            'description': 'New task description',
            'status': status.id,
        })
        
        self.assertEqual(Task.objects.count(), start_count_task + 1)
        self.assertTrue(Task.objects.filter(name='new_task').exists())
        task = Task.objects.get(name='new_task')
        self.assertEqual(task.author, user)
        self.assertEqual(response.status_code, 302)

    def test_update_task(self):
        user = User.objects.get(username='test_user')
        task = Task.objects.get(name='test_task')
        status = Status.objects.get(name='another_status')
        self.client.force_login(user)
        
        response = self.client.post(reverse('update_task', args=[task.id]), {
            'name': 'updated_task',
            'description': 'Updated description',
            'status': status.id,
        })
        
        task.refresh_from_db()
        self.assertEqual(task.name, 'updated_task')
        self.assertEqual(response.status_code, 302)

    def test_delete_task(self):
        user = User.objects.get(username='test_user')
        task = Task.objects.get(name='another_task')
        self.client.force_login(user)
        
        response = self.client.post(reverse('delete_task', args=[task.id]))
        self.assertFalse(Task.objects.filter(name='another_task').exists())
        self.assertEqual(response.status_code, 302)

    def test_fixture_loaded(self):
        self.assertEqual(Task.objects.count(), 2)
        self.assertTrue(Task.objects.filter(name='test_task').exists())

    def test_task_with_executor(self):
        task = Task.objects.get(name='test_task')
        executor = User.objects.get(username='second_user')
        self.assertEqual(task.executor, executor)

    def test_task_with_labels(self):
        task = Task.objects.get(name='test_task')
        label = Labels.objects.get(name='test_label')
        self.assertIn(label, task.labels.all())

    def test_task_without_executor(self):
        task = Task.objects.get(name='another_task')
        self.assertIsNone(task.executor)
