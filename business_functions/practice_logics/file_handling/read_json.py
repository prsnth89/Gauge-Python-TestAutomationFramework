import json
import os

def read_json(path):
    json_load=None
    with open(path,'r') as file:
        json_load=json.load(file)
    return json_load

file_name=os.path.join(os.getcwd(),"./business_functions/practice_logics/file_handling/input.json")
print(file_name)

json_read=read_json(file_name)
print(json_read)
for json in json_read:
    print(json)