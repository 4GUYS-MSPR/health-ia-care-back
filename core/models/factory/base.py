import datetime
import random

from abc import ABC, abstractmethod

from django.db.models import Model

class Factory(ABC):

    @abstractmethod
    def handle(self):
        pass

    @staticmethod
    def enum(model: Model, create: bool = False):
        if create:
            value, _ = model.objects.get_or_create(
                value = random.choice(model.get_factory_values()),
                create_at = datetime.datetime.now()
            )
        else:
            values = model.objects.all()
            value = random.choice(values)
        return value
