todo = [ ]
to1 = input("What do you want on your to do list?")
print()
todo.append(to1)
print("," .join(todo))
print()

while True:
   
    ques = input("Do you want to add or remove from the list?")
    print()


    if ques == "add":
        add = input("what do you want to add?")
        print()
        if add:
            todo.append(add)
            print(",".join(todo))
            print()
        else:
            print(todo)

    if ques == "remove":
        rem = input("Which one do you want to remove?")
        del todo [rem - 1]
