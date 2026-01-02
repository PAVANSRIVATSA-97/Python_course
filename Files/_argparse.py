import argparse
parser = argparse.ArgumentParser(description="Hello world")
parser.add_argument("num1", type=float, help="First number")
parser.add_argument("num2", type=float, help="second number")
parser.add_argument("name", default = "pavan", choices=["Add", "sub", "mul", "div"])


args = parser.parse_args()
if(args.name == "Add"):
    print(f"The sum is {args.num1+args.num2}")
elif(args.name == "sub"):
    print(f"The difference is {args.num1-args.num2}")
elif(args.name == "mul"):
    print(f"The mul is {args.num1*args.num2}")
elif(args.name == "div"):
        if(args.num2 != 0):
            print(f"The div is {args.num1/args.num2}")
        else:
             print("You canont divide by zero")
else:
    print("Some error occured")

    

    