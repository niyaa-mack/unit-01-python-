Contact = {}

while True:
    print()
    print("Contact Book:")  
    print("1. Add Contact")
    print("2. Delete Contact")
    print("3. View the list")
    print("4. Exit")
    print()
    ans = int(input("Enter your choice:")) #pick the choice
    print()

    if ans == 1: #adding contacts
        name = input("What is the name?") 
        numb = int(input("what is the number of the person? no spaces")) #asking for their name and number 
        Contact[name] = numb #adds it to the dictionary
        print("The contact is saved!")
       
     
    if ans == 2:
        dele = input("Enter the name of the person you want to delete:") #asks what person do they want to delete 
        if dele in Contact:
            del Contact[dele] #delete them from the dictionary 
            print(f'Contact "{name}" deleted successfully.')
        else: 
            print(f'Contact "{name}" not found') #if they are not in the dictionary then it will say this 

    if ans == 3:
        if Contact:
            print("-----Contact Book--------")
            for x in Contact: # lists out the contact lists
                print(x)
                print(Contact[x])

    if ans == 4:
        break #exit the book
    
    

   
    
    
    



    

