# A decorator is a special type of function in Python that is used to modify the behavior of another function or method.
# Decorator takes a function as input and returns a new function that usually extends the behavior of the original function without modifying its code.
# def sample_decorator(f):
#     def wrapper(a,b):
#         print("This is a simple print stament in the decorator before calling the actual function.")
#         f(a,b)
#         print("This is a simple print statement in the decorator after calling the actual function.")
        
#     return wrapper

# @sample_decorator
# def add(a, b):
#     c = a + b
#     print(c) 
# add(2,3)


def repeat(n):
    def decorator(func):
        def wrapper(*args, **kwargs):
            for j in range(args[1],n+1):
                func(args[0],j)
        return wrapper
    return decorator

b = int(input("Enter the range: "))
c = int(input("Enter the number from which multiplication starts: "))
@repeat(b)
def multiply(num, current_i):
    print(f"{num} X {current_i} = {num * current_i}") 
a = int(input("Enter a number to multiply: "))
multiply(a,c)   

