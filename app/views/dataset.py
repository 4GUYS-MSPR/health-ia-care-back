import csv
import io
import json

from django.core.files.uploadedfile import UploadedFile
from django.http import HttpRequest
from django.utils.module_loading import import_string

from rest_framework import viewsets
from rest_framework.parsers import JSONParser, MultiPartParser

from app.imports.actions import BaseAction
from app.imports.request import ImportRequest, PartialImportRequest
from app.logs.logger import logger
from app.utils.validation import validate_request
from app.utils.response import JsonResponse

class DataImportViewSet(viewsets.ViewSet):

    parser_classes = [JSONParser, MultiPartParser]

    def create(self, request: HttpRequest):

        if request.content_type.startswith("application/json"):
            payload = json.loads(request.body.decode())
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

        action: BaseAction = cls(request.user)
        valid_data, errors = action.validate(validated.data)

        if errors:
            return JsonResponse.errors(errors)
        return action.handle(valid_data)

    def _handle_file_upload(self, request: HttpRequest):
        if "data" not in request.FILES:
            raise ValueError("Missing data file")

        uploaded_file = request.FILES["data"]
        filename = uploaded_file.name.lower()

        if filename.endswith(".json"):
            return self._parse_json_file(uploaded_file, request)

        if filename.endswith(".csv"):
            return self._parse_csv_file(uploaded_file, request)

        raise ValueError("Unsupported file format (json or csv only)")

    def _parse_json_file(self, file, request: HttpRequest):
        try:
            data = json.load(file)
        except Exception as e:
            raise ValueError(f"Invalid JSON file: {str(e)}") from e

        return {
            "classname": request.POST.get("classname"),
            "data": data,
        }

    def _parse_csv_file(self, file: UploadedFile, request: HttpRequest):
        try:
            body = request.POST.dict()

            decoded = file.read().decode("utf-8")
            reader = csv.DictReader(io.StringIO(decoded))

            validated = validate_request(PartialImportRequest, body)

            classname = validated.classname.value
            class_path = f"app.imports.actions.{classname}.{classname}"
            try:
                cls = import_string(class_path)
            except ImportError as e:
                raise ValueError(f"Invalid classname file: {str(e)}") from e
            action: BaseAction = cls(request.user)
            data = [action.scheme().model_validate(row).model_dump() for row in reader]
        except Exception as e:
            logger.exception("Invalid CSV file")
            raise ValueError(f"Invalid CSV file: {str(e)}") from e

        return {
            "classname": classname,
            "data": data,
        }
