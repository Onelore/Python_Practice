people_info = {
    'jack': {'last_name': 'lore',
             'age': 23,
             'city': 'wuhan'},
    'clark': {'last_name': 'cline',
              'age': 29,
              'city': 'xian'}
}
for name, info in people_info.items():
    print(name.title() + " " + info['last_name'].title())
    print("\t" + str(info['age']))
    print("\t" + info['city'].title())
