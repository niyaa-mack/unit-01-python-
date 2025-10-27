"""
Task 1: People Class
Define a class called Person with attributes name and age.
Then, write a method within the class to introduce the person with their name and age.

Create a new object using this new class, and call the method you created.
"""
class Person: 
    def __init__(self, name, age): #init method to use for the class so it can use the attributes
        self.name = name 
        self.age = age

    def hello(self): #hello method to introduce the person 
        print(f"Hello, my name is " + self.name)
bob = Person("Bob", 23) #made a variable for the name and age of the person 
bob.hello()
print()
"""
Task 2: Animals Speak
Create a base class Animal with a empty method called speak. 
Then create two subclasses, Dog and Cat, each with their own speak method. 
Create objects using these subclasses and call the speak method.    
"""
class Animal: 
    def speak(self):# make a empty method 
        pass

class Dog: # made a dog subclass for the dog to speak
    def speak(self):   
        print("BARK") 
dog = Dog()
dog.speak()
print()
class Cat: #made a cat class so when it prints out the cat speaks
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
    def __init__(self, owner, balance = 0): #
        self.owner = owner
        self.balance = balance

    def deposit(self, amount): #when the user wants to deposit add the amount to the balance 
        self.balance += amount
        print("deposited:", amount)

    def withdraw(self, amount): #withdraw the amount from the balance 
        if amount <= self.balance:
            self.balance -= amount
            print("Withdrew:", amount)
        
        else:
            print("Not enough balance.") 

account = BankAccount("Shaniya", 88) #the testing of the class
account.deposit(54)
account.withdraw(30)
account.withdraw(90)