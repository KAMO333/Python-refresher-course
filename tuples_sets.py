# A Tuple is a collection which is ordered and unchangeable. Allows duplicate members.
 
# Create a tuple
fruits = ('Apples', 'Oranges', 'Grapes')
# Tuple constractor
# fruits2 = tuple(('Apple','Oranges', 'Grapes'))

# Single value needs trailing comma
fruits2 = ('Apples',)

# Get a value
print(fruits[1])

# Can't change a value
# fruits[0] = 'Pears'

# Delete tuple
del fruits2

# Get length 
print(len(fruits))


 
# A Set is a collection which is unordered and unindexed. No duplicate members.

# Create a set

fruits_set = {'Guava', 'Mango', 'Banana'}

# Check if in set
print('Guava' in fruits_set)

# Add to set
fruits_set.add('Citrus')
print(fruits_set)

# Remove a value
fruits_set.remove('Citrus')
print(fruits_set)

# Delete 
del fruits_set

print(fruits_set)

# Clear a set

fruits_set.clear()

print(fruits_set)
