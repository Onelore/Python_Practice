filename = "guest_book.txt"
while True:
    name = input("please enter your name!")
    with open(filename, 'a') as file_object:
        file_object.write(name.title() + "\n")
        print("Hello, " +name.title())