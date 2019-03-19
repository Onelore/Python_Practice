def make_album(name, album_name, song_num=''):
    album = {'singer': name, 'album': album_name}
    if song_num:
        album['number'] = song_num
    return album
# new_album = make_album('jack', 'Hello world')
# print(new_album)
# new_album1 = make_album('mophine', 'look at me', 90)
# print(new_album1)
while True:
    album_name = input("The album's name:(enter 'q' to exit) ")
    if album_name == 'q':
        break
    singer_name = input("The album is belong to:(enter 'q' to exit) ")
    if singer_name == 'q':
        break
    new_album = make_album(album_name, singer_name)
    print(new_album)
