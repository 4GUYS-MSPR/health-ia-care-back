def validate_fields_fata(data_list, fields: list[dict]) -> dict:
    invalid = {}
    for f in fields:
        valid_data = [r.value for r in f["model"].objects.all()]
        for data in data_list:
            data = data.model_dump()

            field_value = data.get(f["name"])
            if field_value is None:
                continue

            if not f["is_list"]:
                if not data[f["name"]] in valid_data:
                    add_to_dict(invalid, f["name"], data[f["name"]])
            else:
                for e in data[f["name"]]:
                    if not e in valid_data:
                        add_to_dict(invalid, f["name"], e)
    return invalid

def add_to_dict(d: dict, name, value):
    if name in d.keys():
        d[name].append(value)
    else:
        d[name] = [value]

def validate_request(model, request):
    return model(**request)
