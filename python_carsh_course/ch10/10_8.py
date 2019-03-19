def file_any(filename):
    try:
        with open(filename) as file_object:
            contents = file_object.readlines()
    except FileNotFoundError:
        print(filename + "文件不存在")
    else:
        for line in contents:
            print(line.rstrip()+"\t")

file_cats = file_any('cats.txt')
file_dogs = file_any('dogsa.txt')