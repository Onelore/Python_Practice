import json
filename = 'number.json'
with open(filename) as f_object:
    numbers = json.load(f_object)
print(numbers)
