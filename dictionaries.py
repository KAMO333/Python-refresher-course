# A Dictionary is a collection which is unordered, changeable and indexed. No duplicate members.
# Read more about dictionaries at https://docs.python.org/3/tutorial/datastructures.html#dictionaries

# Create a dictionary
person = {
    'first_name': 'John',
    'last_name': 'Doe',
    'age': 31
}

# Use contractor
# person2 = dict(first_name='Sara', last_name='Williams')

# Get a value
print(person['first_name'])
print(person.get('last_name'))

# Add a key/value
person['phone'] = '060 000 5555'

# Get keys
print(person.keys())

# Get items
print(person.items())

# Copy a dict
person2 = person.copy()
person2['city'] = 'Cape Town'

print(person2)

# Remove an item
del person['age']
person.pop('phone')

# Clear
person.clear()

# Get length
print(len(person2))

# List of dict
people = [
    {'name': 'Martha', 'age': 30},
    {'name': 'Dorothy', 'age': 25}
]

print(people[0]['name'])