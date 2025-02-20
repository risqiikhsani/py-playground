file = open("filehandle/example.txt", "r")
# Read the entire file
content = file.read()
print(content)

# Read one line at a time
line = file.readline()
print(line)

# Read all lines into a list
lines = file.readlines()
print(lines)

file.close()


# To write to an existing file, you must add a parameter to the open() function:
# "a" - Append - will append to the end of the file
# "w" - Write - will overwrite any existing content

f = open("filehandle/demofile2.txt", "a")
f.write("Now the file has more content!")
f.close()

#open and read the file after the appending:
f = open("filehandle/demofile2.txt", "r")
print(f.read()) 

f = open("filehandle/demofile3.txt", "w")
f.write("Woops! I have deleted the content!")
f.close()

#open and read the file after the overwriting:
f = open("filehandle/demofile3.txt", "r")
print(f.read()) 


# To create a new file in Python, use the open() method, with one of the following parameters:
# "x" - Create - will create a file, returns an error if the file exist
# "a" - Append - will create a file if the specified file does not exist
# "w" - Write - will create a file if the specified file does not exist


f = open("filehandle/demofile.txt", "x")


# To delete a file, you must import the OS module, and run its os.remove() function:

import os
if os.path.exists("filehandle/demofile.txt"):
  os.remove("filehandle/demofile.txt")
else:
  print("The file does not exist")