# .remove(x)
#
# This operation removes element  from the set.
# If element  does not exist, it raises a KeyError.
# The .remove(x) operation returns None.
# >>> s = set([1, 2, 3, 4, 5, 6, 7, 8, 9])
# >>> s.remove(5)
# >>> print s
# set([1, 2, 3, 4, 6, 7, 8, 9])
# >>> print s.remove(4)
# None
# >>> print s
# set([1, 2, 3, 6, 7, 8, 9])
# >>> s.remove(0)
# KeyError: 0


set_remove = {1, 2, 3, 4, 5, 6, 7, 8, 9}
set_remove.remove(5)
print("Removed:",set_remove)


print("Removed:",set_remove.remove(4))

set_remove.discard(4)
print("Discarded:",set_remove)

set_remove.remove(0)
