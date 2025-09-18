
room = input("What is the room number?")
if "B" in room or "C" in room:
    windows = input("Are the windows closed?")
    if windows == "yes":
        print("Good, if you are in a B or C room close them")
    else: 
       print("WARNING!!!, Windows must be closed")
else: 
    print("This is not a upper room")


students = int(input("What is the count of students?"))
if students <= 30:
    teacher = input("Is a teacher present?")
    if teacher == "yes": 
        print("Good, there should always be a teacher")
    else:
        print("CODE RED!!")
else:
    print("FAIL THE TEST")
    
exit = input("Is the exit door clear?")
if exit == "yes":
    print("Great!!")
else:
    print("UHH OHHH, GO FIND ANOTHER ONE FASTTT")

lights = input("Are the lights off?") 
if lights == "yes":
    print("Lights should be off for evacuation")
else:
    print("Keep them off")