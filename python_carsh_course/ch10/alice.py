filename = 'alice.txt'
try:
    with open(filename) as file_object:
        name = file_object.read()

except FileNotFoundError:
    msg = "sorry, the file " + filename + " doesn't exit"
    print(msg)
else:
    words = name.split()
    new_words = len(words)
    print("the file " + filename + " has about " + str(new_words) + " words.")