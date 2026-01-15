from abc import ABC, abstractmethod
from pydantic import BaseModel, ValidationError
from app.utils.response import JsonResponse

class BaseAction(ABC):

    def __init__(self, scheme: BaseModel):
        self.scheme = scheme

    @abstractmethod
    def handle(self, data):
        return JsonResponse.notImplemented()

    def validate(self, data: list):
        errors = []
        valid = []
        for _, item in enumerate(data):
            try:
                scheme = self.scheme(**item)
                valid.append(scheme)
            except ValidationError as e:
                errors.append(e.json())
        return errors, valid

    def response(self, data: dict, code: int):
        return JsonResponse.response(data, code)
