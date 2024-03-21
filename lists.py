# A List is a collection which is ordered and changeable. Allows duplicate members.

# Create list
numbers = [1, 2, 3, 4, 5]
fruits = ['Apples', 'Pears', 'Oranges', 'Grapes']

# Use a contryctor
# numbers2 = list((1, 2, 3, 4, 5))

# Get a value
print(fruits[1])

# Get the length
print(len(fruits))

# Append to list
fruits.append('Mangoes')

# Remove from list
fruits.remove('Grapes')

# Insert into position
fruits.insert(2, 'Bananas')

# Change value
fruits[0] = 'Blueberries'

# Remove with pop
fruits.pop(2)

# Reverse the list
fruits.reverse()

# Sort the list
fruits.sort()

# Reverse sort
fruits.sort(reverse=True)
print(fruits)