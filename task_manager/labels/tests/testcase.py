from django.test import Client, TestCase

from task_manager.labels.models import Labels
from task_manager.users.models import User


class LabelTestCase(TestCase):
    fixtures = ['test_users.json', 'test_labels.json']

    def setUp(self):
        self.client = Client()

        self.label1 = Labels.objects.get(id=1)
        self.label2 = Labels.objects.get(id=2)

        self.user1 = User.objects.get(id=1)
        self.user2 = User.objects.get(id=2)

        self.label_count = Labels.objects.count()

        self.valid_label_data = {
            'name': 'Refactoring',
        }

        self.update_label_data = {
            'name': 'Feature',
        }