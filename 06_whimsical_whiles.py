"""
1. Simple Counter:
Write a program that uses a while loop to print numbers from 1 to 10.
"""
s = 0 #made a variable 
while s < 10: #going to keep going until the s variable is greater than 10
        s += 1 #increase the number 
        print(s) #print the increased number 
"""
2. Countdown:
Write a program that uses a while loop to print numbers from 10 to 1 in descending order.
"""
i = 10 #made a variable for the number 
while i > 0: #if the variable i is greater than 0 then it would print 
        print(i)
        i -= 1 #decrease the i variable 
       
        
"""
3. Factorial Calculation:
Write a program that calculates the factorial of a given number using a while loop.
"""
number = int(input("give me a number")) #ask the user for a number 
result = 1 
while number > 0: #if the number is greater then 0 then it would print the factorial 
        print(number)
        print()
        result = number * result #calculations for the factorial 
        number -= 1 #decrease the number after doing the factorial
        print(result)
    
"""
4. Password Guessing Game:
Create a simple password guessing game using a while loop. Ask the user to guess a predefined password and provide appropriate feedback.
"""

password = "guess123" #made variable for the right password
user = input("put your password") #ask the question to the user

#make a loop for the password guesser 
while user != password: 
         print("TRY AGAIN")
         user = input("put your password") #keep asking until they get it right
else:
    print("ACCESS GRANTED") 
    
"""
6. Fibonacci Series:
Write a program that prints the first n numbers in the Fibonacci sequence using a while loop.
"""
