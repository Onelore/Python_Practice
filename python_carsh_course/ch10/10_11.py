import json


def favorite_new_num():
    filename = 'favoritenum.json'
    with open(filename, 'w') as f_object:
        favoritenum = input("what's your favorite num?")
        json.dump(favoritenum, f_object)


def favorite_num():
    filename = 'favoritenum.json'
    try:
        with open(filename) as f_object:
            favoritenum = json.load(f_object)
    except FileNotFoundError:
        return None
    else:
        return favoritenum


def outnum():
    favoritenum = favorite_num()
    if favoritenum:
        print("i know your num, " + favoritenum)
    else:
        favoritenum = favorite_new_num()
        print("i will your num")


outnum()
