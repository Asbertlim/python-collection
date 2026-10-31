# os -> lets the programme interact with the operating system

import os

print(os.getcwd()) # returns the current working directory

items = os.listdir() # returns a list of names of the contents of current working directory
print(items)

# os.mkdir("test.txt") # creates a directory called "test.txt" in the current wrking directory
os.makedirs("data/students/reports", exist_ok=True)
# exist_ok=True tells Python not to raise an error merely bcs the final directory already exists
# os.makedirs creates nested directories

print(os.path.exists("notes.txt")) # returns True if the file exists in the directory

print(os.path.isfile("notes.txt")) #returns True if "notes.txt" is a file
print(os.path.isdir("data")) #returns True if "data" is directory

folder = "data"
filename = "students.json"
path = os.path.join(folder, filename)
print(path)

path = "data/students.json"
absolute_path = os.path.abspath(path) # convert a path to an absolute path
print(absolute_path)

# os.rename("reports", "new_reports.txt")
# os.remove("notes.txt")
# os.rmdir("empty_folder") #delete an empty directory


for root, dirs, files in os.walk("data"):
  print("Current folder:", root)
  print("Subfolders:", dirs)
  print("Files:", files)
  print()
# os.walk() -> explores an entire directory tree
# root -> the directory currently being examined
# dirs -> the names of its immediate subdirectories
# files -> names of its immediate files

# os.chdir('data') # changes the process' current working directory to data
print(os.getcwd()) 

# size = os.path.getsize()
# print(size)
