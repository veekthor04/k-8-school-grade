from django.urls import reverse
from django.test import TestCase
from rest_framework import status
from rest_framework.test import APIClient

from core.models import School
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
