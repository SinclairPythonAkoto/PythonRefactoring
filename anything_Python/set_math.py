"""Set Math

Sets have quite a few other mathematical methods.
We will go over: intersection & union.

Union:  Generates a new set by combinining sets 
togther and removing any duplicates.

Intersection:  Generates a new set by recording the
values that appear in both sets.
"""


# Suppose we have a teacher that teaches two classes:
math_students = {"Matthew", "Helen", "Paris", "James", "Aaron"}
biology_students = {"Jane", "Matthew", "Charlotte", "Max", "Oliver", "James"}


# To generate a set with all unique students (union)
all_students = math_students | biology_students

print(f"union: {all_students}")


# Generate a set with students who are in both courses (intersection)
students_in_both_classes = math_students & biology_students

print(f"intersection: {students_in_both_classes}")
