"""Set Comprehensions

Similar to list & dictionary comprehensions, set comprehensions allows you to copy, manipulate
create mew versions of a set from an existing set.
"""

new_set = {num**2 for num in range(10)}
print(new_set)


# set comprehension from a string
# it will remove the duplicate characters from the string
letters = {char.upper() for char in "hello"}
print(letters)


def all_vowels_in_string(string):
    """Checks if all 5 vowels are in a string."""

    match = (
        len({char for char in string if char in "aeiou"}) == 5
    )  # check the num of vowel matches, to match 5x vowels
    void_result = {char for char in string}  # set of characters user got wrong
    if match:
        return f"{match} You matched!"
    return f"{match} Your word did not match. Result: {void_result}"


print(all_vowels_in_string("good"))
print(all_vowels_in_string("sequoia"))
