# .pop()
#
# This operation removes and return an arbitrary element from the set.
# If there are no elements to remove, it raises a KeyError.
#
# Example
#
# >>> s = set([1])
# >>> print s.pop()
# 1
# >>> print s
# set([])
# >>> print s.pop()
# KeyError: pop from an empty set

s = {1}
print("Pop:",s.pop())
print(s.pop())  #KeyError
set([])
print(s.pop())
