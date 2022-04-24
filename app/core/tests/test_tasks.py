import os
from django.test import TestCase
from unittest.mock import patch

from core.tasks import create_dataset_load_task
from core.models import School


DEMO_DATASET = os.getcwd() + "/core/tests/demo_dataset.csv"


class TestTasks(TestCase):
    @patch("core.utils.get_csv_file_path")
    def test_create_dataset_load_task(self, get_csv_file_path):
        """
        Test create_dataset_load_task synchronously and locally
        """
        get_csv_file_path.return_value = DEMO_DATASET
        task = create_dataset_load_task.s().apply()

        self.assertEqual(task.result, "School dataset load completed")

        saved_schools = School.objects.all()
        self.assertEqual(saved_schools.count(), 4)
