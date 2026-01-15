import datetime
from django.core.management import call_command
from django.core.management.base import BaseCommand, CommandError
from django.contrib.auth.models import User
from loguru import logger

from app.models.setup import Setup

class Command(BaseCommand):
    help = "Setup app"

    def handle(self, *args, **options):
        if Setup.objects.count() == 0:
            try:
                logger.info("Seeding Database")
                call_command("seed", logs=False)

                logger.info("Creating admin user")
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
                logger.error(e)
