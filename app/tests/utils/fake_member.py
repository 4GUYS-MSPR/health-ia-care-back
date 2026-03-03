import datetime
from app.models.member import Member
from app.models.gender import Gender
from app.models.level import Level
from app.models.subscription import Subscription


def create_gender():
    gender = Gender.objects.create(value = "FEMALE", create_at = datetime.datetime.now())
    return gender

def create_level():
    level = Level.objects.create(value = "BEGINNER", create_at = datetime.datetime.now())
    return level

def create_subscription():
    subscription = Subscription.objects.create(value = "FREE", create_at = datetime.datetime.now())
    return subscription


def create_member(client, **kwargs):
    """
        Just a function to create a fake member
    """
    gender = create_gender()
    level = create_level()
    subscription = create_subscription()

    defaults = {
            "age" : 18,
            "bmi" : 10.5,
            "fat_percentage" : 18.2,
            "height" : 180.2,
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

def create_expected_member(client, **kwargs):
    """
        Just a function to create a fake expected member
    """
    gender = create_gender()
    level = create_level()
    subscription = create_subscription()

    defaults = {
            "id": 4,
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
