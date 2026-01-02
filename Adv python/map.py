even_num = [2, 4, 6, 8, 10]

def fun(x):
    return x * x * x
squared_even_num = list(map(fun, even_num)) # using map you can apply a function to all the items in an iterable (like list, tuple etc.) and return a map object (which is an iterator) and then you can convert it to a list using list() function
print(squared_even_num)