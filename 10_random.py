import random
"""
Task 1 (random module):
Write a program that simulates rolling a six-sided die 10 times.
Print each roll result.
"""
for i in range(10): #make the loop go 10 times
    dice = random.randrange(1,7) #make a variable for the dice and print it 
    print("Roll:", {dice}) 

    

"""
Task 2 (random module):
Write a program that generates 5 random floating-point numbers between 0 and 1.
Then generate 5 random floating-point numbers between 10 and 20.
Print both sets of numbers.
"""
for i in range(5): #loop for 5 times
    float = random.randint(0,1) 
    print(float) #print random number 0 - 1 fives time 
else:
    for i in range(5): #loop for 5 times
        roll_t = random.randrange(10,21)
        print(roll_t) #print random numbers 10-20 5 times 


"""
Task 3 (random module):
Create a list of colors: ["red", "blue", "green", "yellow", "purple"].
Write a program that randomly selects and prints 3 colors from this list without replacement.
"""
my_list = ["red", "blue", "green", "yellow", "purple"] #make a list 
for i in range(3): 
    print(random.choice(my_list)) #print a color from the list 3 times
"""
Task 4 (random module):
Write a program that creates a list of numbers from 1 to 10, then shuffles the list
and prints the shuffled result.
"""
list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10] #made a list 
rand = random.randint(1, 10) #variable for randomizing the number 1 - 10 and printing the result
print(rand)