import random
"""
Task 1 (random module):
Write a program that simulates rolling a six-sided die 10 times.
Print each roll result.
"""
for i in range(10):
    dice = random.randrange(1,7)
    print("Roll:", {dice})

    

"""
Task 2 (random module):
Write a program that generates 5 random floating-point numbers between 0 and 1.
Then generate 5 random floating-point numbers between 10 and 20.
Print both sets of numbers.
"""
for i in range(5):
    float = random.randint(0,1)
    print(float)
else:
    for i in range(5):
        roll_t = random.randrange(10,21)
        print(roll_t)


"""
Task 3 (random module):
Create a list of colors: ["red", "blue", "green", "yellow", "purple"].
Write a program that randomly selects and prints 3 colors from this list without replacement.
"""
my_list = ["red", "blue", "green", "yellow", "purple"]
by = random.sample(my_list, 3)
for color in by:
    print(f"COLOR: {by}")

"""
Task 4 (random module):
Write a program that creates a list of numbers from 1 to 10, then shuffles the list
and prints the shuffled result.
"""
list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
rand = random.randint(1, 10)
print(rand)