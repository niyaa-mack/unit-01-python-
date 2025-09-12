"""
TASK 1:
Create a float variable, and then convert it to an integer
Print both the original variable and the converted integer.

"""
print("-----------task 1---------------")
print()


a_flo = 18.976 
print(a_flo)
a_int=int(a_flo)
print(a_int)


print()
print()
print("--------------task 1-------------")
print()
print()
"""
TASK 2:
Write code that takes a number as input and prints whether 
it's positive, negative, or zero using if-elif-else statements.
"""

print("--------------task 2-------------")
print()

numb = int(input("Can you give me a number"))
if numb > 0 :
    print("This is a postive number")
elif numb == 0 :
    print("The number is zero")
elif numb < 0 :
    print("This is a negative number")


print("--------------task 2-------------")
print()
print()
"""
TASK 3:

Write code that takes two numbers as input (an integer and a float), 
performs addition, subtraction, multiplication, and division, and prints the results.
"""

print("--------------task 3-------------")
print()

num = float(input("give me a number"))
number = int(input("give me another number"))
print(num + number)
print(num - number)
print(num * number)
print(num / number)

print()
print()
print("--------------task 3-------------")
print()
print()
"""
TASK 4:

Create a dictionary with keys as fruit names and values as their respective quantities. 
Then print out the quantity of one of the fruits.
"""

print("--------------task 4-------------")
print()

y = {
    'mango' : 8,
    'pineapples' : 9
}
print(y["mango"])


print()
print()
print("--------------task 4-------------")
print()
print()
"""
TASK 5:

Create a string variable with that is a list of numbers and convert that string into a tuple.
Then print out the both the original string and tuple.
"""

print("--------------task 5-------------")
print()

my_string = "234"
my_tuple = my_string.split(" ,")
print(my_string)
print(my_tuple)


print()
print()
print("--------------task 5-------------")
print()
print()
"""
TASK 6:

Create a list of your favorite subjects (as strings). 
Use the join() function to combine all subjects into a single string separated by commas.
Then create another version using " - " as the separator.
Print both the original list and both joined strings.
"""

print("--------------task 6-------------")
print()


my_lis = ["math", "english", "science"]
print(my_lis)
my_thing = " , ".join(my_lis)
print(my_thing)






print()
print()
print("--------------task 6-------------")
print()
print()