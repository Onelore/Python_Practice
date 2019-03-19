def build_person(first_name, last_name, age=''):
    person = {'first': first_name, 'last': last_name}
    if age:
        person['age'] = age
    return person
name = build_person('jimi', 'john', age=32)
print(name)