the_rivers = {
    'nile': 'egypt',
    'long river': 'china',
    'yellow river': 'china'
}
for river in the_rivers:
    print("The " + river.title() + " runs through " + the_rivers[river].title())
print("\n")
for country in the_rivers.values():
    print(country.title())

print("\n")
for river in the_rivers.keys():
    print(river.title())
