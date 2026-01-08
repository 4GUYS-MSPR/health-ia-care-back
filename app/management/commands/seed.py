import json

from pathlib import Path
from django.core.management.base import BaseCommand, CommandError
from django.db import models

from app.models.body_part import BodyPart
from app.models.category import Category
from app.models.equipment import Equipment
from app.models.gender import Gender
from app.models.level import Level
from app.models.muscle import Muscle
from app.models.subscription import Subscription

class SeedFile:
    model: models.Model
    file: str

    def __init__(self, model: models.Model, file: str):
        self.model = model

        BASE_APP_DIR = Path(__file__).resolve().parent
        self.file = BASE_APP_DIR.parent.parent / 'seeders' / 'data' / file

class Command(BaseCommand):
    help = "Seed database"

    def handle(self, *args, **options):
        try:
            seeders: list[SeedFile] = [
                SeedFile(model=BodyPart, file='body_part.json'),
                SeedFile(model=Category, file='category.json'),
                SeedFile(model=Equipment, file='equipment.json'),
                SeedFile(model=Gender, file='gender.json'),
                SeedFile(model=Muscle, file='muscle.json'),
                SeedFile(model=Level, file='level.json'),
                SeedFile(model=Subscription, file='subscription.json'),
            ]
            for seeder in seeders:
                ok = 0
                ko = []
                self.stdout.write(self.style.MIGRATE_HEADING(f"Processing {seeder.model._meta.model_name}:"))
                with open(seeder.file, 'r', encoding='utf-8') as data:
                    for row in json.load(data):
                        try:
                            seeder.model.objects.get_or_create(**row)
                            ok+=1
                        except Exception as e:
                            ko.append(row)
                            self.stdout.write(self.style.ERROR(e))
                self.stdout.write(self.style.SUCCESS(f"    - {ok} elements inserted"))
                if len(ko) > 0:
                    self.stdout.write(self.style.ERROR(f"   - {len(ko)} errors:"))
                    for error in ko:
                        self.stdout.write(self.style.ERROR(f"       \n- {json.dumps(error)}"))
        except CommandError as e:
            self.stdout.write(e)
