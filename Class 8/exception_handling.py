'''
def sum(a,b):
   return a*b

a = sum(12,12)
print(a)
print(sum(a,12))'''



a =0
try:
    a = int(input('Enter a number: '))
except ValueError:
    print('invalid')
except Exception:
    print('Somethimg going wrong')
print(a)
