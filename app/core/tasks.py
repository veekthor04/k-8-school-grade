from app.celery import app

from core.utils import upload_school_dataset
from core.models import Chart


@app.task()
def create_dataset_load_task():

    upload_school_dataset()

    return "School dataset load completed"


@app.task()
def create_chart_image_task(chart_pk: int):
    """task to create task image for filtered schools"""

    Chart.objects.get(pk=chart_pk).create_chart_image()

    return "Chart image has been created"
