from django.urls import path

from school_grade.views import SchoolListView


app_name = "school_grade"

urlpatterns = [
    path("", SchoolListView.as_view(), name="school-list"),
]
