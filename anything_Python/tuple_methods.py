"""Tuple Mthods"""

# .count()
# returns the number of times a value appears in a tuple

numbers = (1, 2, 3, 3, 3)
num2 = numbers.count(2)  # 1
num3 = numbers.count(3)  # 3

print(num2)
print(num3)


# .index()
# returns the index at which a value if found in a tuple

num = (1, 2, 3, 3, 3)
num1 = num.index(1)
# my_num = num.index(5)  # valueError: tuple.index(x): x not in tuple
num3 = num.index(3)

print(num1)
print(num3)
