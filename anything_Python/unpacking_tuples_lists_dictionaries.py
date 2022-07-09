"""Unpacking Lists, Tuples & Dictionaries

Unpacking is when we turn every item in a list, tuple or 
dictionary into an arguement.

*list_name or *tuple_name is how we unpack lists or tuples
**dict_name is how we unpack all the keyword arguements.
"""

# unpacking lists / tuples
# create a function that will add values that are passed in.


def sum_all_values(*args):
    total = 0
    for num in args:
        total += num
    return total


# passing in individual arguments
print(sum_all_values(1, 30, 2, 5, 6))

# If we had a list and wanted to pass each item as a variable
# then we would need to unpack it using '*'.

# Imaginary shopping cart.  We want to add ead item
cart = [1.99, 2.69, 9.99, 8.50, 12.10]

# sum_all_values(cart) # this will cause a TypeError

# using the unpacking method
print(sum_all_values(*cart))

# more exaples
person = ["Sinclair", 35, "London", False, 1.6]
city = [city for city in person if city == "London"]
print(*city)

# same as manually unpacking
person = ["Sinclair", 35, "London", False, 1.6]
(name, age, city, isFemale, hours) = person
print(city)


# unpacking dictionaries
# create a function displaying the names of the users
def display_names(first, second):
    return f"{first} says hello to {second}"


names = {"first": "John", "second": "Julie"}
print(display_names(**names))


# more examples
def add_and_multiply_numbers(a, b, c):
    return a + b * c


data = dict(a=1, b=2, c=3)

print(add_and_multiply_numbers(**data))


"""Exercises & Examples"""

"""
There is a function called count_sevens, call it with the arguments 1,4,7 and 
save the result to a variable called result1.
Next, call the count_sevens function, passing in all the numbers contained in the
nums list as individual arguments.  Save the result to a variable called result2.
"""


def count_sevens(*args):
    return args.count(7)


nums = [
    90,
    1,
    35,
    67,
    89,
    20,
    3,
    1,
    2,
    3,
    4,
    5,
    6,
    9,
    34,
    46,
    57,
    68,
    79,
    12,
    23,
    34,
    55,
    1,
    90,
    54,
    34,
    76,
    8,
    23,
    34,
    45,
    56,
    67,
    78,
    12,
    23,
    34,
    45,
    56,
    67,
    768,
    23,
    4,
    5,
    6,
    7,
    8,
    9,
    12,
    34,
    14,
    15,
    16,
    17,
    11,
    7,
    11,
    8,
    4,
    6,
    2,
    5,
    8,
    7,
    10,
    12,
    13,
    14,
    15,
    7,
    8,
    7,
    7,
    345,
    23,
    34,
    45,
    56,
    67,
    1,
    7,
    3,
    6,
    7,
    2,
    3,
    4,
    5,
    6,
    7,
    8,
    9,
    8,
    7,
    6,
    5,
    4,
    2,
    1,
    2,
    3,
    4,
    5,
    6,
    7,
    8,
    9,
    0,
    9,
    8,
    7,
    8,
    7,
    6,
    5,
    4,
    3,
    2,
    1,
    7,
]
result1 = count_sevens(1, 4, 7)
result2 = count_sevens(*nums)

print(result1)  # 1
print(result2)  # 14


"""
Create a function called calculate that accepts a list of keyword arguments

- make_float:   a boolean which returns a float if True or integer if False 
- operation:    which is either add, subtract, multiply and divide
- first:        which is a number, 'second' (another number), and 'message' (a string that can be added)

The function should return the result of actually running the specified operation with the first
and second keyword arguments. The result of the operation with the 'first' and 'second' is an integer
if make_float keyword is Flase, otherwise the result of th eoperation is a float.  If a message is 
specified, it should return the message keyword arguement and the result of the operation.  Otherwise,
it should return the string "The result is " joined with the result of operation.
"""


def calculate(first, second, operation, **kwargs):

    if operation == "add":
        result = {
            "result": first + second,
            "first number": first,
            "second number": second,
            "option": kwargs,
        }
        if result["option"] and kwargs["make_float"] == True:
            return (
                "Result: " + str(float(result["result"])),
                "First num: " + str(float(result["first number"])),
                "Second num: " + str(float(result["second number"])),
                f"Message: " + kwargs["message"],
            )
        return result
    elif operation == "subtract":
        result = {
            "result": first - second,
            "first number": first,
            "second number": second,
            "option": kwargs,
        }
        if result["option"] and kwargs["make_float"] == True:
            return (
                "Result: " + str(float(result["result"])),
                "First num: " + str(float(result["first number"])),
                "Second num: " + str(float(result["second number"])),
                f"Message: " + kwargs["message"],
            )
        return result
    elif operation == "multiply":
        result = {
            "result": first * second,
            "first number": first,
            "second number": second,
            "option": kwargs,
        }
        if result["option"] and kwargs["make_float"] == True:
            return (
                "Result: " + str(float(result["result"])),
                "First num: " + str(float(result["first number"])),
                "Second num: "
                + str(
                    float(result["second number"]),
                ),
            )
        return result
    elif operation == "divide":
        result = {
            "result": first / second,
            "first number": first,
            "second number": second,
            "option": kwargs,
        }
        if kwargs["make_float"] == True:
            return (
                "Result: " + str(float(result["result"])),
                "First num: " + str(float(result["first number"])),
                "Second num: " + str(float(result["second number"])),
                f"Message: " + kwargs["message"],
            )
        return result
    else:
        return "Please provide a valid operation - either 'add', 'subtract', 'multiply' or 'divide'."


add1 = {"first": 5, "second": 2, "operation": "add"}
add2 = {"first": 123, "second": 456, "operation": "add"}

print(calculate(**add1, make_float=True, message="Hello wolrd"))
print(calculate(**add2, make_float=False, message="Add two numbers together"))

subtract1 = {"first": 19.99, "second": 5.65, "operation": "subtract"}
subtract2 = {"first": 2022, "second": 1986, "operation": "subtract"}

print(
    calculate(**subtract1, make_float=True, message="This is subtracting two numbers")
)
print(calculate(**subtract2, make_float=False, message="Years of age"))

mul1 = {"first": 11.5, "second": 7, "operation": "multiply"}
mul2 = {"first": 16, "second": 12, "operation": "multiply"}

print(calculate(**mul1, make_float=True, message="Multiply two numbers"))
print(calculate(**mul2, make_float=True, message="16 x 12"))

div1 = {"first": 78, "second": 16.5, "operation": "divide"}
div2 = {"first": 244, "second": 12, "operation": "divide"}

print(calculate(**div1, make_float=True, message="Divide two numbers"))
print(calculate(**div2, make_float=True, message="244 / 12"))
