from typing import TypeVar, List

from pydantic import BaseModel
from pydantic_core import ErrorDetails

from app.schemas.validation_error_item import ValidationErrorItem

T = TypeVar('T', bound=BaseModel)

def validate_fields_data(data_list: List[T], fields: List[dict]) -> dict:
    invalid = {}
    index = 1
    for f in fields:
        valid_data = [r.value for r in f["model"].objects.all()]
        for data in data_list:
            data = data.model_dump()

            field_value = data.get(f["name"])
            if field_value is None:
                continue

            if not f["is_list"]:
                if not data[f["name"]].upper() in valid_data:
                    add_to_dict(invalid, index, f["name"], data[f["name"]].upper())
            else:
                for e in data[f["name"]]:
                    if not e.upper() in valid_data:
                        add_to_dict(invalid, index, f["name"], e.upper())
        index+=1
    return invalid

def add_to_dict(d: dict, index: int, name: str, value):
    if not index in d.keys():
        d[index] = {}
    if name in d[index].keys():
        d[index][name].append(value)
    else:
        d[index][name] = [value]

def validate_request(model, request):
    return model(**request)

def validate_errors(errors: list[ErrorDetails]) -> list[ValidationErrorItem]:
    validation_errors = []
    for err in errors:
        fields = [str(f) for f in err.get("loc", [])]
        message = err.get("msg", "")
        input_value = err.get("input", "")
        expected = err.get("ctx", {}).get("expected", "")

        item = ValidationErrorItem(
            fields=fields,
            message=message,
            input=input_value,
            expected=expected
        )
        validation_errors.append(item.model_dump())
    return validation_errors
