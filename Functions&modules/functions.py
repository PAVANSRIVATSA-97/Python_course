# function defination
def function(a,b,c):    #a,b,c are called parameters
    sum = a+b+c

    return sum    # returns only the sum so that we can assign the value to any variable when calling the function
function(1,2,3)    # function call.....this function does not print as the function does not contain print statement
    # The values that are passed during the function call are called the arguments    

n = function(b=2,a=1,c=13)  # keyword argument
m = function(2,3,4)  # positional argument is that order of the arguments will be same as the paramentes
# print(m) 
# print(n)


#Lambda Function - In line function
cube = lambda x: x*x*x
'''This is a cube function which returns the cube of a number'''  
# print(cube(3))

#Recursion - function inside a function
# def fibo(n):
#     if (n==0 or n==1): base case
#         return n
#     return fibo(n-2) + fibo(n-1)
# print(fibo(6))    
# 0 1 1 2 3 5 8

