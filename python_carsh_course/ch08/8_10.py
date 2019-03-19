def show_magicians(name):
    for name in name:
        print(name.title())


def make_great(name):
    for value in range(0, len(name)):
        name[value] = "The Great " + name[value]


names = ['jack', 'bob', 'john', 'phil']
names1 = names[:]
make_great(names1)
show_magicians(names1)
print(names)
