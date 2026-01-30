from abc import ABC, abstractmethod
from pydantic import BaseModel, ValidationError

from django.db import transaction

from app.utils.response import JsonResponse
from app.utils.types import AnyUser
from app.utils.validation import validate_errors, ValidationErrorItem

from logs.models import Log
from logs.levels import LogLevel

class BaseAction(ABC):

    def __init__(self, scheme: type[BaseModel], user: AnyUser):
        self._scheme = scheme
        self.user = user

    @abstractmethod
    @transaction.atomic
    def handle(self, data):
        return JsonResponse.not_implemented()

    def validate(self, data: list):
        errors: list[ValidationErrorItem] = []
        valid = []
        for _, item in enumerate(data):
            try:
                scheme = self._scheme(**item)
                valid.append(scheme)
            except ValidationError as err:
                errors.extend(validate_errors(err.errors()))
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

    def success(self, count):
        Log.objects.create(
            type = LogLevel.SUCCESS,
            message = f"{self.scheme().__name__} import success",
            context = {
                "model": self.scheme().__name__,
                "rows": count
            }
        )
        return JsonResponse.success({"message": f"{count} row{'s' if count > 1 else ''} imported."})
