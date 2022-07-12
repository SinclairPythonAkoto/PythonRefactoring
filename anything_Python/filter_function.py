# Filter Function #

'''
Similar to the map() function, the filter() function applies a function to each iterable item
but only returns the true values.
an eaier way than to use a for loop to check on each item and return what we want.

By default it returns a filter object that can be converted to a list, dict, tuple etc.

filter(function, iterable)
'''

def add7(num):
    return num + 7

def is_odd(num):
    return num % 2 != 0

numbers_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

list2 = list(filter(is_odd, numbers_list))

list3 = list(map(add7, list2))    # add onto each item of the filtered list 
list4 = list(map(add7, filter(is_odd, numbers_list)))    # same as list3


print(f"Original numbers: {numbers_list}")
print(f"filter odd numbers: {list2}")
print(list3)
print(list4)


# we can complete the same using lamba with the map() & filter()
numbers_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

list5 = list(filter(lambda num: num % 2 != 0, numbers_list))    # checking which ones are odd
list6 = list(map(lambda num: num + 7, list5))                   # adding 7 to each item in filtered list
list7 = list(map(lambda num: num + 7, filter(lambda num: num % 2 !=  0, numbers_list)))    # combine map() & filter()


print(f"Original numbers: {numbers_list}")
print(f"filter odd numbers: {list5}")
print(list6)
print(list7)


# more examples 
"""
Use lambda and the filter funtion to create a new list os unused users.
"""
users = [
    {"username": "samuel", "tweets": ["I love cake", "I love chicken"]},
    {"username": "katie", "tweets": ["I love my cat"]},
    {"username": "jeff", "tweets": []},
    {"username": "bob123", "tweets": []},
    {"username": "doggo_luvr", "tweets": ["Dogs are best!"]},
    {"username": "guitar_gal", "tweets": []}
]

# check if the list is empty
# this way you have to use len, and not use False or None
inactive_users = filter(lambda user: len(user['tweets']) == 0, users)
print(list(inactive_users))

# using the 'not' keyword to do the same
inactive_users = filter(lambda user: not user['tweets'], users)
print(list(inactive_users))

# combine filter() & map()
inactive_usernames = list(map(lambda user: user['username'].upper(), filter(lambda user: not user['tweets'], users)))
print(inactive_usernames)

# sometimes you can achieve the same using a list comprehension (but not always)
username_comprehension = [user['username'] for user in users if not user['tweets']]
print(username_comprehension)


"""Exercises and Examples"""

"""
Write a function called removed_negatives that accepts a list of numbers and returns a copy of the list wiht all
negative numbers removed.  Use filter() not a lit comprehension!
"""
def removed_negatives(numbers):
    return(list(filter(lambda nums: nums >= 0, numbers)))

print(removed_negatives([-1, 3, 4, -99]))           # [3, 4]
print(removed_negatives([-7, 0, 1, 2, 3, 4, 5]))    # [0, 1, 2, 3, 4, 5]
print(removed_negatives([50, 60, 70]))              # [50, 60, 70]