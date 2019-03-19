favorite_languages = {
    'jen': ['python', 'java'],
    'sarah': ['c'],
    'edward': ['ruby', 'c#'],
    'phil': ['python', 'c++']
}
for name, languages in favorite_languages.items():
    print(name.title() + "'s favorite language is: ")
    for language in languages:
        print("\t" + language)

