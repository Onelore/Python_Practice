print("give me two numbers , and i'll divide them.")
print("enter 'q' to quit")
while True:
    first_number = input("\nfirst number")
    last_number = input("\nlast number")
    try:
        answer = int(first_number) + int(last_number)
    except ValueError:
        pass
    else:
        print(answer)