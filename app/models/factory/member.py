import random

from django.contrib.auth.models import User
from django.utils import timezone

from app.models import Gender, Level, Member as Model, Objective, Subscription

from core.models.factory import Factory

class Member(Factory):

    def handle(self, number: int):
        client = User.objects.create(
            
        )
        for _ in range(number):
            data = {
                "id": 4,
                "age" : 18,
                "bmi" : 10.5,
                "fat_percentage" : 18,
                "height" : 180,
                "weight" : 80.5,
                "workout_frequency" : 3,
                "client" : client,
                "gender" : Factory.enum(Gender),
                "level" : Factory.enum(Level),
                "subscription" : Factory.enum(Subscription),
                "create_at" : timezone.now()
            }
            model = Model.objects.create(**data)

            for _ in range(random.randint(0, 10)):
                Objective.objects.create(
                    member=model,
                    value="Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s",
                    create_at=timezone.now()
                )
