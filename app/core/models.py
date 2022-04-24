from django.db import models


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
