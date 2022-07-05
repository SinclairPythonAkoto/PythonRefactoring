"""List Comprehensions

Allows you to make a new list but from an exisiting list.
You can also apply conditional logic to list comprehensions

[variable_name for varibale_name in list]
"""


from stat import FILE_ATTRIBUTE_NO_SCRUB_DATA
from unicodedata import name


nums = [1, 2, 3]
print([x * 10 for x in nums])




"""List Comprehension vs Loops

A list comprehension is just the same as using a for loop to 
create a new list - but with more lines of syntax
"""


# for loop
numbers = [1, 2, 3, 4, 5]
doubled_numbers = []

for num in numbers:
    doubled_number = num * 2
    doubled_numbers.append(doubled_number)

print(doubled_numbers)


# list comprehension 
numbers2 = [1, 2, 3, 4, 5]
doubled_numbers2 = [num * 2 for num in numbers2]  # reduced 4x lines of code to just 1x

print(doubled_numbers2)   # both results are the same



# List Comprehension examples
name = "Sinclair"

print([char.upper() for char in name])


friends = ["john", "julie", "ashley"]

print([friend[0].upper() for friend in friends]) # this returns the first letters of name, capitalised


# More examples
print([num * 10 for num in range(1,6)])

print([bool(val) for val in [0, [], 10, "", "hello world"]])   # This will return a list of True/False 


# List comprehensions can be used to convert data stypes within a data structure
numbers = [1, 2, 3, 4, 5]
string_list = [str(num) for num in numbers]

print(string_list)




"""List Comprehensoins with Conditional Logic

You can add logic to your list comprehensions by adding the if statement 
after your comprehension.  The new list will now only be created if 
a condition is met.

You can also use an else statement in a list comprehension.

[variable_name for variable_name in list if condition]

[variable_name if condition else variable_name for variable_name in list]
"""



numbers = [1, 2, 3, 4, 5]

evens = [num for num in numbers if num % 2 == 0]

odd = [num for num in numbers if num % 2 != 0]

print(evens)
print(odd)


# using the in keyword for conditional logic
line = "This is so much fun!"
new_line = "".join(letter for letter in line if letter not in "aeiou")

print(new_line)




"""List Comprehension Exercises & Examples"""

'''
From the list create a variable called answer, which is a new list containing the first letter of each name in the list.
names = ["Ellie", "Tim", "Matt"]
'''
names = ["Ellie", "Tim", "Matt"]
answer1 = [letter[0] for letter in names]

print(f"ANSWER 1: {answer1}")


'''
Create a new variable called answer2, which is a new list of all the even values.
numbers = [1, 2, 3, 4, 5, 6]
'''
numbers = [1, 2, 3, 4, 5, 6]
answer2 = [num for num in numbers if num % 2 == 0]

print(f"ANSWER 2: {answer2}")


'''
Given two lists, create a variable called answer3, which is a new list that is the 
itersection of the two (the output should be [3,4]).
list1 = [1, 2, 3, 4]
list2 = [3, 4, 5, 6]
'''
list1 = [1, 2, 3, 4]
list2 = [3, 4, 5, 6]
answer3 = [num for num in list1 if num in list2]

print(f"ANSWER 3: {answer3}")


'''
Given a list of words, create a variable called answer4, which is a new list with each word 
reversed and in lowercase.
words = ["Ellie", "Tim", "Matt"]
'''
words = ["Ellie", "Tim", "Matt"]
answer4 = [word[::-1].lower() for word in words]

print(f"ANSWER 4: {answer4}")


'''
For all numbers between 1 - 100 (inclucluding 100), create a create a variable called answer5, whcih 
is a list that are divisible by 12 (12, 24, etc)
'''
answer5 = [num for num in range(1,101) if num % 12 == 0]

print(f"ANSWER 5: {answer5}")


'''
Given the string "amazing", create a variable called answer6, which is a list containing all the letters 
from "amazing" but not the vowels.
'''
answer6 = [letter for letter in "amazing" if letter not in "aeiou"]

print(f"ANSWER 6: {answer6}")


'''
List comprehensions with multile if statements.  This is like using a nested if statement.
'''
numbers = [1, 2, 3, 4, 5]

# double if statement
nums_x = [x for x in numbers if x > 1 if x != 3]
print(nums_x)
# nested if statement
for y in numbers:
    if y > 1:
        if y != 3:
            print(y)


# using the 'and' operator
nums_x = [x for x in numbers if x > 1 and x != 3]
print(nums_x)

for y in numbers:
    if y > 1 and y != 3:
        print(y)

'''
List comprehensions with multiple for loops is like using a nested for loop instead
'''
fruits = ["Apples", "Pears", "Peaches", "Oranges", "Pineapple"]

# double for loop
new_list = [(num,fruit) for num in numbers if num > 1 for fruit in fruits]
print(new_list)


# nested for loop:
for num in numbers:
    if num > 1:
        for fruit in fruits:
            print(num,fruit)


# double for loop & double if
new_list2 = [(num,fruit) for num in numbers if num > 1 if num !=3 for fruit in fruits]


# nested loops
for num in numbers:
    if num > 1:
        if num !=3:
            for fruit in fruits:
                print(num,fruit)


# double for & 3x if 
new_list3 = [(num,fruit) for num in numbers if num > 1 if num != 3 for fruit in fruits if fruit != "Pears"]
print(new_list3)


# nested loops
for num in numbers:
    if num > 1:
        if num != 3:
            for fruit in fruits:
                if fruit != "Pears":
                    print(num,fruit)

# you can even break down the comprehension to make it more clearer (do not add comma)
new_list4 = [
    (num,fruit) for num in numbers 
    if num > 1 
    if num != 3 
    for fruit in fruits 
    if fruit != "Pears" 
    and fruit != "Apples"
]
print(new_list4)


# nested loops
for num in numbers:
    if num > 1:
        if num != 3:
            for fruit in fruits:
                if fruit != "Pears" and fruit != "Apples":
                    print(num,fruit)