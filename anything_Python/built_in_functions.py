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
Abs, Sum, Round Function
"""