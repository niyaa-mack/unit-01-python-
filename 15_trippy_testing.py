"""
Exercise 1: Divide
"""
def divide(a, b):
  """Divides two numbers, handling potential division by zero.

  Args:
    a: The numerator.
    b: The denominator.

  Returns:
    The quotient, or None if b is zero.
  """

  if b == 0:
    return None
  else:
    return a / b
  
assert divide(6, 2) == 3 
assert divide(16, 8) == 2 #testing different results 
try: #extra credit 
    assert divide(32, 2) == 12
except AssertionError:
    pass

"""
Exercise 2: Factorial
"""
def factorial(n):
  """Calculates the factorial of a non-negative integer.

  Args:
    n: A non-negative integer.

  Returns:
    The factorial of n.
  """

  if n == 0:
    return 1
  else:
    return n * factorial(n - 1)

assert factorial(5) == 120
assert factorial(3) == 6 #assert testing factorial 
try: #making an error an exception 
    assert factorial(3) == 4 
except AssertionError:
    pass 

"""
Exercise 3: String Reverse
"""
def reverse_string(string):
  """Reverses a given string.

  Args:
    string: A string to be reversed.

  Returns:
    The reversed string.
  """

  reversed_string = ""
  for char in string:
    reversed_string = char + reversed_string
  return reversed_string


assert reverse_string("hello") == "olleh"
assert reverse_string("booyah") == "hayoob" #trippy testing the function 
try: 
    assert reverse_string("world") == "wormxdx" #using an error code 
except AssertionError: 
   pass  #making the error code a non-error

"""
Exercise 4: Fibonacci
"""
def fibonacci(n):
  """Generates the nth Fibonacci number.

  Args:
    n: The index of the Fibonacci number to calculate.

  Returns:
    The nth Fibonacci number.
  """

  if n <= 0:
    return 0
  elif n == 1:
    return 1
  else:
    return fibonacci(n - 1) + fibonacci(n - 2)


assert fibonacci(4) == 3
assert fibonacci(6) == 8 #trying out different values 
try: #try method to make the error work 
    assert fibonacci(3) == 323
except:
   pass

""" 
Exercise 5: Email Validation
"""

import re

def is_valid_email(email):
  """Determines whether email is valid or not

  Args:
    email: The email to validate

  Returns:
    Boolean value if email is valid
  """
  email_regex = r"^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,4})+"
  return re.match(email_regex, email) is not None

assert is_valid_email("shaniyamack11@gmail.com") == True
assert is_valid_email("kaitlynsmith23@gmail.com") == True #using different emails to see what works or not
try: #try is for the error code 
    assert is_valid_email("somethingschool3422") == True 
except AssertionError: #except is to use an exception for the error
   pass