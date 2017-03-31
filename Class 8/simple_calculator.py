'''
def add(num1, num2):
    return(num1+num2)
def mul(num3, num4):
    return(num3-num4)
def sub(num5, num6):
    return(num5*num6)
def div(num7, num8):
    return(num7/num8)
a = int(input('Enter first number: '))
b = int(input('Enter Second number: '))
print()
print('Enter 1 for Addition, Enter 2 for Multiplication, Enter 3 for Substitution, Enter 4 for division')
print()
r = int(input('Choose what do you want to do: '))

x= add(a,b)
y = mul(a,b)
z = sub(a,b)
zz = div(a,b)
if r==1:
    print(a,'+',b,'=',x)
elif r==2:
    print(a,'-',b,'=',y)
elif r==3:
    print(a,'*',b,'=',z)
elif  r==4:
    print(a,'/',b,'=',zz)
'''
