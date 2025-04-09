

def build_person(first_name, last_name, age=None):
    """
    返回字典

    """
    person = {'first': first_name, 'last': last_name}
    # age有值时，返回true，None时，返回false
    if age:
        person['age'] = age
    return person

musician = build_person('jimi', 'hendrix', age=27)
print(musician)