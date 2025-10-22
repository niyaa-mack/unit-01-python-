"""
Task 1: People Class
Define a class called Person with attributes name and age.
Then, write a method within the class to introduce the person with their name and age.

Create a new object using this new class, and call the method you created.
"""
class Person:
    def __init__(self, name, age):
        self.name = name 
        self.age = age

    def hello(self):
        print(f"Hello, my name is " + self.name)
bob = Person("Bob", 23)
bob.hello()
print()
"""
Task 2: Animals Speak
Create a base class Animal with a empty method called speak. 
Then create two subclasses, Dog and Cat, each with their own speak method. 
Create objects using these subclasses and call the speak method.    
"""
class Animal:
    def speak(self):
        pass
class Dog: 
    def speak(self):   
        print("BARK")
dog = Dog()
dog.speak()
print()
class Cat: 
    def speak(self):
        print("MEOW")
cat = Cat()
cat.speak()
print()
"""
Task 3: Banking
Create a class BankAccount with attributes balance and owner. 
Include methods for depositing and withdrawing money, which should modify the balance attribute.
Test these methods with instances of the class.
"""
class BankAccount:
    def __init__(self, owner, balance = 0):
        self.owner = owner
        self.balance = balance
    def deposit(self, amount):
        if amount > 0:
            
        amount1 = input("how much money do you want to deposit ")
        print("I would like to deposit $" + amount1 + "dollars")

    def withdraw(self): 
        if 
        amount2 = input("How much you want to withdraw?")
