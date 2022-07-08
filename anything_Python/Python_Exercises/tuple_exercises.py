# 1. Write a Python program to create a tuple.
isMale = True
my_tuple = ("Sinclair", 16, isMale)

print(my_tuple)


# 2. Write a Python program to create a tuple with different data types.
my_tuple = ("Sinclair", 1.6, True)
print(my_tuple)


# 3. Write a Python program to ceate a tuple with numbers and
# print one item.
numbers = (10, 16, 86)
print(numbers[0])

# 4. Write a Python script to unpack a tuple in several variables.
fruits = ("apple", "banana", "cherry")
(green, yellow, red) = fruits

print(green)
print(yellow)
print(red)

numbers = (16, 10, 86)
(day, month, year) = numbers

print(day)
print(month)
print(year)


# 5. Write a Python program to add an item in a tuple.
new_tup = (100, False, "London", "fruits", 4.6)
new_tup = new_tup + ("sports",)

print(new_tup)


# 6. Write a script to convert a tuple to a string
hello_tuple = ("h", "e", "l", "l", "o")
hello = "".join(letter for letter in hello_tuple)
print(hello)

name = "Sinclair"
sinclair_tuple = tuple(name)
new_string = "".join(char for char in sinclair_tuple)

print(f"My name is {new_string}")


# 7. Write Python program to get the 4th element and 4th element from
# last of a tuple.
numbers = (1, 2, 2, 4, 5, 6, 6, 7, 8, 9)
fourth_element = numbers[3]
last_fourth_element = numbers[-4]

print(fourth_element)
print(last_fourth_element)


# 8. Write a Python script to create a colon of a tuple.
tuplex = ("Sinclair", 16, [], True)
new_list = list(tuplex)
new_list[2].append(50)
tuplex = tuple(new_list)

print(tuplex)


# 9. Write a script to find the repeated items of a tuple.
my_tup = (1, 3, 5, 5, 6, 7, 8, 9, 9, 2, 4)
for result in my_tup:
    if my_tup.count(result) > 1:
        print(result)

my_tup = list(my_tup)
new_tup = tuple([num for num in my_tup if my_tup.count(num) > 1])

print(f"Duplicate numbers: {new_tup}")


# 10. Write a Python program to check whether an element exists within a tuple.
fruits = ("apple", "mango", "grapes", "cherry", "oranges")


def check_fruits(fruit):
    if fruit in fruits:
        return True
    return False


print(check_fruits("apple"))
print(check_fruits("berries"))
print(check_fruits("plum"))
print(check_fruits("grapes"))


# 11. Write a script to convert a list to a tuple.

# 12. Write a Python script ro remove an item from a tuple.
# 13. Write a script to remove an item from a tuple.
# 14. Write a Python program that will find the index of an item of item.
# 15. Write a program to find the length of a tuple.
# 16. Write a program to convert a tuple to a dictionary.
# 17. Write a Python program to unzip a list of tuples into individual lists.
# 18. Write a Python program to reverse a tuple.
# 19. Write a Python program to convert a list of tuples into a dictionary.
# 20. Write a Python program to print a tuple with string formatting.
# 21. Write a Python program to replace last value of tuples in a list.
# 22. Write a Python program to remove an empty tuple(s) from a list of tuples.
# 23. Write a Python program to sort a tuple by its float element.
# 24. Write a Python program to count the elements in a list until an element
# is a tuple.
# 25. Write a Python program convert a given string list to a tuple.
# 26. Write a Python program calculate the product, multiplying all
# the numbers of a given tuple.
# 27. Write a Python program to calculate the average value of the numbers
# in a given tuple of tuples.
# 28. Write a Python program to convert a tuple of string values to
# a tuple of integer values.
# 29. Write a Python program to convert a given tuple of positive
# integers into an integer.
# 30. Write a Python program to check if a specified element presents in
# a tuple of tuples.
# 31. Write a Python program to compute element-wise sum of given tuples.
# 32. Write a Python program to compute the sum of all the elements of each
# tuple stored inside a list of tuples.
# 33. Write a Python program to convert a given list of tuples to a list of lists.
