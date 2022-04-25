from django.urls import path

from school_grade.views import SchoolListView, ChartRetrieveView


app_name = "school_grade"

urlpatterns = [
    path("school/", SchoolListView.as_view(), name="school-list"),
    path(
        "chart/<str:chart_id>/",
        ChartRetrieveView.as_view(),
        name="chart-retrieve",
    ),
]
