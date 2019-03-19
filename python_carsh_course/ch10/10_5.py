filename = "question.txt"
while True:
    message = input("why u like programing?")
    with open(filename,'a') as file_object:
        file_object.write(message.title())
    if message =='q':
        break