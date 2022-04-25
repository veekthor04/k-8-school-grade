import django_filters

from core.models import School


class SchoolFilter(django_filters.FilterSet):
    """
    School filterset
    """

    category = django_filters.ChoiceFilter(choices=School.CATEGORY_CHOICES)

    class Meta:
        model = School
        fields = {
            "asian": ["lte", "gte"],
            "black": ["lte", "gte"],
            "hispanic": ["lte", "gte"],
            "other": ["lte", "gte"],
            "white": ["lte", "gte"],
            "female": ["lte", "gte"],
            "male": ["lte", "gte"],
        }
