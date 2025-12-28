# This operation also removes element  from the set.
# If element  does not exist, it does not raise a KeyError.
# The .discard(x) operation returns None.
#
# Example
#
# >>> s = set([1, 2, 3, 4, 5, 6, 7, 8, 9])
# >>> s.discard(5)
# >>> print s
# set([1, 2, 3, 4, 6, 7, 8, 9])
# >>> print s.discard(4)
# None
# >>> print s
# set([1, 2, 3, 6, 7, 8, 9])
# >>> s.discard(0)
# >>> print s
# set([1, 2, 3, 6, 7, 8, 9])

s = {1, 2, 3, 4, 5, 6, 7, 8, 9}
s.discard(5)
print("Discarded:",s)

# s.discard(4)
print("Discarded:",s.discard(4))
print("Discarded:",s)

s.discard(0)
print("Discarded:",s)


