Contact = {}

while True:
    print()
    print("Contact Book:")  
    print("1. Add Contact")
    print("2. Delete Contact")
    print("3. View the list")
    print("4. Exit")
    print()
    ans = int(input("Enter your choice:"))
    print()

    if ans == 1:
        name = input("What is the name?")
        numb = int(input("what is the number of the person? no spaces"))
        Contact[name] = numb
        print("The contact is saved!")
       
     
    if ans == 2:
        dele = input("Enter the name of the person you want to delete:")
        if dele in Contact:
            del Contact[dele]
            print(f'Contact "{name}" deleted successfully.')
        else: 
            print(f'Contact "{name}" not found')

    if ans == 3:
        if Contact:
            print("-----Contact Book--------")
            for x in Contact:
                print(x)
                print(Contact[x])

    if ans == 4:
        break
    
    

   
    
    
    



    

