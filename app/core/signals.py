from django.db.models.signals import post_save
from django.dispatch import receiver

from core.models import Chart
from core.tasks import create_chart_image_task


@receiver(post_save, sender=Chart)
def post_save_transfer_created_receiver(
    sender, instance: Chart, created, **kwargs
) -> None:
    """
    Triggers the create chart image task
    """
    if created:
        create_chart_image_task.delay(instance.pk)
