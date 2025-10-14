from datetime import date 
from datetime import time
from datetime import datetime
"""
Exercise 1:
Write a Python program that prints the current date and time using the datetime module.
"""
print()
my_datetime = datetime.now() #use this to get the current day
print(my_datetime) #it will show in terminal

"""
Exercise 2:
Write a Python program that prints the current date and time using the datetime module.
Using the strftime function format the date in standard U.S. date format (MM/DD/YYYY)
"""
print()
my_datetimef = datetime.now()
new = datetime.strftime(my_datetimef, "%m/%d/%Y") #formatting the current date and time 
print(new)

"""
Exercise 3:
Using the strptime function, convert two strings into dates.
Then find the difference in days between the two.
"""
print()
str = "05 - 23 - 2008"
str1 = "10/23/20" #made two strings 
string1 = datetime.strptime(str, "%m - %d - %Y")
string2 = datetime.strptime(str1, "%m/%d/%y") #formatting the two strings 
print(string1)
print(string2) #printing both strings in the format 
print()
print("the difference is", string2 - string1) #the difference of both dates 
"""
Excercise 4:
Write a program that asks the user for their birthdate and calculates their current 
age using the datetime module.
"""
print()
day = input("what is your birthday in the format MM/DD/YYYY?: ")
user_birthdate = datetime.strptime(day, "%m/%d/%Y") #formatting user input 
cur_day = datetime.today()
age = cur_day - user_birthdate #calculating user age
print(age) 
print()