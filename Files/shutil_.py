#shutil is a module that provides a higher level interface for file operations compared to os module.
#SHOULS BE VERY CAREFUL WHILE USING SHUTIL MODULE AS IT CAN DELETE NON-EMPTY DIRECTORIES AND THEIR CONTENTS.
import shutil
import os
# shutil.rmtree("Files/testdir") # removes the directory named 'testdir' and all its contents recursively
# shutil.copy("Files/pavan.txt", "Files/pavan_copy.txt") # copies the file 'pavan.txt' to 'pavan_copy.txt'
# os.remove("Files/pavan_copy.txt") # removes the copied file to clean up
# shutil.move("Files/pavan.txt", "Basics/") # moves/renames the file 'pavan.txt' to the 'Basics' directory
shutil.move("Basics/pavan.txt", "Files/pavan_new.txt") # moves/renames the file back to 'Files' directory with a new name