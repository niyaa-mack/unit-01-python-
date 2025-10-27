"""
Identify the potential errors in the following code snippets and modify 
them to include appropriate try/except blocks to handle exceptions gracefully.
"""


"""
Example 1: Division
"""
print()
def divide_numbers(num1, num2): 
    try:
        result = num1 / num2
        print("Result:", result)
    except ZeroDivisionError: #the type of error it gets so you have to tell them what they are doing wrong
        print("You cant put the second number as 0. ")

# Example usage:
divide_numbers(10, 0)
print()
"""
Example 2: Opening Files
"""

def read_file(filename): 
    try: #this code is being analyzed by 
        file = open(filename, 'r')
        contents = file.read()
    except FileNotFoundError: # 
        print("There is no file found named nonexistent.txt")
    

# Example usage:
read_file("nonexistent.txt")
print()

"""
Example 3: List Items
"""

def get_item(lst, index):
    try:
        item = lst[index]
        print("Item:", item)
    except IndexError:
        print("Computer starts at 0 ")

# Example usage:
my_list = [1, 2, 3]
get_item(my_list, 5)

"""
Example 4: Dictionaries
"""
print()
def get_value(dictionary, key):
    try:
        value = dictionary[key]
        print("Value:", value)
    except KeyError:
        print("there is no c.")
# Example usage:
my_dict = {"a": 1, "b": 2}
get_value(my_dict, "c")
print()

"""
Example 5: Else/Finally
Modify the following code to include an else block to execute code if no exceptions occur 
and a finally block to ensure that a certain action is always performed, regardless of whether an exception is raised.
"""
def process_file(filename):
    try:
        with open(filename, 'r') as file:
            contents = file.read()
            print("File contents:", contents)
    except FileNotFoundError:
            print("Error: File not found.")
    else:
        print("the code works no errors")
    finally:
        print("the file is not here so you have to make one.")

# Example usage:
process_file("example.txt")

