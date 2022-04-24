import os
import pandas as pd
from drf_yasg.inspectors import SwaggerAutoSchema

from core.models import School


class CustomAutoSchema(SwaggerAutoSchema):
    """
    Custom SwaggerAutoSchema to add tags to views
    """

    def get_tags(self, operation_keys=None) -> list:
        tags = self.overrides.get("tags", None) or getattr(
            self.view, "my_tags", []
        )
        if not tags:
            tags = [operation_keys[0]]

        return tags


def get_csv_file_path() -> str:
    """
    Returns dataset csv file path
    """
    return os.getenv("DATASET_CSV_PATH")


def upload_school_dataset() -> None:
    """
    Loads school dataset into database
    """
    df = pd.read_csv(get_csv_file_path())

    df = clean_and_limit_dataset(df)

    row_iter = df.iterrows()
    schools = []
    for index, row in row_iter:

        school = initialize_school_object_from_row(row)
        schools.append(school)
    if schools:

        School.objects.bulk_create(schools)


def clean_and_limit_dataset(df: pd.DataFrame) -> pd.DataFrame:
    """
    Returns dataset after cleaning
    """
    df.sort_values(by=["DBN"], inplace=True)

    # drop rows where total enrollment is missing
    df = df[df["Total Enrollment"].notna()]

    df = df.iloc[:1000]  # limits to 1000 entries

    missing_values = ["s", "No Data"]
    df = df.replace(missing_values, None).replace(r"^\s*$", None, regex=True)

    return df


def initialize_school_object_from_row(row: dict) -> School:
    """
    Initializes school object from row columns
    """
    category_dict = {value: key for key, value in School.CATEGORY_CHOICES}
    return School(
        dbn=row["DBN"],
        school_name=row["School Name"],
        category=category_dict[row["Category"]],
        year=row["Year"],
        total_enrollment=row["Total Enrollment"],
        grade_k=row["#Grade K"],
        grade_1=row["#Grade 1"],
        grade_2=row["#Grade 2"],
        grade_3=row["#Grade 3"],
        grade_4=row["#Grade 4"],
        grade_5=row["#Grade 5"],
        grade_6=row["#Grade 6"],
        grade_7=row["#Grade 7"],
        grade_8=row["#Grade 8"],
        female=row["#Female"],
        male=row["#Male"],
        asian=row["#Asian"],
        black=row["#Black"],
        hispanic=row["#Hispanic"],
        other=row["#Other"],
        white=row["#White"],
        ela_test_takers=row["ELA #Test Takers"],
        ela_level_1=row["ELA #Level 1"],
        ela_level_2=row["ELA #Level 2"],
        ela_level_3=row["ELA #Level 3"],
        ela_level_4=row["ELA #Level 4"],
        ela_l3_l4=row["ELA #L3+L4"],
        math_test_takers=row["Math #Test Takers"],
        math_level_1=row["MATH #Level 1"],
        math_level_2=row["MATH #Level 2"],
        math_level_3=row["MATH #Level 3"],
        math_level_4=row["MATH #Level 4"],
        math_l3_l4=row["MATH #L3+L4"],
    )
