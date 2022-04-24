from django.core.management import BaseCommand

from core.tasks import create_dataset_load_task
from core.models import School


class Command(BaseCommand):
    """
    Loads school dataset into database if no school exist
    """

    help = "Loads schools dataset."

    def handle(self, *args, **options):
        self.stdout.write("Creating dataset load task.")

        if not School.objects.all().exists():

            create_dataset_load_task.delay()

            self.stdout.write(
                self.style.SUCCESS("Dataset load task has been created.")
            )
        else:

            self.stdout.write(
                self.style.ERROR(
                    "Dataset load task can only be created if no "
                    "school data exist"
                )
            )
