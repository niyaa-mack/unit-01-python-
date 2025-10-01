todo = [ ]
print()

print()

while True:
    print()

    print(", " .join(todo))
    ques = input("Do you want to add or remove from the list?")



    if ques == "add":
        add = input("what do you want to add?")
        print()
        if add:
            todo.append(add)
            print(",".join(todo))
            print()
        else:
            print("nothing was added")
            print(todo)

    elif ques == "remove":
        remove = int(input("Which one do you want to remove?"))
        if remove:
            del todo[remove - 1]
        
