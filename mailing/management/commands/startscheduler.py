from django.conf import settings
from apscheduler.schedulers.blocking import BlockingScheduler
from django.core.management.base import BaseCommand
from mailing.services import start_send_mailing


class Command(BaseCommand):
    def handle(self, *args, **options):
        scheduler = BlockingScheduler(timezone=settings.TIME_ZONE)
        scheduler.add_job(start_send_mailing, 'interval', seconds=60)
        scheduler.start()