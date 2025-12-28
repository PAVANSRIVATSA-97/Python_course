while True:
    try:
        a = int(input("Enter a number: "))
        b = int(input("Enter another number: "))    
        result = a / b
        print(f"The result of {a} divided by {b} is {result}")

    except ZeroDivisionError:
        print("Error: Division by zero is not allowed.")    
    except ValueError:
        print("Error: Invalid input. Please enter numeric values only.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
    else:                                              # This block executes if no exceptions were raised in the try block
        print("Division performed successfully.")
    finally:
        print("Execution of the try-except block is complete.") # This block always executes irrespective of an exception occurring or not