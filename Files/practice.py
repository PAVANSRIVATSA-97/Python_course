with open("Files\pavan_new.txt", "r") as f:
    content = f.read()

with open("Files\pavan_updated.txt", "w") as f:
    string = content.upper()
    f.write(string)
print("Hello")
