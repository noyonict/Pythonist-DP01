'''
a= []
true = 'This is true'
c = [1,2,3,4,['a','b','c','d'],True,true]
print (c.count(2))
print (c.count(4))
print (c.count('a'))
print (c[4].count('a'))
'''

'''
a = []
b = input()
true = 'This is true'
c = [1,2,3,4,['a','b','c','d'],True,true]
#print (c.count(b))
print (c[4].count('a'))
'''

'''
a = []
true = 'This is true'
c = [1,2,3,4,['a','b','c','d'],True,true]
a = c.copy()
print(a)
'''

a = []
true = 'This is true'
c = [1,2,3,4,['a','b','c','d'],True,true]
c.clear()
print(c)


a = []
true = 'This is true'
c = [1,2,3,4,['a','b','c','d'],True,true]
c.remove(2)
print(c)


a = []
true = 'This is true'
c = ['a','z','A','Bqsd']
c.reverse()
print(c)



a = []
true = 'This is true'
c = ['a','z','A','Bqsd']
n = c.index('Bqsd')
print(n)



a = []
true = 'This is true'
c = ['a','z','A','Bqsd']
n = c.index('z')
c[n]='mehedi'
c.insert(n+1, 12)
print(c)
