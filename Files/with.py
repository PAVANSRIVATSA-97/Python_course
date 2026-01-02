# another way to work with files is to use 'with' keyword
with open("Files/pavan.txt", "r") as f: # opens the file and automatically closes it after the block
    content = f.read()
    print(content)
    # no need to explicitly close the file