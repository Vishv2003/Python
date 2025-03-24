import json

json_data = '{"name": "Vishv", "age": 22, "city": "Ahmedabad"}'


dict_data = json.loads(json_data)


print(dict_data)
print(type(dict_data))  
