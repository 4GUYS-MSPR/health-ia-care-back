import json

from django.utils.module_loading import import_string

from rest_framework import viewsets
from rest_framework.parsers import JSONParser, MultiPartParser

from app.imports.request import ImportRequest
from app.utils.validation import validate_request
from app.utils.response import JsonResponse

class DataImportViewSet(viewsets.ViewSet):

    parser_classes = [JSONParser, MultiPartParser]

    def create(self, request):

        if request.content_type.startswith("application/json"):
            payload = request.data
        elif request.FILES:
            payload = self._handle_file_upload(request)
        else:
            return JsonResponse.errors("Unsupported content type")

        validated = validate_request(ImportRequest, payload)

        classname = validated.classname.value
        class_path = f"app.imports.actions.{classname}.{classname}"
        try:
            cls = import_string(class_path)
        except ImportError:
            return JsonResponse.response({"message": f"{classname} not found."}, 404)

        action = cls()
        valid_data, errors = action.validate(validated.data)

        if errors:
            return JsonResponse.errors(errors)
        return action.handle(valid_data)

    def _handle_file_upload(self, request):
        if "data" not in request.FILES:
            raise ValueError("Missing data file")

        uploaded_file = request.FILES["data"]
        filename = uploaded_file.name.lower()

        if filename.endswith(".json"):
            return self._parse_json_file(uploaded_file, request)

        raise ValueError("Unsupported file format (json only)")

    def _parse_json_file(self, file, request):
        try:
            data = json.load(file)
        except Exception as e:
            raise ValueError(f"Invalid JSON file: {str(e)}") from e

        return {
            "classname": request.data.get("classname"),
            "data": data,
        }
