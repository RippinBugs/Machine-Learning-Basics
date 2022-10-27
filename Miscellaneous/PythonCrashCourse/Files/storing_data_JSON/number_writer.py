import json

numbers = [2,3,4,6,7,11,14]

#json.dump() -> this will store values into the memory
filename = 'numbers.json'
with open(filename,'w') as file_object:
    json.dump(numbers,file_object)