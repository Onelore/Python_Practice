def greet_users(names):
    for name in names:
        message = "Hello, " + name.title() + "!"
        print(message)
user_names = ['hannah', 'try', 'xixi']
greet_users(user_names)
