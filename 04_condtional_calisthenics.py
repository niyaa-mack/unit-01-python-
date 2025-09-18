'''
Exercise 1:
Check if an integer is even and greater than 10.
Return True if both conditions are met, False otherwise.
'''
num = (input("Give me a number"))
if num >    10: 
    print("True")
#if they are greater than 10 then it would be true 
else: 
    print("False")
#if not then it would be wrong
'''
Exercise 2:
Determine the ticket price based on age and student status.
Price is $10 if under 18 or a student, $20 otherwise.
'''
age = input("How old are you?")
ss =  input("Are you a student?")
#ask the questions
if age < 18 or ss == "yes":
    print("The price is $10")
#if they are under 18 or a student the price would be $10
else: 
    print("The price is $20")
#if not then it would be $20
'''
Exercise 3:
Prompt the user to enter a fruit name. Check if the fruit is in the list. 
If it is, print "Yes, that fruit is in the list." 
If it's not, print "No, that fruit is not in the list."
'''
ques = input("Put a fruit")
fruits = ['mango', 'grape', 'pineapple']
#make a list
if ques not in fruits:
    print("No, that fruit is not in the list.")
#if the fruit that the user typed in is not in my list then it would print that
else:
    print("Yes, that fruit is in the list.")
#if it is then it would say yes


'''
Exercise 4:
Check if a year is a century year and a leap year.
'''

'''
Exercise 5:
Calculate the cost of shipping for an online order based on the order weight and destination zone. 
The shipping cost is $5 per kilogram for Zone A and $7 per kilogram for Zone B. 
If the order weight is less than 0 kg, return an error message.
'''
weight = float(input("What is the weight of the package?"))#ask what is the weight of the package
zon = input("What is the destination zone? Zone a or Zone b?")#ask what zone they are in 
us = weight * 7
we = weight * 5
#make the variables for both of the zones 
if weight > 0:
    if zon == "a":
        print("the price is" , we) 
    #if they pick A then the price would whatever the weight is times 5
    if zon == "b":
         print("the price is", us) 
     #if they pick B then the price would whatever the weight is times 7
else:
    print("ERROR MESSAGE")
    #


    

    


'''
Exercise 6:
Determine the type of a triangle based on side lengths.
Equilateral, Isosceles, Scalene, or Not a triangle.
'''
