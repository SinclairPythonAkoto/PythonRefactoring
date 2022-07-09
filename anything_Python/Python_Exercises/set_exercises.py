"""Set Exercises

Source: https://www.w3resource.com/python-exercises/sets/
"""

# 1. Write a Python program to create a set.
new_set = {1, 3, 4, 5}
set_x = {1, 3, 4, 5}

print(new_set, set_x)


# 2. Write a Python program to iteration over sets.
numbers = {1, 3, 4, 5}
for num in numbers:
    print(num)


# 3. Write a Python program to add member(s) in a set.
numbers = {1, 3, 4, 5}
numbers.add(10)

print(numbers)

# 4. Write a Python program to remove item(s) from a given set.
my_set = {16, 10, 1986, "Sinclair", "London", "Developer"}
print(my_set)

my_set.discard("Sinclair")
print(my_set)


# 5. Write a Python program to remove an item from a set if it is present in the set.
my_set = {16, 10, 1986, "Sinclair", "London", "Developer"}
if "London" in my_set:
    my_set.discard("London")

print(my_set)


# 6. Write a Python program to create an intersection of sets.
set1 = {1, 3, 4, 5, 6, 6, 5, 2, 7}
set2 = {2, 3, 5, 7, 8, 9}

intersection = set1 & set2

print(intersection)


# 7. Write a Python program to create a union of sets.
set1 = {1, 3, 4, 5, 6, 6, 5, 2, 7}
set2 = {2, 3, 5, 7, 8, 9}

union_set = set1 | set2

print(union_set)


# 8. Write a Python program to create set difference.
set1 = {1, 3, 4, 5, 6, 6, 5, 2, 7}
set2 = {2, 3, 5, 7, 8, 9}

set_difference = set1.difference(set2)

print(set_difference)


# 9. Write a Python program to create a symmetric difference.
set1 = {1, 3, 4, 5, 6, 6, 5, 2, 7}
set2 = {2, 3, 5, 7, 8, 9}

symmetric_difference = set1.symmetric_difference(set2)

print(symmetric_difference)


# 10. Write a Python program to check if a set is a subset of another set.
set1 = {1, 3, 4, 5, 6, 6, 5, 2, 7}
set2 = {2, 3, 5, 7, 8, 9}

subset = set1.issubset(set2)
print(f"Is subset? {subset}")

set3 = {1, 2, 3, 4, 5}
set4 = set3.copy()
set5 = {1, 2, 3, 4, 5}

print(f"Is subset? {set3.issubset(set4)}")
print(f"Is subset? {set3.issubset(set5)}")


# 11. Write a Python program to create a shallow copy of sets.
# 12. Write a Python program to remove all elements from a given set.
# 13. Write a Python program to use of frozensets.
# 14. Write a Python program to find maximum and the minimum value in a set.
# 15. Write a Python program to find the length of a set.
# 16. Write a Python program to check if a given value is present in a set or not.
# 17. Write a Python program to check if two given sets have no elements in common.
# 18. Write a Python program to check if a given set is superset of itself and superset of another given set.
# 19. Write a Python program to find the elements in a given set that are not in another set.
# 20. Write a Python program to remove the intersection of a 2nd set from the 1st set. #
