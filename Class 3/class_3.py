'''
str1 = 'This is python 3.6'

print(len(str1))  #Length of the String

print(str1[0]) # T
print(str1[4]) # ' '
print(str1[5]) # i
print(str1[16])

print(str1[-1]) # 6

print(str1[0:3])
print(str1[0:4])
print(str1[8:14])
print(str1[:])

print(str1[-10:-4])
print(str1[-10:14])
print(str1[8:-4])

print(str1[::-1])  #Reverse
print(str1[::-2])
print(str1[::-3])

print(str1[::2])   #For Skipping 2 index each time
print(str1[0:17:2]) #For Skipping 2 index each time start 0 end 17
print(str1[:2])
print(str1[:10:2])
print(str1[0:10:2])
print(str1[::3])
print(str1[::1])
#print(str1[::0])  #Slice step can not be zero. It's give error
print(str1+ str1)
str1 = str1 + str1
print(str1)'''


'''str1 = 'This is python 3.6.'
str1 = str1 + str1
print(str1)'''


'''str1 = 'This is python 3.6.'
print(str1*2)
print(str1*3)'''

'''str1 = 'This is python class 3.'
str1 = (str1+' ')*3
print(str1)'''


#Split the String
'''
str1 = 'python 3.6 and python 2.7'
print(str1)
print(str1.split())
one,two,three,four,five = str1.split()
print(one)
print(two)
print(three)
print(four)
print(five)
print(one,two)
print(one+two)
print(str1.split('and'))
print(str1.split('3.6'))
print(str1.split('python'))
print(str1.split('p'))
print(str1.split('.'))
'''


#Capitalize , Casefold & count the String
'''
s = 'python class 3'
print(s.capitalize()) # Python class 3

s = 'python class 3 and python 2' 
print(s.capitalize())

s = 'python class 3 and python 2'
print(s[7:12].capitalize()) # Class


s = 'python class 3 and python 2'
print(s.upper()) 


s = 'THIS IS PYTHON CLASS'
print(s.capitalize()) 


s = 'THIS IS PYTHON CLASS'
print(s.casefold())

s = 'THIS IS PYthon CLASS'
print(s.casefold()) # all lower case


s = 'THIS IS PYTHON CLASS'
print(s[8:14].casefold()) # all lower case start 8 end 14


s = 'THIS IS PYTHON CLASS'
print(s[15:20].casefold()) 



s = 'THIS IS PYTHON CLASS'
print(s.lower()) # all lower case


s = 'THIS IS PYTHON CLASS'
print(s.count('S'))


s = 'python class 3 and python 2'
print(s.count('s'))
'''


#Center of String
'''
s= 'python 3'

print(s.center(50))
print(s.center(50,'*'))
print(s.center(50,'a'))
'''


#StarWith & EndsWith in String
'''
s = 'pyhton 3'

print(s.startswith('p'))
print(s.startswith('a'))


print(s.endswith('3'))
print(s.endswith('3.6'))
'''


#Find in String

s = 'python 3'

print(s.find('p')) # gives 'p' index number
print(s.find('python'))
print(s.find('on'))
print(s.find('on',5))
print(s.find('on',4))
print(s.find('on',0,-1))
print(s.find('3'))

