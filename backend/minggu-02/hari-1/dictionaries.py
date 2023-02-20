person = {
    'first_name': 'afriska',
    'last_name': 'yusuf',
    'age': '213',
    'country': 'Indonesia',
    'is_married': False,
    'skills': ['HTML', 'CSS', 'Python', 'Flask'],
    'address': {
        'street': 'mystreet',
        'zipcode': '01234'
    }
}
print(len(person))
print(person['skills'][2])
person['job'] = 'backend'
print(person)
person['skills'].append('Django')
print(person['skills'])

#-----------------------------------------------------------------------#
dct = {'key1':'value1', 'key2':'value2', 'key3':'value3', 'key4':'value4'}
print(dct)
dct.pop('key1')
print(dct)
dct.popitem()
print(dct)
print(dct.items())
keys = dct.keys()
print(keys, type(keys))
values = dct.values()
print(values, type(values))
