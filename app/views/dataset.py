import csv
import io
import json

from django.core.files.uploadedfile import UploadedFile
from django.http import HttpRequest
from django.utils.module_loading import import_string

from pydantic import ValidationError

from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.parsers import JSONParser, MultiPartParser

from app.imports.actions import BaseAction
from app.imports.request import ActionEnum, ImportRequest, PartialImportRequest
from app.utils.logger import logger
from app.utils.response import JsonResponse
from app.utils.validation import validate_errors, validate_request

from logs.levels import LogLevel

class DataImportViewSet(viewsets.ViewSet):

    parser_classes = [JSONParser, MultiPartParser]

    def list(self, _):
        return JsonResponse.success({
            "classname": [a.value for a in ActionEnum],
            "data": ["objects"]
        })

    # ====================================================
    # | Changer les logs pour utiliser celle de la PR 46 |
    # ====================================================
    @action(detail=False, methods=['get'], url_path='(?P<classname>[^/.]+)')
    def action_help(self, request: HttpRequest, classname = None):
        if classname not in [a.value for a in ActionEnum]:
            logger.error("Invalid classname")
            return JsonResponse.errors({
                "input": classname
            }, message="Invalid classname")

        class_path = f"app.imports.actions.{classname}.{classname}"
        try:
            cls = import_string(class_path)
        except ImportError:
            return JsonResponse.response({"message": f"{classname} not found."}, 404)

        classname_action: BaseAction = cls(request.user)

        return JsonResponse.success(classname_action.scheme().model_json_schema())

    def create(self, request: HttpRequest):
        fullname = getattr(request.user, "get_full_name", lambda: "Anonymous")()
        username = fullname if fullname != "" else str(request.user.username)

        try:
            if request.content_type and request.content_type.startswith("application/json"):
                payload = json.loads(request.body.decode())
            elif request.FILES:
                payload = self._handle_file_upload(request)
            else:
                return logger.new(
                    level = LogLevel.ERROR,
                    message = "Unsupported content type",
                    http_code = status.HTTP_400_BAD_REQUEST,
                    context = {
                        "user": username,
                        "content-type": request.content_type,
                        "files": request.FILES
                    }
                )

            validated = validate_request(ImportRequest, payload)

            classname = validated.classname.value
            class_path = f"app.imports.actions.{classname}.{classname}"
            try:
                cls = import_string(class_path)
            except ImportError:
                return logger.new(
                    level = LogLevel.ERROR,
                    message = "Classname not found",
                    http_code = status.HTTP_400_BAD_REQUEST,
                    context = {
                        "user": username,
                        "classname": classname
                    }
                )

            action: BaseAction = cls(request.user)
            valid_data, errors = action.validate(validated.data)

            if errors:
                return logger.validationErrors(username, errors)
            return action.handle(valid_data)
        except ValidationError as error:
            return logger.validationErrors(username, validate_errors(error.errors()))
        except ValueError as error:
            return logger.new(
                level = LogLevel.ERROR,
                message = "Error during import",
                http_code = status.HTTP_400_BAD_REQUEST,
                context = {
                    "type": type(error.__cause__).__name__,
                    "message": str(error.__cause__)
                }
            )

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
            classname_action: BaseAction = cls(request.user)
            data = [classname_action.scheme().model_validate(row).model_dump() for row in reader]
        except Exception as e:
            raise ValueError(f"Invalid CSV file {str(e)}") from e

        return {
            "classname": classname,
            "data": data,
        }
