# To make a CoffeeCup class definition
# A class is: 
# It can save save you a lot of lines of code
# A class can have methods
# Classes can have variables (aka state)


class CoffeeCup():
    def __init__(self, capacity): # this is the constructor!
        # pass #NOOP - does nothing
        self.capacity = capacity # instance variables
        self.amount = 0
    
    # An example of method overriding
    def __str__(self):
        return f'This {self.capacity} oz coffee cup is {self.amount} oz full'

    def fill(self, amount):
        self.amount += amount
        if(self.amount >= self.capacity):
            self.amount = self.capacity
            print('Whoops! We spilled some coffee')

my_coffee_cup = CoffeeCup(12)
# print(CoffeeCup) # Printed the class definition
# print(my_coffee_cup) # Printed the memory address where this object is at
# print(dir(my_coffee_cup))
# print(my_coffee_cup)

# In OOP - this would be a bad convention
# my_coffee_cup.amount = 10
# print(my_coffee_cup)
# It would be better to have some sort of INTERFACE to use instead
# my_coffee_cup.fill(10)
# my_coffee_cup.fill(10)
# print(my_coffee_cup)

# henrys_coffee = CoffeeCup(10)
# print(henrys_coffee)
# westons_coffee = CoffeeCup(24)
# print(westons_coffee)
colins_coffee = CoffeeCup(14)
print(dir(colins_coffee))