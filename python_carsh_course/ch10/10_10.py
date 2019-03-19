filename = 'Gutenberg.txt'
try:
    with open(filename) as file_object:
        contents = file_object.read()
except FileNotFoundError:
    pass
else:
    print(contents.count(' are '))
