from django.test import TestCase

from core.models import School


class ModelTests(TestCase):
    def test_saving_and_retrieving_schools(self):
        """Test creating, saving and retrieving schools"""

        first_school = School()
        first_school.dbn = "dbn_1"
        first_school.school_name = "School name 1"
        first_school.category = School.ALL_STUDENTS
        first_school.year = "2021-22"
        first_school.total_enrollment = 200
        first_school.save()

        second_school = School()
        second_school.dbn = "dbn_2"
        second_school.school_name = "School name 2"
        second_school.category = School.ALL_STUDENTS
        second_school.year = "2021-22"
        second_school.total_enrollment = 201
        second_school.save()

        saved_schools = School.objects.all()
        self.assertEqual(saved_schools.count(), 2)

        first_saved_school = saved_schools[0]
        second_saved_school = saved_schools[1]
        self.assertEqual(first_saved_school.dbn, "dbn_1")
        self.assertEqual(second_saved_school.dbn, "dbn_2")
