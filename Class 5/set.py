# Special note
# initial empty set but it is not a set it's a dict
s1 = {}
print(type(s1))  # it's a dict


# initial empty set with set() constructor
s = set()
print(s)

ss ={1, 9, 8}
# initial set and assign value
s = {1, 2, 3, 4}
print(s)
s.add(5)  # add five if it is not in set s
print(s)
s.remove(2)  # for removing item to set
print(s)
s.update(ss)  # add ss set to set s
print(s)
print(s.pop())  # remove and return an element from set
s.clear()  # for cleaning all set
print(s)

even = {2, 4, 6, 8, 10}
odd = {1, 3, 5, 7, 9, 11}
prime = {2, 3, 5, 7}
fib = {1, 1, 2, 3, 5, 8}

even_union_odd = even.union(odd)
print('Even U Odd =', even_union_odd)

even_int_odd = even.intersection(odd)
print('Even n Odd =', even_int_odd)

prime_intersection_fib = prime.intersection(fib)
print('Prime intersection fib =', prime_intersection_fib)

fib_union_prime = fib.union(prime)
print('Fib Union Prime =', fib_union_prime)

unuse_number = even_union_odd.difference(fib_union_prime)
print('Unused number for prime and fib =', unuse_number)








