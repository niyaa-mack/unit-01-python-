"""
Exercise 1:
Write a program to print numbers from 1 to 10 using a for loop.
"""
print()
print()
set = ["1","2","3","4","5","6","7","8","9","10"]
for x in range(1,11):
    print(x)

"""
Exercise 2:
Write a program to count by 10s from 900 to 1000
"""
print()
print()
for x in range(900, 1001, 10):
    print(x)
"""
Exercise 3:
Write a program that counts form 1-100 by 9
"""
print()
print()
for x in range (1, 101, 9):
    print(x)
"""
Exercise 4:
Write a program to calculate the sum of all numbers from 1 to 10 using a for loop.
"""
print()
print()

for x in range(1,11):
    print(x)
    
print()
print()
"""
Excercise 5:
Uncomment the following code and run it. Then answer the following:
- What is the ouput of the code?

- Explain the iterative process that this code executes to get that output
"""
rows = 5
 
for i in range(rows):
    for j in range(i + 1):
        print('*', end=' ')
    print()
