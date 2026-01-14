def validateFieldsData(dataList, fields: list[dict]) -> dict:
    invalid = {}
    for f in fields:
        valid_data = [r.value for r in f["model"].objects.all()]
        for data in dataList:
            data = data.model_dump()
            if not f["enum"]:
                if not data[f["name"]] in valid_data:
                    addToDict(invalid, f["name"], data[f["name"]])
            else:
                for e in data[f["name"]]:
                    if not e in valid_data:
                        addToDict(invalid, f["name"], e)
    return invalid

def addToDict(d: dict, name, value):
    if name in d.keys():
        d[name].append(value)
    else:
        d[name] = [value]
