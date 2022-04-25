from rest_framework import serializers

from core.models import School, Chart


class SchoolSerializer(serializers.ModelSerializer):
    """
    School serializer
    Returns all fields except id
    """

    class Meta:
        model = School
        exclude = ["id"]


class ChartSerializer(serializers.ModelSerializer):
    """
    Chart serializer
    Returns all fields except id and query_params_dict
    """

    class Meta:
        model = Chart
        exclude = ["id", "query_params_dict"]
