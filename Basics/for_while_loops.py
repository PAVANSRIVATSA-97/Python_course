for i in range(1, 11):
    print("2 X", i, "=", 2*i)

# num = int(input("Enter a number\n"))
num  = {"1","52","X"}
sum = 0
for i in num:
    if not i.isdigit():
        continue
    sum = sum +int(i)
print(sum)
    

    # continue skips the current iteration
    

   