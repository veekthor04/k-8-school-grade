import os
import pandas as pd
from django.test import TestCase
from unittest.mock import patch

from core.utils import (
    upload_school_dataset,
    clean_and_limit_dataset,
    initialize_school_object_from_row,
)
from core.models import School


DEMO_DATASET = os.getcwd() + "/core/tests/demo_dataset.csv"


class TestUtilsFunctions(TestCase):
    @patch("core.utils.get_csv_file_path")
    def test_upload_school_dataset(self, get_csv_file_path):
        """
        Test upload_school_dataset function
        """
        get_csv_file_path.return_value = DEMO_DATASET
        upload_school_dataset()

        saved_schools = School.objects.all()
        self.assertEqual(saved_schools.count(), 4)
        self.assertEqual(saved_schools.first().dbn, "01M015")

    def test_clean_and_limit_dataset(self):
        """
        Test clean_and_limit_dataset function
        """

        df = pd.read_csv(DEMO_DATASET)
        cleaned_df = clean_and_limit_dataset(df)

        self.assertEqual(cleaned_df.shape[0], 4)
        self.assertNotIn("No Data", cleaned_df["#Grade K"].unique())
        self.assertNotIn("s", cleaned_df["#Asian"].unique())

    def test_initialize_school_object_from_row(self):
        """
        Test initialize_school_object_from_row function
        """
        df = pd.read_csv(DEMO_DATASET)
        row_iter = df.iterrows()
        index, row = next(row_iter)
        school = initialize_school_object_from_row(row)

        self.assertIsInstance(school, School)
        self.assertEqual(school.dbn, "01M015")
