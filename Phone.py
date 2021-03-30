class Phone():
    def __init__(self, phone_number):
        self.phone_number = phone_number
    
    def __str__(self):
        return f'{self.phone_number}'

    def call(self, other_number):
        print(f'Calling {other_number}')

    def text(self, other_number, msg):
        print(f'Sending text msg from {self.phone_number} to {other_number}')
        print(msg)

my_phone = Phone('(222)333-4567')
print('this is my phone', my_phone)
# my_phone.call('(123)456-7890')
my_phone.text('(123)456-7890', 'heyyy')

# INHERITANCE!
class IPhone(Phone): # 'extends' keyword in JavaScript
    def __init__(self, phone_number, generation, color='black'):
        # super keyword
        super().__init__(phone_number)
        self.generation = generation
        self.color = color

    # method overriding - a good example of Inheritance and Polymorphism
    def text(self, other_number, msg):
        print(f"'{msg}' - Sent from my iPhone")

my_iPhone = IPhone('(222)123-1234', '7s')
my_iPhone.call('(123)999-9999')
my_iPhone.text('(123)999-9999', 'heyyyyy')
print(my_iPhone.color)