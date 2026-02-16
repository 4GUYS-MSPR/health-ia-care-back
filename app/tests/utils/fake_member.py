from app.models.member import Member
from app.models.gender import Gender
from app.models.level import Level
from app.models.subscription import Subscription
import datetime

def create_member(client, **kwargs):
    """
        Just a function to create a fake member
    """
    gender = Gender.objects.create(value = "FEMALE", create_at = datetime.datetime.now())
    level = Level.objects.create(value = "BEGINNER", create_at = datetime.datetime.now())
    subscription = Subscription.objects.create(value = "FREE", create_at = datetime.datetime.now())

    defaults = {
            "age" : 18,
            "bmi" : 10.5,
            "fat_percentage" : 18,
            "height" : 180,
            "weight" : 80.5,
            "workout_frequency" : 3,
            "objectives" : [],
            "client" : client,
            "gender" : gender,
            "level" : level,
            "subscription" : subscription,
            "create_at" : datetime.datetime.now()
    }

    defaults.update(kwargs)
    return Member.objects.create(**defaults)
        