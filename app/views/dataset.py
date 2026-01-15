from django.utils.module_loading import import_string

from rest_framework import viewsets
from rest_framework.parsers import JSONParser

from app.imports.request import ImportRequest
from app.utils.validation import validate_request
from app.utils.response import JsonResponse

class DataImportViewSet(viewsets.ViewSet):

    parser_classes = [JSONParser]

    def create(self, request):
        if not isinstance(request.data, dict):
            return JsonResponse.errors("dict excepted")
        validated = validate_request(ImportRequest, request.data)

        data = validated.data
        classname = validated.classname.value
        class_path = f"app.imports.actions.{classname}.{classname}"
        try:
            cls = import_string(class_path)
        except ImportError:
            return JsonResponse.response({"message": f"{classname} not found."}, 404)

        action = cls()
        valid_data, errors = action.validate(data)

        if errors:
            return JsonResponse.errors(errors)
        return action.handle(valid_data)
