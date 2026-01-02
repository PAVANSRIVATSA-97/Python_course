# when we are dealing eith files in python, we need to follow 3 steps
# 1. open the file
# 2. read or write the file 
# 3. close the file
f = open("Files/pavan.txt", "r")  # open file in read mode
content = f.read()  # read the content of the file
print(content)  # print the content of the file
f.close()  # close the file to free up system resources