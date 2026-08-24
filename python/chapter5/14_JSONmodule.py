# JSON -> javascript object notation 
# key : value   pairs 

import json

json_str = '{"name": "Shardha", "isTeacher":true}'
py_obj = json.loads(json_str)

print(type(py_obj))
print(py_obj)
