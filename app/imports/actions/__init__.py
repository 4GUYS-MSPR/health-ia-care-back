from abc import ABC, abstractmethod
from pydantic import BaseModel, ValidationError

from django.db import transaction

from app.utils.response import JsonResponse

class BaseAction(ABC):

    def __init__(self, scheme: type[BaseModel]):
        self.scheme = scheme

    @abstractmethod
    @transaction.atomic
    def handle(self, data):
        return JsonResponse.not_implemented()

    def validate(self, data: list):
        errors = []
        valid = []
        for _, item in enumerate(data):
            try:
                scheme = self.scheme(**item)
                valid.append(scheme)
            except ValidationError as e:
                errors.append(e.json())
        return valid, errors

    @staticmethod
    def response(data: dict, code: int):
        return JsonResponse.response(data, code)
