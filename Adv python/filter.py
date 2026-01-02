age = [21, 34, 24, 4, 5, 87, 61, 10, 46, 35, 11]
def check_age(x):
    if x>18:
        return (True)
    else:
        return False

filtered_list = list(filter(check_age, age)) # filter function is used to filter the items in an iterable (like list, tuple etc.) based on a condition and return a filter object (which is an iterator) and then you can convert it to a list using list() function
# filtered_list = list(filter(lambda x: x>18, age)) -- using lambda function
print(filtered_list)
