def count_words(filename):
    try:
        with open(filename) as file_object:
            contents = file_object.read()
    except FileNotFoundError:
        # message = "sorry, the file " + filename +"doesn't exit"
        # print(message)
        pass
    else:
        words = contents.split()
        num_wordds = len(words)
        print("the file " + filename + " has about " + str(num_wordds))


filenames = ['alice.txt', 'siddle.txt', 'moby_dick.txt', 'little_women.txt']
for filename in filenames:
    count_words(filename)
