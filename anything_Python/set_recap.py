"""Sets Recap

This is a quick overview on sets and some of the set methods.

- Sets in Python are like formal mathematical sets.
- Sets do NOT have duplicate values (it will not add the duplicate instead of throwing an error).
- Elements in sets are NOT ordered.
- You cannot acess set items by index.
- Sets can be useful if you need to keep track of a collection of uniuqe data, without any duplicates.

A common use case for sets is to take data from a list and remove the duplicates by converting the list
to a set.  With this you have the option to convert it back to a list or do something else with it.
"""

# sets cannot have duplicates
my_set = set({1, 2, 3, 4, 5, 5, 5, 6})

print(my_set)  # {1, 2, 3, 4, 5, 6}


# creating a new set
new_set = set({1, 2, 3, 4})

# same as above
new_set2 = {1, 2, 3, 4}

print(new_set, new_set2)

# check if a value is in a set
print(4 in new_set)
print(8 in new_set2)
print("h" in new_set)


# access all values by using a for loop
numbers = {1, 2, 3, 4}

for num in numbers:
    print(num)


# common use case for sets.. (getting rid of duplicate data in a list)
# Imagine we have a form that users complete and we have stored all the user's city entries
# in a list.  This list will have duplicated entries from multiple users.

cities = [
    "London",
    "Paris",
    "Berlin",
    "Leeds",
    "London",
    "Manchester",
    "Berlin",
    "London",
    "Liverpool",
    "Paris",
    "Newcastle",
    "Manchester",
    "London",
]

# converting list to a set (getting unique values)
set_cities = set(cities)
print(set_cities)

# converting the set back to a list
list_cities = list(set_cities)
print(list_cities)

# the same as above - more effiecient
list_cities = list(set(cities))
print(list_cities)

# get number of unqie cities
unique_cities = len(set(cities))
print(unique_cities)


"""Set Methods"""

# .add()
# if the value already exists it doesn't add instead of throing an error
set_cities.add("Brighton")
set_cities.add("Warrington")
print(f"Add new cities: {set_cities}")

# .remove()
# returns a keyError if not found
set_cities.remove("Paris")
print(f"Removed a given city: {set_cities}")

# .discard()
# you won't get a KeyError if the value does not exist
set_cities.discard("Bradford")
print(f"Discarded a given city (that didn't exist): {set_cities}")

set_cities.discard("Berlin")
set_cities.discard("Newcastle")
print(f"Removed more cities: {set_cities}")

# .copy()
# creates a copy of the set
new_cities = set_cities.copy()
print(f"Copied set: {new_cities}")

# .clear()
# removes all contents of the set
new_cities.clear()
print(new_cities)
