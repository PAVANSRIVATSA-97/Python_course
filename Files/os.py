import os # importing os module to interact with the operating system. 
a = os.listdir("Basics")
print(os.getcwd()) # prints the current working directory
print(a)
# os.rmdir("Files/testdir") # removes the directory named 'testdir'. remove only empty directories
# os.remove("Files/sample.txt") # removes the file named 'sample.txt'
bool = os.path.exists("Files/pavan.txt") # checks if the file 'pavan.txt' exists in the 'Files' directory
print(bool)