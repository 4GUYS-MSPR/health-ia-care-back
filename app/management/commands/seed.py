import json

from pathlib import Path
from django.core.management.base import BaseCommand, CommandError
from django.db import models
from app.logs.logger import logger

from app.models.activity import Activity
from app.models.allergie import Allergie
from app.models.body_part import BodyPart
from app.models.category import Category
from app.models.dietary_restriction import DietaryRestriction
from app.models.disease_type import DiseaseType
from app.models.equipment import Equipment
from app.models.food_category import FoodCategory
from app.models.gender import Gender
from app.models.level import Level
from app.models.meal_type import MealType
from app.models.muscle import Muscle
from app.models.preferred_cuisine import PreferredCuisine
from app.models.recommendation import Recommendation
from app.models.severity import Severity
from app.models.subscription import Subscription

class SeedFile:
    model: type[models.Model]
    file: str

    def __init__(self, model: type[models.Model], file: str):
        self.model = model

        BASE_APP_DIR = Path(__file__).resolve().parent
        self.file = str(BASE_APP_DIR.parent.parent / 'seeders' / 'data' / file)

class Command(BaseCommand):
    help = "Seed database"

    def add_arguments(self, parser):
        parser.add_argument(
            '--logs',
            type=bool,
            help='Display logs',
            default=True
        )

    def get_seeders(self):
        return [
            SeedFile(model=Activity, file='activity.json'),
            SeedFile(model=Allergie, file='allergie.json'),
            SeedFile(model=BodyPart, file='body_part.json'),
            SeedFile(model=Category, file='category.json'),
            SeedFile(model=DietaryRestriction, file='dietary_restriction.json'),
            SeedFile(model=DiseaseType, file='disease_type.json'),
            SeedFile(model=Equipment, file='equipment.json'),
            SeedFile(model=FoodCategory, file='food_category.json'),
            SeedFile(model=Gender, file='gender.json'),
            SeedFile(model=Level, file='level.json'),
            SeedFile(model=MealType, file='meal_type.json'),
            SeedFile(model=Muscle, file='muscle.json'),
            SeedFile(model=PreferredCuisine, file='preferred_cuisine.json'),
            SeedFile(model=Recommendation, file='recommendation.json'),
            SeedFile(model=Severity, file='severity.json'),
            SeedFile(model=Subscription, file='subscription.json'),
        ]

    def handle(self, *args, **options):
        logs = options.get('logs')
        try:
            seeders: list[SeedFile] = self.get_seeders()
            for seeder in seeders:
                ok = 0
                ko = []
                if logs:
                    logger.info(f"Processing {seeder.model._meta.model_name}:")
                with open(seeder.file, 'r', encoding='utf-8') as data:
                    for row in json.load(data):
                        row["value"] = row["value"].upper()
                        try:
                            seeder.model.objects.get_or_create(**row)
                            ok+=1
                        except Exception:
                            ko.append(row)
                if logs:
                    logger.success(f"    {ok} elements inserted")
                    if len(ko) > 0:
                        logger.error(f"    {len(ko)} errors:")
                        for error in ko:
                            logger.error(f"     - {json.dumps(error)}")
                elif len(ko) > 0:
                    logger.error(f"{len(ko)} errors on model: {seeder.model._meta.model_name}")
        except CommandError as e:
            logger.exception(e)
