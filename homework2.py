import json

data={
    "name": "John",
    "age": 30,
    "department": "IT",
    "is logged in": True,
    "test": None,
}

json_string=json.dumps(data, indent=4)
print(type(json_string))
print(json_string)


data='{"name": "John", "age": 30, "department": "IT", "is logged in": true, "test": null}'

python_dict=json.loads(data)
print(type(python_dict))
print(python_dict)