#if-else


a = 10
b = 20
if a > b:
    print('a is getter than b')
else:
    print('a is less than b')

# **********************************

a = int(input('a = '))
b = int(input('a = '))
if a > b:
    print('a is getter than b')
else:
    print('a is less than b')


# *****************************************************
a = eval(input('a = '))
b = eval(input('b = '))
c = eval(input('c = '))

if a>b:
    if a>c:
        print('a is gretter than b,c')
    else:
        print('c is gretter than a,b')
elif b>a:
    if b>c:
        print(print('b is gretter than a,c'))
    else:
        print('c is gretter than a,b')
else:
    if c>a:
        print(print('c is gretter than a,b'))
    else:
        print('a is gretter than b,c')


# ******************************************************
if a==b and a==c:
    print('a = b =c')
elif a>=b and a>=c:
    print('a is gretter than b,c')
elif b>=a and b>=c:
    print('b is gretter than a,c')
elif c>=a and c>=b:
    print('c is gretter than a,b')



if b>a and a>c:
    print('b>a>c')
elif a>c and c>b:
    print('a>c>b')
#elif c>a and c>b:
 #   print('c is gretter than a,b')
else:
    print('a=b=c')


