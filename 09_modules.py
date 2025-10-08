import os
import sys

"""
Task 1 (os module):
Write a Python program that prints the current folder (working directory) using the os module.
"""
print()
print()
current_directory = os.getcwd()
print("The current folder")

"""
Task 2 (os module):
Create a new directory called "test_folder" in the current directory.
Then print a list of all files and directories in the current directory.
"""
print()
print()
print(os.listdir())


"""
Task 3 (os module):
Write a program that checks if a directory called "data" exists in the current 
working directory. If it doesn't exist, create it. If it does exist, print 
"Directory already exists."
"""
print()
print()
if os.path.isdir("data"):
    print("the folder already exist")
else:
    print("the folder does not exist")
    os.mkdir("data")

"""
Task 4 (os.path module):
Write a program that checks if a file called "config.txt" exists in the current directory.
If it exists, print its path. If it doesn't exist, print "File not found."
"""
print()
print()
config_file = "config.txt"
if os.path.isfile(config_file):
    print(f"the file is there: {os.path.abspath(config_file)}")
else:
    print("file not found")
"""
Task 5 (sys module):
Write a program that prints the Python version you are currently using.
"""
print()
print()
print(sys.version)
print()
print()

"""
Task 6 (sys module):
Write a program that prints the platform your Python interpreter is running on
(e.g., 'linux', 'win32', 'darwin'). The output should be user friendly names
"Linux", "Windows", "MacOS"
"""
platform = sys.platform
if platform.startswith("linux"):
    print("Platform: Linux")
elif platform == "win32":
    print("Platform: Windows")
elif platform == "darwin":
    print("Platform: MacOS")
else:
    print(f"Platform: Unknown ({platform})")
