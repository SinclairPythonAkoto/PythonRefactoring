# Filter Function #

'''
Similar to the map() function, the filter() function applies a function to each iterable item
but only returns the true values.
an eaier way than to use a for loop to check on each item and return what we want
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
