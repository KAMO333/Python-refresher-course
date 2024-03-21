# Strings in python are surrounded by either single or double quotation marks. Let's look at string formatting and some string methods

name = 'Kamogelo'
age  = 31

# Contatinate
# print('Hello, my name is ' + name + ' and I am ' + str(age))

# STRING FORMATTING

# Arguments by position
# print('Hello, my name is {name}  and I am {age} '.format(name=name, age=age))

# F-string
# print(f'Hello, my name is {name} and I am {age}')

# STRING METHODS

s = 'hello world'
# Capitalize string
print(s.capitalize())

# Make all uppercase
print(s.upper())

# Make all lower
print(s.lower())

# Swapcase
print(s.swapcase())

# Get length
print(len(s))

# Replace
print(s.replace('world', 'everyone'))

# Count
sub = 'h'
print(s.count(sub))

# Starts with
print(s.startswith('hello'))

# End with
print(s.endswith('d'))

# Split into a list
print(s.split())

# Find popsition
print(s.find('r'))

# Is all alphanumeric
print(s.isalnum())

# Is all alphabets
print(s.isalpha())

# Is all numeric
print(s.isnumeric())
