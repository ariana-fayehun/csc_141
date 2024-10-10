def build_person(first_name, last_name, age=None):
    """Return a dictionary of info abour a person."""
    person = {'first': first_name, 'last': last_name}
    if age:
        person['age'] = age
    return person

musician = build_person('jimmi', 'hendrix', age=27)
print(musician)