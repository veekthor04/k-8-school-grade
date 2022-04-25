from rest_framework import generics
from django_filters import rest_framework as filters

from core.models import School
from school_grade.serializers import SchoolSerializer
from school_grade.filter import SchoolFilter


class SchoolListView(generics.ListAPIView):
    """
    List view for schools
    """

    queryset = School.objects.all()
    serializer_class = SchoolSerializer
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_class = SchoolFilter
    my_tags = ["School"]
