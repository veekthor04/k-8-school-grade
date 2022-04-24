from rest_framework import serializers

from core.models import School


class SchoolSerializer(serializers.ModelSerializer):
    """
    School serializer
    Returns all fields except id
    """

    class Meta:
        model = School
        exclude = ["id"]
