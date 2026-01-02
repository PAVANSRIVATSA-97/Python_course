# def sum(a, b):
#     return a + b

# print(sum(2, 3, 4))  # TypeError: sum() takes 2 positional arguments but 3 were given and to solve this we use args
def sum_args(*args): # using *args to accept variable number of positional arguments
    print(args)  # args is a tuple of all the positional arguments passed to the function
    total = 0
    for num in args:
        total += num
    return total
print(sum_args(2, 3, 4, 5, 6))  # now this works fine and prints 20

def sum_kwargs(**kwargs): # using **kwargs to accept variable number of keyword arguments
    print(kwargs)  # kwargs is a dictionary of all the keyword arguments passed to the function
    total = 0
    print(kwargs.keys()) # prints all the keys in the kwargs dictionary
    for key, value in kwargs.items():
        total += value
    return total    
print(sum_kwargs(a=2, b=3, c=4))  # now this works fine and prints 9