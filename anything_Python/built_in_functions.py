"""Built In Functions
"""

# all() - returns true if all elements are true or empty
print(all([0, 1, 2, 3]))    # False

people = ["Charlie", "Casey", "Cody", "Cristina"]
print(all([name[0]=='C' for name in people]))    # check if all names begin with 'C'

people.append("Kirtsy")
print(all([name[0]=='C' for name in people]))    # now False because 'K' for Kirsty


# any() - returns true if any element is true
print(any([0, 1, 2, 3]))    # True

print(any([val for val in [1,2,3] if val > 2]))    # True
print(any([val for val in [1,2,3] if val > 5]))    # False

nums = [2, 60, 26, 18, 21]
print(any([num % 2 == 0 for num in nums]))    # check if any num even - True
print(any([num % 2 == 1 for num in nums]))    # check if any num odd - True
print(any([num % 2 == 2 for num in nums]))    # False


# sorted() - works on anything that is iterable
# this doesn't change the value of original tuple/list
more_numbers = [6, 1, 8, 2]

print(f"Sorted: {sorted(more_numbers)}")
print(f"Original list: {more_numbers}")    # original list unchanged

# descending order
print(f"Sorted (highest to lowest): {sorted(more_numbers, reverse=True)}")

# sorted() on a tuple 
print(f"Sorted tuple: {sorted((2, 1, 45, 35, 99))}")


# max() - returns max value or largest arguement
print(f"Max val: {max(3, 67, 99)}")
print(f"Max val: {max('c', 'd', 'a')}")

print(f"Max list: {max([3, 4, 1, 2])}")                      # 4
print(f"Max tuple: {max((1, 2, 3, 4))}")                     # 4
print(f"Max string: {max('awesome')}")                       # w - returns highest alphabetical character
print(f"Max dictionary: {max({1: 'a', 3: 'c', 2: 'b'})}")    # 3 - returns the dict key

nums = [40, 32, 6, 5, 10]

print(f"Max number: {max(nums)}")
print(f"Max string: {max('hello world')}")


# min() - returns minimum value
names = ["Arya", "Samson", "Dora", "Tim", "Ollivander"]

# shortest name
print(f"Min name: {min(names, key=lambda name: len(name))}")


# reversed() returns a reverse iterator object
nums = [1, 2, 3, 4]
print(f"Reversed: {list(reversed(nums))}")    # [4, 3, 2, 1] 
print(nums[::-1])                             # [4, 3, 2, 1]

print(f"Reversed: {reversed('hello')}")       # iterator objact
for char in reversed("hello world"):
    print(char)

for num in reversed(range(0, 10)):
    print(num)


# abs() - returns absolute value
print(f"Asbsolute: {abs(-23)}")
print(f"Asbsolute: {abs(23)}")

print(f"Asbsolute: {abs(-2.3333)}")
print(f"Asbsolute: {abs(2.3333)}")


# sum() - sum of everything in interable plus the start
# default start is 0
print(f"Sum list - [1, 2, 3]: {sum([1, 2, 3])}")
print(f"Sum list with optional start (10): {sum([1, 2, 3], start=10)}")
print(f"Sum list with optional start (-6): {sum([1, 2, 3], -6)}")

print(f"Sum tuple & floats: {sum((1.5, 2, 3.7))}")
print(f"Sum set: {sum({1, 50, 100})}")


# round() - returns nearest int unless we specify how many decimals want to round to
print(f"Round to nearest int: {round(10.212345)}")          # 10
print(f"Round to nearest 2 decimals: {round(10.212345, 2)}")   # 10.21
print(f"Round: {round(3.51234, 3)}")
print(f"Round: {round(3.51234, None)}")


# zip() - combines 2+ individual lists/tuples/sets/dict into one list of tuples
# you can use '*' to unpack lists/tuples/sets/dict - returns list of tuples.
first_zip = zip({1, 2, 3}, {4, 5, 6})
list_zip = list(first_zip)
dict_zip = dict(first_zip)

print(first_zip)    # zip object
print(list_zip)     # [(1, 4), (2, 5), (3, 6)]
print(dict_zip)

nums1 = [1, 2, 3, 4, 5]
nums2 = [6, 7, 8, 9, 10]
z = zip(nums1, nums2)

print(list(z))
print(dict(z))
print(tuple(z))

nums1 = [1, 2, 3, 4, 5]
nums2 = [6, 7, 8, 9, 10, 11, 12]
z = dict(zip(nums1, nums2))

print(z)    # {1: 6,...,5: 10} - cuts out value without pairs

nums1 = [1, 2, 3, 4, 5]
nums2 = [6, 7, 8, 9, 10, 11, 12]
words = ["hi", "lol", "haha", ":)"]
z = list(zip(words, nums1, nums2))

print(z)    # [('hi', 1, 6), ('lol', 2, 7), ('haha', 3, 8), (':)', 4, 9)]

# unpacking with zip() '*'
five_by_two = [(0, 1), (1, 2), (2, 3), (3, 4), (4, 5)]
unpack_zip = list(zip(*five_by_two))

print(unpack_zip)   # [(0, 1, 2, 3, 4), (1, 2, 3, 4, 5)]


"""Exercises & Examples"""

"""
And & All Function
"""
def is_all_strings(item):
    return all(type(val) == str for val in item)

print(is_all_strings(['a', 'b', 'c']))       # True
print(is_all_strings([2, 'g', 'h', 'i']))    # False


"""
Sorted Function
"""
users = [
    {"username": "samuel", "tweets": ["I love cake", "I love milkshakes!", "I love Fridays!"]},
    {"username": "katie", "tweets": ["I love my cat"]},
    {"username": "jeff", "tweets": []},
    {"username": "bob123", "tweets": []},
    {"username": "doggo_luvr", "tweets": ["dogs are the best", "I love my dog"]},
    {"username": "guitar_gal", "tweets": []}
]

# sort by username
print(f"Sorted usernames: {sorted(users, key=lambda user: user['username'])}")

# sort by number of tweets
print(f"Sorted tweets: {sorted(users, key=lambda user: len(user['tweets']))}")

songs = [
    {"title": "happy birthday", "playcount": 1},
    {"title": "Survive", "playcount": 6},
    {"title": "21 Seconds", "playcount": 99},
    {"title": "Toxic", "playcount": 31}
]

# sort most commonly played songs
print(f"Most played songs: {sorted(songs, reverse=True, key=lambda song: song['playcount'])}")


"""
Max & Min Function
"""
songs = [
    {"title": "happy birthday", "playcount": 1},
    {"title": "Survive", "playcount": 6},
    {"title": "21 Seconds", "playcount": 99},
    {"title": "Toxic", "playcount": 31}
]

# maximum played songs
print(f"Max object: {max(songs, key=lambda song: song['playcount'])}")    # returns dict
print(f"Max songs: {max(songs, key=lambda song: song['playcount'])['title']}")
print(f"Max playcount: {max(songs, key=lambda song: song['playcount'])['playcount']}")

# minimum played songs
print(f"Min songs: {min(songs, key=lambda song: song['playcount'])['title']}")
print(f"Min playcount: {min(songs, key=lambda song: song['playcount'])['playcount']}")


"""
Write a function called extremes which accepts an iterable.  It should return a tuple containing 
the maximum & minimum elements.
"""
def extremes(element):
    return (min(element), max(element))

print(extremes([1, 2, 3, 4, 5]))    # (1, 5)
print(extremes((99, 25, 30, -7)))   # (-7, 99)
print(extremes("alcatraz"))         # ('a', 'z')


"""
Write a function max_magnitude that accepts a single list full of numbers.  It should return the
magnitude (the number that is furthest away from zero). 
"""
def max_magnitude(numbers):
    return max((abs(num) for num in numbers))

print(max_magnitude([300, 20, -900]))   # 900
print(max_magnitude([10, 11, 12]))      # 12
print(max_magnitude([-5, -1, -89]))     # 89


"""
Write a function called sum_even_values.  This should accept a variable number of arguments and 
return the sum of all the arguments that are divisible by 2.  If there are no numbers divisible by
2, the function should return 0.  
"""
def sum_even_values(*args):
    return sum(num for num in args if num % 2 == 0)

print(sum_even_values(1, 2, 3, 4, 5, 6))    # 12
print(sum_even_values(4, 2, 1, 10))         # 16
print(sum_even_values(1))                   # 0


"""
Write a function called sum_floats.  This function should accept a variable number of arguments.
The function should return the sum of all the parameters that are floats.  If there are no floats 
the function should return 0.
"""
def sum_floats(*args):
    return sum(num for num in args if type(num) == float)
    

print(sum_floats(1.5, 2.4, 'awesome!', [], 1,))     # 3.9
print(sum_floats(1, 2, 3, 4, 5))                    # 0


"""
A teacher has a list of students and their mid-term grades & final grades.  Use zip to find
the highest grade of each student.  This should be returned in a dictionary:
{'dan': 98, 'julie': 91, 'kate': 78}
"""
midterms = [80, 91, 78]
finals = [98, 89, 53]
students = ['dan', 'julie', 'kate']

# map function
final_grades = dict(
    zip(
        students,
        map(
            lambda pair: max(pair),
            zip(midterms, finals)
        )
    )
)
print(final_grades)     # {'dan': 98, 'julie': 91, 'kate': 78}

# dictionary comprehension
final_grades_list_comp = {data[0]: max(data[1], data[2]) for data in zip(students, midterms, finals)}
print(final_grades_list_comp)     # {'dan': 98, 'julie': 91, 'kate': 78}

# finding the average grade
average_grades = dict(
    zip(
        students,
        map(
            lambda pair: ((pair[0] + pair[1]) / 2),
            zip(midterms, finals)
        )
    )
)
print(average_grades)


"""
Write a function called 'interleave' that accepts two strings.  It should return a new 
string contaiing the 2x strings interwoven or zipped together.
"""
def interleave(word1, word2):
    return "".join("".join(char) for char in list(zip(word1, word2)))

print(interleave('hi', 'ha'))      # hhia
print(interleave('aaa', 'zzz'))    # azazaz
print(interleave('lzr', 'iad'))    # lizard


"""
Write a function called triple_and_filter.  This function should accept a list of numbers,
filter out every number that is not divisible by 4, and return a new list where every
remaining number is tripled.
"""
def triple_and_filter(nums):
    return list((num * 3) for num in nums if num % 4 == 0)

print(triple_and_filter([1, 2, 3, 4]))      # [12]
print(triple_and_filter([6, 8, 10, 12]))    # [24, 36]

# same as above using filter() & map()
def interleave2(word1, word2):
    return list(filter(lambda num: num % 4 == 0, map(lambda num: num*3, nums)))

print(triple_and_filter([1, 2, 3, 4]))      # [12]
print(triple_and_filter([6, 8, 10, 12]))    # [24, 36]


"""
Write a function called extract_full_name.  This function should accept a list of 
dictionaries and return a new list of strings with the first name and last name 
keys in each dictionary concatenated.
"""
def extract_full_name(data):
    # return list(map(lambda name: name["first"] + " " + name["last"], data))
    return list(map(lambda name: f"{name['first']} {name['last']}", data))  # same as above

names = [
    {"first": "Cynthia", "last": "Asante"},
    {"first": "Sinclair", "last": "Akoto"}
]
print(extract_full_name(names))     # ['Cynthia Astante', 'Sinclair Akoto']