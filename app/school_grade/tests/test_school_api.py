from django.urls import reverse
from django.test import TestCase
from rest_framework import status
from rest_framework.test import APIClient

from core.models import School, Chart
from school_grade.serializers import SchoolSerializer


SCHOOL_LIST_URL = reverse("school_grade:school-list")


class SchoolViewTest(TestCase):
    """
    Test the school list view api
    """

    def setUp(self) -> None:
        self.client = APIClient()

    def test_school_list(self):
        """
        Test school list url to list schools
        """
        School.objects.create(
            dbn="dbn_1",
            school_name="School name 1",
            category=School.ALL_STUDENTS,
            year="2021-22",
            total_enrollment=200,
        )

        School.objects.create(
            dbn="dbn_2",
            school_name="School name 2",
            category=School.ALL_STUDENTS,
            year="2021-22",
            total_enrollment=201,
        )

        response = self.client.get(SCHOOL_LIST_URL)

        schools = School.objects.all()
        serializer = SchoolSerializer(schools, many=True)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn("results", response.json())
        self.assertEqual(response.json()["results"], serializer.data)

    def test_chart_model_is_created_for_school_list_view(self):
        """
        Test that chart model is created when a school list is used
        """
        School.objects.create(
            dbn="dbn_1",
            school_name="School name 1",
            category=School.ALL_STUDENTS,
            year="2021-22",
            total_enrollment=200,
        )

        response = self.client.get(SCHOOL_LIST_URL)

        saved_charts = Chart.objects.all()
        self.assertEqual(saved_charts.count(), 1)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        saved_chart = saved_charts[0]
        self.assertEqual(saved_chart.query_params_dict, "{}")

    def test_multiple_chart_model_is_not_created_for_the_same_list_query(self):
        """
        Test that multiple chart model is not created for the same school list
        view use
        """
        School.objects.create(
            dbn="dbn_1",
            school_name="School name 1",
            category=School.ALL_STUDENTS,
            year="2021-22",
            total_enrollment=200,
        )

        response = self.client.get(
            SCHOOL_LIST_URL, {"category": School.ALL_STUDENTS}
        )

        response = self.client.get(
            SCHOOL_LIST_URL, {"category": School.ALL_STUDENTS}
        )

        self.assertEqual(response.status_code, status.HTTP_200_OK)

        saved_charts = Chart.objects.all()
        self.assertEqual(saved_charts.count(), 1)
