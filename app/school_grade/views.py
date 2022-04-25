from rest_framework import generics
from django_filters import rest_framework as filters

from core.models import School, Chart
from school_grade.serializers import SchoolSerializer, ChartSerializer
from school_grade.filter import SchoolFilter


class SchoolListView(generics.ListAPIView):
    """
    List school view
    """

    queryset = School.objects.all()
    serializer_class = SchoolSerializer
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_class = SchoolFilter
    my_tags = ["School"]

    def list(self, request, *args, **kwargs):

        response = super().list(request, *args, **kwargs)
        chart = self.__get_or_create_chart_for_request(request)

        # include chart detail in response
        response.data["chart_id"] = chart.chart_id
        return response

    @staticmethod
    def __get_or_create_chart_for_request(request) -> Chart:
        """
        Gets query prams and removes page if available,
        Retrives or create chart by query parameters
        """
        query_params_dict = request.query_params.copy()
        query_params_dict.pop("page", None)

        chart, created = Chart.objects.get_or_create(
            query_params_dict=str(request.query_params)
        )

        return chart


class ChartRetrieveView(generics.RetrieveAPIView):
    """
    Retrieve chart view
    """

    queryset = Chart.objects.all()
    serializer_class = ChartSerializer
    lookup_field = "chart_id"
    my_tags = ["Chart"]
