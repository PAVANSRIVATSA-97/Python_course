list = ["pavan", 42, 3.14, False]  # A list containing different data types
another_list = [1,2,3,4,5]
print(list)
list.append("new_item")  # Adding an item to the list
print(list)
list.pop(3)  # Removing the item at index 1 or any index mentioned
print(list)
list.remove(3.14)  # Removing the item with value 3.14 or any value mentioned
list.remove("pavan")
print(list)
list.extend(another_list)  # Extending the list by adding elements from another list
print(list)
list.insert(1, 6)  # Inserting an item at a specific index
print(list)
num = [5, 2, 9, 1, 5, 6]
num.sort() # Sorting the list (only works if all items are of the same data type)
print(num)
list.reverse()  # Reversing the list
print(list)
list.copy()  # Creating a shallow copy of the list
print(list)
print(num.count(5))  # Counting occurrences of an item in the list
  # Clearing all items from the list
list.clear()
print(list)


table = [7*i for i in range(1,11)]  # List comprehension to create a multiplication table of 7
print(table)

a = int(input("Enter the number to get its multiplication table: "))
multiplication_table = [a*i for i in range(1,11)]
print(multiplication_table)