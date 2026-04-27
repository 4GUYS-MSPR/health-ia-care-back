import datetime
from app.models import Gender, Level, Member, Objective, Subscription

def create_gender():
    gender = Gender.objects.create(value = "FEMALE", create_at = datetime.datetime.now())
    return gender

def create_level():
    level = Level.objects.create(value = "BEGINNER", create_at = datetime.datetime.now())
    return level

def create_subscription():
    subscription = Subscription.objects.create(value = "FREE", create_at = datetime.datetime.now())
    return subscription


def create_member(user, client, **kwargs):
    """
        Just a function to create a fake member
    """
    gender = create_gender()
    level = create_level()
    subscription = create_subscription()

    objectives = [] if "objectives" not in dict.keys(kwargs) else kwargs["objectives"]

    defaults = {
            "age" : 18,
            "bmi" : 10.5,
            "fat_percentage" : 18.2,
            "height" : 180.2,
            "weight" : 80.5,
            "workout_frequency" : 3,
            "user" : user,
            "client" : client,
            "gender" : gender,
            "level" : level,
            "subscription" : subscription,
            "created_at" : datetime.datetime.now()
    }

    defaults.update(kwargs)
    member = Member.objects.create(**defaults)
    for objective in objectives:
        Objective.objects.create(member=member, value=objective)
    return member

def create_expected_member(client, **kwargs):
    """
        Just a function to create a fake expected member
    """
    gender = create_gender()
    level = create_level()
    subscription = create_subscription()

    objectives = [] if "objectives" not in dict.keys(kwargs) else kwargs["objectives"]

    defaults = {
            "id": 4,
            "age" : 18,
            "bmi" : 10.5,
            "fat_percentage" : 18,
            "height" : 180,
            "weight" : 80.5,
            "workout_frequency" : 3,
            "client" : client,
            "gender" : gender,
            "level" : level,
            "subscription" : subscription,
            "create_at" : datetime.datetime.now()
    }

    defaults.update(kwargs)
    member = Member.objects.create(**defaults)
    for objective in objectives:
        Objective.objects.create(member=member, value=objective)
    return member
