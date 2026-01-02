num = int(input("Enter a number:\n"))
match num:
    case a if a<0:
        print("Enter valid number")
    case a if a<18:
        print("You are not eligible to vote")
    case _:
        print("You are eligible to vote")
        


