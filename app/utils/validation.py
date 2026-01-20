from pydantic import BaseModel

def validate_fields_data(data_list: list[BaseModel], fields: list[dict]) -> dict:
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
