print("Welcome to my smarty calculator")
print()
num1 = float(input("Give me a number"))
num2 = float(input("Give me another number"))
print("""
Pick an operation (1-7):
1. Add
2. Subtract
3. Multiply
4. Divide
5. Exponent
6. Floor Division
7. Remainder
""")
answer = input("what is the number you want?")
print()
print()

if answer == "1":
    add1 = num1 + num2
    print(add1)

elif answer == "2":
    sub2 = num1 - num2
    print(sub2)

elif answer == "3":
    mul3 = num1 * num2
    print(mul3)


elif answer == "4":
        if num2 == 0:
            print("YOU CANT DO THAT")
        else:
            print("Result:", num1/num2)


elif answer == "5":
    exp5 = num1 ** num2 
    print (exp5)

elif answer == "6":
    if num2 == 0:
         print("YOU CANT DO THAT")
    else:
        fd6 = num1 // num2
        print(fd6)

elif answer == "7":
    if num2 == 0:
         print("YOU CANT DO THAT")
    else:
        rem7 = num1 % num2 
        print(rem7)

else:
     print("that is not a choice.")


