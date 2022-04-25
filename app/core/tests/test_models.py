from django.test import TestCase
from django.db.models import signals

from core.models import School, Chart


class ModelTests(TestCase):
    def test_saving_and_retrieving_schools(self):
        """
        Test creating, saving and retrieving schools
        """

        first_school = School()
        first_school.dbn = "dbn_1"
        first_school.school_name = "School name 1"
        first_school.category = School.ALL_STUDENTS
        first_school.year = "2021-22"
        first_school.total_enrollment = 200
        first_school.save()

        second_school = School()
        second_school.dbn = "dbn_2"
        second_school.school_name = "School name 2"
        second_school.category = School.ALL_STUDENTS
        second_school.year = "2021-22"
        second_school.total_enrollment = 201
        second_school.save()

        saved_schools = School.objects.all()
        self.assertEqual(saved_schools.count(), 2)

        first_saved_school = saved_schools[0]
        second_saved_school = saved_schools[1]
        self.assertEqual(first_saved_school.dbn, "dbn_1")
        self.assertEqual(second_saved_school.dbn, "dbn_2")

    def test_saving_and_retrieving_charts(self):
        """
        Test creating, saving and retrieving Charts
        """
        signals.post_save.disconnect(sender=Chart, dispatch_uid="my_id")
        first_chart = Chart()
        first_chart.query_params_dict = "test params"
        first_chart.save()

        second_chart = Chart()
        second_chart.query_params_dict = "test params 2"
        second_chart.save()

        saved_charts = Chart.objects.all()
        self.assertEqual(saved_charts.count(), 2)

        first_saved_chart = saved_charts[0]
        second_saved_chart = saved_charts[1]
        self.assertEqual(first_saved_chart.query_params_dict, "test params")
        self.assertEqual(second_saved_chart.query_params_dict, "test params 2")

    def test_create_chart_image(self):
        """
        Test create_chart_image method creates an image
        """
        signals.post_save.disconnect(sender=Chart, dispatch_uid="my_id")
        chart = Chart.objects.create(query_params_dict="{}")

        chart.create_chart_image()

        chart.refresh_from_db()
        self.assertTrue(bool(chart.image))
