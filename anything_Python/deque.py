# Collections: Deque #

'''
Deque is part of the collections module.  Like, lists but faster at adding elements
to the end and beginning of the list.
'''

import collections
# Create a deque
DoubleEnded = collections.deque(["Mon","Tue","Wed"])
print (DoubleEnded)

# Append to the right
print("Adding to the right: ")
DoubleEnded.append("Thu")
print (DoubleEnded)

# append to the left
print("Adding to the left: ")
DoubleEnded.appendleft("Sun")
print (DoubleEnded)

# Remove from the right
print("Removing from the right: ")
DoubleEnded.pop()
print (DoubleEnded)

# Remove from the left
print("Removing from the left: ")
DoubleEnded.popleft()
print (DoubleEnded)

# Reverse the dequeue
print("Reversing the deque: ")
DoubleEnded.reverse()
print (DoubleEnded)


# you can also extend a list
DoubleEnded.extend('123')
DoubleEnded.extend(["Thur", "Fri", "Sat", "Sun"])

print(DoubleEnded)



'''
Rotate Method
Rotating by positive numbers moves to the right.
Rotating negative numbers moves to the left. 
The number is the amount of spaces moved.
'''
# rotate left
DoubleEnded.rotate(-1)
print(DoubleEnded)

# rotate right
DoubleEnded.rotate(1)


'''
maxlen is a method used to constrict the amount of attributes in the object
'''
from collections import deque

days = deque(["Mon", "tue", "Wed"], maxlen=5)
days.extend(["Thur", "Fri", "Sat", "Sun"])

print(days)    # it will remove the first 2x elements from list to allow new items
