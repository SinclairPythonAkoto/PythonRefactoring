"""Scope: Global & Nonlocal

Global:      Allows you to access/manipulate variables outside of the function.
             To do this we would need to use the 'global' keyword before 
             refrencing the variable.

Nonlocal:    Allows you to modify a parent's variable in a child function
             (nested function).
"""


# global
total = 0


def increment():
    global total  # if we remove this line we get an error
    total += 1
    return total


print(increment())


# nonlocal
def outer():
    count = 0

    def inner():
        nonlocal count
        count += 1
        return count

    return inner()


print(outer())
