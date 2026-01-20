from abc import ABC, abstractmethod
from pydantic import BaseModel, ValidationError

from django.db import transaction

from app.utils.response import JsonResponse
from app.utils.types import AnyUser

class BaseAction(ABC):

    def __init__(self, scheme: type[BaseModel], user: AnyUser):
        self._scheme = scheme
        self.user = user

    @abstractmethod
    @transaction.atomic
    def handle(self, data):
        return JsonResponse.not_implemented()

    def validate(self, data: list):
        errors = []
        valid = []
        for _, item in enumerate(data):
            try:
                scheme = self._scheme(**item)
                valid.append(scheme)
            except ValidationError as e:
                errors.append(e.json())
        return valid, errors

    @staticmethod
    def response(data: dict, code: int):
        return JsonResponse.response(data, code)

    def scheme(self):
        return self._scheme

    def upper(self, value: str | list[str]):
        if isinstance(value, list):
            return [v.upper() for v in value]
        return value.upper()
