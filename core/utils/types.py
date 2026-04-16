from typing import Union

from django.contrib.auth.models import AnonymousUser

from core.utils.user import User

AnyUser = Union[User, AnonymousUser]
