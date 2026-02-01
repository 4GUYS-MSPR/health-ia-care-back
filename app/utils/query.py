from django.db import models

from app.utils.types import AnyUser

def getQueryALLForUser(model: models.Model, user: AnyUser):
    return model.objects.all() if user.is_superuser else model.objects.all().filter(client=user)
