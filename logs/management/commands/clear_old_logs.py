from datetime import timedelta

from django.core.management.base import BaseCommand
from django.utils import timezone

from logs.models import Log

class Command(BaseCommand):
    help = 'Delete old logs from 30days'

    def handle(self, *args, **options):
        limite = timezone.now() - timedelta(days=30)

        old_logs = Log.objects.filter(created_at__lt=limite)

        amount = old_logs.count()

        old_logs.delete()

        self.stdout.write(
            self.style.SUCCESS(f'Clean logs done : {amount} lignes deleted.')
        )
