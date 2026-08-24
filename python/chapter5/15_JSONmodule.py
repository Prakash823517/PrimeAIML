import json

py_obj = {
    "name": "Shardha",
    "isTeacher": True
}

json_str = {
    "name": "Shardha",
    "isTeacher": None
}

json_str = json.dumps(py_obj)
print(type(json_str), json_str)
