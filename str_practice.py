# 1.1
name = "Pavansrivatsa Meka"
print(name[0])
print(name[-1])
print(len(name))

# 1.2 concatination
str1 = "Hello"
str2 = "world"
print(str1 + str2) #this does not give space in between
print(str1 +" "+str2)
print(str1,str2) #this gives space

# 1.3
text = "Python Programming"
print(text[0:6])
print(text[-6:])
print(text[::2])

print(text[::-1])

#1.4 
string = " i love python programming "
print(string.strip()) # removes extra spaces
print(string.title())
print(string.count("o")) # counts the appearence of letter
string1 = "ABC123"
print(string1.isalnum())
print(string1.isdigit())

#1.5
name = "John"
age = 24
print(f"My name is {name} and iam {age} years old")
sentence = "My name is {} and iam {} years old"
print(sentence.format(name,age))

#1.6
line = "Coding in python is fun"
new_line = line.replace("fun", "awesome")   #replaces fun with 
print(new_line)
index = line.find("python")   #finds the index of word/letter
print(index)
print(line.upper())

letter = "My name is Pavan"
letter2 = input("Enter a sentence\n")
sum = 0
vowels = ['a','e','i','o','u']
for char in letter2:
    if char in vowels:
        sum+=1

print(f"There are {sum} vowels in the sentence")

#1.7
palindrome = "madam"
if(palindrome == palindrome[::-1]):
    print("Palindrome")
    
