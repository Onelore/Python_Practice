print("give me two numbers , and i'll divide them.")
print("enter 'q' to quit")
while True:
    first_number = input("\nfirst number")
    last_number = input("\nlast number")
    try:
        answer = int(first_number)/int(last_number)
    except ZeroDivisionError:
        print("you can't divide by 0")
    else:
        print(answer)