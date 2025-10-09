import os
import sys

"""
Task 1 (os module):
Write a Python program that prints the current folder (working directory) using the os module.
"""
print()
print()
current_directory = os.getcwd() #make a variable opening the current directory 
print("The current folder")

"""
Task 2 (os module):
Create a new directory called "test_folder" in the current directory.
Then print a list of all files and directories in the current directory.
"""
print()
print()
print(os.listdir()) #print the lines and directory in the folder ur in 


"""
Task 3 (os module):
Write a program that checks if a directory called "data" exists in the current 
working directory. If it doesn't exist, create it. If it does exist, print 
"Directory already exists."
"""
print()
print()
if os.path.isdir("data"): #if the file that you are in is not made 
    print("the folder already exist") #then it will print this
else:
    print("the folder does not exist") #if its not then
    os.mkdir("data") #it will make the directory

"""
Task 4 (os.path module):
Write a program that checks if a file called "config.txt" exists in the current directory.
If it exists, print its path. If it doesn't exist, print "File not found."
"""
print()
print()
config_file = "config.txt"
if os.path.isfile(config_file): #in the directory you are in has a file called config.txt 
    print(f"the file is there: {os.path.abspath(config_file)}") #then it would print this
else:
    print("file not found") #if not then print its not found
"""
Task 5 (sys module):
Write a program that prints the Python version you are currently using.
"""
print()
print()
print(sys.version) #tell the user what type of python version they are in 
print()
print()

"""
Task 6 (sys module):
Write a program that prints the platform your Python interpreter is running on
(e.g., 'linux', 'win32', 'darwin'). The output should be user friendly names
"Linux", "Windows", "MacOS"
"""
platform = sys.platform #made a variable for the platform
if platform.startswith("linux"): #if the platform is linux 
    print("Platform: Linux") #then it would that
elif platform == "win32": #if its win32 
    print("Platform: Windows") #then it would print
elif platform == "darwin": #but if platform is darwin
    print("Platform: MacOS") #print MacOS
else:
    print(f"Platform: Unknown ({platform})") 
