"""
TASK 1:
Write code that checks if a user entered the correct password.
The password should not be case sensitive

"""




"""
TASK 2:
Write code that checks if a user inputs an empty string
If the string is empty, print "invalid" otherwise print "valid"
"""
user = input("what is a food you would like to try?")
if user.strip == "":
    print("invalid")
else :
    print("valid ")
"""
TASK 3:

Write a program that will replace the word "cat" with the word "dog"
It should replace all occurances regardless of captilization 
"""
cat = str(input("give a word with cat inside of it"))
new_cat = cat.replace("cat", "dog")
print(new_cat)

"""
TASK 4:

Write a program that takes a person's name and age as input and prints it
"""
name = str(input("what is your name?"))
age = int(input("and what is your age?"))

print (name + " " + str(age))

"""
TASK 5:

Write a program that takes in two floats, and prints the quotient
The result should be rounded to the nearest tenth (1 decimal place)
"""
