"""Unpacking Lists, Tuples & Dictionaries

Unpacking is when we turn every item in a list, tuple or 
dictionary into an arguement.

*list_name or *tuple_name is how we unpack lists or tuples
**dict_name is how we unpack all the keyword arguements.
"""

# unpacking lists / tuples
# create a function that will add values that are passed in.
from tkinter.font import names


def sum_all_values(*args):
    total = 0
    for num in args:
        total += num
    return total


# passing in individual arguments
print(sum_all_values(1, 30, 2, 5, 6))

# If we had a list and wanted to pass each item as a variable
# then we would need to unpack it using '*'.

# Imaginary shopping cart.  We want to add ead item
cart = [1.99, 2.69, 9.99, 8.50, 12.10]

# sum_all_values(cart) # this will cause a TypeError

# using the unpacking method
print(sum_all_values(*cart))

# more exaples
person = ["Sinclair", 35, "London", False, 1.6]
city = [city for city in person if city == "London"]
print(*city)

# same as manually unpacking
person = ["Sinclair", 35, "London", False, 1.6]
(name, age, city, isFemale, hours) = person
print(city)


# unpacking dictionaries
# create a function displaying the names of the users
def display_names(first, second):
    return f"{first} says hello to {second}"


names = {"first": "John", "second": "Julie"}
print(display_names(**names))


# more examples
def add_and_multiply_numbers(a, b, c):
    return a + b * c


data = dict(a=1, b=2, c=3)

print(add_and_multiply_numbers(**data))
