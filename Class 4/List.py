'''
a = list ()
b = []
c = [1,2,3,4]
print (type(a))
print (type(b))
print (type(c))

true = 'This is true'
d = [1,2,3,4,['a','b','c','d'], True, true]
print (d[4])
print (d[-1])
print (d[-2])
print (d[4][-1])
print (d[4][3])


list = [12, 'python', 16.2, 4, True]
print (type(list))
print (list)
print (list[0])
print (list[0:2])
print (list.append(6))
'''

'''
a = []
b = list()
true = 'This is true'
c= [1,2,3,4,['a','b','c','d'], True, true]
c[1]= 'Mehedi'
print(c)
print (c[1])
print (c[2])

c= [1,2,3,4,['a','b','c','d'], True, true]
c[1]= ['Mehedi',12,13]
print(c)
print (c[1][2])
print (c[3]+c[1][1])

c= [1,2,3,4,['a','b','c','d'], True, true]
c[1]= ['Mehedi','12',13]
print (c[3],c[1][1])
print(str(c[3])+c[1][1])
print(str(c[3])+" "+c[1][1])
'''

#Append & Extend
'''
b = list()
print(b)
b.append(12)
print(b)
b.append([12,13,14,'name'])
print(b)

b = list()
print (b)
b.append(12)
print(b)
b.extend([12,13,14,'name'])
print(b)
'''
'''
a = []
true = 'This is true'
c = [1,2,3,4,['a','b','c','d'],True,true]
a.extend(c)
print(a)

a = []
true = 'This is true'
c = [1,2,3,4,['a','b','c','d'],True,true]
a = c[:]
print(a)

a = []
true = 'This is true'
a.extend([1,2,3,4,['a','b','c','d'],True,true])
print(a)
'''

'''
a = []
x =12
y = 'python 3'
a.extend([x,y])
print(a)

a= []
true = 'This is true'
c = [1,2,3,4,['a','b','c','d'],True,true]
x= 12
y=13
a.extend([c,x,y])
print(a)
'''
