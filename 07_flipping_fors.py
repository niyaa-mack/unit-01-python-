"""
Exercise 1:
Write a program to print each character of a given string using a for loop.
"""
print()
print()
hey = "hey friend" #made a variable
for char in hey: #for loop to make the loop for the char
    print (char) #print out the characters in the string 
print()
print()
"""
Exercise 2:
Write a program to calculate the sum of elements in a list using a for loop.
"""
lock = [89, 5, 3] #made a list
count = 0 

for num in lock: 
    count += num #added all the number together in the list 
    
print("The sum of the elements are", count) #printing out the sum of the list 
print()
print()
    
"""
Exercise 3:
Write a program to print the length of each word in a sentence using a for loop and a list.
"""
real = "Jayden is annoying"

words = real.split() #variable to seperate the words 

for x in words: 
    print(len(x)) #for loop to found how long the words are

print()
print()
"""
Excercise 4:
Write a program that creates a dictionary (atleast 4 key:value pairs) and then
iterates through a dictionary and prints the result

In a comment, answer the following, what do you notice about the output of your code?
Is it what you expected?
"""
print()
print()
bro = {
    'mango': 5,
    'school': "BGHS",
    'banana': 4, 
    'apple': 8
} #made a dict

for key, value in bro.items():
    print(key,value) # print the keys and values of the dictionary 

print()
print()