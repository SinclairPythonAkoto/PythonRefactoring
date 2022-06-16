# Collections #
import collections
from collections import Counter

'''
Collections allows us to manage and use data types differently.
'''

# Containers
# list
# set
# dictionary
# tuple

# Types in collections
# 1 counter
# 2 deque
# 3 namedTuple()
# 4 orderedDict
# 5 defaultdict

c = Counter('gallad')    # count all the letters in the string 
print(c)
d = Counter(['a', 'a', 'b', 'c', 'c'])
print(d)
e = Counter({'a':1, 'b':2})
print(e)
f = Counter(cats=4, dogs=7)
print(f)

print(f['cats'])    # print individual element of the counter object
'''
If you use data that is not in the counter object you get 0 returned.
'''
print(f['pets'])    # 0 will be returned becuase does not exist

print(list(f.elements()))    # you can print out all the elements in the counter
print(list(c.elements()))
print(list(d.elements()))

# using the most_common() method
print(d.most_common(2))    # top 2 most common elements returned

'''
You can use the subtract() method that will take the value of the parameter
away from the value of the counter object it is being called on.
'''

my_list = Counter(a=4, b=2, c=0, d=-2)
list2 = ['a', 'b', 'b', 'c']
my_list.subtract(list2)
print(my_list)

'''
You can use the update() method where it will add the value from the parameter
to the value of the counter object it is being called on.
'''
my_list.update(list2)
print(my_list)

'''
clear() clears all the elements from the Counter object
'''
my_list.clear()
print(my_list)


'''
You can add the counters together 
'''
obj1 = Counter(a=4, b=2, c=0, d=-2)
obj2 = Counter(['a', 'b', 'b', 'c'])

print(obj1 + obj2)
print(obj1 - obj2)    # will not show values less or equal to 0

# union & intersection

'''
Interection is the smallest value in both counter object, we use use the '&'
symbol inbetween the two counter objects.
'''
print(obj1 & obj2)

'''
Union is the max element displayed for each counter object, we use the '|'
symbol inbetween the two counter objects.
'''
print(obj1 | obj2)
