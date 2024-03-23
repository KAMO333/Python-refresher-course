# Python has functions for creating, reading, updating, and deleting files.

# Open a file
myFile = open('myfile.tsxt', 'w')

# Get some info
print('Name: ', myFile.name)
print('is Closed: ', myFile.closed)
print('Open Mode: ', myFile.mode)


# Write to file
myFile.write('I love Python')
myFile.write(' and JavaScript')
myFile.close()

# Append to file
myFile = open('myfile.txt', 'a')
myFile.write(' and I also like PHP and Java')
myFile.close()

# Read a file
myFile = open('myfile.txt', 'r+')
text = myFile.read(100)
print(text)
