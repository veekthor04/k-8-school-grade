from app.celery import app
from core.utils import upload_school_dataset


@app.task()
def create_dataset_load_task():

    upload_school_dataset()

    return "School dataset load completed"
