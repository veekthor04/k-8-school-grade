from rest_framework import generics

from core.models import School
from school_grade.serializers import SchoolSerializer


class SchoolListView(generics.ListAPIView):
    """
    List view for schools
    """

    queryset = School.objects.all()
    serializer_class = SchoolSerializer
    my_tags = ["School"]
