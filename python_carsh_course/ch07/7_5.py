active = True
while active:
    age = input("\nwhat's your age?(enter 'quit' to exit)")
    if age == 'quit':
        active = False
        break
    elif int(age) < 3:
        print("\nPlease free to watch movie!")
    elif 3 <= int(age) <= 12:
        print("\nPlease pay $9 to watch movie!")
    elif int(age) > 12:
        print("\nPlease pay $19 to watch movie!")
