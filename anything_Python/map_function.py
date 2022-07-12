# Using Map Function #

'''
The map() function applies a function to each item in a list (or any iterable)
and then returns a map object which can be converted into a another data
structure - list, tuple, dictionary etc..

map(function, iterable)
'''

li = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# we want to create a function that will multiply by itself
def func(num):
    return num ** num

new_list = []
for item in li:
    new_list.append(func(item))

print(new_list)


'''
The map() function does basically the same thing, wihtout the need for a for loop etc.
It takes two parameters, the function then the iterable that the function will be applied on.
'''

print(list(map(func, li)))    # the answer will be the same

# you can use list comprehensions to achieve the same but with expressions

print([func(item) for item in li if item % 2 == 0 ])    # if its an even number - % by 2, remainder is 0


"""Exercises and Examples"""

"""
Double every number in nums list using the map function.
"""
nums = [2, 4, 6, 8, 10]
doubles = (map(lambda num: num*2, nums))

print(doubles)          # map object 
print(list(doubles))    # converted into list


"""
Create a new list of uppercased names using the map function.
"""
people = ["Darcy", "Christina", "Dana", "Annabelle"]
names = map(lambda name: name.upper(), people)

print(list(names))


# more examples
names = [
    {'first': 'Derek', 'last': 'Astante'},
    {'first': 'Sandra', 'last': 'Astante'},
    {'first': 'Cynthia', 'last': 'Astante'}
]

first_names = list(map(lambda name: name['first'], names))

print(first_names)


"""
Write a function called decrement_list that accepts a single list of numbers a parameter.
It should return a copy of the list where each item has been decremented by one.  Use map to do this!
"""
def decrement_list(numbers):
    return list(map(lambda num: num-1, numbers))

print(decrement_list([1, 2, 3]))       # [0, 1, 2]
print(decrement_list([20, 14, 11]))    # [19, 13, 10]