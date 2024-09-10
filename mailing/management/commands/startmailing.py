from django.core.management.base import BaseCommand
from mailing.services import start_send_mailing


class Command(BaseCommand):
    def handle(self, *args, **options):
        start_send_mailing()
