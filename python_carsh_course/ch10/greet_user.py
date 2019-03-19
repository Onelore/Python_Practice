import json
filename = 'username.json'
with open(filename) as f_object:
    username = json.load(f_object)
    print("welcome back, " + username)