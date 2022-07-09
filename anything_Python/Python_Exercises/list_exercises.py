"""List Exercises

Source: https://www.w3resource.com/python-exercises/list/
"""

# 1. Write a Python program to sum all the items in a list.
numbers = [1, 2, 4, 3, 5, 8, 7]
total = 0
for num in numbers:
    total += num

print(f"Total: {total}")


# 2. Write a Python program to multiply all the items in a list.
numbers = [1, 2, 4, 3, 5, 8, 7]
multiplied_numbers = [num * 10 for num in numbers]

print(multiplied_numbers)


# 3. Write a Python program to get the largest number from a list.
numbers = [1, 2, 4, 3, 5, 8, 6, 7]
print(f"Max Number: {max(numbers)}")


# 4. Write a Python program to get the smallest number from a list.
numbers = [1, 2, 4, 3, 5, 8, 6, 7]
print(f"Min Number: {min(numbers)}")


# 5. Write a Python program to count the number of strings where the string length is 2 or
# more and the first and last character are same from a given list of strings.
names = ["Amanda", "Paul", "James", "Phlip", "John", "Bob"]

new_list = [
    (name, (name[0], name[-1]))
    for name in names
    if len(name) > 2
    if name.lower()[0] == name.lower()[-1]
]

print(new_list)


# 6. Write a Python program to get a list, sorted in increasing order by the last element in
# each tuple from a given list of non-empty tuples.
people = [("Sinclair", 35), ("John", 30), ("Mary", 80), ("sean", 14), ("Julie", 25)]
print(f"Original list: {people}")
new_list1 = []

for person in people:
    # take last item of each tuple
    new_list1.append((person[1], person[0]))
    # sort them from lowest to highest
    new_list1.sort()

# print back values in ascending order
print(f"Reordered list from lowest to highest: {new_list1}")


# 7. Write a Python program to remove duplicates from a list.
list1 = [1, 2, 2, 2, 3, 3, 4, 5, 5, 6, 6, 7]
remove_dupilcates = set(list1)
remove_dupilcates = list(remove_dupilcates)

print(remove_dupilcates)


# 8. Write a Python program to check a list is empty or not.
def is_empty(content):
    if len(content) == 0:
        return True
    return False


var = ""
nums = [1, 2, 3, 4, 5]
empty_list = []

print(is_empty([]))
print(is_empty(empty_list))
print(is_empty(var))
print(is_empty([1, 2, 3]))


# 9. Write a Python program to clone or copy a list.
list2 = [
    2,
    1020,
    47,
    873,
    37,
    9,
]
list3 = list2.copy()

print(f"Copied list: {list3}")


# 10. Write a Python program to find the list of words that are longer than n from a given
# list of words.

# 11. Write a Python function that takes two lists and returns True if they have at least one
# common member.
# 12. Write a Python program to print a specified list after removing the 0th, 4th and 5th elements.
# 13. Write a Python program to generate a 3*4*6 3D array whose each element is *.
# 14. Write a Python program to print the numbers of a specified list after removing even numbers from it.
# 15. Write a Python program to shuffle and print a specified list.
# 16. Write a Python program to generate and print a list of first and last 5 elements where the
# values are square of numbers between 1 and 30 (both included).
# 17. Write a Python program to generate and print a list except for the first 5 elements, where
# the values are square of numbers between 1 and 30 (both included).
# 18. Write a Python program to generate all permutations of a list in Python.
# 19. Write a Python program to get the difference between the two lists.
# 20. Write a Python program access the index of a list.
# 21. Write a Python program to convert a list of characters into a string.
# 22. Write a Python program to find the index of an item in a specified list.
# 23. Write a Python program to flatten a shallow list.
# 24. Write a Python program to append a list to the second list.
# 25. Write a Python program to select an item randomly from a list.
# 26. Write a python program to check whether two lists are circularly identical.
# 27. Write a Python program to find the second smallest number in a list.
# 28. Write a Python program to find the second largest number in a list.
# 29. Write a Python program to get unique values from a list.
# 30. Write a Python program to get the frequency of the elements in a list.
# 31. Write a Python program to count the number of elements in a list within a specified range.
# 32. Write a Python program to check whether a list contains a sublist.
# 33. Write a Python program to generate all sublists of a list.
# 34. Write a Python program using Sieve of Er
# 35. Write a Python program to create a list by concatenating a given list which range goes from 1 to n.
# 36. Write a Python program to get variable unique identification number or string.
# 37. Write a Python program to find common items from two lists.
# 38. Write a Python program to change the position of every n-th value with the (n+1)th in a list.
# 39. Write a Python program to convert a list of multiple integers into a single integer.
# 40. Write a Python program to split a list based on first character of word.
# 41. Write a Python program to create multiple lists.
# 42. Write a Python program to find missing and additional values in two lists.
# 43. Write a Python program to split a list into different variables.
# 44. Write a Python program to generate groups of five consecutive numbers in a list.
# 45. Write a Python program to convert a pair of values into a sorted unique array.
# 46. Write a Python program to select the odd items of a list.
# 47. Write a Python program to insert an element before each element of a list.
# 48. Write a Python program to print a nested lists (each list on a new line) using the print() function.
# 49. Write a Python program to convert list to list of dictionaries.
# 50. Write a Python program to sort a list of nested dictionaries.
# 51. Write a Python program to split a list every Nth element.
# 52. Write a Python program to compute the difference between two lists.
# 53. Write a Python program to create a list with infinite elements.
# 54. Write a Python program to concatenate elements of a list.
# 55. Write a Python program to remove key values pairs from a list of dictionaries.
# 56. Write a Python program to convert a string to a list.
# 57. Write a Python program to check if all items of a given list of strings is equal to a given string.
# 58. Write a Python program to replace the last element in a list with another list.
# 59. Write a Python program to check whether the n-th element exists in a given list.
# 60. Write a Python program to find a tuple, the smallest second index value from a list of tuples.
# 61. Write a Python program to create a list of empty dictionaries.
# 62. Write a Python program to print a list of space-separated elements.
# 63. Write a Python program to insert a given string at the beginning of all items in a list.
# 64. Write a Python program to iterate over two lists simultaneously.
# 65. Write a Python program to move all zero digits to end of a given list of numbers.
# 66. Write a Python program to find the list in a list of lists whose sum of elements is the highest.
# 67. Write a Python program to find all the values in a list are greater than a specified number.
# 68. Write a Python program to extend a list without append.
# 69. Write a Python program to remove duplicates from a list of lists.
# 70. Write a Python program to find the items starts with specific character from a given list.
# 71. Write a Python program to check whether all dictionaries in a list are empty or not.
# 72. Write a Python program to flatten a given nested list structure.
# 73. Write a Python program to remove consecutive duplicates of a given list.
# 74. Write a Python program to pack consecutive duplicates of a given list elements into sublists.
# 75. Write a Python program to create a list reflecting the run-length encoding from a given list
# of integers or a given list of characters.
# 76. Write a Python program to create a list reflecting the modified run-length encoding from a
# given list of integers or a given list of characters.
# 77. Write a Python program to decode a run-length encoded given list.
# 78. Write a Python program to split a given list into two parts where the length of the first
# part of the list is given.
# 79. Write a Python program to remove the K'th element from a given list, print the new list.
# 80. Write a Python program to insert an element at a specified position into a given list.
# 81. Write a Python program to extract a given number of randomly selected elements from a given list.
# 82. Write a Python program to generate the combinations of n distinct objects taken from the elements
# of a given list.
# 83. Write a Python program to round every number of a given list of numbers and print the total sum
# multiplied by the length of the list.
# 84. Write a Python program to round the numbers of a given list, print the minimum and maximum numbers
# and multiply the numbers by 5. Print the unique numbers in ascending order separated by space.
# 85. Write a Python program to create a multidimensional list (lists of lists) with zeros.
# 86. Write a Python program to create a 3X3 grid with numbers.
# 87. Write a Python program to read a matrix from console and print the sum for each column. Accept
# matrix rows, columns and elements for each column separated with a space(for every row) as input
# from the user.
# 88. Write a Python program to read a square matrix from console and print the sum of matrix primary
# diagonal. Accept the size of the square matrix and elements for each column separated with a space
# (for every row) as input from the user.
# 89. Write a Python program to Zip two given lists of lists.
# 90. Write a Python program to count number of lists in a given list of lists.
# 91. Write a Python program to find the list with maximum and minimum length.
# 92. Write a Python program to check if a nested list is a subset of another nested list.
# 93. Write a Python program to count the number of sublists contain a particular element.
# 94. Write a Python program to count number of unique sublists within a given list.
# 95. Write a Python program to sort each sublist of strings in a given list of lists.
# 96. Write a Python program to sort a given list of lists by length and value.
# 97. Write a Python program to remove sublists from a given list of lists, which contains an element
# outside a given range.
# 98. Write a Python program to scramble the letters of string in a given list.
# 99. Write a Python program to find the maximum and minimum values in a given heterogeneous list.
# 100. Write a Python program to extract common index elements from more than one given list.
