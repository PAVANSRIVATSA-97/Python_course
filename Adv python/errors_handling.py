# try and except block to handle invalid input
# try and except block is used to catch and handle exceptions (errors) that may occur during the execution of a program.
# It allows the programmer to gracefully handle errors without crashing the program.

while True: 
    try:
        x = int(input("Please enter num: "))
        y = int(input("Please enter num: "))
        print(f"sum is {x / y}")
    
    except ZeroDivisionError:
        print("Division by zero is not allowed. Please enter a valid number.")
    except ValueError:
        print("Invalid input. Please enter numeric values only.")   
    except Exception as e:
        print("Oops!That was no valid number.Try again...",e) # e prints the actual error message   
 
        