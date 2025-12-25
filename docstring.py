import math
def sqrt(x):
    '''This is a Docstring'''  # only works when it is in the first line after function definition
    result = math.sqrt(x)
    '''This is a Docstring'''  #works as comment
    print(result)
sqrt(45)
print(sqrt.__doc__)
import functions
# print(math.sqrt(25))
print(functions.cube(4))
# why Docstring -- when you want to print the information of the function like how many parameters it is taking or the return value
# when you hover on any keyword, the information that it tells you is the docstring
