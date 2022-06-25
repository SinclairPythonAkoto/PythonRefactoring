# Named Tuples #

'''
Named tuples are basically easy-to-create, lightweight object types. Named tuple instances can be referenced using object-like variable dereferencing or the standard tuple syntax.
'''

# normal tuple
pt1 = (1.0, 5.0)
pt2 = (2.5, 1.5)

from math import sqrt

line_length = sqrt((pt1[0]-pt2[0])**2 + (pt1[1]-pt2[1])**2)

print(line_length) 


# named tuple
from collections import namedtuple

Point = namedtuple('Point', 'x y')    # class name, attributes

pt1 = Point(1.0, 5.0)
pt2 = Point(2.5, 1.5)

from math import sqrt

line_length = sqrt((pt1.x-pt2.x)**2 + (pt1.y-pt2.y)**2)    # referencing by tuple index

print(line_length)
print(pt1)
print(pt1.x, pt1.y)

# named tuples are still backwards compatible with normal tuples, so the following will still work:
Point = namedtuple('Point', 'x  y')
pt1 = Point(1.0, 5.0)
pt2 = Point(2.5, 1.5)

from math import sqrt

# use index referencing
line_length = sqrt((pt1[0]-pt2[0])**2 + (pt1[1]-pt2[1])**2)

# use tuple unpacking
x1, y1 = pt1

print(line_length)
print(pt1)

'''
***You should use named tuples instead of tuples anywhere you think object notation will make your code more pythonic and more easily readable.***
You can use them to represent very simple value types, particularly when passing them as parameters to functions.
It makes the functions more readable, without seeing the context of the tuple unpacking.
'''

# named tuple methods

# _asdict()
Person = namedtuple('Person', 'name age occupation')

sinclair = Person("Sinclair", 35, "Developer")

print(sinclair.name)

print(sinclair)
print(sinclair._asdict())

# fields method
print(sinclair._fields)

# replace method
sinclair = sinclair._replace(name="John")
print(sinclair)
print(sinclair.name)

# make method 
'''
This allows you to create data that will be applied to your class attributes in your namedtuple()
'''
julie = Person._make(["Julie", 21, "Data Analyst"])

print(julie)
print(julie.name)
