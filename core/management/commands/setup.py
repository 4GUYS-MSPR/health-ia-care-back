import datetime

from django.core.management import call_command
from django.core.management.base import BaseCommand, CommandError
from django.contrib.auth.models import User

from app.models import Setup

from core.utils.logger import logger

class Command(BaseCommand):
    help = "Setup app"

    def add_arguments(self, parser):
        parser.add_argument(
            '--force',
            action='store_true',
            help='Force setup'
        )

    def handle(self, *args, **options):
        force = options.get('force')

        if Setup.objects.count() == 0 or force:
            try:
                logger.log.info("Seeding Database")
                call_command("seed", logs=False)

                logger.log.info("Creating admin user")
                admin, created = User.objects.get_or_create(
                    username="admin",
                    defaults={
                        "first_name": "Admin",
                        "is_active": True,
                        "is_staff": True,
                        "is_superuser": True,
                    }
                )
                if created:
                    admin.set_password("admin")
                    admin.save()
                Setup.objects.create(date=datetime.datetime.now())
            except CommandError as e:
                logger.log.exception(e)
