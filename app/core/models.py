import io
import uuid
import pandas as pd
import plotly.graph_objects as go
from django.db import models
from django.core.files.images import ImageFile


class School(models.Model):
    """
    School model to keep school details
    """

    ALL_STUDENTS = "all_students"
    OUTSIDE_DISTRICT = "attend_school_outside_district_of_residence"
    ENGLISH_LEANERS = "english_language_learners"
    POVERTY = "poverty"
    TEMPORARY_HOUSING = "reside_in_temporary_housing"
    STUDENT_WITH_dISABILITIES = "students_with_disabilities"

    CATEGORY_CHOICES = (
        (ALL_STUDENTS, "All Students"),
        (OUTSIDE_DISTRICT, "Attend school outside district of residence"),
        (ENGLISH_LEANERS, "English Language Learners"),
        (POVERTY, "Poverty"),
        (TEMPORARY_HOUSING, "Reside in temporary housing"),
        (STUDENT_WITH_dISABILITIES, "Students with Disabilities"),
    )

    dbn = models.CharField(max_length=50)
    school_name = models.CharField(max_length=255)
    category = models.CharField(max_length=255, choices=CATEGORY_CHOICES)
    year = models.CharField(max_length=50)
    total_enrollment = models.PositiveIntegerField()

    grade_k = models.PositiveIntegerField(null=True, blank=True)
    grade_1 = models.PositiveIntegerField(null=True, blank=True)
    grade_2 = models.PositiveIntegerField(null=True, blank=True)
    grade_3 = models.PositiveIntegerField(null=True, blank=True)
    grade_4 = models.PositiveIntegerField(null=True, blank=True)
    grade_5 = models.PositiveIntegerField(null=True, blank=True)
    grade_6 = models.PositiveIntegerField(null=True, blank=True)
    grade_7 = models.PositiveIntegerField(null=True, blank=True)
    grade_8 = models.PositiveIntegerField(null=True, blank=True)

    female = models.PositiveIntegerField(null=True, blank=True)
    male = models.PositiveIntegerField(null=True, blank=True)

    asian = models.PositiveIntegerField(null=True, blank=True)
    black = models.PositiveIntegerField(null=True, blank=True)
    hispanic = models.PositiveIntegerField(null=True, blank=True)
    other = models.PositiveIntegerField(null=True, blank=True)
    white = models.PositiveIntegerField(null=True, blank=True)

    ela_test_takers = models.PositiveIntegerField(null=True, blank=True)
    ela_level_1 = models.PositiveIntegerField(null=True, blank=True)
    ela_level_2 = models.PositiveIntegerField(null=True, blank=True)
    ela_level_3 = models.PositiveIntegerField(null=True, blank=True)
    ela_level_4 = models.PositiveIntegerField(null=True, blank=True)
    ela_l3_l4 = models.PositiveIntegerField(null=True, blank=True)

    math_test_takers = models.PositiveIntegerField(null=True, blank=True)
    math_level_1 = models.PositiveIntegerField(null=True, blank=True)
    math_level_2 = models.PositiveIntegerField(null=True, blank=True)
    math_level_3 = models.PositiveIntegerField(null=True, blank=True)
    math_level_4 = models.PositiveIntegerField(null=True, blank=True)
    math_l3_l4 = models.PositiveIntegerField(null=True, blank=True)

    class Meta:
        ordering = ["dbn", "school_name", "category"]

    def __str__(self) -> str:
        return f"DBN: {self.dbn}, School Name: {self.school_name}"


class Chart(models.Model):
    """
    Chart models to keep chart image and query params dict
    """

    chart_id = models.UUIDField(
        default=uuid.uuid4, editable=False, unique=True, db_index=True
    )
    image = models.ImageField(null=True, blank=True, upload_to="chart/")
    query_params_dict = models.TextField(max_length=1000)

    def __str__(self) -> str:
        return f"Chart for {self.query_params_dict}"

    def create_chart_image(self) -> None:
        """
        Creates chart image from query parameter
        """

        schools = School.objects.filter(**eval(self.query_params_dict))

        df = pd.DataFrame.from_records(schools.values())

        x_labels = [
            "ela_level-1",
            "ela_level_2",
            "ela_level_3",
            "ela_level_4",
            "ela_l3+l4",
            "math_level_1",
            "math_Level_2",
            "math_Level_3",
            "math_Level_4",
            "math_l3+l4",
        ]

        try:
            group_df = df.groupby(by="category", axis=0)
        except KeyError:
            group_df = df

        all_students = self.__get_mean_values_for_group(
            group_df, School.ALL_STUDENTS
        )
        outside_district = self.__get_mean_values_for_group(
            group_df, School.OUTSIDE_DISTRICT
        )
        english_learners = self.__get_mean_values_for_group(
            group_df, School.ENGLISH_LEANERS
        )
        poverty = self.__get_mean_values_for_group(group_df, School.POVERTY)
        temporary_housing = self.__get_mean_values_for_group(
            group_df, School.TEMPORARY_HOUSING
        )
        students_with_disabilities = self.__get_mean_values_for_group(
            group_df, School.STUDENT_WITH_dISABILITIES
        )

        fig = self.__create_fig_for_category_groups(
            x_labels,
            all_students,
            outside_district,
            english_learners,
            poverty,
            temporary_housing,
            students_with_disabilities,
        )

        # Change the bar mode
        fig.update_layout(barmode="group")

        file = io.BytesIO()
        fig.write_image(file)
        self.image = ImageFile(file, name=f"chart-{str(self.chart_id)}.png")
        self.save()

        print(self.image)

    @staticmethod
    def __get_mean_values_for_group(
        group_df: pd.DataFrame, group: str
    ) -> list:
        """
        Returns a list of mean value on selected group if exist
        """
        try:
            return group_df.get_group(group).mean().values
        except (AttributeError, KeyError):
            return []

    @staticmethod
    def __create_fig_for_category_groups(
        x_labels,
        all_students,
        outside_district,
        english_learners,
        poverty,
        temporary_housing,
        students_with_disabilities,
    ):
        """
        creates fig for category groups
        """
        return go.Figure(
            data=[
                go.Bar(name="All Students", x=x_labels, y=all_students),
                go.Bar(
                    name="Attend school outside district of residence",
                    x=x_labels,
                    y=outside_district,
                ),
                go.Bar(
                    name="English Language Learners",
                    x=x_labels,
                    y=english_learners,
                ),
                go.Bar(name="Poverty", x=x_labels, y=poverty),
                go.Bar(
                    name="Reside in temporary housing",
                    x=x_labels,
                    y=temporary_housing,
                ),
                go.Bar(
                    name="Students with Disabilities",
                    x=x_labels,
                    y=students_with_disabilities,
                ),
            ]
        )
