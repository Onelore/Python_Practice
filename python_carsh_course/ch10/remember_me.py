import json


#
# filename = 'username.json'
# try:
#     with open(filename) as f_object:
#         username = json.load(f_object)
# except FileNotFoundError:
#     username = input("what is your name?")
#     with open(filename, 'w') as f_object:
#         json.dump(username, f_object)
#         print("we'll remember you when you come back," + username)
# else:
#     print("welcome back, " + username)
def greet_user():

    username = get_stored_username()
    if username:
        print("welcome back, " + username)

    else:
        username = get_new_username()
        print("we'll remember when you back, " + username)


def get_stored_username():
    filename = 'username.json'
    try:
        with open(filename) as f_object:
            username = json.load(f_object)
    except FileNotFoundError:
        return None
    else:
        return username


def get_new_username():
    username = input("what is your name?")
    filename = 'username.json'
    with open(filename, 'w') as f_object:
        json.dump(username, f_object)
    return username


greet_user()
