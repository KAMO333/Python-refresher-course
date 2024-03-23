# A class is like a blueprint for creating objects. An object has properties and methods(functions) associated with it. Almost everything in Python is an object

# Create a class
class User:
    # Constructor
    def __init__(self, name, email, age):
     self.name = name
     self.email = email
     self.age = age


    def greeting (self):
       return f'Hello, my name is {self.name} and I am {self.age} years old'
    
    def has__birthday(self):
       self.age += 1

# Extend class
class Customer(User):
     # Constructor
    def __init__(self, name, email, age):
     self.name = name
     self.email = email
     self.age = age
     self.balance = 0


    def set_balance(self, balance):
        self.balance = balance

    


    def greeting (self):
       return f'Hello, my name is {self.name} and I am {self.age} and my balnce is {self.balance}'

# init user object
kamo = User('Kamo Mmops', 'k@gmail.com', 31)
# init customer object
janet = Customer('Janet Johnson', 'janet@yahoo.com', 25)

janet.set_balance(500)
print(janet.greeting())


kamo.has__birthday()
print(kamo.greeting())
