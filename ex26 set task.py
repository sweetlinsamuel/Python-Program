# You have a non-empty set , and you have to execute  commands given in  lines.
# The commands will be pop, remove and discard.
#
# Input Format
# The first line contains integer n , the number of elements in the set s.
# The second line contains n space separated elements of set s. All of the elements are non-negative integers, less
# than or equal to 9.
# The third line contains integer N, the number of commands.
# The next N lines contains either pop, remove and/or discard commands followed by their associated value.
#
# Constraints
# 0<n<20
# 0<N<20
#
# Output Format
# Print the sum of the elements of set  on a single line.

# Sample Input
# 9
# 1 2 3 4 5 6 7 8 9
# 10
# pop
# remove 9
# discard 9
# discard 8
# remove 7
# pop
# discard 6
# remove 5
# pop
# discard 5


s = {1,2,3,4,5,6,7,8,9}
s.pop()
print(s)

s.remove(9)
print(s)

s.discard(9)
print(s)

s.discard(8)
print(s)

s.remove(7)
print(s)

s.pop()
print(s)

s.discard(6)
print(s)

s.remove(5)
print(s)

s.pop()
print(s)

s.discard(5)
print(s)