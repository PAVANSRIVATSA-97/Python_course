from functools import reduce # first we need to import reduce from internal module functools called functools
try:
    list = [1,5,7,3,8,5,3,7]
    #      [5,7,3,8,5,3,7] -> [35,3,8,5,3,7] -> [105,8,5,3,7] -> [840,5,3,7] -> [4200,3,7] -> [12600,7] -> [88200]

    def mul(a, b):
        return a * b

    reduced_list = list(reduce(mul, list)) # reduce function is used to apply a binary function (a function that takes two arguments) cumulatively to the items of an iterable (like list, tuple etc.) from left to right, so as to reduce the iterable to a single value.
    # reduced_list = reduce(lambda a, b: a * b, list) -- using lambda function
    print(reduced_list)
except Exception as e:
    print(f"An error occurred: {e}")