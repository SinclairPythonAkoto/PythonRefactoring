"""*args & **kwargs

*args:      A special name we can pass to functions.
            It gathers remaining arguments as a tuple.
            (This is just a parameter it can be given any name).

**kwargs:  This gathers remaining keyword arguements as a dictionary.
           (We can also call this by any name)
"""


# *args
from sys import prefix


def sum_all_nums(*args):
    total = 0
    for num in args:
        total += num
    return total


print(sum_all_nums(4, 6, 9, 4, 10))
print(sum_all_nums(4, 6))


def ensure_correct_info(*args):
    if "akoto" in args and "sinclair" in args:
        return "Welcome back Sinclair!"

    return "Not sure who you are..."


print(ensure_correct_info("hello", False, 78))
print(ensure_correct_info(10, True, "SINCLAIR".lower(), 16, "akoto"))

"""Exercises & Examples"""

"""
Define a function contains_purple that accepts an unlimited number of arguements.
It should return True if any of the arguements are "purple" (all lowercase).
Otherwise it should return False.
"""


def contains_purple(*args):
    if "purple".lower() in args:
        return True
    return False


print(contains_purple(25, "purple"))
print(contains_purple("green", False, 37, "blue", "hello world"))
print(contains_purple("purple"))
print(contains_purple("a", 99, "blah blah blah", 1, True, False, "purple"))
print(contains_purple(1, 2, 3))


# **kwargs
def fav_colours(**kwargs):
    print(kwargs)


fav_colours(amy="purple", ben="red", charlse="green")  # print kwarg elements


def fav_colours(**kwargs):
    for person, colour in kwargs.items():
        print(f"{person}'s favourite colour is {colour}")


fav_colours(amy="purple", ben="red", charlse="green")
fav_colours(amy="purple", ben="red", charlse="green", diane="blue")
fav_colours(fiona="royal blue", gary="orange")


def special_greeting(**kwargs):
    if "Sinclair" in kwargs and kwargs["Sinclair"] == "special":
        return "You get a special greeting Sinclair!"
    elif "Sinclair" in kwargs:
        return f"{kwargs['Sinclair']} Sinclair!"

    return "Not sure who this is..."


print(special_greeting(Sinclair="Hello"))  # Hello Sinclair
print(special_greeting(Bob="hello"))  # Not sure who this is..
print(special_greeting(Sinclair="special"))  # You get a special greeting Sinclair!
print(special_greeting(Heather="hello", Sinclair="special"))


"""Exercises & Examples"""

"""
Write a function called combined_words which appears a single string called word, 
and any number of additional key word arguements.  If a prefix is provided, return
the prefix followed by the word.  If a suffix is provided, return the word followed
by the suffix.  If neither is provided, just return the word.xx
"""
# func("child", prefix="man")


def combined_words(word, **kwargs):
    if "prefix" in kwargs:
        return f"{kwargs['prefix']}{word}"

    elif "suffix" in kwargs:
        return f"{word}{kwargs['suffix']}"

    return word


print(combined_words("child"))
print(combined_words("child", prefix="man"))
print(combined_words("child", suffix="ish"))
print(combined_words("work", suffix="er"))
print(combined_words("work", prefix="home"))
