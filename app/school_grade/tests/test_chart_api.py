from django.urls import reverse
from django.db.models import signals
from django.test import TestCase
from rest_framework import status
from rest_framework.test import APIClient

from core.models import Chart
from school_grade.serializers import ChartSerializer


def chart_retrieve_url(chart_id: str):
    """Return the retrieve url for a chart"""
    return reverse("school_grade:chart-retrieve", args=[chart_id])


class ChartViewTest(TestCase):
    """
    Test the chart view view api
    """

    def setUp(self) -> None:
        self.client = APIClient()

    def test_retrieve_chart(self):
        """
        Test retrieve chart with right ID
        """
        signals.post_save.disconnect(sender=Chart, dispatch_uid="my_id")
        chart = Chart.objects.create(
            query_params_dict="test query param",
        )

        url = chart_retrieve_url(chart.chart_id)
        response = self.client.get(url)

        retrieved_chart = Chart.objects.get(chart_id=chart.chart_id)
        serializer = ChartSerializer(retrieved_chart, many=False)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.json(), serializer.data)

    def test_retrieve_chart_not_found(self):
        """
        Test retrieve chart with wrong ID
        """

        chart_id = "test_id"

        url = chart_retrieve_url(chart_id)
        response = self.client.get(url)

        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
