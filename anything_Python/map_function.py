# Using Map Function #

'''
The map() function applies a function to each item in a list (or any iterable)
and then returns a new list from the results
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
