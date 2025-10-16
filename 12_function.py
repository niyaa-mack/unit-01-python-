"""
Task 1: Greeting
Write a function that takes a name as a 
agrument and prints a greeting message like "Hello, [name]!".
"""
print()
print()
def my_function(name):
    """
        Prints hello and you have to add a name to the argument.
         output example: Hello Jayden
    """
    print("Hello" + " " + name)
my_function("Shaniya")
print()
"""
Task 2: Square of a Number
Write a function that takes an integer as an argument and returns its square.
"""
print()
def integer(numb):
    """
        The code takes a number and square it and you get back the result.
         output example: input would be 9 and the result is 81
    """
    return numb ** 2
x = integer(7)
print(x)
    
"""
Task 3: Even or Odd
Write a function that takes a number as a argument that 
returns `True` if the number is even, and `False` otherwise.
"""
print()
def ft(number):
    """
        Seeing if the argument is a even number or odd number if even it will say True and if odd False
    """
    return number % 2 == 0 
print(ft(4))
print(ft(9))



"""
Task 4: Area of a Rectangle
Write a function that takes the length and width of a rectangle and returns its area.
"""
print()
def rectangle(w, l):
    """
        The width and length is being multiplied to get the area. 
    """
    return w * l
s = rectangle(3, 12)
print(s)
"""
Task 5: Celsius to Fahrenheit
Write a function that takes a temperature in Celsius and returns 
the equivalent temperature in Fahrenheit using the correct formula
"""
print()
def cf(c):
    """
        Using the converting formula the tempature in Celsius is converted to Fahrenheit
    """
    return (c * 1.8) + 32
d = cf(32)
print(d)

"""
Task 6: Average of Numbers
Write a function that takes a list of numbers as an argument
and returns the average (mean) of those numbers.
"""
print()
def list(meant):
    """
        The sum of the list divided by the amount of values finds the means of the number 
    """
    return sum(meant)/len(meant)
print(list([30,40,50]))
print()

"""
Task 7: Total Calculator
Create a function that has arguments for the price and quantity of something, 
and returns the total.

Your function should also optionally accept a 3rd argument for discount as a float, 
and return the discounted if provided.
"""
def calculator(p, q):
    """
        The price of something multiply the quantity of it and adds the discount if there is one
    """
    return (p * q) - 0.9
e = calculator(32,4)
print(e)