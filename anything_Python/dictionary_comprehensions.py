"""Dictionary Comprehensions

Iterates over keys by default, you can ieterate through keys & values
by using .ites()

{key:value for key,value in dict}
"""

numbers = dict(first=1, second=2, third=3)

squared_numbers = {key: value ** 2 for key,value in numbers.items()}

print(squared_numbers)


# creating a dictionary comprehension from a list
new_dict = {num: num ** 2 for num in [1, 2, 3, 4, 5]}

print(new_dict)

# more examples
str1 = "ABC"
str2 = "123"
combo = {str1[i]: str2[i] for i in range(0, len(str1))}

print(combo)

instructor = {'name': 'Sinclair', 'city': 'London', 'colour': 'blue'}
yelling_instructor = {k.upper():v.upper() for k,v in instructor.items()}

print(yelling_instructor)


# conditional logic with dictionary comprehensions
num_list = [1, 2, 3, 4]
new_num = {num: ("even" if num % 2 == 0 else "odd") for num in num_list}

print(new_num)

# write logic to change one element of a dictionary
instructor = {'name': 'Sinclair', 'city': 'London', 'colour': 'blue'}
yelling_instructor = {(k.upper() if k is 'colour' else k):v.upper() for k,v in instructor.items()}


# my own examples
person = {}.fromkeys(['name', 'age', 'occupation', 'salary', 'city'], "--")
print(person)    # creates an empty values for the keys

sinclair = {key:value for key,value in person.items()}
sinclair.update(name='Sinclair', age=35, occupation='Developer')
print(sinclair)
