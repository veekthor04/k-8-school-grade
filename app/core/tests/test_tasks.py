import os
from django.db.models import signals
from django.test import TestCase
from unittest.mock import patch

from core.tasks import create_dataset_load_task, create_chart_image_task
from core.models import School, Chart


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

    def test_create_chart_image_task(self):
        """
        Test create_chart_image_task synchronously and locally
        """

        signals.post_save.disconnect(sender=Chart, dispatch_uid="my_id")
        chart = Chart.objects.create(
            query_params_dict="{}",
        )

        task = create_chart_image_task.s(chart.pk).apply()

        self.assertEqual(task.result, "Chart image has been created")

        chart.refresh_from_db()
        self.assertTrue(bool(chart.image))
