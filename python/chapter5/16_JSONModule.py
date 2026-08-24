import json

with open("chapter5/data.json", "r") as f:
    py_obj = json.load(f)
    print(py_obj)
    print(type(py_obj))



data = {
    "name": "shardha",
    "age": 27,
    "isTeacher": True
}
with open("chapter5/data.json", "w") as f:
    # data.json file will be overwritten by above data object 
    json.dump(data, f) 
    # json.dump(data, f, indent = 4) 
    # json.dump(data, f, indent = 4, sort_keys = True) 

