import json
filename = 'storing_data_JSON/numbers.json'
with open(filename,'r') as file_object:
    numbers = json.load(file_object)

print(numbers)