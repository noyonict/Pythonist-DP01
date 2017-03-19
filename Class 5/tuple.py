#  first method to create a tuple
t = ()
print(t)
#  Second method to create a tuple
t = tuple()
print(t)

#  Third method to create a tuple
t = 1,
print(t)

#  Fourth method to create a tuple
t = 1, 2, 3, 4, 5
print(t)

#  Fifth method to create a tuple
t = (1, 3, 2, 4, 3, 3, 3, 4, 4, 4, 5, 3)
print(t)

#  count() finction ]
n = t.count(3)  # count how many times 3 is used in this tuple and return count number
print('Number of 3 in use of t tuple is', n, 'times.')
ind = t.index(5)  # return the index number of 5
print('The index number of 5 is', ind)







